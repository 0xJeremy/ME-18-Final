import csv

TIMESTAMP = False
ROWS = ['Ax', 'Ay', 'Az', 'Gx', 'Gy', 'Gz']
if TIMESTAMP:
	ROWS.append('time')


def load_file_to_dict(path):
	data = {item: [] for item in ROWS}
	with open(path, newline='') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if row[0] in ROWS: continue
			[data[ROWS[i]].append(float(row[i])) for i in range(len(row))]
	return data

# data = load_file_to_dict('../data/0405_110_1.csv')
# print(data)