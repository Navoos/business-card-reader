import unittest
from parser.text_parser import TextParser

class TestTextParser(unittest.TestCase):
    def test_parse_text(self):
        sample_text = "John Smith\nCEO\njohn.smith@example.com\n+1 234-567-8900\n1234 Elm St."
        result = TextParser.parse_text(sample_text)
        print(f"result: {result}")
        self.assertEqual(result['name'], "John Smith")
        self.assertEqual(result['email'], "john.smith@example.com")
        self.assertEqual(result['phone'], "+1 234-567-8900")
        self.assertEqual(result['address'], "1234 Elm St.")

if __name__ == "__main__":
    unittest.main()
