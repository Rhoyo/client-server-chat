import socket

#create client socket
def startClient():
    clientS = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    clientS.connect(('localhost', 3501))
    print("Client connecting on: localhost 3501")
    return clientS

#main
client = startClient()

msg="Client Connected"
print("\n")
print("--------ChatRoom--------")

while True:
    msg = input("Client: ")
    client.send(msg.encode())

    #if "/q" is typed client disconnects
    if(msg== "/q"):
        print("Client disconnected from chat")
        break

    #receive server message and print, if "/q" then server disconnected, disconnect
    msg= client.recv(4096).decode()
    if(msg== "/q"):
        print("Server disconnected from chat")
        break

    print(msg)

client.close()
