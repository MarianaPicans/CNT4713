#UDPServer.py

#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one 
#datagram and get one reply and then the connection terminates.
import time
import random
from socket import socket, SOCK_DGRAM, AF_INET

#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
#AF_INET is the Internet address family for IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print ("Waiting for connections")
while True:
    start = time.time()
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(2048)
    print (message, address)
    message = message.upper()
    if rand < 4:
        print("The packet was lost")
    else:
        serverSocket.sendto(message, address)
    end = time.time()
    rtt = end - start
    print ("RTT = ", str(rtt))
serverSocket.close()


#Configure the server so that it randomly drops packets.
#Include information about how long each response took. This will be the RTT.

#Citations: 
#https://stackoverflow.com/questions/38174877/python-measuring-dns-and-roundtrip-time
#https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/
#https://stackoverflow.com/questions/37650716/python-fixed-wait-time-for-receiving-socket-data

