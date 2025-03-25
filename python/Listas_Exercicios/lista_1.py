# Exercício 1
print("\n")
print("Exercicio 1 - Conversão de Temperatura:")
celsius = float(input("Digite a Temperatura em C°: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Sua temperatura {celsius}°C em Fahrenheit e: {fahrenheit}°F.")

# Exercício 2
print("\n")
print("Exercicio 2 - Soma de Números Inversos:")
number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))
number3 = float(input("Digite o terceiro número: "))
inNumber1 = 1 / number1
inNumber2 = 1 / number2
inNumber3 = 1 / number3
soma = (inNumber1) + (inNumber2) + (inNumber3 )
print(f"A soma dos números inversos dos informados é: {soma:.2f}. Sendo Número 1 ({number1}) = {inNumber1:.2f} / Número 2 ({number2}) = {inNumber2:.2f} / Número 3 ({number3:.2f}) = {inNumber3:.2f} /")

# Exercício 3
import random
print("\n")
print("Exercicio 3 - Cálculo de Pedido:")
idPedido = random.randint(1, 1000)
nameProd = str(input("Digite o nome do seu produto: "))
qtdComprada = int(input("Digite a quantidade comprada: "))
valorUnit = float(input("Digite o valor unitário desse produto: "))
desconto = float(input("Digite o desconto aplicado no pedido (em porcentagem): ")) / 100
valorProdTotal = qtdComprada * valorUnit
valorDesconto = valorProdTotal * desconto
valorFinal = valorProdTotal - valorDesconto
porcentDesc = desconto * 100
print(f"O Pedido n° {idPedido} do seu produto: {nameProd}, tem o custo final de: R${valorFinal:.2f}, já com o desconto de {porcentDesc:.2f}% aplicado.")

# Exercício 4
print("\n")
print("Exercicio 4 - Conversão de Real para Dólar:")
valorReal = float(input("Digite um valor em Reais: "))
valorCotacao = float(input("Digite a cotação de conversão: "))
valorDolar = valorReal * valorCotacao
print(f"O valor de R${valorReal} a partir da cotação de ${valorCotacao} resulta em ${valorDolar:.2f} Dólares.")

# Exercício 5
print("\n")
print("Exercicio 5 - Conversão de Tempo para Segundos:")
hora = int(input("Digite a hora atual: "))
minutos = int(input("Digite o minutos atuais: "))
segundos = int(input("Digite os segundos atuais: "))
calculoSegundos = (hora * 3600) + (minutos * 60) + segundos
print(f"Toda a hora informada de: {hora}:{minutos}:{segundos}, resulta em {calculoSegundos}s.")