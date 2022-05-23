
import serial
import time

arduino = serial.Serial('COM20', 9600)
#time.sleep(2)


#var = arduino.readline()
#print ("Enter '1' to turn 'on' the LED and '0' to turn LED 'off'")

while True:
    print ("Enter '1' to turn 'on' the LED and '0' to turn LED 'off'")
    var = input() #raw_input
    print ("You Entered :", var)

    if(var == '1'):
      
        arduino.write(var.encode())
        print("LED turned on")
        time.sleep(1)

    if(var == '0'):
        
        arduino.write(var.encode())
        print("LED turned off")