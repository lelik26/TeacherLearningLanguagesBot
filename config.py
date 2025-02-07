import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Загружаем API ключи
# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# DeepL
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
DEEPL_API_URL = os.getenv("DEEPL_API_URL", "https://api-free.deepl.com/v2/translate")

# OpenAI
OPEN_API_KEY = os.getenv("OPEN_API_KEY")

# ELEVANLABS
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Список доступных голосов
VOICES = [
    {"name": "Lily", "id": "pFZP5JQG7iQjIQuC4Bku"},
    {"name": "Fatih Yıldırım", "id": "7VqWGAWwo2HMrylfKrcm"},
    {"name": "Laura", "id": "FGY2WhTYpPnrIDTdsKH5"},
    {"name": "George", "id": "JBFqnCBsd6RMkjVDRZzb"},
    {"name": "River", "id": "SAz9YHcvj6GT2YYXdXww"},
    {"name": "Will", "id": "bIHbv24MWmeRgasZH58o"},
    {"name": "Sarah", "id": "EXAVITQu4vr4xnSDxMaL"},
    {"name": "Daniel", "id": "onwK4e9ZLuTAKqWW03F9"},
    # Добавьте больше голосов, если нужно
]

# Языки
SUPPORTED_LANGUAGES = {
    "🇬🇧 English": "EN",
    "🇷🇺 Русский": "RU",
    "🇨🇳 中文": "ZH",  # Китайский
    "🇹🇷 Türkçe": "TR",
    "🇸🇦 العربية": "AR", # Арабский
    "🇪🇸 Español": "ES",  # Испанский
    "🇵🇹 Português": "PT",  # Португальский
    "🇫🇷 Français": "FR",  # Французский
    "🇩🇪 Deutsch": "DE",  # Немецкий
    "🇮🇹 Italiano": "IT",  # Итальянский
    "🇮🇩 Bahasa Indonesia": "ID",  # Индонезийский
    "🇧🇬 Български": "BG",  # Болгарский
    "🇨🇿 Čeština": "CS",  # Чешский
    "🇩🇰 Dansk": "DA",  # Датский
    "🇬🇷 Ελληνικά": "EL",  # Греческий
    "🇪🇪 Eesti": "ET",  # Эстонский
    "🇫🇮 Suomi": "FI",  # Финский
    "🇭🇺 Magyar": "HU",  # Венгерский
    "🇯🇵 日本語": "JA",  # Японский
    "🇰🇷 한국어": "KO",  # Корейский
    "🇱🇹 Lietuvių": "LT",  # Литовский
    "🇱🇻 Latviešu": "LV",  # Латышский
    "🇳🇴 Norsk Bokmål": "NB",  # Норвежский Букмол
    "🇳🇱 Nederlands": "NL",  # Нидерландский
    "🇵🇱 Polski": "PL",  # Польский
    "🇷🇴 Română": "RO",  # Румынский
    "🇸🇰 Slovenčina": "SK",  # Словацкий
    "🇸🇮 Slovenščina": "SL",  # Словенский
    "🇸🇪 Svenska": "SV",  # Шведский
}


# Логирование
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "bot.log"

