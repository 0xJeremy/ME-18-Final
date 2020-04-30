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

def zero_time(data):
	data_copy = copy.deepcopy(data)
	stime = data['time'][0]
	time = []
	for item in data['time']:
		time.append(item-stime)
	data_copy['time'] = time
	return data_copy

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

def cut_to_times(data, start, end):
	data_copy = copy.deepcopy(data)
	start_index = 0
	for i in range(len(data['time'])):
		if data['time'][i] > start:
			start_index = i
			break
	end_index = len(data['time'])
	for i in range(len(data['time'])):
		if data['time'][i] > end:
			end_index = i
			break
	for key in data_copy.keys():
		data_copy[key] = data_copy[key][start_index:end_index]
	return data_copy

def split_times(data, times):
	data_copy = {}
	for key in data.keys():
		data_copy[key] = []
	for i in range(1, len(times)):
		tmp = cut_to_times(data, times[i-1], times[i])
		for key in tmp.keys():
			data_copy[key] += tmp[key]
	return data_copy

def zip_data_no_offset(data_list):
	data_copy = {}
	for key in data_list[0]:
		data_copy[key] = []
	for item in data_list:
		for key in item.keys():
			data_copy[key].extend(item[key])
	return data_copy

def zip_data_offset(data_list, items_to_offset):
	data_copy = {}
	for key in data_list[0]:
		data_copy[key] = []
	for item in data_list:
		for key in item.keys():
			if(key in items_to_offset and data_copy[key] != []):
				tmp = [x+data_copy[key][-1] for x in item[key]]
			else:
				tmp = item[key]
			data_copy[key].extend(tmp)
	return data_copy
