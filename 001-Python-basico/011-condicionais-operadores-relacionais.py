# Operadores Relacionais ==, >, >=, <, <=, !=

# exemplos basicos de uso
num_1 = 10
num_2 = 50
num_3 = 5

print(num_2 == num_3)
print(num_1 > num_3)
print(num_2 < num_1)
print(num_2 >= num_3)
print(num_2 <= num_3)
print(num_2 != num_3)

# uso com condicionais

if num_1 > num_2:
    print(f'O numero {num_1} é maior que o numero {num_2}')
else:
    print(f'O numero {num_1} é menor que o numero {num_2}')
