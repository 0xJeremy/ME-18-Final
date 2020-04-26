from scipy import signal

def find_peaks(data, col):
	d = data[col]
	return signal.find_peaks(d)[0]
