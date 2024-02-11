#Desafio 2
''' Criar uma função chamada calcular_valores que recebe 2 parametros o primeiro o 
preço de um produto e o segundo parâmetro é a quantidade, porém a quantidade deve haver
um valor padrão de 1. Sua função deve exibir o resultado do preço do produto,
multiplicando a quantidade escolhida '''

def calcular_valores(preço, quantidade=1):
    print(preço * quantidade)

calcular_valores(10,2)