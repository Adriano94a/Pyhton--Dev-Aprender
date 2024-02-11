#Desafio 1 - Transformar a frase 1 em uma lista de palavras e guardar o resultado em uma variável chamada palavras1

frase1 = 'Desafio manipulação de string'
palavras1 = (frase1.split())
print(palavras1)

#Desafio2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2
frase2 = 'jhonatan,rafael,carol,camilla'
palavras2 = frase2.split(',')
print(palavras2)

#Desafio3: Pegue o palavras1 e transforme elas no seguinte string:
# "Desafio,manipulação,de,strings".Imprima o resultado no console
print(','.join(palavras1))

#Desafio4: Pegue o palavras2 e transforme elas no seguinte string: frase2 =
#jhonatan & rafael & carol & camilla". Imprima o resultado no console.

print(' & '.join(palavras2))