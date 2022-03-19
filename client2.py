from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import time
import os

connection_code = "45 15f 72 65 66 20 59 69 11f 69 74 62 61 15f 131"

try:
    def display():
        while True:
            data, addr = sock.recvfrom(1024)
            data = data.decode()
            if data == "ls":
                data = os.popen("ls")
                data = data.read()
                sock.sendto(data.encode(),host)
            else:
                data = data.split("=")
                print(data[0]+"\n"+data[1])
                print()

                

    def get_ip():
        s = socket(AF_INET, SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def sendconnection():
        sock.sendto(connection_code.encode(), host)

except:
    pass

def file_downlaod():
    client_ip = input("Enter client ip > ")
    port_number = 5001

    s = socket()
    s.connect((client_ip, port_number))

    filename = input("Filename > ")
    if filename != 'q':
        s.send(filename.encode())
        data = s.recv(1024)
        data = data.decode()
        if data[:6] == 'EXISTS':
            filesize = int(data[6:])
            message = input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send("OK".encode())
                f = open(filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print("{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done")
                print("Download Complete!")
                f.close()
        else:
            print("File Does Not Exist!")

    s.close()

def RetrFile(sck):
    filename = sck.recv(1024)
    filename = filename.decode()
    if os.path.isfile(filename):
        sck.send(("EXISTS " + str(os.path.getsize(filename))).encode())
        userResponse = sck.recv(1024)
        userResponse = userResponse.decode()
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sck.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sck.send(bytesToSend)
    else:
        sck.send("ERR ".encode())

    sck.close()

def file_share():
    m_ip = "25.61.11.161"
    port_number = 5001


    s = socket()
    s.bind((m_ip,port_number))

    s.listen(5)

    while True:
        c, addr = s.accept()
        print("client connedted ip:<" + str(addr) + ">")
        RetrFile(c)
        


host = ("25.61.11.161", 4567)
my_ip = ("25.61.11.161", 4545)
sock = socket(family=AF_INET, type=SOCK_DGRAM)
sock.bind(my_ip)
sendconnection()
taccept = Thread(target=display).start()
recive = Thread(target=file_share).start()

while True:
    down_load = input("Press Enter for file download\n")
    if down_load == "":
        file_downlaod()
