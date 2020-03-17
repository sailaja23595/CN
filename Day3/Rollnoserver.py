import socket, os
print('MSIT Attendance Marking-2019')
roll_number_list = [2019501088, 2019501057, 2019501058, 2019501067, 2019501063,201950100,2019501023]
string = str(roll_number_list[0])
print('students in the class: \n')
print(roll_number_list)

s=socket.socket()
s.bind(('127.0.0.1',8188))
s.listen(10)
while True:
        conn,addr = s.accept()
        roll_number = conn.recv(1024).decode()
        checkroll = int(roll_number)
        if checkroll in roll_number_list:
                roll_number_list.remove(checkroll)
                print("Attendance marked for" + roll_number + "\n")
                print("Absentees are"+ str(roll_number_list)+"\n")
        else:
                print("roll_number is not found \n")
s.close()