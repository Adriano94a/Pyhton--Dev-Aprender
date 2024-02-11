'''# Enumerate
for indice, numero in enumerate(range(1, 11),0):
    print(indice, numero)
    if indice == 5:
        print('Estamos na metade da lista')

nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']

for indice, nome in enumerate (nomes, 1):
    print(indice, nome)
    if indice == 3:
        print('Já temos 3 pessoas registradas ')
'''
#Desafio Itere sobre a lista Abaixo exibindo o número do indice + nome da fruta.
#Porém quando o índice for 3 exiba 'Nº índice + nome da fruta EM PROMOÇÃO'
frutas = ['Maça', 'Laranja', 'Morango', 'Limão']
for indice, fruta in enumerate(frutas,0):
    if indice == 3:
        print(f'{indice} {fruta} EM PROMOÇÃO' )
    else:
        print(indice, fruta)
    