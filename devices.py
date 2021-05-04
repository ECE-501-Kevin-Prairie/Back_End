# Import Required Libaries
import RPi.GPIO as GPIO
import time
import sounddevice as sd
from scipy.io.wavfile import write
import wave
import socket
import sys

# Set pin #'s, Pin Modes, Button Event, PyAudio settings
def startSetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    button = 23
    LED = 24
    buzzer = 25
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(button, GPIO.RISING, callback=buttonCallback)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.setup(buzzer, GPIO.OUT)
# Function that occurs when the button is pressed   
def buttonCallback(x):
    print("\nButton was pressed")
    #connection.sendall("Button was pressed")

# Play buzzer
def startBuzzer():
    buzzer = 25
    GPIO.output(buzzer, GPIO.HIGH)
    print("Beep")

# Stop buzzer and pause for 1 second    
def stopBuzzer():
    buzzer = 25
    GPIO.output(buzzer, GPIO.LOW)
    print("No Beep")

# Toggle buzzer 4 times 
def toggleBuzzer():
    buzzer = 25
    stopBuzzer()
    
    for i in range(1, 5):
        startBuzzer()
        time.sleep(0.5)
        stopBuzzer()
        time.sleep(0.5)

# Turn LED On   
def startLED():
    LED = 24
    print("LED on")
    GPIO.output(LED, GPIO.HIGH)

# Turn LED Off
def stopLED():
    LED = 24
    print("LED off")
    GPIO.output(LED, GPIO.LOW)

# Toggle LED 4 times    
def toggleLED():
    LED = 24
    stopLED()
    
    for i in range(1, 5):
        startLED()
        time.sleep(0.5)
        stopLED()
        time.sleep(0.5)

# Start Microphone and record for 10 seconds
# Then save to a .wav file      
def startMicrophone():
    fs = 44100
    seconds = 10
    
    myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 2)
    sd.wait()
    write('output.wav', fs, myrecording)