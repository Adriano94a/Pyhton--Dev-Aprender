'''import random

cores = ['verde', 'azul', 'vermelho', 'rosa']
print(random.choices(cores, k=2)) #Escolher opção aleatória

cartas_do_baralho = ['Az de ouro', 'Joker', 'Dama', 'Rei', 'Sete de copas'] #Embaralhar uma lista
print(random.shuffle(cartas_do_baralho))
print(cartas_do_baralho)
'''
import random
#Desafio1 Simular a opção de jogar uma moeda e resultar em cara ou coroa,jogue as opções dentro de uma lista
#depois crie um programa que imprimi 'cara' ou 'coroa' na tela.
'''face = ['cara', 'coroa']
print(random.choices(face))'''

#Desafio2 Sorteio de um nome entre 5 da lista , o nome deve ser exibido na tela:
'''nomes = ['Adriano', 'Lucia', 'Miguel', 'Tais', 'Maria']
print(random.choices(nomes))'''

print('O número sorteado foi:',(random.randint(10,100)))


