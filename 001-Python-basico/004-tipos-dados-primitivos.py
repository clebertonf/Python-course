# Tipos de dados primitivos
# Python é uma linguagem de tipagem dinâmica

"""
    str - string (Cadeias de texto)
    int - inteiro (numeros inteiros)
    float - real / ponto flutuante (mumeros com casas decimais (1.5, 10.10))
    bool - booleano / lógico (True / False)
"""
nome = "Cleberton"
idade = 27
nota = 9.9
ativo = True

print(type(nome))  # <class 'str'>
print(type(idade))  # <class 'int'>
print(type(nota))  # <class 'float'>
print(type(ativo))  # <class 'bool'>

print('###################')
# Converter tipos

idade = 27
print(type(idade))
nova_idade = str(idade)  # convertendo para str
print(type(nova_idade))

