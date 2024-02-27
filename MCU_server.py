#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

attributes = []
message = ""

while message != "END":
    
    #  Wait for next request from client
    message = socket.recv()
    message = message.decode("utf-8")
    print(f"Received request: {message}")
    
    attributes.append(message)
    
    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string(f"Recieved {message}")

print(attributes)