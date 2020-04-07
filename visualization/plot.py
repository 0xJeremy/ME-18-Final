import matplotlib.pyplot as plt
plt.style.use('dark_background')

def plot_acceleration(raw, modified=None):
	x = [i for i in range(len(raw['Ax']))]
	fig, axs = plt.subplots(2, 2)
	axs[0, 0].set_title('Acceleration Ax')
	axs[0, 0].scatter(x, raw['Ax'], color='blue')

	axs[0, 1].set_title('Acceleration Ay')
	axs[0, 1].scatter(x, raw['Ay'], color='blue')

	axs[1, 0].set_title('Acceleration Az')
	axs[1, 0].scatter(x, raw['Az'], color='blue')

	if modified is not None:
		axs[0, 0].plot(x, modified['Ax'], color='orange')
		axs[0, 1].plot(x, modified['Ay'], color='orange')
		axs[1, 0].plot(x, modified['Az'], color='orange')

	plt.show()

	return axs

def plot_gyroscope(raw, modified=None):
	x = [i for i in range(len(raw['Gx']))]
	fig, axs = plt.subplots(2, 2)
	axs[0, 0].set_title('Gyroscope Gx')
	axs[0, 0].scatter(x, raw['Gx'], color='blue')

	axs[0, 1].set_title('Gyroscope Gy')
	axs[0, 1].scatter(x, raw['Gy'], color='blue')
	
	axs[1, 0].set_title('Gyroscope Gz')
	axs[1, 0].scatter(x, raw['Gz'], color='blue')

	if modified is not None:
		axs[0, 0].plot(x, modified['Gx'], color='orange')
		axs[0, 1].plot(x, modified['Gy'], color='orange')
		axs[1, 0].plot(x, modified['Gz'], color='orange')

	plt.show()

	return axs

def plot_all(raw, modified, s=1, t=1):
	x = [i for i in range(len(raw['Gx']))]
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
		axs[0, 0].plot(x, modified['Ax'], color='orange', linewidth=1)
		axs[0, 1].plot(x, modified['Ay'], color='orange', linewidth=1)
		axs[0, 2].plot(x, modified['Az'], color='orange', linewidth=1)
		axs[1, 0].plot(x, modified['Gx'], color='orange', linewidth=1)
		axs[1, 1].plot(x, modified['Gy'], color='orange', linewidth=1)
		axs[1, 2].plot(x, modified['Gz'], color='orange', linewidth=1)

	plt.tight_layout()
	plt.show()

	return axs
