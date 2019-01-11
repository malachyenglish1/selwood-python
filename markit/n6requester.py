import requests, datetime, time
from pprint import pprint

BASE_URL = 'https://api-services-dv-04.markit.partners'
USERNAME = 'markit/resellers/API_OPS/accounts/test_python.dev'
PASSWORD = 'Pith0n@2018'

"""
ENVIRONMENT REQUIREMENT
----------

Python version
- python version must be >= 3.5

Required packages
- requests

USAGE
----------
- Make sure BASE_URL, USERNAME, PASSWORD is correct
- See the end of code (within `if __name__ == '__main__'` section) for usage.

Yan<yan.xue@ihsmarkit.com>, 20180907
"""


class Subscription:
    result = None

    def __init__(self, namespace, name, **kwargs):
        self.api = N6Utils()
        self.namespace = namespace
        self.name = name
        self.kwargs = kwargs

    def next(self):
        self.result = self.api._get(self.namespace, self.name, method='stream', **self.kwargs)
        if 'after' in self.result:
            self.kwargs['after'] = self.result['after']
        return self.result

    @property
    def current_raw(self):
        if self.result:
            return self.result
        return self.next()

    @property
    def current(self):
        if 'data' in self.current_raw and isinstance(self.current_raw['data'], list):
            return self.current_raw['data']
        else:
            return []


class N6Utils:
    BASE_URL = BASE_URL
    USERNAME = USERNAME
    PASSWORD = PASSWORD
    _api_key = None

    @property
    def api_key(self):
        if self._api_key:
            return self._api_key
        url = '/apikey'
        r = requests.post(self.BASE_URL + url, data={'username': self.USERNAME, 'password': self.PASSWORD})
        return r.text

    @property
    def default_param(self):
        return {'apiKey': self.api_key}

    def _get(self, namespace, name, *, method, **kwargs):
        url = f'{self.BASE_URL}/{namespace}/{name}/{method}'
        if kwargs:
            for k, v in kwargs.items():
                if isinstance(v, list):
                    kwargs[k] = ','.join(v)
        params = {**self.default_param, **kwargs}
        r = requests.get(url, params=params)
        try:
            result = r.json()
        except:
            raise Exception(r.text)
        if 'errorMessage' in result:
            raise Exception(result['errorMessage'])
        return result

    def get_latest(self, *args, **kwargs):
        return self._get(method='latest', *args, **kwargs)

    def get_timeseries(self, *args, date_form, date_to, **kwargs):
        """For dates here, always use either string, a naive datetime object, or a datetime object with UTC timezone"""
        if not isinstance(date_form, str):
            date_form = date_form.strftime('%Y-%m-%dT%H:%M:%SZ')
        if not isinstance(date_to, str):
            date_to = date_to.strftime('%Y-%m-%dT%H:%M:%SZ')

        kwargs['from'] = date_form
        kwargs['to'] = date_to

        return self._get(method='timeseries', *args, **kwargs)

    @staticmethod
    def subscribe_stream(namespace, name, **kwargs):
        subscription = Subscription(namespace, name, **kwargs)
        return subscription


if __name__ == '__main__':
    n6 = N6Utils()

    request_type = 'stream'

    if request_type == 'latest':
        pprint(n6.get_latest('csbpi', 'Price', limit=3, isin=['XS1185955306', 'JP2230001F34']))

        # pprint(n6.get_latest('csbpi', 'Price', limit=3, isin=['XS1185955306', 'JP2230001F34']))
        # pprint(n6.get_latest('csbpi', 'Price', limit=3, isin=['XS1185955306', 'JP2230001F34'], fields=['id', 'isin']))
        # pprint(n6.get_latest('csbpi', 'Price', limit=3, isin=['XS1185955306', 'JP2230001F34'], fields=['id', 'isin']))
        # pprint(n6.get_latest('cilp', 'Curve', limit=3, red9=['something', 'somethingelse']))

    elif request_type == 'timeseries':
        pprint(n6.get_timeseries('csbpi', 'Price', date_form=datetime.datetime.now() - datetime.timedelta(days=600),
                                 date_to=datetime.datetime.now(), limit=3, isin=['XS1185955306', 'JP2230001F34'],
                                 fields=['id', 'isin']))
    elif request_type == 'stream':
        sub = n6.subscribe_stream('csbpi', 'Price', limit=1, isin=['XS1198103456'])
        # sub = n6.subscribe_stream('csbpi', 'Price', limit=1)

        while True:
            sub.next()
            pprint(sub.current)
            time.sleep(1)
