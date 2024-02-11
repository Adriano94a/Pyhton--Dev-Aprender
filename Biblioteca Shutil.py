import shutil
import os

shutil.copy(src=os.getcwd() + os.sep + 'fotos' + os.sep + 'foto1.jpg',
            dst=os.getcwd() + os.sep + 'backup')

shutil.copytree(src=os.getcwd() + os.sep + 'fotos',
                dst=os.getcwd() + os.sep + 'fotos backup')

shutil.move(src=os.getcwd() + os.sep + 'fotos backup',
            dst=os.getcwd() + os.sep + 'backup')

shutil.move(src=os.getcwd() + os.sep + 'fotos' + os.sep +
            'foto2.jpg',dst=os.getcwd() + os.sep + 'backup')

shutil.rmtree(os.getcwd() + os.sep + 'musicas') #para excluir todo uma pasta

shutil.make_archive('backup_fotos', 'zip', os.getcwd() + os.sep + 'fotos') #compactar um arquivo

shutil.make_archive('backup_vs_code', 'zip', os.getcwd()) #Compactar toda uma pasta

shutil.unpack_archive('backup_vs_code.zip','backup_vs_code') #Descompactar
