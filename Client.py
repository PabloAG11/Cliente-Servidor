import socket

# Configuración del cliente
HOST = "192.168.1.100"  # IP del servidor (cámbiala por la IP de la otra PC)
PORT = 8000             # Debe coincidir con el puerto del servidor

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Escribe un mensaje (o 'salir' para terminar): ")
    if message.lower() == "salir":
        break
    client_socket.sendall(message.encode("utf-8"))
    data = client_socket.recv(1024)
    print("Servidor:", data.decode("utf-8"))

client_socket.close()
