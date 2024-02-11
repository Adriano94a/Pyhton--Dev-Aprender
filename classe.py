'''#classe
class Computador:
    def __init__(self):
        self.marca = 'Asus'
        self.memoria_ram = '8gb'
        self.placa_de_video = 'NVIDIA'

#marca , memória ram, placa de vídeo
computador1 = Computador()
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_video)
'''
#classe
class Computador:
    def __init__(self, marca,memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

#marca , memória ram, placa de vídeo
computador1 = Computador('Asus', '8Gb', 'Nvidia')
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_video)
computador2 = Computador('Dell', '6Gb', 'ATI')
print(computador2.marca)
print(computador2.memoria_ram)
print(computador2.placa_de_video)
computador3 = Computador('Positivo', '12Gb', 'Intel')
print(computador3.marca)
print(computador3.memoria_ram)
print(computador3.placa_de_video)
