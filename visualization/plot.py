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
