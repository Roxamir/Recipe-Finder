#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import time
context = zmq.Context()

#  Socket to talk to server
print("Connecting to MCU...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

attributes = ["Spider-Man", 10, 20, 30, 40, "Hulk", 40, 40, 40, 40, "END"]

#  10 requests, 5 for each character
print(f"Sending attributes...")
for request in range(11):
    print("Sending " + str(attributes[request]))
    socket.send_string(str(attributes[request]))
    time.sleep(1)
    #  Get the reply.
    message = socket.recv()
    message = message.decode("utf-8")
    print(f"Received reply {request} [ {message} ]")