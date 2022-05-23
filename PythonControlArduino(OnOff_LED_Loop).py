import serial
import time

ser = serial.Serial("COM20", 9600)
while True:
    input_value = "LED13-ON"
    print(input_value)
    ser.write(input_value.encode())
    time.sleep(2)

    input_value = "LED13-OFF"
    print(input_value)
    ser.write(input_value.encode())
    time.sleep(1)