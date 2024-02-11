#1 - Copie o arquivo nomes.txt para a pasta 'Arquivos 2010'
import shutil
import os

shutil.copy(src=os.getcwd() + os.sep + 'Cursos' + os.sep +'Manipula_arquivo' + os.sep + 'nomes.txt', 
            dst=os.getcwd() + os.sep + 'Cursos' + os.sep + 'Manipula_arquivo' + os.sep + 'Arquivos 2010')

shutil.move(src=os.getcwd() + os.sep + 'Cursos' + os.sep +  'Manipula_arquivo' + os.sep + 'inscrições.pdf',
            dst=os.getcwd() + os.sep + 'Cursos' + os.sep +  'Manipula_arquivo' + os.sep + 'Documentação')

