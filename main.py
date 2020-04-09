from visualization.plot import plot_all
from visualization.plot import plot_accelerometer
from visualization.plot import plot_gyroscope
from visualization.plot import plot_column

from pre_processing.load_data import load_file_to_dict
from pre_processing.load_data import add_time_differential
from pre_processing.tools import smooth_convolution
from pre_processing.tools import savitzky_golay_filter
from pre_processing.tools import rolling_window
from pre_processing.tools import double_digital_filter

from post_processing.tools import add_accumulation_column
from post_processing.tools import double_accumulation

####################
### DATA LOADING ###
####################

ROWS = ['Ax', 'Ay', 'Az', 'time']

data = load_file_to_dict('data/0407_1d_1/0407_10_fast_1.csv', ROWS)
data = add_time_differential(data)

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

smoothed = double_accumulation(smoothed, 'Ay', 'i_Ay', 'ii_Ay')


#########################
### DATA VISUALZATION ###
#########################


plot_accelerometer(data, smoothed)

plot_column(smoothed, 'ii_Ay')



