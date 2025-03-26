# Exercício 1
print("\n")
print("Exercicio 1 - Cálculo IMC:")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
calculoImc = peso / (altura * altura)

if calculoImc <= 18.5:
    print(f"Seu IMC é {calculoImc:.2f} e você está Abaixo do peso!!")
elif calculoImc > 18.5 and calculoImc <= 25:
    print(f"Seu IMC é {calculoImc:.2f} e você está com o peso Normal!!")
elif calculoImc > 25 and calculoImc <= 30:
    print(f"Seu IMC é {calculoImc:.2f} e você está Acima do Peso!!")
elif calculoImc > 30:
    print(f"Seu IMC é {calculoImc:.2f} e você está Obeso!!")


# Exercício 2
print("\n")
print("Exercicio 2 - Verificação Triângulo:")
lado1 = float(input("Digite o primeiro lado de um triângulo em cm: "))
lado2 = float(input("Digite o segundo lado de um triângulo em cm: "))
lado3 = float(input("Digite o terceiro lado de um triângulo em cm: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os lados informados resultam em um triângulo!! :)")
else:
    print("Os lados informados não resultam em um triângulo!! :(")


# Exercício 3
print("\n")
print("Exercicio 3 - Localização de Quadrante:") 
pontoX = float(input("Digite a coordenada X do seu ponto: "))
pontoY = float(input("Digite a coordenada Y do seu ponto: "))

if pontoX == 0 and pontoY == 0:
    print("Seu ponto está na Origem!")
elif pontoX == 0 and pontoY > 0:
    print("Seu ponto está Para Cima!")
elif pontoX == 0 and pontoY < 0:
    print("Seu ponto está Para Baixo!")
elif pontoY == 0 and pontoX > 0:    
    print("Seu ponto está a Direita!")
elif pontoY == 0 and pontoX < 0:
    print("Seu ponto está a Esquerda!")
elif pontoX > 0 and pontoY > 0:
    print("Seu ponto está no 1°Quadrante!")
elif pontoX < 0 and pontoY > 0:
    print("Seu ponto está no 2°Quadrante!")
elif pontoX < 0 and pontoY < 0:
    print("Seu ponto está no 3°Quadrante!")
elif pontoX > 0 and pontoY < 0:
    print("Seu ponto está no 4°Quadrante!")
else:
    print("Erro a Encontrar Localização de Ponto!")


# Exercício 4
print("\n")
print("Exercicio 4 - Identificação de Signo:") 
nome = input("Digite seu nome: ")
dia = int(input("Digite o dia em que você nasceu: "))
mes = int(input("Digite o mes (numérico) em que você nasceu: "))
ano = int(input("Digite o ano em que você nasceu: "))

if ano <= 2025 and ano >= 1800:
    if (mes == 1 and dia >= 20 and dia <= 31) or (mes == 2 and dia >= 1 and dia <= 18):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Aquário.")
    elif (mes == 2 and dia >= 19 and dia <= 31) or (mes == 3 and dia >= 1 and dia <= 20):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Peixes.")
    elif (mes == 3 and dia >= 21 and dia <= 31) or (mes == 4 and dia >= 1 and dia <= 19):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Áries.")
    elif (mes == 4 and dia >= 20 and dia <= 31) or (mes == 5 and dia >= 1 and dia <= 20):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Touro.")
    elif (mes == 5 and dia >= 21 and dia <= 31) or (mes == 6 and dia >= 1 and dia <= 20):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Gêmeos.")
    elif (mes == 6 and dia >= 21 and dia <= 31) or (mes == 7 and dia >= 1 and dia <= 22):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Câncer.")
    elif (mes == 7 and dia >= 23 and dia <= 31) or (mes == 8 and dia >= 1 and dia <= 22):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Leão.")
    elif (mes == 8 and dia >= 23 and dia <= 31) or (mes == 9 and dia >= 1 and dia <= 22):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Virgem.")
    elif (mes == 9 and dia >= 23 and dia <= 31) or (mes == 10 and dia >= 1 and dia <= 22):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Libra.")
    elif (mes == 10 and dia >= 23 and dia <= 31) or (mes == 11 and dia >= 1 and dia <= 21):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Escorpião.")
    elif (mes == 11 and dia >= 22 and dia <= 31) or (mes == 12 and dia >= 1 and dia <= 21):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Sagitário.")
    elif (mes == 12 and dia >= 22 and dia <= 31) or (mes == 1 and dia >= 1 and dia <= 19):
        print(f"Seu nome é {nome}, nasceu em {dia}/{mes}/{ano} e é de Capricórnio.")
    else:
        print("Data Inválida.")
else:
    print("Data Inválida.")


# Exercício 5
print("\n")
print("Exercicio 5 - Cálculo de Premiação Salarial:") 
salarioBase = float(input("Digite seu salário mensal: "))
totalVendas = float(input("Digite o valor do total de vendas realizadas: "))

if totalVendas < 1000:
    valorPremiacao = 0
elif totalVendas >= 1000 and totalVendas <= 5000:
    valorPremiacao = 500
elif totalVendas > 5000 and totalVendas <= 7500:
    valorPremiacao = 750
elif totalVendas > 7500:
    valorPremiacao = 1000

salarioFinal = salarioBase + valorPremiacao
print(f"Salário Inicial: R${salarioBase:.2f} / Valor Premiação: R${valorPremiacao:.2f} / Salário Final: R${salarioFinal:.2f}")
