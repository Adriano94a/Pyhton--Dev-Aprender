numero_atrasos = 3
if numero_atrasos >= 3:
    print('Vá para a diretoria!')
elif numero_atrasos == 2:
    print('Essa é sua segunda falta!')
elif numero_atrasos == 1:
    print('Essa é sua primeira falta!')
else:
    print('Aluno ideal, pode entrar!')

#Operador ternário

velocidade = 120
print('Você foi multado!') if velocidade >= 100 else print('Siga em frente!')