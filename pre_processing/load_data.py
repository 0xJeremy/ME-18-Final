import csv

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
