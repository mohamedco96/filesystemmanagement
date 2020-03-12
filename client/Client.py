import socket
import os
# fileSize=os.stat("C:\\Users\\Mohamed Ibrahim\\ITI\\Project\\client\\"+filename).st_size
#         for data in range(0,fileSize,1024):
#             l=f.read(1024)
#             s.sendall(l)
def put(commandName):
    s.send(commandName.encode('utf-8'))
    filename=input("Enter File Name To Send\n>>")
    s.send(filename.encode('utf-8'))
    fileSize=os.stat("C:\\Users\\Mohamed Ibrahim\\ITI\\Project\\client\\"+filename).st_size
    fz=str(fileSize)
    s.send(fz.encode('utf-8'))
    with open("C:\\Users\\Mohamed Ibrahim\\ITI\\Project\\client\\"+filename, "rb") as f:
        for data in range(0,fileSize,1024):
            l=f.read(1024)
            s.sendall(l)
    print ('File has Send Successful To Server')
    return 
    # l = f.read(1024)
    # while (l):
    #     s.send(l)
    #     l = f.read(1024)
    # print("File has send")
    # Continue()
def get(commandName):
    s.send(commandName.encode())
    filename=input("Enter File Name To Receive\n>>")
    s.send(filename.encode())
    with open('C:\\Users\\Mohamed Ibrahim\\ITI\\Project\\client\\'+filename, 'wb') as f:
        while True:
            data = s.recv(1024)
            if not data:
                break
            else:
                print (data)
                f.write(data)
                # f.close()
            break
    print ('File has Receive Successful From Server')
    return
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",9999))

while(1):
    chose=input('--------------------------------------\nEnter The Number Of Operation You Want\n--------------------------------------\n1-Send File To Server\n2-Get File From Server\n3-Show Your File In Directory\n4-Show Your File In Server\n5-Exit\n>>')
    if(chose=='1'):
        put(chose)
    if(chose=='2'):
        get(chose)
    if(chose=='3'):
        print("Client Files\n")
        clientFiles = os.listdir('C:\\Users\\Mohamed Ibrahim\\ITI\\Project\\client')
        print(clientFiles)
    if(chose=='4'):
        print("Server Files\n")
        serverFiles = os.listdir('C:\\Users\\Mohamed Ibrahim\\ITI\\Project\\server\\')
        print(serverFiles)
    if(chose=='5'):
        s.send('exit'.encode())
        break
s.close()