print("\nBem Vindo a Lista 2 de Exercícios em Python:")
while True:
    escolherExercicio = int(input("\nDigite qual exercício deseja realizar (1) (0 = Finaliza o Programa): "))
    if escolherExercicio == 1:

        # Exercício 1
        print("\n")
        print("Exercicio 1 - Arquivos de Nota e Média de Alunos:")
        qtdAlunos = int(input("Quantos alunos você possui? "))

        if qtdAlunos >= 1:
            escreveAluno = open("C:\\xampp\\htdocs\\college_projects\\python\\Lista_7\\alunos.txt", "w")
            escreveNota = open("C:\\xampp\\htdocs\\college_projects\\python\\Lista_7\\notas.txt", "w")
            escreveMedia = open("C:\\xampp\\htdocs\\college_projects\\python\\Lista_7\\medias.txt", "w")

            for i in range(1, qtdAlunos + 1):
                
                nome = input(f"\nDigite o nome do seu aluno {i}: ")
                escreveAluno.write(str(nome) + "\n")
                
                nota1 = float(input(f"Digite a nota da P1 do seu aluno {i}: "))
                nota2 = float(input(f"Digite a nota da P2 do seu aluno {i}: "))
                escreveNota.write("P1: " + str(nota1) + "," + " P2: " + str(nota2) + "\n")
                
                media = (nota1 + nota2) / 2
                if media >= 7:
                    status = "Aprovado"
                else:
                    status = "Reprovado"
                escreveMedia.write(str(nome) + "," + " Média: " + str(media) + "," + " Status: " + str(status) + "\n")
                
            escreveAluno.close()
            escreveNota.close()
            escreveMedia.close()
            print("\nDados Gravados com sucesso!!")

        else:
            print("\nQuantidade de Alunos informada incorreta!!")

    elif escolherExercicio == 0:
        break
    else:
        print("Exercício não encontrado")