import numpy as np

def smooth_convolution(data, smoothing_coefficient):
	box = np.ones(smoothing_coefficient)/smoothing_coefficient
	for key in data:
		data[key] = np.convolve(data[key], box, mode='same')
	return data