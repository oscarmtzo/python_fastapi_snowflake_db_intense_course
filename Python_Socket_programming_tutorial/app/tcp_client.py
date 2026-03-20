import socket

#AF_INET = IPV4
#SOCK_STREAM = TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT_IP_ADDR = socket.gethostname()
print(CLIENT_IP_ADDR)

client.connect(("192.168.1.12", 8081))# le indicas al SO donde iniciar la conexion, y el puerto al que dirigirse
msg = "hola servidor".encode("utf-8")
client.send(msg)
client.close()

"""
while True:
    print(client.recv(1024).decode())
    print("Escibe un mensaje al servidor:")
    #client.send("Hola desde el cliente".encode("utf-8"))
    user_msg = input().encode("utf-8")
    client.send(user_msg)
    #print(client.recv(1024).decode())
    if user_msg == "SHUTDOWN":
        client.close()
    elif user_msg == "SHUTDOWN-SERVER":
        client.send
"""