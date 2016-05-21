# client.py

import pjd                   # Importa seu modulo
filename = 'recebido.txt'
PORT=55555                 # Porto onde o servidor vai esperar por conexoes
SRV="nome da maquina"      # Nome da maquina onde o servidor sera executado


s = pjd.activeOpen(SRV,PORT) # Abre uma conexao

with open(filename, 'wb') as f:
    print 'Arquivo aberto/criado'
    while True:
        print('Recebendo dados...')
        data = s.recv(1024)        # Esse recv deve ser implementado por voce
        if not data:
            break
        f.write(data)              # salva os dados no arquivo

f.close()
print('Arquivo recebido')
s.close()                          # Esse close deve ser implementado por voce
print('Conexao fechada')
