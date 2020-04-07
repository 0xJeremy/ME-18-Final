from visualization.plot import plot_all
from pre_processing.load_data import load_file_to_dict
from pre_processing.tools import smooth_convolution

data = load_file_to_dict('data/0405_110_1.csv')
smoothed = smooth_convolution(data, smoothing_coefficient=5)

plot_all(data, smoothed)
