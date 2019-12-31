from socket import *
import numpy as np
import smbus
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
mpu.InitMPU()
V = 0
R = 0
C = 0
#accelerometer_data = sensor.get_accel_data()
while True:
    n = np.random.random()
    tcpDataSock,addr=tcpSerSock.accept()
    print("accepted")
    #print(accelerometer_data)
    Ax = mpu.readMPU(ACCEL_X)
    Ay = mpu.readMPU(ACCEL_Y)
    Az = mpu.readMPU(ACCEL_Z)

    Gz = mpu.readMPU(GYRO_Z)
    
    message = str(Ax)+','+str(Ay)+','+str(Az)+','+str(Gz)+'\r\n'
    tcpDataSock.send(message.encode('UTF-8'))
    print(n)
