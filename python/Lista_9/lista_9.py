print("\nBem Vindo a Lista 2 de Exercícios em Python:")
while True:
    escolherExercicio = int(input("\nDigite qual exercício deseja realizar (1) (0 = Finaliza o Programa): "))
    if escolherExercicio == 1:

        # Exercício 1
        print("\n")
        print("Exercicio 1 - Dicionário de Aunos e Notas:")
        alunos = {}
        qtdAlunos = int(input("Digite a quantidade de Alunos que você possui: "))

        if qtdAlunos >= 1:
            number = 1
            for i in range(qtdAlunos):
                nome = input(f"\nDigite o nome do seu aluno {number}: ")
                nota1 = float(input(f"Digite a nota da P1 do seu aluno {number}: "))
                nota2 = float(input(f"Digite a nota da P2 do seu aluno {number}: "))
                alunos.update({nome: [nota1, nota2]})
                number = number + 1

            print("\n")
            for nome, notas in alunos.items():
                media = (notas[0] + notas[1]) / 2

                if media >= 7:
                    status = "Aprovado"
                else:
                    status = "Reprovado"

                print(f"{nome}: P1 = {notas[0]}, P2 = {notas[1]} / Média = {media} / Status = {status}")

        else:
            print("\nQuantidade de Alunos informada incorreta!!")

    elif escolherExercicio == 0:
        break
    else:
        print("Exercício não encontrado")