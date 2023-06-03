import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# pylint: disable=import-error

from translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):

    def test_english_to_french(self):
        english_text = 'Hello'
        expected_translation = 'Pepitoooo'
        result = english_to_french(english_text)
        self.assertEqual(result, expected_translation)

    def test_french_to_english(self):
        french_text = 'Bonjour'
        expected_translation = 'Hello'
        result = french_to_english(french_text)
        self.assertEqual(result, expected_translation)

if __name__ == '__main__':
    unittest.main()
