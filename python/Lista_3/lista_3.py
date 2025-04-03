print("\nBem Vindo a Lista 3 de Exercícios em Python:")
while True:
    escolherExercicio = int(input("\nDigite qual exercício deseja realizar (1, 2, 3, 4 ou 5) (0 = Finaliza o Programa): "))
    if escolherExercicio == 1:

        # Exercício 1
        print("\n")
        print("Exercicio 1 - Conferência de Número Triangular:")
        numberAleatorio = 1
        numberVerify = int(input("Digite um número para saber se ele é triangular: "))

        while numberAleatorio + (numberAleatorio + 1) + (numberAleatorio + 2) <= numberVerify:
            if numberAleatorio + (numberAleatorio + 1) + (numberAleatorio + 2) == numberVerify:
                print("Seu número é triangular! :)")
                break
            else:
                numberAleatorio += 1
        else:
            print("Seu número não é triangular! :(")

    elif escolherExercicio == 2:

        # Exercício 2
        print("\n")
        print("Exercicio 2 - Soma dos Quadrados:")
        numberQtd = int(input("Digite o número de valores que deseja calcular a soma de seus quadrados: "))
        calculoSoma = 0

        for i in range(0, numberQtd, 1):
            valorNumber = float(input(f"Digite o valor do {i+1}º número: "))
            calculoSoma += (valorNumber ** 2)

        print(f"A soma dos quadrados dos valores inseridos é: {calculoSoma}")

    elif escolherExercicio == 3:

        # Exercício 3
        print("\n")
        print("Exercicio 3 - Cálculo Quociente:")
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        restoCalculo = 0
        quociente = 0
        calculo = 0

        while calculo + b <= a:
            calculo += b
            quociente += 1

        restoCalculo = a - calculo
        print(f"A partir do valor A = {a}, e B = {b}. O Quociente da divisão de A/B é {quociente} e o Resto é {restoCalculo}.")

    elif escolherExercicio == 4:

        # Exercício 4
        print("\n")
        print("Exercicio 4 - Cálculo de Dias entre Datas:")
        from datetime import datetime
        dataInicial = input("Digite a data inicial do cálculo (Escreva nesse modelo: dd/mm/aaaa): ")
        dataFinal = input("Digite a data final do cálculo (Escreva nesse modelo: dd/mm/aaaa): ")
        dataInicial = datetime.strptime(dataInicial, "%d/%m/%Y")
        dataFinal = datetime.strptime(dataFinal, "%d/%m/%Y")
        calculoData =  dataFinal - dataInicial
        selecaoDia = abs(calculoData.days)

        print(f"A quantidade de dias no intervalo de {dataInicial.strftime('%d/%m/%Y')} - {dataFinal.strftime('%d/%m/%Y')} é {selecaoDia} dias.")

    elif escolherExercicio == 5:

        # Exercício 5
        print("\n")
        print("Exercicio 5 - Calculadora entre 2 Operandos:")
        while True:
            escolhaOperacao = int(input("Digite o número correspondente a operação que deseja realizar, sendo:\n\n1-Soma\n2-Subtração\n3-Produto\n4-Divisão\n5-Fechar Exercício\n\nEscolha: "))
            if escolhaOperacao == 5:
                print("\nSaindo...\n")
                break
            elif 1 <= escolhaOperacao <= 4:
                operando1 = float(input("Digite o valor do Primeiro Operando para o cálculo: "))
                operando2 = float(input("Digite o valor do Segundo Operando para o cálculo: "))
                if escolhaOperacao == 1:
                    soma = operando1 + operando2
                    print(f"\nA soma dos Operandos é: {operando1} + {operando2} = {soma}.\n")
                elif escolhaOperacao == 2:
                    sub = operando1 - operando2
                    print(f"\nA subtração dos Operandos é: {operando1} - {operando2} = {sub}.\n")
                elif escolhaOperacao == 3:
                        mult = operando1 * operando2
                        print(f"\nO produto dos Operandos é: {operando1} x {operando2} = {mult}.\n")
                elif escolhaOperacao == 4:
                    div = operando1 / operando2
                    print(f"\nA divisão dos Operandos é: {operando1} / {operando2} = {div}.\n")
            else:
                print("\nNúmero Inválido, digite novamente...\n")

    elif escolherExercicio == 0:
        break
    else:
        print("Exercício não encontrado")















