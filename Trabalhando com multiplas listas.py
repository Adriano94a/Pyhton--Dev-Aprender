#Trabalhando com multiplas listas
from itertools import zip_longest
'''
a_lista = ['A', 'B', 'C', 'D', 'E']
b_lista = [1, 2, 3, 4, 6]

for a, b in zip (a_lista, b_lista):
    print(a)
    print(b)

produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
precos = [250, 150, 220, 550, 50]
for a, b in zip(produtos, precos):
    print(f'Salvando produto {a} valor R$ {b}')

titulos = ['Titulo 1', 'Titulo 2', 'Titulo 3', 'Titulo 4']
descricoes = ['Descrição 1', 'Descrição 2', 'Descrição 3']
for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'Encontramos o {titulo} descrição:{descricao}')

'''
#desafio 1
produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos =  ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

for produto, preco in zip_longest(produtos,precos):
    print(f'Produto: {produto} encontrado no valor de {preco}')