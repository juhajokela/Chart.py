# Chart.py

Python wrapper for Chart.js

## Install

`pip install git+https://github.com/juhajokela/Chart.py`

## Usage

``` python
from chart_py import MixedChart


chart = MixedChart(['a', 'b', 'c'])
chart.add_dataset([1, 2, 3], type='bar')
chart.add_dataset([1, 3, 6], type='line')
chart.as_html()
```
