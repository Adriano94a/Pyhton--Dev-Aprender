import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(levelname)s - %(asctime)s') #setar o nível

try:
    email = input('Digite seu e-mail: ')
    senha = int(input('Digite sua senha bancária: '))
    if senha == '1234':
        logging.info(f'{email} entrou em sua conta bancária')
except ValueError as erro:
    print('favor Digitar apenas números')
    logging.warning(erro)