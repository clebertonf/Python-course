# Laço de repetição while em python

# enquanto o numero for menor que 10 imprime na tela o numero
numero = 0
while numero <= 10:
    print(numero)
    numero += 1

# continue
print('######################################################')
numero_2 = 0

while numero_2 <= 5:
    if numero_2 == 3:  # esse bloco só e executado caso o nuemro for 3
        numero_2 += 1  # ira pular o numero 3
        continue  # as linhas apos o continue não são executadas, então ele volta para o inicio do while
    print(numero_2)
    numero_2 += 1

# break
print('######################################################')

numero_3 = 0

while numero_3 <= 5:
    if numero_3 == 3:  # esse bloco só e executado caso o nuemro for 3
        numero_3 += 1
        break  # o laço para e o codigo é encerrado (imprime somente 0, 1 e 2)
    print(numero_3)
    numero_3 += 1

