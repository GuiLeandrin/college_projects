print("\nBem Vindo a Lista 2 de Exercícios em Python:")
while True:
    escolherExercicio = int(input("\nDigite qual exercício deseja realizar (1, 2, 3) (0 = Finaliza o Programa): "))
    if escolherExercicio == 1:

        # Exercício 1
        import unicodedata
        print("\n")
        print("Exercicio 1 - Verificação de vogal em frase:")
        frase = input("Digite a frase que deseja verificar a quantidade de vogais: ")
        padronizaFrase = frase.upper()
        retiraAcento = ''.join(c for c in unicodedata.normalize('NFD', padronizaFrase) if not unicodedata.combining(c))
        vogais = ["A", "E", "I", "O", "U"]
        qtdVogais = len([letra for letra in retiraAcento if letra in vogais])

        print(f"Sua frase possui {qtdVogais} vogais.")

    elif escolherExercicio == 2:

        # Exercício 2
        print("\n")
        print("Exercicio 2 - Retirar vogais de uma frase:")
        frase = input("Digite a frase que deseja verificar a quantidade de vogais: ")
        vogais = [
            "A", "E", "I", "O", "U",
            "a", "e", "i", "o", "u",
            "Á", "É", "Í", "Ó", "Ú",
            "á", "é", "í", "ó", "ú",
            "À", "È", "Ì", "Ò", "Ù",
            "à", "è", "ì", "ò", "ù",
            "Â", "Ê", "Î", "Ô", "Û",
            "â", "ê", "î", "ô", "û",
            "Ã", "Õ", "ã", "õ",
            "Ä", "Ë", "Ï", "Ö", "Ü",
            "ä", "ë", "ï", "ö", "ü"
        ]

        for vogal in vogais:
            frase = frase.replace(vogal, "")

        print(f"Sua frase sem vogais fica: {frase}")

    elif escolherExercicio == 3:

        # Exercício 3
        print("\n")
        print("Exercicio 3 - Retirar Espaços em Branco:")
        frase = input("Digite a frase que deseja retirar os espaços em branco: ")
        arrayFrase = frase.split()
        fraseSemEspacos = ''.join(arrayFrase)

        print(f"Sua frase sem espaços fica: {fraseSemEspacos}")

    elif escolherExercicio == 0:
        break
    else:
        print("Exercício não encontrado")