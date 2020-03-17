import socket
host = 'localhost'
port = 8188
s= socket.socket()
s.connect((host,port))
print('MSIT Attendance Marking-2019')
print('Enter your roll number:')
roll_number = input()
s.send(roll_number.encode())
s.close()
