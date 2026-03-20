# el SO crea un socket y retorna una administrador (file descriptor – indice/referencia del recurso que el proceso creó)
import socket

import time

#domain = tipo de IPV4-6, 
#family/type = tipo de protocolo (_STREAM = TCP, _DGRAM = UDP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind – le dice al SO que direccion usar y que puerto – los envuelve
SERVER_IP_ADDRESS = socket.gethostname()
#socket.gethostbyaddr((hostname/IP number)) -> [(name), (aliaslist), (addresslist)]

print(SERVER_IP_ADDRESS, type(socket.gethostname()))
#bind(<IP_number_addr>, <port>)
server.bind((SERVER_IP_ADDRESS, 8081)) #une ambos ip_num_addr y puerto

#.listen()
server.listen() # le indica el SO que acepte conexiones entrantes en el puerto 8081

client_socket_connection, address = server.accept()# le indica al SO que acepte las conexiones y que configure la direccion entrante 
while True:
    #.accept() -> retorna la conexion y la direccion 
    #client_socket_connection, address = server.accept()# le indica al SO que acepte las conexiones y que configure la direccion entrante 
    try:
        print( f"direccion: {address}")
        print(client_socket_connection.recv(1024).decode())
    finally:
        closed = server.close()
        if closed == None: 
            print("cerrando server ...")
            break
    
