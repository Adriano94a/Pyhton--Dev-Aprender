#Desafio manipulação de arquivos
#Criação de 3 listas, frutas, cores e linguagens de programação

import os


frutas = ['Manga', 'Banana', 'Pera', 'Morango', 'Kiwi']
cores = ['Azul', 'Verde', 'Roxo' ,'Cinza','Rosa']
linguagens = ['Python', 'C++', 'PHP', 'Java', 'React']

''''Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todas as 5 frutas
que estão na lista de frutas'''

with open('frutas.txt', 'w', newline='') as arquivo:
       for fruta in frutas:
            arquivo.write(str(fruta) + os.linesep)

'''Desafio 2 - Imprima na tela todas as linhas que estão dentro do arquivo frutas.txt'''
with open('frutas.txt', 'r') as arquivo:
        for linha in arquivo:
            print(linha)

'''Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores
que estão dentro da sua lista de cores ao arquivo frutas.txt'''

with open('frutas.txt', 'a', newline='') as arquivo:
      for cor in cores:
          arquivo.write(os.linesep + cor)
'''Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo , de forma com que cada linguagem 
ocupe apenas uma linha'''
with open('Top 5 Linguagens.txt', 'w', newline='') as arquivo:
     for linguagem in linguagens:
          arquivo.write(linguagem + os.linesep)

#Bonus - Como você poderia criar vários arquivos vazios, usando um laço for ?
arquivos = ['musica.mp3', 'foto.jpg', 'senhas.txt', 'relatorio.pdf']
for arquivo in   arquivos:
      with open(arquivo, 'w') as arquivo:
            pass    