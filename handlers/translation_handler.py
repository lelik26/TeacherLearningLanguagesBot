from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler, MessageHandler, filters, CommandHandler
from config import SUPPORTED_LANGUAGES
from services.translator import DeepLTranslator, TranslationError
from utils.logger import setup_logger

logger = setup_logger(__name__)

CHOOSING_LANGUAGE, TRANSLATING = range(2)


class TranslationHandlers:
    def __init__(self):
        self.translator = DeepLTranslator()
        self.languages = SUPPORTED_LANGUAGES

    async def start_translation(self, update: Update, context: CallbackContext) -> int:
        keyboard = [[lang] for lang in self.languages.keys()]
        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            one_time_keyboard=True,
            resize_keyboard=True
        )

        await update.message.reply_text(
            "🌍 Выбери язык для перевода:",
            reply_markup=reply_markup
        )
        return CHOOSING_LANGUAGE

    async def handle_language_choice(self, update: Update, context: CallbackContext) -> int:
        user_choice = update.message.text

        if user_choice not in self.languages:
            await update.message.reply_text("❌ Пожалуйста, выбери язык из списка.")
            return CHOOSING_LANGUAGE

        context.user_data["target_lang"] = self.languages[user_choice]
        await update.message.reply_text(
            f"📝 Теперь отправь текст для перевода на {user_choice}",
            reply_markup=ReplyKeyboardRemove()
        )
        return TRANSLATING

    async def handle_translation(self, update: Update, context: CallbackContext) -> int:
        user_text = update.message.text
        target_lang = context.user_data.get("target_lang", "RU")

        try:
            translated_text = self.translator.translate(user_text, target_lang)
            await update.message.reply_text(
                f"🌐 Перевод ({target_lang}):\n{translated_text}",
                parse_mode="Markdown"
            )
        except TranslationError as e:
            logger.error(f"Translation failed: {str(e)}")
            await update.message.reply_text("❌😔 Ошибка перевода. Попробуйте позже.")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            await update.message.reply_text("❌😱 Произошла непредвиденная ошибка.")

        return ConversationHandler.END

    async def cancel_translation(self, update: Update, context: CallbackContext) -> int:
        await update.message.reply_text("🚫 Операция отменена.")
        return ConversationHandler.END

    def get_conversation_handler(self) -> ConversationHandler:
        return ConversationHandler(
            entry_points=[CommandHandler("translate", self.start_translation)],
            states={
                CHOOSING_LANGUAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_language_choice)],
                TRANSLATING: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_translation)],
            },
            fallbacks=[CommandHandler("cancel", self.cancel_translation)],
        )