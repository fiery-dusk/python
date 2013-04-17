import socket
import sys
import time
host=('')
port=(int('7879'))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((host, port))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
s.listen(5)
print "Socket now listening"
conn, addr = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])
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
conn.recv(1024)
print("Waiting for other player")
print ("")

conn.sendall('3')
print("3")
time.sleep(1)
conn.sendall('2')
print("2")
time.sleep(1)
conn.sendall('1')
print("1")
time.sleep(1)
conn.sendall('Begin!')
print("What is your choice")
p1=raw_input(": ")
p2=conn.recv(1024)
result=((2**float(p1))/(2**float(p2)))
if result ==.25 or result ==2:
    winner="player 1"
elif result ==.5 or result==4:
    winner="player 2"
elif result ==1:
    winner="no one"
else:
    print"summin' went wrong"
conn.sendall(str(winner)+" wins!")
print(str(winner)+" wins!")
raw_input("press enter to continue")
s.close
