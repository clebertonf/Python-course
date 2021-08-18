# Formatando valores com modificadores

"""
    :s - Strings
    :d - Int
    :f - Float
    :. - Quantidade de casas decimais Float
    : - Caractere (> ou < ou ^) (Quantidade) (Tipo s, d ou f)

    > esquerda
    < direita
    ^ centro
"""

# exemplo do uso da formatação :. (:f :d)
numero_1 = 10
numero_2 = 3
divisao = numero_1 / numero_2
print(f'Divisão formatada em duas casas decimais {divisao:.2f}')
print(f'Divisão formatada em duas casas decimais {numero_1:d}')


# exemplo :s
nome = 'Cleber'
print(f'Ola mundo! {nome:s}')

# Caractere (> ou < ou ^) (Quantidade) (Tipo s, d ou f)

numero_3 = 1
print(f'{numero_3:0>10}')  # Adicionando 10 casas a direita no numero
print(f'{numero_3:0<10}')  # Adicionando 10 casas a esquerda no numero
print(f'{numero_3:0^10}')  # Adicionando 10 casas e coloca o numero no centro

# exemplo com strings

print(f'{nome:#>10}')  # direita
print(f'{nome:#<10}')  # esquerda
print(f'{nome:#^10}')  # centro

