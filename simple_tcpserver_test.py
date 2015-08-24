import socket
import sys
import os

#Command : xxxx.py arg1 arg2 arg3

if __name__ == '__main__':

	HOST = ''
	PORT = 5000
	print (HOST,":",PORT)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)

	conn, addr = s.accept()
	print 'Connected by', addr

	while 1:
		data = conn.recv(1024)
		if not data: break
		conn.send(data)
	conn.close()

