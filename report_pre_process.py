from visualization.plot import plot_all
from visualization.plot import plot_accelerometer
from visualization.plot import plot_gyroscope
from visualization.plot import plot_column
from visualization.plot import plot_3d
from visualization.plot import show_plot

from pre_processing.load_data import load_file_to_dict
from pre_processing.load_data import get_csv_list
from pre_processing.load_data import add_time_differential
from pre_processing.load_data import get_file_metadata
from pre_processing.load_data import cut_data
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

import matplotlib.pyplot as plt
plt.style.use('dark_background')

ROWS = ['Ax', 'Ay', 'Az', 'time']
META = [
	('date', str),
	('d1', int),
	('speed', str),
	('trial', int)
]
PATH = 'data/0407_1d_1/'
FILE = '0407_0_na_1.csv'

data = load_file_to_dict('{}{}'.format(PATH, FILE), ROWS)
meta = get_file_metadata(FILE, META)
data = add_time_differential(data)

data = remove_all_bias(data, 'Ax')
data = remove_all_bias(data, 'Ay')
data = remove_all_bias(data, 'Az')

smooth1 = rolling_window(data, smoothing_coefficient=1)
smooth2 = rolling_window(data, smoothing_coefficient=10)
smooth3 = rolling_window(data, smoothing_coefficient=100)


plt.scatter(data['time'], data['Ax'], color='blue', s=1, label='Raw Data')
plt.plot(data['time'], smooth1['Ax'], color='orange', linewidth=0.3, label='Window Size 1')
plt.plot(data['time'], smooth2['Ax'], color='red', linewidth=0.75, label='Window Size 10')
plt.plot(data['time'], smooth3['Ax'], color='green', linewidth=1, label='Window Size 100')

plt.title('Acceleration over Time (Rolling Window)')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude (x-axis)')

plt.legend()

plt.grid(True, linewidth=0.1)

plt.show()

