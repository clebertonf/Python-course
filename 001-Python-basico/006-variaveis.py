from datetime import date

# Uma variável se inicia com uma letra, nunca com um numero, mas pode conter
# um numero, palavras compostas separe com _  minha_variavel, letras minúsculas

nome = "Cleber"
data = date.today()

print(nome, type(nome), sep="--> ")
print(data, type(data))


# calculo IMC


def calc_imc(peso, altura):
    result = peso / (altura ** 2)
    print("Seu imc é:", round(result, 1))


calc_imc(75, 1.69)
