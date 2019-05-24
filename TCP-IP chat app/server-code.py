#ChatRoomServer

#Citations: 
#https://www.biob.in/2018/04/simple-server-and-client-chat-using.html
#https://pymotw.com/2/socket/tcp.html
#https://www.geeksforgeeks.org/simple-chat-room-using-python/
#TCP Server example provided by the professor Ruben Balmaceda


#TCP (SOCK_STREAM) is a connection-based protocol. The connection is established and the two 
#parties have a conversation until the connection is terminated by one of the parties or by a network error.
#Importing the necessary modules
from socket import socket, SOCK_STREAM, AF_INET

print("\nMariana's Chat Room to talk about GOT\n")
print("Initialising....\n")

#creating a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort=12001
#binding the socket with the IP address and port number
serverSocket.bind(('', serverPort))
name = input(str("Enter your character's fav name: "))

#enabling the server to accept connectios from the client           
serverSocket.listen(1)
print("\nWaiting for incoming connections...\n")

#wait and accepts the client's connection request
conn, addr = serverSocket.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

#recieving the message sent to the server through TCP
s_name = conn.recv(1024)

#using codec the message is decoded
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")

#sends an encoded message to the client through TCP
conn.send(name.encode())

#while the TCP connection with the client was succeful then messages will
#be exchanged between the client and the server
while True:
    message = input(str("Me : "))
    #if the server wants to exit the chat room then, the server will get notified
    if message == "[exit]":
        message = "Left chat room!"
        #sends an encoded message to the client through TCP
        conn.send(message.encode())
        print("\n")
        break
    #sends an encoded message to the client through TCP
    conn.send(message.encode())

    #recieving the message sent to the server through TCP
    message = conn.recv(1024)
    #using codec the message is decoded
    message = message.decode()
    print(s_name, ":", message)