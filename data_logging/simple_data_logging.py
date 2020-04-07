import time
import board
import busio
import adafruit_mpu6050
import csv

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)


def write_to_file(duration, sample_rate, filename):
	with open(filename, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(['Ax', 'Ay', 'Az', 'Gx', 'Gy', 'Gz', 'time'])
		start = time.time()
		for i in range (1, int(duration*samp_rate)):
			writer.writerow(mpu.acceleration + mpu.gyro + [time.time()])
			print(i)
			#time.sleep(1 / samp_rate)
		end = time.time()
	print('Actual Sampling Rate: {}'.format((duration*samp_rate)/(start-end)))


def main():
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
	write_to_file(dur, samp_rate, filename)

if __name__ == '__main__':
	main()