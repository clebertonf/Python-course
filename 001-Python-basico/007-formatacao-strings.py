# f strings para formatação de strings

nome = "Cleberton"
idade = 27
altura = 1.69999

print(
    f"Olá {nome} você tem {idade} anos, sua altura é: {altura:.2f}"
)  # arredondando numero

# Segunda forma formatar string com variaveis usadno format

print("Olá {} você tem {} anos, sua altura é: {:.2f}".format(
    nome, idade, altura
))
