#Criando e lendo arquivo CSV lendo direto no Terminal
from csv import DictReader, DictWriter

'''with open('csv_exemplo.csv') as arquivo:
    dados = DictReader(arquivo)
    for dado in dados:
        print(dado['OrderId']+ '' + dado['Age'])'''


# Criar um arquivo CSV

'''
with open('computadores.csv','w',newline='',encoding='utf-8') as arquivo:
    '''
cabecalho = ['Marca','Preço','Ano de Lançamento']
'''
    csv_writer = DictWriter(arquivo,fieldnames=cabecalho)
    csv_writer.writeheader()
    csv_writer.writerow({
        'Marca': 'Asus',
        'Preço': 2500,
        'Ano de Lançamento': 2014
    })
    csv_writer.writerow({
        'Marca': 'Dell',
        'Preço': 4000,
        'Ano de Lançamento': 2018
    })
    csv_writer.writerow({
        'Marca': 'Positivo',
        'Preço': 1500,
        'Ano de Lançamento': 2023
    }),'''

#Alterando um arquivo CSV

with open('Computadores.csv', 'r', newline='',encoding='utf-8') as arquivo_original:
    dados_originais = DictReader(arquivo_original)
    computadores = list(dados_originais)
    with open('computadores_v2.csv','w', newline='', encoding='utf-8') as novo_arquivo:
        csv_writer = DictWriter(novo_arquivo, fieldnames=cabecalho)
        csv_writer.writeheader()
        for computador in computadores:
            csv_writer.writerow({
                'Marca': computador["Marca"],
                'Preço': 'R$' + computador["Preço"],
                'Ano de Lançamento': computador["Ano de Lançamento"]
            })


