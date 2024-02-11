'''Desafios
Monte o seguinte cenário usando condicionais:Você está montando um sistema para um salão de beleza para calcular 
 o preço do corte de cabelos grandes que irá seguir as seguintes regras
 *Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00
 *Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00
 *Se seu cabelo estiver entre 31cm a 50 cm você paga o valor de R$100
 *Acima de 50cm Favor consultar na recepção'''

cabelo = 59
if cabelo <= 20:
    print('Você vai pagar R$50,00')
elif cabelo >= 21 and cabelo <=30:
    print('Você vai pagar R$70,00')
elif cabelo >=31 and cabelo <= 50:
    print('Você vai pagar o valor de R$100,00')
else:
    print('Favor consultar a recepção!')
