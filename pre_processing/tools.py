import numpy as np
from scipy import signal
import pandas as pd
import copy

def smooth_convolution(data, smoothing_coefficient=1):
	box = np.ones(smoothing_coefficient)/smoothing_coefficient
	data_copy = copy.deepcopy(data)
	for key in data:
		if key == 'time' or key == 'delta':
			continue
		data_copy[key] = np.convolve(data[key], box, mode='same')
	return data_copy

def savitzky_golay_filter(data, smoothing_coefficient=1):
	window = smoothing_coefficient
	order = 3
	data_copy = copy.deepcopy(data)
	for key in data:
		if key == 'time' or key == 'delta':
			continue
		data_copy[key] = signal.savgol_filter(data[key], window, order)
	return data_copy

def rolling_window(data, smoothing_coefficient=1):
	data_copy = copy.deepcopy(data)
	for key in data:
		if key == 'time' or key == 'delta':
			continue
		data_copy[key] = pd.Series(data[key]).rolling(window=smoothing_coefficient).mean()
	return data_copy

def double_digital_filter(data, order=3, cutoff=0.1):
	N  = order    # Filter order
	Wn = cutoff   # Cutoff frequency
	sos = signal.butter(N, Wn, output='sos')
	data_copy = copy.deepcopy(data)
	for key in data:
		if key == 'time' or key == 'delta':
			continue
		data_copy[key] = signal.sosfiltfilt(sos, data[key])
	return data_copy

# Investigate https://en.wikipedia.org/wiki/Finite_impulse_response
