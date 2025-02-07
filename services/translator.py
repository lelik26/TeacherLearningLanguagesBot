import requests
from typing import Optional
from config import DEEPL_API_KEY, DEEPL_API_URL, SUPPORTED_LANGUAGES
from utils.logger import setup_logger

logger = setup_logger(__name__)


class TranslationError(Exception):
    pass


class DeepLTranslator:
    def __init__(self):
        self.validate_config()

    @staticmethod
    def validate_config():
        if not DEEPL_API_KEY:
            raise ValueError("DeepL API key is missing")
        if not DEEPL_API_URL:
            raise ValueError("DeepL API URL is missing")

    @staticmethod
    def validate_language(target_lang: str) -> bool:
        return target_lang in SUPPORTED_LANGUAGES.values()

    def translate(self, text: str, target_lang: str) -> str:
        try:
            if not text or not isinstance(text, str):
                raise ValueError("Invalid text input")

            if not self.validate_language(target_lang):
                raise ValueError(f"Unsupported target language: {target_lang}")

            response = requests.post(
                DEEPL_API_URL,
                headers={"Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"},
                data={"text": text, "target_lang": target_lang}
            )
            response.raise_for_status()

            translated_text = response.json()["translations"][0]["text"]
            logger.info(f"Translated: '{text}' -> '{translated_text}'")
            return translated_text

        except requests.exceptions.RequestException as e:
            logger.error(f"API Request failed: {str(e)}")
            raise TranslationError("Translation service unavailable") from e
        except (KeyError, IndexError) as e:
            logger.error(f"API Response parsing error: {str(e)}")
            raise TranslationError("Failed to parse translation response") from e