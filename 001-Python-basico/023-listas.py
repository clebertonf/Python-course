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
print(lista_4) # G removidp

