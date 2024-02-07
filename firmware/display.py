import time
import board
import busio

# Kindly transcribed (stolen) from pedro11x:
# https://github.com/pedro11x/Arduino-US2066-OLED

scl = board.GP1
sda = board.GP0
i2c = busio.I2C(scl, sda)#, freq=400000)

addr = 0x3c
OLED_Command_Mode = 0x80
OLED_Data_Mode = 0x40
DEFAULT_STATE = 0x0C # OLED is ON, no cursor
ON = 0x04
BLINKING_CURSOR = 0x01

state = 0

def init():
    while not i2c.try_lock():
        pass

    # *** I2C initialization from the OLEDM1602 datasheet *** # 
    
    
    # Disable internal regulator
    # sendCommand(0x2a) # RE=1
    # sendCommand(0x71)
    # sendCommand(0x00)
    # sendCommand(0x28) # RE=0, IS=0

    # set display to OFF
    sendCommand(0x08)

    # Set display clock devide ratio, oscillator freq
    sendCommand(0x2a) # RE=1
    sendCommand(0x79) # SD=1
    sendCommand(0xd5)
    sendCommand(0x70)
    sendCommand(0x78) # SD=0

    # Set display mode
    sendCommand(0x08)

    # Set remap
    sendCommand(0x06)

    # CGROM/CGRAM Management
    sendCommand(0x72)
    sendData(0x01)    # ROM A
    
    # Set OLED Characterization
    sendCommand(0x2a) # RE=1
    sendCommand(0x79) # SD=1
    
    
    # Set SEG pins Hardware configuration
    sendCommand(0xda)
    sendCommand(0x10)

    # Set contrast control
    sendCommand(0x81)
    sendCommand(0xff)

    # Set precharge period
    sendCommand(0xd9)
    sendCommand(0xf1)

    # Set VCOMH Deselect level
    sendCommand(0xdb) 
    sendCommand(0x30)

    # Exiting Set OLED Characterization
    sendCommand(0x78) # SD=0
    sendCommand(0x28) # RE=0, IS=0

    # Clear display
    sendCommand(0x01)

    # Set DDRAM Address
    sendCommand(0x80)

    time.sleep(0.1)
    # Set display to ON
    sendCommand(0x0c)


def cursor(row, col):
    row_offsets = [0x00, 0x40];
    sendCommand(0x80 | (col + row_offsets[row]))

def clear():
    sendCommand(0x01)

def off():
    global state
    state &= ~ON;
    updateState()

def on():
    global state
    state |= ON;
    updateState()

def home():
    cursor(0,0)

#def blinkingCursor(state):
#   if state:
#       state = state | BLINKING_CURSOR
#   else
#       state = state & ~BLINKING_CURSOR
#   updateState()


def writeData(data):
    for c in data:
        sendData(ord(c))


def updateState():
    global state
    print(f"state = {state}")
    sendCommand( 0x08 | state )

def sendCommand(command):
    print(f"Sending command: {command:x}");
    res = i2c.writeto(addr, bytearray([OLED_Command_Mode, command]))
    print(res)

def sendData(data):
    res = i2c.writeto(addr, bytearray([OLED_Data_Mode, data]))
    print(res)

def sendDataContinuation(data):
    res = i2c.writeto(addr, bytearray([OLED_Data_Mode | OLED_Command_Mode, data]))
    print(res)

def contrast(cont):
    sendCommand(0x2A)
    sendCommand(0x79)      # Set OLED Command set

    sendCommand(0x81)      #  Set Contrast
    sendCommand(cont)      #  send contrast value
    sendCommand(0x78)      #  Exiting Set OLED Command set
    sendCommand(0x28)







