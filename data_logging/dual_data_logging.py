import time
import board
import busio
import adafruit_mpu6050
import csv

i2c = busio.I2C(board.SCL, board.SDA)
ADD = busio.I2C.scan(i2c)
mpu1 = adafruit_mpu6050.MPU6050(i2c,ADD[0])
mpu2 = adafruit_mpu6050.MPU6050(i2c,ADD[1])


def write_to_file(duration, sample_rate, filename):
	with open(filename, 'w', newline='') as f:
		writer = csv.writer(f)
		#writer.writerow(['Ax1', 'Ay1', 'Az1', 'Ax2', 'Ay2', 'Az2', 'time'])
		writer.writerow(['Ax1', 'Ay1', 'Az1', 'Gx1', 'Gy1', 'Gz1', 'Ax2', 'Ay2', 'Az2', 'Gx2', 'Gy2', 'Gz2', 'time'])
		start = time.time()
		for i in range (1, int(duration*sample_rate)):
			#writer.writerow(mpu1.acceleration + mpu2.acceleration + (time.time(),))
			writer.writerow(mpu1.acceleration + mpu1.gyro + mpu2.acceleration + mpu2.gyro + (time.time(),))
			#print(i)
			#time.sleep(1 / samp_rate)
		end = time.time()
	print('Actual Sampling Rate: {}'.format((duration*sample_rate)/(end-start)))


def main():
	filename = input('Enter the filename to save the data to: ')
	print('Enter duration and smpling rate in seconds, data/sec.')
	req = input('Separate by space: (default 10 sec, ~ 65 Hz) ')
	filename = '../data/0428_1d_1/' + filename + '.csv' 
	# filename = filename + '.csv'
	if len(req) == 0:
		dur = 5
		samp_rate = 125
	elif len(req) == 1:
		dur = int(req)
		samp_rate = 10
	else:
		dur, samp_rate = req.split()
		dur = float(dur)
		samp_rate = int(samp_rate)
	write_to_file(dur, samp_rate, filename)

if __name__ == '__main__':
	main()