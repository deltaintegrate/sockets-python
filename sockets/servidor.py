import socket

my_socket = socket.socket()
my_socket.bind(('localhost',8050))
my_socket.listen(5)

while True:
    conexion, dirr = my_socket.accept()
    print "nueva conexion establecida"
    print dirr

    conexion.send("Buenos Dias Clase Distribuidos")
    conexion.close()

