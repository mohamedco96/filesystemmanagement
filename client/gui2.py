import socket
import os
import tkinter as Hakim
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",9999))

root= Hakim.Tk()
root.title("File System Management")
canvas1 = Hakim.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

#label
label1 = Hakim.Label(root, text='File System Management')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

#label
label2 = Hakim.Label(root, text='Enter File Name')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

#File Name Text Filed
entry1 = Hakim.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

#Text Area
S = Hakim.Scrollbar(root)
T = Hakim.Text(root, height=4, width=50)
S.pack(side=Hakim.RIGHT, fill=Hakim.Y)
T.pack(side=Hakim.LEFT, fill=Hakim.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

#Insert into text area
quote = "Server Files Here"
T.insert(Hakim.END, quote)

#upload
def put():
    commandName='1'
    s.send(commandName.encode('utf-8'))
    # filename=input("Enter File Name To Send\n>>")
    filename = entry1.get()
    s.send(filename.encode('utf-8'))
    fileSize=os.stat("C:\\Users\\Mohamed Ibrahim\\ITI\\Project\\client\\"+filename).st_size
    fz=str(fileSize)
    s.send(fz.encode('utf-8'))
    with open("C:\\Users\\Mohamed Ibrahim\\ITI\\Project\\client\\"+filename, "rb") as f:
        for data in range(0,fileSize,1024):
            l=f.read(1024)
            s.sendall(l)
    label3 = Hakim.Label(root, text= 'File "' + filename + '" is Uploded Successful To Server',font=('helvetica', 10))
    canvas1.create_window(200, 270, window=label3)
    return 

#download
def get():
    commandName='2'
    s.send(commandName.encode())
    # filename=input("Enter File Name To Receive\n>>")
    filename = entry1.get()
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
    label3 = Hakim.Label(root, text= 'File "' + filename + '" is Download Successful From Server',font=('helvetica', 10))
    canvas1.create_window(200, 270, window=label3)
    return

def uthread():
    Thread(target=put,args=()).start()
    return  

def dthread():
    Thread(target=get,args=()).start()
    return

def ethread():
    s.send('exit'.encode())
    exit()
    return  

#buttons
Upload = Hakim.Button(text='Upload', command=uthread, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
Download = Hakim.Button(text='Download', command=dthread, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
Exit = Hakim.Button(text='Exit', command=ethread, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=Upload)
canvas1.create_window(200, 210, window=Download)
canvas1.create_window(200, 240, window=Exit)

root.mainloop()