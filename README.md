# Teacher Learning Languages Bot

## 📌 О проекте

**Teacher Learning Languages Bot** — это интеллектуальный чат-бот для перевода и озвучивания текстов английского, турецкого и арабского и других языков, интегрированный в Telegram. Бот помогает пользователям переводить тексты,  озвучивать слова или фразы.

## 🚀 Функционал

- 🔹 **Перевод текстов** 28 языков с помощью DeepL API.
- 🔹 **Озвучивание слов и фраз** с использованием ElevenLabs API.
- 🔹 **Выбор 8 голосов** для озвучивания
- 🔹 **Гибкая настройка команд** через TelegramBot API.

## 🛠️ Технологии

- **Язык программирования:** Python 3.12
- **Библиотеки:**
  - python-telegram-bot — для взаимодействия с Telegram API
  - `httpx` — для работы с API
  - `dotenv` — для безопасного хранения API-ключей
  - `DeepL API` — для перевода
  - `ElevenLabs API` — для озвучивания

## 📂 Структура проекта

```
TeacherLearningLanguagesBot/
│── bot.py                # Основной файл бота
│── config.py             # Конфигурация и загрузка API-ключей
│── handlers/             # Обработчики команд
│── services/             # Логика перевода и озвучивания
│── .env                  # Переменные окружения (не загружать в репозиторий!)
│── requirements.txt      # Список зависимостей
│── README.md             # Документация проекта
```

## 🔧 Установка и запуск

1. **Склонируйте репозиторий:**
   ```sh
   git clone https://github.com/lelik26/TeacherLearningLanguagesBot.git
   cd TeacherLearningLanguagesBot
   ```
2. **Создайте виртуальное окружение и установите зависимости:**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```
3. **Создайте файл ************************************`.env`************************************ и добавьте API-ключи:**
   ```ini
   TELEGRAM_BOT_TOKEN=your_telegram_token
   DEEPL_API_KEY=your_deepl_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ```
4. **Запустите бота:**
   ```sh
   python bot.py
   ```

## 📜 Лицензия

Проект распространяется под лицензией MIT.

---

**Автор:** lelik26


