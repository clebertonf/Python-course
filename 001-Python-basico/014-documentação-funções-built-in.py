# Sempre leia a documentação, ela é a maior fonte atualizada da linguagem

# Funçoẽs built-in
# link da documentação: https://docs.python.org/3/library/stdtypes.html

# soma 2 numeros
num_1 = input("digite um numero: ")
num_2 = input("digite um numero: ")

try:
    num_1 = float(num_1)
    num_2 = float(num_2)
    print(num_1 + num_2)
except:
    print("ERROR, Somente numeros")
