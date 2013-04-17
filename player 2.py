import socket
import sys
import time
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=raw_input("Enter the address of the host(player 1: ")
port=(int("7879"))

ip=(socket.gethostbyname(host))
print("Ip adress is ", ip)
s.connect((ip, port))
print ("Socket connected to "+host+" on ip "+ip)
print ("How to play:")
print ("When prompted enter the number of your choice then press enter")
print ("The options are:")
print ("1.Paper")
print ("2.Scissors")
print ("3.Rock")
print ("")
print('get ready to play.')
print ("")
raw_input("Press enter when you are ready")
s.sendall("Ready")
print ("")
while 1:
    data=(s.recv(1024))
    if data=="Begin!":
        print (data)
        break
    else:
        print (data)
print("What is your choice")
p2=raw_input(": ")
s.sendall(p2)
print (s.recv(1024))
raw_input("press enter to continue")
