#Métodos Comuns
#Métodos de Classe(Class Methods)
#Métodos estáticos(Static Methods)
class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria_ram,
              self.placa_de_video, self.sistema_operacional)
        
    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de vídeo - Alto Nível')
    
    @classmethod
    def computador_configuracao_pesado(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo - Alto Nível')
    
    @staticmethod
    def roda_programa_pesado(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False
        
print(Computador.roda_programa_pesado(10))

#Configuração para cliente de escritório
Computador1 = Computador.computador_escritorio('8gb')
#Configuração para  cliente de trabalho pesado(jogos, videos ,3D)
Computador2 = Computador.computador_configuracao_pesado('16gb')


import datetime




    
