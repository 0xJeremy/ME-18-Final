import copy
import numpy as np
import statistics

def remove_gravity_bias(data):
	data_copy = copy.deepcopy(data)
	for i in range(len(data_copy['Az'])):
		data_copy['Az'][i] -= 9.81
	return data_copy

def remove_all_bias(data, axis):
	data_copy = copy.deepcopy(data)
	avg = statistics.mean(data_copy[axis])
	for i in range(len(data_copy[axis])):
		data_copy[axis][i] -= avg
	return data_copy
