# SET
numeros = [2, 2, 5, 8]
frutas = {'maça', 'uva', 'banana', 'maça', 'morango'}
#Convertendo para set
set_numeros = set(numeros)
set_frutas = set(frutas)

print(set_numeros)
print(set_frutas)
#adicionando novos valores
set_numeros.add(10)
print(set_numeros)

#conjuntos
numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]
a = set(numeros1)
b = set(numeros2)
#encontrar valores diferentes
print(a.symmetric_difference(b))
#encontrar valores em comum
print(a.intersection(b))
#fazer união dos valores únicos
print(a.union(b))

