from datetime import datetime
from chart_py import MixedChart


def save(string):
    timestamp = datetime.utcnow().isoformat()
    filename = 'output_{timestamp}.html'.format(timestamp=timestamp)
    filename = 'output.html'  # override
    with open(filename, 'w') as f:
        f.write(string)


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
chart.add_dataset(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    type='bar',
)
chart.add_dataset(
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 80],
    type='line',
)
chart.add_dataset(
    [0, 5, 10, 15, 20, 25, 30, 35, 30, 20, 10, 0],
    type='area',
)
save(chart.as_page())
