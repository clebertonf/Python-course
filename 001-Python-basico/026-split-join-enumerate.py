"""
    split - divide uam string (retorna uma lista)
    join - junta uma lista
    enumerate - enumera elemetos de uma lista 
    count
"""

# split
frase = "Ola seja bem vindo"

frase_separada = frase.split(' ')  # pode separar por espaço, virgula etc 

print(frase_separada)

frases_repitidas = 'aqui esta aqui e esta aqui legal e legal'

frase_separada_lista = frases_repitidas.split(' ')

print(frase_separada_lista)

print(frase_separada_lista.count('aqui'))  # quantas vezes a palavra aqui esta repetida na frase

# for para verificar todas

for palavra in frase_separada_lista:
    print(f'A palavra {palavra} se repetiu {frase_separada_lista.count(palavra)}x vezes na frase')


# join

frase_2 = ['Ola', 'mundo!', 'vamos', 'nessa.']

frase_montadada = ' '.join(frase_2)  # Sera usado o espaço para montar uma string com as palavras da lista 
# Pode se usar qualquer caracter
print(frase_montadada)

# enumerate

for indice, valor in enumerate(frase_2): #  enumera cada item na iteração
    print(indice, valor)