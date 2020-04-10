import numpy as np

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

