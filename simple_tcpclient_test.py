import socket
import sys
import os

#Command : xxxx.py arg1 arg2 arg3

if __name__ == '__main__':

	HOST = '2001:2b8:10:1:a4f8:aafa:2152:a3e2'
	PORT = 5000
	print (HOST,":",PORT)

	var = 1 # for while

	s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

	s.connect((HOST, PORT))
	print ('...connected!')

	while True:
		try:
			data = s.recv(1024)
			if not data:
				s.close()
				break

			s.send(data)
		except KeyboardInterrupt:
			print 'Interrup'
			s.close()
			sys.exit()

