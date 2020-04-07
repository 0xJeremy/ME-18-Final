from visualization.plot import plot_all
from visualization.plot import plot_accelerometer
from visualization.plot import plot_gyroscope
from pre_processing.load_data import load_file_to_dict
from pre_processing.tools import smooth_convolution
from pre_processing.tools import savitzky_golay_filter
from pre_processing.tools import rolling_window
from pre_processing.tools import double_digital_filter

data = load_file_to_dict('data/0405_110_1.csv')
# smoothed = smooth_convolution(data, smoothing_coefficient=100)
# smoothed = savitzky_golay_filter(data, smoothing_coefficient=101)
# smoothed = rolling_window(data, smoothing_coefficient=100)
smoothed = double_digital_filter(data, cutoff=0.1)

plot_all(data, smoothed)
