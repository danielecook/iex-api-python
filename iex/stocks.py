import pandas as pd
import requests
import re
import datetime
import json
from pandas import Series
from iex.utils import (param_bool,
                       parse_date,
                       validate_date_format,
                       validate_range_set,
                       validate_output_format,
                       timestamp_to_datetime,
                       timestamp_to_isoformat)
from iex.constants import (BASE_URL,
                           CHART_RANGES,
                           RANGES,
                           DATE_FIELDS)


class stock:

    def __init__(self, symbol, date_format='timestamp'):
        self.symbol = symbol.upper()
        self.date_format = validate_date_format(date_format)

    def _get(self, url, params={}):
        request_url =f"{BASE_URL}/stock/{self.symbol}/{url}"
        response = requests.get(request_url, params=params)
        print(response.url)
        if response.status_code != 200:
            raise Exception(f"{response.status_code}: {response.content.decode('utf-8')}")
        result = response.json()

        # timestamp conversion
        if type(result) == dict and self.date_format:
            if self.date_format == 'datetime':
                date_apply_func = timestamp_to_datetime
            elif self.date_format == 'isoformat':
                date_apply_func = timestamp_to_isoformat

            for key, val in result.items():
                if key in DATE_FIELDS:
                    result[key] = date_apply_func(val)
        return result

    def book(self):
        return self._get("book")

    def chart(self,
              range='1m',
              chartReset=None,
              chartSimplify=None,
              chartInterval=None):
        """
            Args:
                range - what range of data to retrieve. The variable 'CHART_RANGES'
                        has possible values in addition to a date.
        """

        # Setup parameters
        params = {'chartReset': chartReset,
                  'chartSimplify': chartSimplify,
                  'chartInterval': chartInterval}
        params = {k: param_bool(v) for k, v in params.items() if v}
        if chartReset and type(chartReset) != bool:
            raise ValueError("chartReset must be bool")
        if chartSimplify and type(chartSimplify) != bool:
            raise ValueError("chartSimplify must be bool")
        if chartInterval and type(chartInterval) != int:
            raise ValueError("chartInterval must be int")

        # Validate range is appropriate
        validate_range_set(range, CHART_RANGES)

        # date match
        date_match = re.match('^[0-9]{8}$', range)

        if date_match:
            range = parse_date(range)
            url = f"chart/date/{range}"
        else:
            url = f"chart/{range}"

        return self._get(url, params=params)

    def chart_table(self,
                    range='1m',
                    chartReset=None,
                    chartSimplify=None,
                    chartInterval=None):
        """
            Args:
                range
                chartReset
                chartSimplify
                chartInterval

        """

        params = {'chartReset': chartReset,
                  'chartSimplify': chartSimplify,
                  'chartInterval': chartInterval}
        params = {k: v for k, v in params.items() if v}

        chart_result = self.chart(range, **params)
        if not chart_result:
            return pd.DataFrame.from_dict({})
        if type(chart_result) == dict:
            # If dynamic is specified, return the range to the user.
            chart_range = chart_result.get('range')
            chart_data = chart_result.get('data')
            chart_data = pd.DataFrame.from_dict(chart_data)
            chart_data['range'] = chart_range
            return pd.DataFrame.from_dict(chart_data)
        elif type(chart_result) == list:
            return pd.DataFrame.from_dict(chart_result)
 
    def company(self):
        return self._get("company")

    def delayed_quote(self):
        return self._get("delayed-quote")

    def dividends(self, range='1m'):
        """
            Args:
                range - what range of data to retrieve. The variable
                        'DIVIDEND_RANGES' has possible values in addition to a date.
        """
        validate_range_set(range, RANGES)
        return self._get(f"chart/{range}")

    def dividends_table(self, range='1m'):
        dividends_data = self.dividends(range)
        return pd.DataFrame.from_dict(dividends_data)

    def earnings(self):
        return self._get("earnings")

    def effective_spread(self):
        return self._get("effective-spread")

    def effective_spread_table(self):
        return pd.DataFrame.from_dict(self.effective_spread())

    def financials(self):
        return self._get("financials")['financials']

    def financials_table(self):
        return pd.DataFrame.from_dict(self.financials())

    def stats(self):
        return self._get("stats")

    def logo(self):
        return self._get("logo")

    def news(self, last=10):
        if not 1 <= last <= 50:
            raise ValueError("Last must not be a value between 1 and 50.")
        url = f"news/last/{last}" if last else "news"
        return self._get(url)

    def ohlc(self):
        return self._get("ohlc")

    def peers(self, as_string=False):
        if as_string:
            return [x for x in self._get("peers")]
        else:
            return [stock(x) for x in self._get("peers")]

    def previous(self):
        return self._get(f"previous")

    def price(self):
        return self._get("price")

    def quote(self, displayPercent=False):
        return self._get("quote", params={"displayPercent": param_bool(displayPercent)})

    def relevant(self):
        return self._get("relevant")

    def splits(self, range="1m"):
        validate_range_set(range, RANGES)
        return self._get(f"splits/{range}")

    def time_series(self, range='1m', chartReset=None, chartSimplify=None, chartInterval=None):
        return self.chart(range,
                          chartReset,
                          chartSimplify,
                          chartInterval)

    def volume_by_venue(self):
        return self._get("volume-by-venue")

    def volume_by_venue_table(self):
        return pd.DataFrame.from_dict(self.volume_by_venue())

    def __repr__(self):
        return f"<stock:{self.symbol}>"

