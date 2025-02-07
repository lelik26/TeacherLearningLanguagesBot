# bot.py
import logging

from telegram import Update
from telegram import BotCommand

import config as cfg
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from handlers.translation_handler import TranslationHandlers
from handlers.voice_handler import choose_voice, voice_selected, generate_voice
from config import TELEGRAM_BOT_TOKEN
from services.voices import get_all_voices
from utils.logger import setup_logger

logger = setup_logger(__name__)

class LanguageTeacherBot:
    def __init__(self):
        self.app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        self.translation_handlers = TranslationHandlers()

    def setup_handlers(self):
        # Обработчик команды /start
        self.app.add_handler(CommandHandler("start", self.start))  # <-- добавляем обработчик правильно
        self.app.add_handler(CommandHandler("clear", self.clear_chat))
        self.app.add_handler(CommandHandler("help", self.help_command))

        # Обработчик перевода (ConversationHandler)
        self.app.add_handler(self.translation_handlers.get_conversation_handler())

        # Обработчики для озвучивания
        self.app.add_handler(CommandHandler("voice", choose_voice))
        self.app.add_handler(MessageHandler(filters.TEXT & filters.Regex(f"^({'|'.join([v['name'] for v in cfg.VOICES])})$"),
                                       voice_selected))
        #self.app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^Дальше$"), next_page))  # Обрабатываем переход на следующую страницу
        #self.app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^Назад$|🔙 Вернуться к выбору голоса"), back_page))  # Обрабатываем кнопку "Назад"
        self.app.add_handler(MessageHandler(filters.TEXT, generate_voice))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """Обработчик команды /start"""
        welcome_text = (
            "👋 Привет! Я твой языковой помощник.\n"
            "Используй команды, чтобы взаимодействовать со мной:\n\n"
            "📖 /translate - перевод текста.\n"
            "🔊 /voice - озвучивание текста.\n"
            "🗑 /clear - очистить историю.\n"
            "ℹ️ /help - помощь."
        )
        await update.message.reply_text(welcome_text)

    async def clear_chat(self, update: Update, context: CallbackContext):
        """Очищает историю сообщений, отправленных ботом"""
        await update.message.reply_text("💡Чтобы полностью очистить чат, удалите его вручную и начните новый! 🚀🗑 Очищаю историю чата...")
        context.user_data.clear()  # Очистка данных пользователя

        # Удаление сообщений, если бот является администратором в группе
        try:
            await update.message.delete()
        except Exception as e:
            logger.warning(f"Не удалось удалить сообщение: {e}")

    async def help_command(self, update: Update, context: CallbackContext):
        """Отправляет пользователю список команд и информацию о поддержке"""
        help_text = (
            "ℹ️ **Помощь**\n\n"
            "Я твой языковой помощник! Вот что я умею:\n\n"
            "📖 /translate - перевод текста.\n"
            "🔊 /voice - озвучивание текста.\n"
            "🗑 /clear - очистить историю чата.\n"
            "ℹ️ /help - помощь и связь с поддержкой.\n\n"
            "💬 **Связаться с поддержкой**: [Написать в поддержку](https://t.me/i_VAN_79)"
        )
        await update.message.reply_text(help_text, parse_mode="Markdown", disable_web_page_preview=True)

    async def set_bot_commands(self, app: Application):
        """Устанавливает команды для быстрого выбора в Telegram"""
        commands = [
            BotCommand("start", "Запустить бота"),
            BotCommand("translate", "Перевод текста"),
            BotCommand("voice", "Озвучивание текста"),
            BotCommand("clear", "Очистить историю чата"),
            BotCommand("help", "Помощь и техподдержка")
        ]
        await app.bot.set_my_commands(commands)

    def run(self):
        self.setup_handlers()
        logger.info("Бот запущен...")
        self.app.run_polling()


if __name__ == "__main__":
    bot = LanguageTeacherBot()
    bot.run()
