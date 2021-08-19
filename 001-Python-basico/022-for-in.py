# for in
# range(start, stop, step)

nome = 'Cleberton'

for letra in nome:
    print(letra)

# enumerate
for n, letra in enumerate(nome): # enumerate somente enumera, isso não é o indice da string
    print(letra, n)

# range

for numero in range(10):
    print(numero)

for numero in range(0, 10, 2): # 0 a 10 de 2 em 2
    print(numero)

print('##############################')
frase = 'Ola mundo'
nova_frase = ''

for letra in frase:
    if letra == 'O' or letra == 'o':
        nova_frase += 's'
    elif letra == 'm':
        continue  # quando chega na letra m ele pula, e a letra m não sera concatenada
    elif letra == 'a':
        nova_frase += '@'
    else:
        nova_frase += letra


print(nova_frase)

