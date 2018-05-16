import pandas as pd
import requests
import re
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


class iex_stats:

    def __init__(self, date_format='timestamp', output_format='dataframe'):
        self.output_format = validate_output_format(output_format)
        self.date_format = validate_date_format(date_format)

    def _get(self, url, params={}):
        request_url =f"{BASE_URL}/stats/{url}"
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

        if self.output_format == 'dataframe':
            return pd.DataFrame.from_dict(result)
        else:
            return result

    def intraday(self):
        return self._get("intraday")

    def recent(self):
        return self._get("recent")

    def records(self):
        return self._get("records")

    def historical_summary(self, date=None):
        # Test that valid date is supplied.
        if date:
            if len(date) != 6:
                raise ValueError("Must specify date as YYYYMM")
            parse_date(str(date) + "01")
            params = {'date': date}
        else:
            params = {}
        return self._get("historical", params=params)

    def historical_daily(self, date=None, last=None):
        if date and last:
            raise ValueError("Can only supply date or last; not both")
        if date:
            if len(date) != 6:
                raise ValueError("Must specify date as YYYYMM")
            params = {'date': date}
        elif last:
            if not 0 < last <= 90:
                raise ValueError("last must be between 1 and 90")
            params = {'last': last}
        return self._get("historical/daily", params=params)

    def __repr__(self):
        return f"<iex_stats:{self.symbol}>"


i = iex_stats()
print(i.historical_daily(last=90))