def verifica_palindromo(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def main():
    frase = input("Digite uma frase para verificar se é um palíndromo: ")
    resultado = verifica_palindromo(frase)

    if resultado:
        print("Verdadeiro! É um palíndromo.")
    else:
        print("Falso! Não é um palíndromo.")

if __name__ == "__main__":
    main()