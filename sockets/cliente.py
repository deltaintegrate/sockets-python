import socket

my_socket = socket.socket()
my_socket.connect(('localhost',8050))


my_socket.send("Hola soy el cliente")
respuesta = my_socket.recv(1024)

print respuesta
my_socket.close()
