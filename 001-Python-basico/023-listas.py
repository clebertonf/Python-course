"""
    Listas
    Fatiamento
    append, insert, pop, del, clear, extend, +
    min, maz
    range
"""

lista = [1, 2, 3, 4]
lista_2 = ['Cleber', True, 10]

print(lista, lista_2)

# modificando lista
lista[3] = 6
print(lista)

# percorrendo lista
print(lista[0:3])

# append (insere valor ao final)
lista_3 = ['a', 'b', 'c']
lista_3.append('d')


# extend (junta duas listas)

lista_4 = ['e', 'f', 'g']

lista_3.extend(lista_4)

print(lista_3)

# insert (escolhe o indice que ira inserir)

lista_3.insert(3, 'J')
print(lista_3)


# pop (remove o ultimo valor da lista)

lista_4.pop()
print(lista_4)  # G removido

lista_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista_5)

del(lista_5[0])
del(lista_5[0:4])

print(lista_5)

# menor e maior numero da lista

print(max(lista_5))  # maior numero
print(min(lista_5))  # menor numero

# + juntar duas listas

print(lista_5 + lista_4)

# range lista (list)

print(f'lista {list(range(10))}')

