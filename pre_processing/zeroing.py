import copy
import numpy as np
import statistics

def remove_gravity_bias(data):
	data_copy = copy.deepcopy(data)
	for i in range(len(data_copy['Az'])):
		data_copy['Az'][i] -= 9.81
	return data_copy

def remove_all_bias(data, axes):
	data_copy = copy.deepcopy(data)
	for item in axes:
		avg = statistics.mean(data_copy[item])
		for i in range(len(data_copy[item])):
			data_copy[item][i] -= avg
	return data_copy

def invert(data, axis):
	data_copy = copy.deepcopy(data)
	for i in range(len(data_copy[axis])):
		data_copy[axis][i] = -data_copy[axis][i]
	return data_copy
