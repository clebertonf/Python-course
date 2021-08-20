# For else

nomes = ['Cleber', 'Francisco', 'Katrine']

for nome in nomes:
    if nome.lower().startswith('c'):
        print('Achei a letra')
        break
else:
    print('Acabou laço')

# else no for é executado apos o laço terminar, caso a condição do if seja false
# caso o laço não seja parado, sempre o codigo chegara ao else