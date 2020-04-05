import time, board, busio, adafruit_mpu6050, csv

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

filename = input('Enter the filename to save the data to: ')
print('Enter duration and smpling rate in seconds, data/sec.')
req = input('Separate by space: (default 15 sec 50 Hz) ')

filename = filename + '.csv'
if len(req) == 0:
	dur = 0.75
	samp_rate = 1000
elif len(req) == 1:
	dur = int(req)
	samp_rate = 10
else:
	dur, samp_rate = req.split()
	dur = float(dur)
	samp_rate = int(samp_rate)


with open(filename, 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['Ax', 'Ay', 'Az', 'Gx', 'Gy', 'Gz'])

	timer_a = time.time()
	for i in range (1,int(dur*samp_rate)):
		writer.writerow(mpu.acceleration + mpu.gyro)
		print(i)
		#time.sleep(1 / samp_rate)
	timer_b = time.time()

print('true sampling rate: ', (dur*samp_rate)/(timer_b - timer_a))

f.close()
