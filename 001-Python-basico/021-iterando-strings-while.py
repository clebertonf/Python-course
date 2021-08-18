# Percorrendo frases (strings) com while

frase = 'Ola seja bem vindo!'
contador = 0

while contador < len(frase):
    print(frase[contador])
    contador += 1

frase_2 = 'O rato roeu a roupa do rei de roma.'

contador_2 = 0
nova_frase = ''

while contador_2 < len(frase_2):
    letra = frase_2[contador_2]
    if letra == 'r':
        nova_frase += 'R'
    else:
        nova_frase += letra
    contador_2 += 1

print(nova_frase)