import smbus
import time
import RPi.GPIO as gpio

PWR_M = 0x6B
DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_EN = 0x38
ACCEL_X = 0x3B
ACCEL_Y = 0x3D
ACCEL_Z = 0x3F
GYRO_X = 0x43
GYRO_Y = 0x45
GYRO_Z = 0x47
TEMP = 0x41
bus = smbus.SMBus(1)

Device_Address = 0x68 #device address
AxCal = 0
AyCal = 0
AzCal = 0
GxCal = 0
GyCal = 0
GzCal = 0

def InitMPU():
    bus.write_byte_data(Device_Address, DIV, 7)
    bus.write_byte_data(Device_Address, PWR_M, 1)
    bus.write_byte_data(Device_Address, CONFIG, 0)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    bus.write_byte_data(Device_Address, INT_EN, 1)
    time.sleep(1)
    
def readMPU(addr):
    high = bus.read_byte_data(Device_Address,addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    value = ((high<<8)|low)
    if(value>32768):
        value=value-65536
    return value

