import socket

# Configuración del servidor
HOST = "0.0.0.0"   # Escucha en todas las interfaces de red
PORT = 8000        # Puerto de comunicación (puedes cambiarlo)

# Crear socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor escuchando en {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"Conectado con: {addr}")

while True:
    data = conn.recv(1024)  # Recibe mensaje
    if not data:
        break
    print("Cliente:", data.decode("utf-8"))
    conn.sendall(b"Mensaje recibido!")  # Respuesta al cliente

conn.close()
server_socket.close()
