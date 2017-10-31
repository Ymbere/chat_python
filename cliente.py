import socket
import threading
import sys
import pickle

class Cliente():
	
	def __init__(self, host='10.114.79.40', port=52413):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		self.sock.connect((host, port))


		msg_recv = threading.Thread(target=self.msg_recv)

		msg_recv.daemon = True
		msg_recv.start()

		while True:
			msg = input('->')
			if msg != 'sair':
				self.send_msg(msg)
			else:
				self.sock.close()
				sys.exit()

	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def send_msg(self, msg):
		self.sock.send(pickle.dumps(msg))


c = Cliente()