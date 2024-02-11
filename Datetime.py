'''#Aula011 Datetime
from datetime import datetime
print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year )

#Criar uma data
lancamento_app = datetime(2023, 4, 1)
print(lancamento_app)
#quero receber a data lançamento do meu aplicativo
#01/04/2023
data_de_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo? '),'%d/%m/%Y')
print(type(data_de_lancamento))
#Calcular intervalo de datas
data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)
'''
#Desafio
#Calcule quantos dias faltam até o seu aniversário

from datetime import datetime
aniversario = datetime(2024,1,10)
dias_aniver = aniversario - datetime.now()
print(f'Faltam exatos {dias_aniver} dias para seu aniversário!')