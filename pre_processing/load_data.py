import csv
from os import walk

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

def get_file_metadata(filename):
	f = filename.replace('.csv', '').split('_')
	return {
		'date': f[0],
		'distance': f[1],
		'speed': f[2],
		'trial': f[3]
	}

def remove_gravity_bias(data):
	data_copy = copy.deepcopy(data)
	for i in range(len(data_copy['Az'])):
		data_copy['Az'][i] -= 9.81
	return data_copy
