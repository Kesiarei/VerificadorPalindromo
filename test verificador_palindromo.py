import unittest
from verificador_palindromo import verifica_palindromo

class TestVerificadorPalindromo(unittest.TestCase):

    def test_palindromo_valido(self):
        # Teste para uma frase que é um palíndromo válido
        self.assertTrue(verifica_palindromo("Amor a Roma"))

    def test_palindromo_invalido(self):
        # Teste para uma frase que não é um palíndromo
        self.assertFalse(verifica_palindromo("Teste de palíndromo"))

    def test_palindromo_com_numeros(self):
        # Teste para uma frase que contém números e é um palíndromo válido
        self.assertTrue(verifica_palindromo("Socorram-me subi no ônibus em Marrocos 2021"))

    def test_palindromo_maiusculas(self):
        # Teste para uma frase em maiúsculas que é um palíndromo válido
        self.assertTrue(verifica_palindromo("ANOTARAM A DATA DA MARATONA"))

    def test_palindromo_com_simbolos(self):
        # Teste para uma frase que contém símbolos e é um palíndromo válido
        self.assertTrue(verifica_palindromo("Ame o poema!"))

    def test_palindromo_vazio(self):
        # Teste para uma frase vazia
        self.assertTrue(verifica_palindromo(""))

if __name__ == '__main__':
    unittest.main()