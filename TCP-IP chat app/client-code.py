#ChatRoomClient

#Citations: 
#https://www.biob.in/2018/04/simple-server-and-client-chat-using.html
#https://pymotw.com/2/socket/tcp.html
#https://www.geeksforgeeks.org/simple-chat-room-using-python/
#TCP Client example provided by the professor Ruben Balmaceda

#Importing the necessary modules
from socket import socket, AF_INET, SOCK_STREAM

print("\nWelcome to Chat Room\n")
print("Initialising....\n")

serverName = 'localhost'
serverPort = 12001
#creating a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
name = input(str("\nEnter your character's fav name: "))
print("\nTrying to connect to ", serverName, "(", serverPort, ")\n")
#connecting to the server at the IP address and port number specified
clientSocket.connect((serverName, serverPort))
print("Connected...\n")

#sends an encoded message to the server through TCP
clientSocket.send(name.encode())
#gets a message back from the server through TCP
s_name = clientSocket.recv(1024)
#decodes teh message from the server
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

#while the TCP connection with the server was succeful then messages will
#be exchanged between the client and the server
while True:
    #gets a message from teh server through TCP
    message = clientSocket.recv(1024)
    #decodes the message
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me : "))

    #if the client wants to exit the chat room then, the server will get notified
    if message == "[exit]":
        message = "Left chat room!"
        clientSocket.send(message.encode())
        print("\n")
        break
    clientSocket.send(message.encode())