import numpy as np
from scipy.stats import linregress
import pywt

def _accumulation_column(data, key, new_col_name, timeBased):
	if timeBased:
		if 'delta' not in data.keys():
			raise RuntimeError("delta column not defined in data")
	col = data[key]
	delta = data['delta']
	new = []
	accumulator = 0
	for i in range(len(col)):
		if timeBased:
			accumulator += col[i] * delta[i]
		else:
			accumulator += col[i]
		new.append(accumulator)
	data[new_col_name] = new
	return data

def add_accumulation_column(data, key, new_col_name):
	return _accumulation_column(data, key, new_col_name, False)

def add_time_accumulation_column(data, key, new_col_name):
	return _accumulation_column(data, key, new_col_name, True)

def double_accumulation(data, key, new_col1, new_col2):
	data = add_accumulation_column(data, key, new_col1)
	data = add_accumulation_column(data, new_col1, new_col2)
	return data

def double_time_accumulation(data, key, new_col1, new_col2):
	data = add_time_accumulation_column(data, key, new_col1)
	data = add_time_accumulation_column(data, new_col1, new_col2)
	return data

def rotate_data(data, key, t1, t2):
	R = linregress(data['time'][t1:t2], data[key][t1:t2])
	inter = -R[1] / R[0]
	start = np.where(data['time'] > inter)[0][0]
	term1 = data[key][start:]
	term2 = [R[0]*item for item in data['time'][start:]]
	transformed = term1 - (term2 + R[1])
	new = np.concatenate((data[key][:start], transformed))
	data[key] = new
	return data

def wavelets(data, wavelet, uselevels, mode):
	levels = (np.floor(np.log2(len(data)))).astype(int)
	omit = levels - uselevels
	coeffs = pywt.wavedec(data, wavelet, level=levels)
	A = pywt.waverec(coeffs[:-omit] + [None] * omit, wavelet, mode=mode)
	return A

def wave3(data, mult, mode, k1, k2):
	coeffs = pywt.wavedec(data, 'haar', level=12)
	threshold = np.std(data[k1:k2])*np.sqrt(2*np.log2(len(data)))*mult
	new_coeffs = map(lambda data: pywt.threshold(data, threshold, mode=mode, substitute = 0), coeffs)
	return pywt.waverec(list(new_coeffs), 'haar')
