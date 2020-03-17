import socket
def main():
	host = 'localhost'
	port = 8818
	server = ('localhost', 8888)

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	message = input("Client Input : ")
	while message != '.':
		s.sendto(message.encode(), server)
		data, addr = s.recvfrom(1024)
		print('Received from server as : ' + str(data.decode()))
		message = input("Client Input : ")
	s.close()

if __name__ == '__main__':
	main()
