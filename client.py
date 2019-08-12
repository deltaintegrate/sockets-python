import zmq

ctx = zmq.Context()
s = ctx.socket(zmq.REQ)
s.connect("tcp://192.168.17.27:5555") #conexion sistema puerto operativo

s.send_string("Hola Gonorreas")
m = s.recv()
print("recibi:{}".format(m))
