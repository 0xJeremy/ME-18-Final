from visualization.plot import plot_all
from visualization.plot import plot_accelerometer
from visualization.plot import plot_gyroscope
from visualization.plot import plot_column
from visualization.plot import show_plot

from pre_processing.load_data import load_file_to_dict
from pre_processing.load_data import add_time_differential
from pre_processing.load_data import get_file_metadata
from pre_processing.load_data import remove_gravity_bias
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

data = load_file_to_dict('data/0407_1d_1/0407_10_fast_1.csv', ROWS)
data = add_time_differential(data)
data = remove_gravity_bias(data)

###########################
### DATA PRE-PROCESSING ###
###########################

smoothed = smooth_convolution(data, smoothing_coefficient=10)
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

plot_accelerometer(data, smoothed)

plot_column(x, 'i_Ax')
plot_column(x, 'ii_Ax')
plot_column(y, 'i_Ay')
plot_column(y, 'ii_Ay')
plot_column(z, 'i_Az')
plot_column(z, 'ii_Az')

show_plot()
