import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost",9999))
s.listen(1)
sc, address = s.accept()
while(True):
    print ('New client connected ..')
    print (address)
    print ('Wait For Req...')
    reqCommand = sc.recv(1024)
    reqCommand=reqCommand.decode('utf-8')
    print ('Client Req is> %s' %(reqCommand))
    if (reqCommand == 'exit'):
        break
    if (reqCommand == '1'):
        fileName=sc.recv(1024)
        fileName=fileName.decode('utf-8')
        fileSize=sc.recv(1024)
        fileSize=fileSize.decode('utf-8')
        fz=int(fileSize)
        with open('C:\\Users\\Mohamed Ibrahim\\ITI\\Project\\server\\'+fileName,'wb') as f:
            print('1')
            # l = sc.recv(1024)
            print('2')
            for data in range(0,fz,1024):
                print('3')
                l = sc.recv(1024)
                print('4')
                if not l:
                    break
                f.write(l)
                print('5')
                # f.close
                print('6')
                break 
                print('7')
            print('8')    
        print("File has Receive Successful From Client")
    if (reqCommand == '2'):
        fileName=sc.recv(1024)
        fileName=fileName.decode()
        with open('C:\\Users\\Mohamed Ibrahim\\ITI\\Project\\server\\'+fileName,'rb') as file_to_send:
                for data in file_to_send:
                    sc.sendall(data)
        print ('File has Send Successful To Client')
sc.close()
s.close()
