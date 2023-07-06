import unittest

from Funcoes import inverter_palavras, remover_duplicados, maior_palindrome, anagrama_palindrome, \
    formatar_frase


class MyTestCase(unittest.TestCase):
    def test_inverter_palavras(self):
        self.assertEqual(inverter_palavras("Hello, World! OpenAI is amazing."),
                         "amazing. is OpenAI World! Hello,")

    def test_remover_duplicados(self):
        self.assertEqual(remover_duplicados("Hello, World!"), "Helo, Wrd!")

    def test_maior_palindrome(self):
        self.assertEqual(maior_palindrome("babad"), "bab")

    def test_capitalize_frase(self):
        self.assertEqual(formatar_frase("hello. how are you? i'm fine, thank you."),
                         "Hello. How are you? I'm fine, thank you.")

    def test_anagrama_palindrome(self):
        self.assertEqual(anagrama_palindrome("racecar"), "true")


if __name__ == '__main__':
    unittest.main()
