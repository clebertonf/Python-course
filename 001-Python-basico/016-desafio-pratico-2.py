from datetime import datetime

# Desafio numero par ou impar

number = input('Digite um numero inteiro: ')

try:
    number = int(number)
    if number % 2 == 0:
        print('Numero é par!')
    else:
        print('numero é impar!')
except:
    print('Digite somente numeros inteiros!')

# Desafio hora atual com saudação

now = datetime.now()
hour = f'{now.hour}:{now.minute}:{now.second}'

if now.hour > 0 and now.hour < 11:
    print(f'Bom dia! são exatamente: {hour}')
elif now.hour > 11 and now.hour < 17:
    print(f'Boa tarde! são exatamente: {hour}')
else:
    print(f'Boa noite! são exatamente: {hour}')

# Desafio tamanho do nome

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é muito curto!')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')

