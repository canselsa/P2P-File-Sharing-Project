from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import time

connection_code = "45 15f 72 65 66 20 59 69 11f 69 74 62 61 15f 131"

try:
    def clientrecv():
        while True:
            data, addr = sock.recvfrom(1024)
            data = data.decode()
            if clients_list.count(addr) == 0:
                if data == connection_code:
                    print(addr,"=> connected")
                clients_list.append(addr)
                with open("inf.txt","a",encoding="utf-8") as file:
                    file.write(addr[0]+" Log in ---->"+time.strftime("%d/%m/%Y %H:%M")+"\n")
            else:
                pass
            if data != connection_code:
                for clients in clients_list:
                    if clients != addr:
                        msg = addr[0]+"="+data
                        with open("log.txt","a",encoding="utf-8") as file:
                            file.write("*************\n"+addr[0] +"\n"+data +"*************\n\n\n\n\n\n") 
                        sock.sendto(msg.encode(), clients)
                        

    def listensend():
        while True:
            if len(clients_list) > 1:
                for i in clients_list:
                    msg = "ls"
                    sock.sendto(msg.encode(), i)
                time.sleep(60)
except:
    pass

with open("log.txt","a+") as file:
    file.write("Merhaba")


host = ("25.61.11.161", 4567)



sock = socket(family=AF_INET, type=SOCK_DGRAM)
sock.bind(host)
print("Server is ready...")
clients_list = []

taccept = Thread(target=clientrecv).start()
Thread(target=listensend).start()


