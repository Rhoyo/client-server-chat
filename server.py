import socket
import sys

#create Server socket
def serverStart(port):
    serverS=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverS.bind(('localhost', int(port)))
    serverS.listen(1)
    print("Server listening on: localhost",int(port))
    return serverS

def sendMsg(connectionS):
    msg = input("Server: ")

    #if user inputs "/q" then disconnect flag raised
    if msg == "/q":
        print("Server disconnected from chat")
    else:
        msg = "Server: " + msg
    connectionS.send(msg.encode())

    return msg

def recvMsg(connectionS):
    msg = connectionS.recv(4096).decode()

    #if client sends "/q" to user, raise client disconnect
    if msg == "/q":
        print("Client disconnected from chat")
    else:
        print("Client:",msg)
        msg = sendMsg(connectionS)

    return msg

#main
if len(sys.argv)<2:
    print("run with python3 server.py [port]")
    sys.exit(0)

serverS=serverStart(sys.argv[1])
connectionS, addr = serverS.accept()
print("Client connected at ", addr)
print("--------ChatRoom--------")

msg=""
while msg!="/q":
    msg=recvMsg(connectionS)

connectionS.close()
serverS.close()
