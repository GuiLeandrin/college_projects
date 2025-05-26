print("\nBem Vindo a Lista 2 de Exercícios em Python:")
while True:
    escolherExercicio = int(input("\nDigite qual exercício deseja realizar (1) (0 = Finaliza o Programa): "))
    if escolherExercicio == 1:

        # Exercício 1
        print("\n")
        print("Exercicio 1 - Raíz de Equação de 2º Grau:")
        import math
        import cmath

        def raizes(a, b, c):
            delta = (b ** 2) - (4 * a * c)
            if delta > 0:
                x1 = (-b + (math.sqrt(delta))) / (2 * a)
                x2 = (-b - (math.sqrt(delta))) / (2 * a)

                return f"\nAs raízes da sua equação tem o tipo: (REAL)\nE tem os valores de: x1 = {x1:.2f}, x2 = {x2:.2f}"

            elif delta == 0:
                x = -b / (2 * a)

                return f"\nAs raízes da sua equação tem o tipo: (REAL DUPLA)\nE tem o valor de: x = {x:.2f}"

            elif delta < 0:
                x1 = (-b + cmath.sqrt(delta)) / (2 * a)
                x2 = (-b - cmath.sqrt(delta)) / (2 * a)
                
                return f"\nAs raízes da sua equação tem o tipo: (COMPLEXAS)\nE tem os valores de: x1 = {x1}, x2 = {x2}"
            else:
                return "\nA sua equação não possui raízes reais."
        
        a = float(input("\nDigite qual o valor do (a) da sua equação de 2º Grau: "))
        b = float(input("\nDigite qual o valor do (b) da sua equação de 2º Grau: "))
        c = float(input("\nDigite qual o valor do (c) da sua equação de 2º Grau: "))
        resolucao = raizes(a, b, c)
        print(resolucao)

    elif escolherExercicio == 0:
        break
    else:
        print("Exercício não encontrado")