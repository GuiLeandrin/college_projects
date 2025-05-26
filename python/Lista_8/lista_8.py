print("\nBem Vindo a Lista 2 de Exercícios em Python:")
while True:
    escolherExercicio = int(input("\nDigite qual exercício deseja realizar (1) (0 = Finaliza o Programa): "))
    if escolherExercicio == 1:

        # Exercício 1
        print("\n")
        print("Exercicio 1 - Conjunto de Alunos:")
        alunos = []
        alunosPt = set()
        alunosMt = set()
        qtdAlunos = int(input("Digite a quantidade de Alunos que você possui: "))

        if qtdAlunos >= 1:
            number = 1
            for i in range(qtdAlunos):
                nome = input(f"\nDigite o nome do seu aluno {number}: ")
                alunos.append(nome)
                number = number + 1
            
            number = 1
            for i in range(qtdAlunos):
                materia = int(input(f"\nDigite em qual matéria seu aluno {number} está matriculado: (1-Português / 2-Matemática / 3-As duas): "))

                if materia == 1:
                    alunosPt.add(alunos[i])

                elif materia == 2:
                    alunosMt.add(alunos[i])

                elif materia == 3:
                    alunosPt.add(alunos[i])
                    alunosMt.add(alunos[i])
                
                else:
                    print("Número informado inválido!!")

                number = number + 1
            
            print(f"\nOs alunos que estão cadastrados nas duas matérias são: {alunosPt.intersection(alunosMt)}.")

        else:
            print("\nQuantidade de Alunos informada incorreta!!")

    elif escolherExercicio == 0:
        break
    else:
        print("Exercício não encontrado")