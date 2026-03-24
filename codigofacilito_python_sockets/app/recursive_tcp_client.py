import socket

def ask_usr_shotdown_socket():
    try:
        user_input = input("Deseas terminar la conexión? [y/n]")
        if user_input.lower() == "y":
            print("Okay cerrando socket ....")
            return True
        elif user_input.lower() == "n":
            return True
        else:
            print("no te entendi, seguiré probando la conexión, puedes cerrar en cualquier momento con ctr + 'c'")
            pass
    except: #cuando pulsas 'ctrl' + 'c' y quieres seguir probando el server de nuevo
        print("\nno te entendi, seguiré probando la conexión, puedes cerrar en cualquier momento con ctr + 'c'")
        pass

client_socket = socket.socket()
while True:
    try:
        print(f"intentando conectar con server {'localhost'} en puerto {8000}")
        client_socket.connect( ("localhost", 8000) )
        client_socket.send("Hola servidor desde el cliente".encode("utf-8"))
        print(client_socket.recv(1024))
    except ConnectionRefusedError: #cuando intentas conectar y no hay nadie escuchando 
        print("-> \tEl server esta apagado")
        client_socket.close()
        try:
            if ask_usr_shotdown_socket():
                break
        except KeyboardInterrupt:
            if ask_usr_shotdown_socket():
                break
    except BrokenPipeError: # cuando intentas escribir al server_socket pero ya cerró
        if ask_usr_shotdown_socket():
            break
    except KeyboardInterrupt: #cuando pulsas 'ctrl' + 'c'
        if ask_usr_shotdown_socket():
            break
    except OSError: #cajon de errores del S.O. que aun no puedo clasificar
        try:
            if ask_usr_shotdown_socket():
                break
        except KeyboardInterrupt: #cuando pulsas 'ctrl' + 'c'
            break