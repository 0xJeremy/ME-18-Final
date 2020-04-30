from visualization.plot import plot_all
from visualization.plot import plot_accelerometer
from visualization.plot import plot_gyroscope
from visualization.plot import plot_column
from visualization.plot import plot_3d
from visualization.plot import show_plot

from pre_processing.load_data import load_file_to_dict
from pre_processing.load_data import get_csv_list
from pre_processing.load_data import add_time_differential
from pre_processing.load_data import zero_time
from pre_processing.load_data import get_file_metadata
from pre_processing.load_data import cut_data
from pre_processing.load_data import cut_to_times
from pre_processing.load_data import split_times
from pre_processing.load_data import zip_data_no_offset
from pre_processing.load_data import zip_data_offset
from pre_processing.zeroing import remove_gravity_bias
from pre_processing.zeroing import remove_all_bias
from pre_processing.zeroing import invert
from pre_processing.tools import smooth_convolution
from pre_processing.tools import savitzky_golay_filter
from pre_processing.tools import rolling_window
from pre_processing.tools import double_digital_filter

from post_processing.tools import add_accumulation_column
from post_processing.tools import add_time_accumulation_column
from post_processing.tools import double_accumulation
from post_processing.tools import double_time_accumulation
from post_processing.tools import rotate_data
from post_processing.tools import wavelets
from post_processing.tools import wave3
from post_processing.peaks import find_peaks

####################
### DATA LOADING ###
####################

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
FILE = '0414_0_20_40_60_fast_2.csv'

data = load_file_to_dict('{}{}'.format(PATH, FILE), ROWS)
meta = get_file_metadata(FILE, META)
data = zero_time(data)
data = add_time_differential(data)

def process_subset(data, start, finish):
	tmp = cut_to_times(data, start, finish)
	tmp = remove_all_bias(tmp, ['Ax', 'Ay', 'Az'])
	tmp = smooth_convolution(tmp, smoothing_coefficient=5)
	tmp = double_time_accumulation(tmp, 'Ax', 'i_Ax', 'ii_Ax')
	return tmp


datasets = []
times = [0, 2, 2.5, 4.45, 5.5, 10]
for i in range(1, len(times)):
	datasets.append(process_subset(data, times[i-1], times[i]))

smoothed = zip_data_offset(datasets, ['ii_Ax', 'ii_Ay', 'ii_Az'])


# datasets.append(cut_to_times(smoothed, 0, 2.5))
# datasets.append(cut_to_times(smoothed, 2.5, 5.5))
# datasets.append(cut_to_times(smoothed, 5.5, 10))
# data = cut_to_times(data, 5.5, 10)
# data = split_times(data, [0, 2, 5, 9])

# data = invert(data, 'Ax')

###########################
### DATA PRE-PROCESSING ###
###########################

# smoothed = smooth_convolution(data, smoothing_coefficient=2)
# smoothed = savitzky_golay_filter(data, smoothing_coefficient=5)
# smoothed = rolling_window(data, smoothing_coefficient=100)
# smoothed = double_digital_filter(data, order=5, cutoff=0.9)

############################
### DATA POST-PROCESSING ###
############################

# datasets = []
# datasets.append(cut_to_times(smoothed, 0, 2.5))
# datasets.append(cut_to_times(smoothed, 2.5, 5.5))
# datasets.append(cut_to_times(smoothed, 5.5, 10))

# for i in range(len(datasets)):
# 	datasets[i] = double_time_accumulation(datasets[i], 'Ax', 'i_Ax', 'ii_Ax')

# smoothed = zip_data(datasets)

# smoothed = remove_all_bias(smoothed, 'Ax')
# smoothed = remove_all_bias(smoothed, 'Ay')
# smoothed = remove_all_bias(smoothed, 'Az')

# for item in datasets:
# 	item = double_time_accumulation(item, 'Ax', 'i_Ax', 'ii_Ax')

# smoothed = zip_data(datasets)

# smoothed = double_time_accumulation(data, 'Ax', 'i_Ax', 'ii_Ax')
# smoothed = double_time_accumulation(smoothed, 'Ay', 'i_Ay', 'ii_Ay')
# smoothed = double_time_accumulation(smoothed, 'Az', 'i_Az', 'ii_Az')

#########################
### DATA VISUALZATION ###
#########################

# plot_accelerometer(data, smoothed)

plot_column(smoothed, 'i_Ax', type='velocity')
# plot_column(cut, 'i_Ax', type='velocity')
plot_column(smoothed, 'ii_Ax', type='position', est=[meta['d1']/100, meta['d2']/100, meta['d3']/100, meta['d4']/100])
# plot_column(y, 'i_Ay', name='Velocity (y)')
# plot_column(y, 'ii_Ay', name='Position (y)')
# plot_column(z, 'i_Az', name='Velocity (z)')
# plot_column(z, 'ii_Az', name='Position (z)')

# plot_3d(smoothed, 'ii_A', type='position')

show_plot()
