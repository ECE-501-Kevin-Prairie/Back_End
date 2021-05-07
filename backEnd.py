from devices import *
import socket
import sys
import os
import time
import _thread

def deviceFunctions(command):
# Buzzer Commands
	if(command == 'Turn On Buzzer'):
		startBuzzer() 
	elif(command == 'Turn Off Buzzer'):
		stopBuzzer() 
	elif(command == 'Toggle Buzzer'):
		toggleBuzzer()
# LED Commands
	elif(command == 'Turn On LED'):
		startLED()
	elif(command == 'Turn Off LED'):
		stopLED() 
	elif(command == 'Toggle LED'):
		toggleLED()
# Microphone Commands
	elif(command == 'Record Audio'):
		startMicrophone(), 
	else:
		print('Enter a valid Command')

def onNewClient(connection, clientAddress):
	print("Client Connected: " + str(clientAddress))
	while True:
		command = connection.recv(16)
		command = command.decode("utf-8")
		if(command):
			print(command)
			deviceFunctions(command)
			if(command == "Play Audio"):
				#f = (os.getcwd() + "/output.txt", "rb")
				#with open(os.getcwd() + "/output.txt", 'rb') as text_file:
				#	connection.sendfile(text_file)
				
				f = open(os.getcwd() + "/output.wav", "rb")
				l = f.read(1024)
				while (l):
					connection.send(l)
					print('Sent ', repr(l))
					l = f.read(1024)
				f.close()
		else:
			print("Closing connection...")
			break
	#sock.close()

startSetup()

"""
while True:
    command = input('Enter Command #: ')
    deviceFunctions(command)
"""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.0.0.124'
port = 65432
serverAddress = (host, port)

print("Starting up on port: " + str(serverAddress[1]))
sock.bind(serverAddress)
sock.listen(10)

while True:
	print("Waiting for a Connection...")
	connection, clientAddress = sock.accept()
	_thread.start_new_thread(onNewClient,(connection,clientAddress))
	
sock.close()

