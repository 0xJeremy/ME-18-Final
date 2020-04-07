import numpy as np
import copy

def smooth_convolution(data, smoothing_coefficient):
	box = np.ones(smoothing_coefficient)/smoothing_coefficient
	data_copy = {}
	for key in data:
		data_copy[key] = np.convolve(data[key], box, mode='same')
	return data_copy

