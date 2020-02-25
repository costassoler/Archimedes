from socket import *
import numpy as np
import smbus
import time
#import py_qmc58831
import MPU_Reader as mpu
import py_qmc5883l as qmc
import math
#from mpu6050 import mpu6050
#sensor = mpu6050(0x68)
HOST=''
PORT=52849
BUFSIZE=1024
ADDR=(HOST,PORT)
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
print('Waiting for connection')
print('...connected from:',ADDR)
sensor = qmc.QMC5883L()
sensor.calibration = [[  1.04225578e+00,  -2.08340944e-02,   2.58425997e+02],
                      [ -2.08340944e-02,   1.01027219e+00,   5.72246573e+03],
                      [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00]]
'''
For MPU6050 Modules:
ACCEL_X = 0x3B
ACCEL_Y = 0x3D
ACCEL_Z = 0x3F
GYRO_X = 0x43
GYRO_Y = 0x45
GYRO_Z = 0x47
TEMP = 0x41
mpu.InitMPU()
V = 0
R = 0
g = 9.81/16384#19050
GyroScale=1/12
Yaw = 0

Device_Address = 0x0d
X_axis_H = 0x01
Z_axis_H = 0x05
Y_axis_H = 0x03
declination =-0.0069
pi = 3.1415927

#Magnetometer attempt:

def Magnetometer_Init():
    bus.write_byte_data(Device_Address, 0x0a,0x81)
    bus.write_byte_data(Device_Address, 0x0b, 0x01)
    bus.write_byte_data(Device_Address, 0x09, 0x11)
def read_raw_data(addr):
    #read raw 16-bit value
    high = bus.read_byte_data(Device_Address,addr)
    low=bus.read_byte_data(Device_Address, addr+1)

    #concatenate higher and lower value
    value = ((high<<8)|low)

    #to get signed value from module
    if(value>32768):
        value = value-65536
    return value
#bus=smbus.SMBus(1)

#Magnetometer_Init()

#print("Reading Heading Angle")

                        
#accelerometer_data = sensor.get_accel_data()
#start = time.time()
'''
while True:

    tcpDataSock,addr=tcpSerSock.accept()
    print("accepted")
    m=sensor.get_bearing()
    mcal = m
    print(m)
    Message = str(m)+'\r\n' 
    #Message = str(math.degrees(math.atan2(y,x)))+'\r\n'
    tcpDataSock.send(Message.encode('UTF-8'))
    
    #Ax = mpu.readMPU(ACCEL_X)*g
    #Ay = mpu.readMPU(ACCEL_Y)*g
    #Az = mpu.readMPU(ACCEL_Z)*g 
    #Gz = mpu.readMPU(GYRO_Z)*GyroScale
'''
    #now = time.time()
    #dt = now-start
    #start = now
    #Yaw += round(dt*Gz,2)
    
    #Temp = mpu.readMPU(TEMP)/340+36.53
    
    
    
    #MessageT = str(round(Temp,1))+'\r\n'
    #print(Temp)
    #message = str(Ax)+','+str(Ay)+','+str(Az)+','+str(Gz)+','+str(Temp)+'\r\n'
    #tcpDataSock.send(MessageT.encode('UTF-8'))

    #COMPASS START
    '''
    #print("compass start")
    
    #status = bus.read_byte_data(Device_Address, 0x06)
    #print(status)
    #x = read_raw_data(X_axis_H)
    #z = read_raw_data(Z_axis_H)
    #y = read_raw_data(Y_axis_H)
    #heading = 
    #print(math.degrees(math.atan2(y,x)))
    #COMPASS END
    #time.sleep(.5)

    

