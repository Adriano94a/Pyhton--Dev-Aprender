def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de: R$ {preco}')

 #Argumentos Posicionais   
exibir_preco('Iphone', 5000)
exibir_preco(nome_produto='Iphone Pro',preco=5000)

#Argumentos Nomeados

exibir_preco(preco=5000, nome_produto='Iphone XR')

'''Desafio 3
Criar uma função chamada gerar_objeto_personalizado que irá receber 3 parâmetros, cor , altura, formato. A sua função deve apenas
imprimir na tela o que foi passado para ela, nada mais, nada menos. Porém ela deve seguir as seguintes regras:

1- O primeiro argumento deve ser posicional
2 - Os Argumentos altura e formato precisam OBRIGATORIAMENTE  serem nomeados'''
def gerar_objeto_personalizado(cor,*,altura,formato):
    print(cor,altura,formato)

gerar_objeto_personalizado('Pardo',formato='Quadrado',altura='1,79 cm')
