from chart_py import MixedChart
from chart_py.utilities import combine
from chart_py.utilities import cumulate


chart = MixedChart([
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
])
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
chart.add_dataset(data, type='bar',)
chart.add_dataset(cumulate(data), type='line')
chart.add_dataset(combine(cumulate(data), data), type='area')
chart.save_as_html()
