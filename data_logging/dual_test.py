import time
import board
import busio
import adafruit_mpu6050
 
i2c = busio.I2C(board.SCL, board.SDA)
ADD = busio.I2C.scan(i2c)
mpu1 = adafruit_mpu6050.MPU6050(i2c,ADD[0])
mpu2 = adafruit_mpu6050.MPU6050(i2c,ADD[1])

 
while True:
    print("Acceleration: X1:%.2f, Y1: %.2f, Z1: %.2f m/s^2" % (mpu1.acceleration) + " " + "Acceleration: X2:%.2f, Y2: %.2f, Z2: %.2f m/s^2" % (mpu1.acceleration))
    # print("Acceleration: X2:%.2f, Y2: %.2f, Z2: %.2f m/s^2" % (mpu1.acceleration))
    # print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s" % (mpu.gyro))
    # print("Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(0.001)