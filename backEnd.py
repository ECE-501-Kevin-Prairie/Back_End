from devices import *
import socket
import sys

def deviceFunctions(command):
# Buzzer Commands
	if(command == '0'):
		startBuzzer() 
	elif(command == '1'):
		stopBuzzer() 
	elif(command == '2'):
		toggleBuzzer()
# LED Commands
	elif(command == '3'):
		startLED()
	elif(command == '4'):
		stopLED() 
	elif(command == '5'):
		toggleLED()
# Microphone Commands
	elif(command == '6'):
		startBuzzer(), 
	elif(command == '7'):
		stopBuzzer(), 
	elif(command == '8'):
		toggleBuzzer(),
	else:
		print('Enter a valid Command')

startSetup()

while True:
    command = input('Enter Command #: ')
    deviceFunctions(command)

"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
serverAddress = (host, 10000)

print("Starting up on port: " + str(serverAddress[1]))
sock.bind(serverAddress)
sock.listen(1)

while True:
	print("Waiting for a Connection...")
	connection, clientAddress = sock.accept()
	
	try:
		print("Client Connected: " + str(clientAddress))
		while True:
			command = connection.recv(16)
			command = int(command)
			deviceFunctions(command)
			connection.sendall("Command Complete!\nPlease enter a new command")
	
	finally:
		sock.close()
"""
