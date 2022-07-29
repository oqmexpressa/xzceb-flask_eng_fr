import unittest
import sys

sys.path.append('..')

from machinetranslation.translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(english_to_french(''), '')

    def test_translation(self):
        en_word = 'Hello'
        fr_word = 'Bonjour'
        self.assertEqual(english_to_french(en_word), fr_word)


class TestFrenchToEnglish(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(french_to_english(''), '')

    def test_translation(self):
        en_word = 'Hello'
        fr_word = 'Bonjour'
        self.assertEqual(french_to_english(fr_word), en_word)

if __name__ == '__main__':
    unittest.main()
