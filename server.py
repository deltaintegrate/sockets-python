import zmq

ctx = zmq.Context()
s = ctx.socket(zmq.REP)
s.bind("tcp://*:5555") #conexion sistema puerto operativo

while True:
    m = s.recv() #recibe el mensaje
    pint("mensaje recibido {}".format(m)) #imprimo el mensaje
    s.send_string("mundo")
    
print("esto no deberia aparecer")