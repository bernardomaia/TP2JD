# server.py

import pjd                 # Importa seu modulo 
filename='tp1.txt'         # Garanta que esse arquivo existe
PORT=55555                 # Porto onde o servidor vai esperar por conexoes

print 'Servidor iniciando....'
conn, addr = pjd.passiveOpen(PORT) # Passive open inicia o lado do servidor
print 'Recebeu conexao originada em ', addr

f = open(filename,'rb')
l = f.read(1024)
while (l):
    conn.send(l)           # voce deve implementar essa funcao
    l = f.read(1024)
f.close()

print('Fim do envio')
conn.close()               # voce deve implementar essa funcao
