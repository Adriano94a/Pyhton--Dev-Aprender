from datetime import datetime
import random
nome = input('Digite seu nome:')
idade = int(input('Digite sua idade atual:'))
data_cadastro = datetime.now()
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
data_aniv =datetime.strptime(input('Sua data de aniversário seria?'),'%d/%m/%Y')
sorteio = random.choices(cartoes)



print('-----------------------')
print (f'Olá {nome},seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}. \nParabéns! Houve um sorteio e você ganhou um cartão de compras no valor de {sorteio}')