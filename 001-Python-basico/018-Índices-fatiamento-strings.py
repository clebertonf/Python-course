# Manipulação de strings

"""
    Indices de strings
    Fatiamento [inicio:fim:passo]
    Funções built-in

    Referêcia para estudo:
     Built-in Types¶: https://docs.python.org/3/library/stdtypes.html
     Built-in Functions¶: https://docs.python.org/3/library/functions.html
"""
# Indices de strings

url = 'www.google.com.br/'
print(url[1])  # w
print(url[-1])  # /

# Fatiamento

print(url[0:3])  # www
print(url[4:10])  # google

print(url[::2])  # wwgol.o.r (passo de 2 em 2)
print(url[::-2])  # /bmcego.w (passso de 2 em 2 de tras para frente)

print(url[0:10])  # www.google

nova_string = url[4:10]
print(nova_string)

# Funções built-in

print(url.replace('/', ''))  # troca um caracter por outro
print(len(url))  # quantos caracteres possui a string

# Built-in Functions¶: https://docs.python.org/3/library/functions.html