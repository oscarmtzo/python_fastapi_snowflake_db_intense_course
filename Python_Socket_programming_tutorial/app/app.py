import socket
import threading #crea multiples hilos en nuestro programa principal de python

#mientra un pieza de codigo esta esperando, otra parte puede ejecutarse (parecido a async)

#Definir un puerto
PORT = 5050

SERVER_LOCALIP = socket.gethostbyname(socket.gethostname()) #obtiene automaticamente la IPV4 automaticamente de tu red local de tu dispositivo pc(servidor)
# print(SERVER) # 192.168.1.12
#print(socket.gethostname())

ADDRESS = (SERVER_LOCALIP, PORT) #definido como una tupla – valores inmutables
print(type(ADDRESS))

# debemos parasle un tipo de socketFamily (tipo de socket eg. - socket de bluetooth, IPV6, IPV4 = AF_INET, )
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDRESS)

def handle_client(connection, address):
    pass

def start():
    server.listen()
    while True:
        server.ac
    pass

print("server has started")
start()