import numpy as np

def add_accumulation_column(data, key, new_col_name):
	if 'delta' not in data.keys():
		raise RuntimeError("delta column not defined in data")
	col = data[key]
	delta = data['delta']
	new = []
	accumulator = 0
	for i in range(len(col)):
		accumulator += col[i] * delta[i]
		new.append(accumulator)
	data[new_col_name] = new
	return data

def double_accumulation(data, key, new_col1, new_col2):
	data = add_accumulation_column(data, key, new_col1)
	data = add_accumulation_column(data, new_col1, new_col2)
	return data

