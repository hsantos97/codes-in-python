pesoStr = input("informe seu peso: ")

peso = int(pesoStr)

alturaStr = input("informe sua altura: ")

altura = float(alturaStr)

imc = peso // altura**2

print("Seu imc é: ", imc)
