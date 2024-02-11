 #Variaveis de uma classe
class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self,marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Estou ligando o computador')

Computador.sistema_operacional = 'Windows 7'

#Computador.marca não funciona
computador = Computador ('Dell', '8gb', 'Nvida')
computador.marca = 'Asus'
print(computador.marca)
print(computador.sistema_operacional)

Computador.sistema_operacional = 'Mac'
computador2 = Computador( 'Asus', '2gb', 'ATI')
print(computador2.sistema_operacional)
