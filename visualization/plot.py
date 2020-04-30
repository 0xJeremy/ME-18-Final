import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('dark_background')

def plot_accelerometer(raw, modified=None, s=1, t=1):
	x = [i for i in range(len(raw['Ax']))]
	fig, axs = plt.subplots(3)
	axs[0].set_title('Acceleration Ax')
	axs[0].scatter(x, raw['Ax'], color='blue', s=s)

	axs[1].set_title('Acceleration Ay')
	axs[1].scatter(x, raw['Ay'], color='blue', s=s)

	axs[2].set_title('Acceleration Az')
	axs[2].scatter(x, raw['Az'], color='blue', s=s)

	if modified is not None:
		x = [i for i in range(len(modified['Ax']))]
		axs[0].plot(x, modified['Ax'], color='orange', linewidth=t)
		axs[1].plot(x, modified['Ay'], color='orange', linewidth=t)
		axs[2].plot(x, modified['Az'], color='orange', linewidth=t)

	plt.tight_layout()
	axs[0].grid(True, linewidth=0.1)
	axs[1].grid(True, linewidth=0.1)
	axs[2].grid(True, linewidth=0.1)

	return axs

def plot_gyroscope(raw, modified=None, s=1, t=1):
	x = [i for i in range(len(raw['Gx']))]
	fig, axs = plt.subplots(3)
	axs[0].set_title('Gyroscope Gx')
	axs[0].scatter(x, raw['Gx'], color='blue', s=s)

	axs[1].set_title('Gyroscope Gy')
	axs[1].scatter(x, raw['Gy'], color='blue', s=s)
	
	axs[2].set_title('Gyroscope Gz')
	axs[2].scatter(x, raw['Gz'], color='blue', s=s)

	if modified is not None:
		axs[0].plot(x, modified['Gx'], color='orange', linewidth=t)
		axs[1].plot(x, modified['Gy'], color='orange', linewidth=t)
		axs[2].plot(x, modified['Gz'], color='orange', linewidth=t)

	plt.tight_layout()
	plt.grid(True, linewidth=0.1)
	axs[0].grid(True, linewidth=0.1)
	axs[1].grid(True, linewidth=0.1)
	axs[2].grid(True, linewidth=0.1)

	return axs

def plot_all(raw, modified=None, s=1, t=1):
	x = [i for i in range(len(raw['Ax']))]
	fig, axs = plt.subplots(2, 3)

	axs[0, 0].set_title('Acceleration Ax')
	axs[0, 0].scatter(x, raw['Ax'], color='blue', s=s)

	axs[0, 1].set_title('Acceleration Ay')
	axs[0, 1].scatter(x, raw['Ay'], color='blue', s=s)

	axs[0, 2].set_title('Acceleration Az')
	axs[0, 2].scatter(x, raw['Az'], color='blue', s=s)


	axs[1, 0].set_title('Gyroscope Gx')
	axs[1, 0].scatter(x, raw['Gx'], color='blue', s=s)

	axs[1, 1].set_title('Gyroscope Gy')
	axs[1, 1].scatter(x, raw['Gy'], color='blue', s=s)
	
	axs[1, 2].set_title('Gyroscope Gz')
	axs[1, 2].scatter(x, raw['Gz'], color='blue', s=s)

	if modified is not None:
		axs[0, 0].plot(x, modified['Ax'], color='orange', linewidth=t)
		axs[0, 1].plot(x, modified['Ay'], color='orange', linewidth=t)
		axs[0, 2].plot(x, modified['Az'], color='orange', linewidth=t)
		axs[1, 0].plot(x, modified['Gx'], color='orange', linewidth=t)
		axs[1, 1].plot(x, modified['Gy'], color='orange', linewidth=t)
		axs[1, 2].plot(x, modified['Gz'], color='orange', linewidth=t)

	plt.tight_layout()
	axs[0, 0].grid(True, linewidth=0.1)
	axs[0, 1].grid(True, linewidth=0.1)
	axs[0, 2].grid(True, linewidth=0.1)
	axs[1, 0].grid(True, linewidth=0.1)
	axs[1, 1].grid(True, linewidth=0.1)
	axs[1, 2].grid(True, linewidth=0.1)

	return axs

def plot_column(data, column, s=1, t=1, line=False, type=None, est=[], vert=[]):
	if 'time' in data.keys():
		x = data['time'][0:len(data[column])]
	else:
		x = [i for i in range(len(data[column]))]
	fig, axs = plt.subplots(1)

	plt.xlabel("Time")
	if type == 'velocity':
		axs.set_title("Velocity ({})".format(column[-1]))
		plt.ylabel("Velocity (m/s)")
	if type == 'position':
		axs.set_title("Position ({})".format(column[-1]))
		plt.ylabel("Position (m)")
	else:
		axs.set_title('Plotting Column {}'.format(column))
		plt.xlabel("Time")
		plt.ylabel("Magnitude")

	for v in vert:
		axs.axvline(v, color='red', linewidth=t/2)

	axs.scatter(x, data[column], color='blue', s=s, label="Measured")
	if line:
		axs.plot(x, data[column], color='orange', linewidth=t, label="Measured")

	for item in est:
		axs.plot(x, [item]*len(x), color="green", linewidth=t, label="Actual")

	plt.legend()
	plt.tight_layout()
	plt.grid(True, linewidth=0.1)

	return axs

def plot_3d(data, column, s=1, t=1, line=False, type=None, est=None):
	if 'time' in data.keys():
		x = data['time']
	else:
		x = [i for i in range(len(data[column]))]
	fig = plt.figure()
	axs = fig.add_subplot(111, projection='3d')

	if type == 'velocity':
		axs.set_title("Velocity")
		axs.set_xlabel("Velocity (x, m/s)")
		axs.set_ylabel("Velocity (y, m/s)")
		axs.set_zlabel("Velocity (z, m/s)")
	if type == 'position':
		axs.set_title("Position")
		axs.set_xlabel("Position (x, m)")
		axs.set_ylabel("Position (y, m)")
		axs.set_zlabel("Position (z, m)")
	else:
		axs.set_title('Plotting Column {}'.format(column))

	axs.scatter(data[column+'x'], data[column+'y'], data[column+'z'], color='blue', s=s, label="Measured")
	if line:
		axs.plot(x, data[column], color='orange', linewidth=t, label="Measured")

	if est is not None:
		for item in est:
			axs.plot(x, [item]*len(x), color="green", linewidth=t, label="Actual")

	plt.legend()
	plt.tight_layout()

def show_plot():
	plt.tight_layout()
	plt.show()
