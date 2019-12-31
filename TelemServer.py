from socket import *
import numpy as np
HOST=''
PORT=52849
BUFSIZE=1024
ADDR=(HOST,PORT)
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
print('Waiting for connection')
tcpCliSock,addr=tcpSerSock.accept()
print('...connected from:',ADDR)
L = 0
V = 0
R = 0
C = 0

while True:
    n = np.random.random()
    tcpDataSock,addr=tcpSerSock.accept()
    print("accepted")
    message = str(n)+'welcome to the server!\r\n' #str(L)+','+str(V)+','+str(R)+','+str(angle)+'\r\n'
    tcpDataSock.send(message.encode('UTF-8'))
    print(n)
