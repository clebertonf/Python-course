
frase_2 = 'O rato roeu a roupa do rei de roma.'

contador_2 = 0
nova_frase = ''

while contador_2 <= len(frase_2):
    if frase_2[contador_2] == 'r':
        nova_frase += 'R'
    else:
        nova_frase += frase_2[contador_2]
    contador_2 += 1

print(nova_frase)