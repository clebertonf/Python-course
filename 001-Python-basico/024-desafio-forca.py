
palavra_secreta = input('Digite a palavra secreta: ')
print('Ok, agora peça pro seu amigo advinhar!')

letras_digitadas = []
contador = len(palavra_secreta) * 2

while True:
    if contador <= 0:
        print('Acabou as chances')
        break
    letra_usuario = input('Difite uma letra: ')

    if len(letra_usuario) > 1:
        print('Digite apenas uma letra!')
        continue

    letras_digitadas.append(letra_usuario)

    if letra_usuario in palavra_secreta:
        print(f'A letra {letra_usuario} esta na palavra secreta!')
    else:
        letras_digitadas.pop()
        print('Infelizmente a letra não se encontra!')

    palavra_secreta_temp = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            palavra_secreta_temp += letra_secreta
        else:
            palavra_secreta_temp += '*'
    print(palavra_secreta_temp)

    if palavra_secreta_temp == palavra_secreta:
        print('Voce Ganhou')
        break

    contador -= 1
