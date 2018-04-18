from myAHRS_plus import *
import serial

def myAHRS_plusExample():
    try:
        sensor = myAHRS_plus('/dev/ttyACM0')
    except serial.serialutil.SerialException:
        print("Cannot open serial port.")
        return
    while True:
        items = sensor.getValues()
        print(items)

# Use example
if __name__ == "__main__":
    myAHRS_plusExample()
