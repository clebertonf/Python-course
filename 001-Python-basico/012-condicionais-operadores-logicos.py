# and, or, not, in, not in

num_1 = 2
num_2 = 2
num_3 = 5

# and as duas condições devem ser verdadeiras par retornar True
if num_1 == num_2 and num_2 < num_3:
    print(True)
else:
    print(False)

# or somente uma condição deve ser verdadeira para retornar True
if num_1 == num_2 or num_2 > num_3:
    print(True)
else:
    print(False)

# not inverte a expressão de True para false ou vice e versa
if not num_1 == num_2 or not num_2 < num_3:
    print(True)
else:
    print(False)

value = ''

if not value:
    print('Preencha o campo!')

# in (esta contido)

nome = 'Cleberton'

if 'l' in nome:
    print('A letra está presente!')
else:
    print('Não existe')

# not in (nao esta contido)

if 'l' not in nome:
    print('A letra naão esta presente!')
else:
    print('a letra existe')


num_1 = 0
num_2 = 0
 
if not num_1 != num_2:
    print('Retorno 1')
else:
    print('Retorno 2')
    