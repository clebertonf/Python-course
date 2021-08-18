# While / else

# Acumulador

contador = 0
acumulador = 0

while contador <= 10:
    print(contador)
    acumulador += contador  # soma de todo contador em cada iteração

    contador += 1
    print(acumulador)
else:
    print('Saiu do laço')

# Em python o while possui um else que é executado no final do laço
# else nao e executado se a condição do while passar a ser falsa
# só entra no else caso o laço inteiro for percorrido
# caso você parar, quebrar o laço no meio com alguma condição, o else não será executado