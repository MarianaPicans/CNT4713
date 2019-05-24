#UDPClient.py


from socket import socket, SOCK_DGRAM, AF_INET, timeout

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, addr = clientSocket.recvfrom(2048)
print (modifiedMessage, addr)
clientSocket.close()

#Allow the client to give up if no response has been reveived within 1 second.

#Citations: 
#https://stackoverflow.com/questions/38174877/python-measuring-dns-and-roundtrip-time
#https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/
#https://stackoverflow.com/questions/37650716/python-fixed-wait-time-for-receiving-socket-data