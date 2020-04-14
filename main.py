from visualization.plot import plot_all
from visualization.plot import plot_accelerometer
from visualization.plot import plot_gyroscope
from visualization.plot import plot_column
from visualization.plot import show_plot

from pre_processing.load_data import load_file_to_dict
from pre_processing.load_data import get_csv_list
from pre_processing.load_data import add_time_differential
from pre_processing.load_data import get_file_metadata
from pre_processing.load_data import cut_data
from pre_processing.zeroing import remove_gravity_bias
from pre_processing.zeroing import remove_all_bias
from pre_processing.tools import smooth_convolution
from pre_processing.tools import savitzky_golay_filter
from pre_processing.tools import rolling_window
from pre_processing.tools import double_digital_filter

from post_processing.tools import add_accumulation_column
from post_processing.tools import add_time_accumulation_column
from post_processing.tools import double_accumulation
from post_processing.tools import double_time_accumulation

####################
### DATA LOADING ###
####################

ROWS = ['Ax', 'Ay', 'Az', 'time']
PATH = 'data/0407_1d_1/'
FILE = '0407_40_fast_3.csv'

data = load_file_to_dict('{}{}'.format(PATH, FILE), ROWS)
meta = get_file_metadata(FILE)
data = add_time_differential(data)

# data = cut_data(data, 200, 900)

data = remove_all_bias(data, 'Ax')
data = remove_all_bias(data, 'Ay')
data = remove_all_bias(data, 'Az')



###########################
### DATA PRE-PROCESSING ###
###########################

smoothed = smooth_convolution(data, smoothing_coefficient=3)
# smoothed = savitzky_golay_filter(data, smoothing_coefficient=5)
# smoothed = rolling_window(data, smoothing_coefficient=100)
# smoothed = double_digital_filter(data, cutoff=0.1)

############################
### DATA POST-PROCESSING ###
############################

x = double_time_accumulation(smoothed, 'Ax', 'i_Ax', 'ii_Ax')
y = double_time_accumulation(smoothed, 'Ay', 'i_Ay', 'ii_Ay')
z = double_time_accumulation(smoothed, 'Az', 'i_Az', 'ii_Az')

#########################
### DATA VISUALZATION ###
#########################

# plot_accelerometer(data, smoothed)

# plot_column(x, 'i_Ax', type="velocity")
plot_column(x, 'ii_Ax', type="position", est=[meta['distance'], 0])
# plot_column(y, 'i_Ay', name="Velocity (y)")
# plot_column(y, 'ii_Ay', name="Position (y)")
# plot_column(z, 'i_Az', name="Velocity (z)")
# plot_column(z, 'ii_Az', name="Position (z)")

show_plot()
