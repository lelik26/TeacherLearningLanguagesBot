import unittest
from services.translator import DeepLTranslator

class TestDeepLTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = DeepLTranslator()

    def test_valid_translation(self):
        text = "Hello, world!"
        result = self.translator.translate(text, "RU")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 5)

    def test_invalid_language(self):
        with self.assertRaises(ValueError):
            self.translator.translate("Test", "XX")

    def test_empty_text(self):
        with self.assertRaises(ValueError):
            self.translator.translate("", "RU")

if __name__ == "__main__":
    unittest.main()