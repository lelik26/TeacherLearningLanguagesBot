from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, filters
import config as cfg
from services.voices import generate_audio  # Функция генерации аудио

# Получаем список голосов из config.py
voices = cfg.VOICES


# Функция для создания вертикальной клавиатуры
def create_voice_keyboard():
    buttons = [[v["name"]] for v in voices]  # Каждое имя в отдельной строке
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)


# Обработчик команды /voice для выбора голоса
async def choose_voice(update: Update, context: CallbackContext):
    """Команда /voice - выбор голоса"""
    keyboard = create_voice_keyboard()
    await update.message.reply_text("🎙 Выберите голос для озвучивания:", reply_markup=keyboard)


# Обработчик выбора голоса пользователем
async def voice_selected(update: Update, context: CallbackContext):
    """Пользователь выбрал голос"""
    selected_voice = update.message.text

    # Проверяем, существует ли голос в списке
    if selected_voice not in [v["name"] for v in voices]:
        await update.message.reply_text("❌ Пожалуйста, выберите голос из списка.")
        return

    context.user_data["selected_voice"] = selected_voice  # Храним выбор в user_data
    await update.message.reply_text(f"✅ Вы выбрали голос: 🔊 📍{selected_voice}📍.\n 💬Введите текст для озвучки:",
                                    reply_markup=ReplyKeyboardRemove())


# Обработчик генерации озвучивания
async def generate_voice(update: Update, context: CallbackContext):
    """Генерация озвучки по введенному тексту"""
    user_id = update.message.from_user.id
    selected_voice = context.user_data.get("selected_voice")

    if not selected_voice:
        await update.message.reply_text("⚠️ Сначала выберите голос с помощью /voice")
        return

    # Получаем ID голоса
    voice_id = next(v['id'] for v in voices if v['name'] == selected_voice)

    # Генерируем аудио
    audio_file = generate_audio(update.message.text, voice_id)

    with open(audio_file, 'rb') as audio:
        await update.message.reply_voice(voice=audio)
