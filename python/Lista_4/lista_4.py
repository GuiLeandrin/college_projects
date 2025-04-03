print("\nBem Vindo a Lista 4 de Exercícios em Python:")
while True:
    escolherExercicio = int(input("\nDigite qual exercício deseja realizar (1, 2, 3) (0 = Finaliza o Programa): "))
    if escolherExercicio == 1:

        # Exercício 1
        print("\n")
        print("Exercicio 1 - Deslocamento de Vetores:")
        vetor1 = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
        vetor2 = []
        vetor3 = []

        vetor2.append(vetor1[-1])
        for i in range(len(vetor1) - 1):
            vetor2.append(vetor1[i])

        j = 1
        for i in range(len(vetor1) - 1):
            vetor3.insert(i, vetor1[j])
            j += 1
        vetor3.append(vetor1[0])

        print(f"Seu Vetor 1: {vetor1}.\n\nVetor Rotacionado para a Direita: {vetor2}.\nVetor Rotacionado para a Esquerda: {vetor3}.")

    elif escolherExercicio == 2:

        # Exercício 2
        print("\n")
        print("Exercicio 2 - Números Acima e Abaixo da Média:")
        import random
        numbersRandom = []
        qtdNumber = 1

        while qtdNumber <= 10:
            numbersRandom.append(random.randint(1, 100))
            qtdNumber += 1
        print(f"Os 10 valores são: {numbersRandom}")

        media = 0
        for i in range(len(numbersRandom)):
            calculoMedia = numbersRandom[i] / len(numbersRandom)
            media += calculoMedia
        print(f"A Média é: {media:.2f}\n")

        ordem = 1
        for i in range(len(numbersRandom)):
            if numbersRandom[i] > media:
                print(f"O {ordem}° valor ({numbersRandom[i]}) está Acima da Média.")
            elif numbersRandom[i] < media:
                print(f"O {ordem}° valor ({numbersRandom[i]}) está Abaixo da Média.")
            else:
                print(f"O {ordem}° valor ({numbersRandom[i]}) é igual a Média.")
            ordem += 1
    
    elif escolherExercicio == 3:

        # Exercício 3
        print("\n")
        print("Exercicio 3 - Inversão de Lista:")
        while True:
            lista = []
            for i in range(5):
                lista.append(random.randint(1, 100))
            print(f"Lista: {lista}.\n")
            verification = int(input("Você deseja inverter a lista? (1-SIM / 2-NÃO) "))

            if verification == 1:
                j = 4
                for i in range(3):
                    lista[i], lista[j] = lista[j], lista[i]
                    j -= 1
                print(f"Sua Lista Invertida fica: {lista}.")
                break
            elif verification == 2:
                print("Finalizando...\n")
                break
            else:
                print("Número inválido...Digite Novamente.\n")

    elif escolherExercicio == 0:
        break
    else:
        print("Exercício não encontrado")












