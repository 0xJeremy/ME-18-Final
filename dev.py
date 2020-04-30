from visualization.plot import *
from pre_processing.load_data import *
from pre_processing.zeroing import *
from pre_processing.tools import *
from post_processing.tools import *
from post_processing.peaks import *

ROWS = ['Ax', 'Ay', 'Az', 'time']
META = [
	('date', str),
	('d1', int),
	('d2', int),
	('d3', int),
	('d4', int),
	('speed', str),
	('trial', int)
]
PATH = 'data/0414_1d_1/'
FILE = '0414_0_20_40_60_fast_1.csv'

def get_data(path, file, meta, rows):
	data = load_file_to_dict('{}{}'.format(path, file), rows)
	return add_time_differential(zero_time(data)), get_file_metadata(file, meta)

data, meta = get_data(PATH, FILE, META, ROWS)

def process_subset(data, start, finish):
	tmp = cut_to_times(data, start, finish)
	tmp = remove_all_bias(tmp, ['Ax', 'Ay', 'Az'])
	tmp = smooth_convolution(tmp, smoothing_coefficient=4)
	tmp = double_time_accumulation(tmp, 'Ax', 'i_Ax', 'ii_Ax')
	return tmp


times = [0, 1, 2.5, 4.5, 7, 10]

datasets = [process_subset(data, times[i-1], times[i]) for i in range(1, len(times))]
smoothed = zip_data_offset(datasets, ['ii_Ax', 'ii_Ay', 'ii_Az'])

#########################
### DATA VISUALZATION ###
#########################

plot_accelerometer(data, smoothed)

plot_column(smoothed, 'i_Ax', type='velocity')
plot_column(smoothed, 'ii_Ax', type='position', est=[meta['d1']/100, meta['d2']/100, meta['d3']/100, meta['d4']/100])

show_plot()
