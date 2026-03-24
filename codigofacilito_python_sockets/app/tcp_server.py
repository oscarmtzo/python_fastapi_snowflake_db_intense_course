import socket

#valores por defecto al crear el socket 
server_socket = socket.socket()
#family=-1, type=-1, proto=-1, fileno=None 

#necesita una tupla con el address = host + port
server_socket.bind( ('localhost', 8000) )
#localhost -> IPV4: 127.0.0.1 - pruebas locales sin salir a internet de la red local o exterior – solo acepta conexiones desde la misma máquina

# AF_INET = usar IPv4
# localhost / 127.0.0.1 = solo máquina local
# 0.0.0.0 = escuchar en todas las interfaces IPv4 de la máquina inclusive IP WiFi – IP Ethernet

#cantidad de peticiones que puede encolar o manejar en cola nuestro socket
server_socket.listen(5)# para mantener hasta 5 conexiones al pendientes de ser aceptadas (encoladas)

while True:
    try:
        client_conn_obj, client_address = server_socket.accept()#desempaquetado tupla que devuelve el metodo accept()
        print(client_address)
        client_msg = client_conn_obj.recv(1024).decode("utf-8") # leer hasta 1024 bytes en esa llamada
        print(f"Mensaje del cliente: {client_msg}")
        client_conn_obj.send("hola desde el tcp_server".encode("utf-8"))
        print("Cerrando conexion del cliente")
        print(client_conn_obj)
        client_conn_obj.close()
        #break
    except KeyboardInterrupt:
        respuesta_user = input("\nestas seguro que quieres cerrar consola [y/n]? ")
        if respuesta_user.lower() == "y":
            print("\ncerrando server")
            server_socket.close()
            break
        elif respuesta_user.lower() == "n":
            pass
        else:
            print("\nno entendi – seguire encendido o presiona 'ctrl' + 'c'")
            pass