#Exemplo com o usuário nos passando seu nome
def boas_vindas (nome):
    print(f'Seja bem vindo {nome} é um prazer te receber!')

nomes = str(input('Digite seu nome: '))

boas_vindas(nomes)

'''DESAFIO 1
Crie uma função chamada gerar_nome_completo que recebe
como parametro o nome e sobrenome de alguém e dá boas vindas
para essa pessoa '''

def gerar_nome_completo(nome, sobrenome):
    print(f'{nome} {sobrenome}')

gerar_nome_completo('Jeff', 'Bezos')