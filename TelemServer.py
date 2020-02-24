from socket import *
import numpy as np
import smbus
import time
import MPU_Reader as mpu
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
#accelerometer_data = sensor.get_accel_data()
start = time.time()
while True:

    tcpDataSock,addr=tcpSerSock.accept()
    print("accepted")
    '''Ax = mpu.readMPU(ACCEL_X)*g
    Ay = mpu.readMPU(ACCEL_Y)*g
    Az = mpu.readMPU(ACCEL_Z)*g '''
    Gz = mpu.readMPU(GYRO_Z)*GyroScale

    #now = time.time()
    #dt = now-start
    #start = now
    #Yaw += round(dt*Gz,2)
    
    Temp = mpu.readMPU(TEMP)/340+36.53
    
    
    
    MessageT = str(round(Temp,1))+'\r\n'
    print(Temp)
    #message = str(Ax)+','+str(Ay)+','+str(Az)+','+str(Gz)+','+str(Temp)+'\r\n'
    tcpDataSock.send(MessageT.encode('UTF-8'))

