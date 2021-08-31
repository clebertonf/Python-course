# Desempacotamento em python

list_names = ["Cleber", "Lucas", "Maria", "Paulo", "Carlos", "João"]

nome_1, nome_2, *resto = list_names

print(resto)  # recebe um array com os valores restantes da lista

list_ages = [18, 27, 35]

age_1, age_2, age_3 = list_ages

print(age_2)

list_numbers = [1, 5, 8, 12, 10]

# Apos o *restante, se eu buscar algum numero começara de forma decrescente
n1, n2, *restante, ultimo_numero = list_numbers

print(ultimo_numero)
