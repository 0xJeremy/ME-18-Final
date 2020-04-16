from os import walk
import csv
import copy

def get_csv_list(path):
	files = []
	for (dirpath, dirnames, filenames) in walk(path):
		for file in filenames:
			if file.endswith('.csv'):
				files.append(file)
	return files

def load_file_to_dict(path, ROWS):
	data = {item: [] for item in ROWS}
	with open(path, newline='') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if row[0] in ROWS: continue
			[data[ROWS[i]].append(float(row[i])) for i in range(len(row))]
	return data

def add_time_differential(data):
	time = data['time']
	delta = [0]
	for i in range(1, len(time)):
		delta.append(time[i] - time[i-1])
	data['delta'] = delta
	return data

def get_file_metadata(filename, meta):
	f = filename.replace('.csv', '').split('_')
	data = {}
	for i in range(len(meta)):
		name, typ = meta[i]
		data[name] = typ(f[i])
	return data

def cut_data(data, start, end):
	data_copy = copy.deepcopy(data)
	for key in data_copy.keys():
		data_copy[key] = data_copy[key][start:end]
	return data_copy
