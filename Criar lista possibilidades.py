#Como podemos criar listas ?
# Criar listas usando loops e Range()
numeros = []
for i in range (1,6):
    numeros.append(i)
print(numeros)
#Map
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']

def aprovar_pessoa(nome):
    return nome + ' APROVADO'

print(list(map(aprovar_pessoa, nomes)))