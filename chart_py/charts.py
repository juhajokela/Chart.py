import json
import os
from datetime import datetime
from string import Template


__all__ = (
    'MixedChart',
)


THIS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(THIS_DIRECTORY, 'templates/widget.html')) as f:
    template_html = Template(f.read())
with open(os.path.join(THIS_DIRECTORY, 'templates/page.html')) as f:
    template_page = Template(f.read())


class BaseChart(object):

    _DEFAULT_COLORS = [
        (54,  162, 235),
        (75,  192, 192),
        (153, 102, 255),
        (201, 203, 207),
        (255,  99, 132),
        (255, 159,  64),
        (255, 205,  86),
    ]

    def __init__(self, labels):
        self.labels = labels
        self.datasets = []

    def _set_default_color(self, kwargs):
        idx = len(self.datasets) % len(self._DEFAULT_COLORS)
        color = self._DEFAULT_COLORS[idx]
        kwargs.setdefault(
            'borderColor', 'rgba({}, {}, {}, 1)'.format(*color)
        )
        kwargs.setdefault(
            'backgroundColor', 'rgba({}, {}, {}, 0.1)'.format(*color)
        )

    def add_dataset(self, data, **kwargs):
        self._set_default_color(kwargs)
        # set default dataset label
        kwargs.setdefault('label', 'Dataset {}'.format(len(self.datasets) + 1))
        kwargs['data'] = data
        self.datasets.append(kwargs)

    def as_dict(self):
        raise NotImplementedError

    def as_json(self, indent=2):
        return json.dumps(
            self.as_dict(),
            ensure_ascii=False,
            sort_keys=True,
            indent=indent
        )

    def as_html(self):
        return template_html.substitute(data=self.as_json(indent=None))

    def as_page(self):
        return template_page.substitute(content=self.as_html())

    def save_as_html(self, filename=''):
        timestamp = datetime.utcnow().isoformat()
        filename = (
            filename or 'chart_{timestamp}.html'.format(timestamp=timestamp)
        )
        with open(filename, 'w') as f:
            f.write(self.as_page())


class MixedChart(BaseChart):

    _TYPES = {
        'bar': {
            'type': 'bar',
        },
        'line': {
            'type': 'line',
            'fill': False,
        },
        'area': {
            'type': 'line',
            'fill': True,
        },
    }

    def add_dataset(self, data, type='bar', **kwargs):
        kwargs.update(self._TYPES[type])
        if type == 'bar':
            kwargs.setdefault('borderWidth', 1)
        super().add_dataset(data, **kwargs)

    def as_dict(self):
        return {
            'type': 'bar',
            'data': {
                'labels': self.labels,
                'datasets': self.datasets,
            },
        }
