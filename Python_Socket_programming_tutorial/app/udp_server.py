#UDP server side
import socket

#usara tambien INET = IPV4
#usara esta vez SOCK_DGRAM = UPD
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #indicamos que usa IPV4 y UDP al SO 

PORT = 8082
SERVER_IP_ADDRESS = socket.gethostname() #Obtenemos dinamicamnte la IPV4
#requiere el metodo bind() para atarlo ambas (IPV4 y PORT) para que se relacionen 
server_socket.bind(SERVER_IP_ADDRESS, PORT)#indicaremos el puerto a usar 8082