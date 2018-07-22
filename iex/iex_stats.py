import re
import requests
import pandas as pd

from iex.utils import (parse_date,
                       convert_pandas_datetimes,
                       validate_date_format,
                       validate_range_set,
                       validate_output_format,
                       timestamp_to_datetime,
                       timestamp_to_isoformat)

from iex.constants import (BASE_URL,
                           CHART_RANGES,
                           RANGES,
                           DATE_FIELDS)


class IexStats:

    def __init__(self, date_format='timestamp', output_format='dataframe'):
        self.output_format = validate_output_format(output_format)
        self.date_format = validate_date_format(date_format)

    def _get(self, url, params={}):
        request_url =f"{BASE_URL}/stats/{url}"
        response = requests.get(request_url, params=params)
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
            result = pd.DataFrame.from_dict(result)
            # Transpose certain datasets
            if url in ['intraday', 'records']:
                result = result.transpose()
            result = convert_pandas_datetimes(result, self.date_format)
            return result
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
            if not bool(re.match(r"[0-9]{6}", str(date))):
                raise ValueError("Must specify date as YYYYMM")
            parse_date(str(date) + "01")
            params = {'date': date}
        else:
            params = {}
        return self._get("historical", params=params)

    def historical_daily(self, date=None, last=None):
        params = {}
        if date is not None and last is not None:
            raise ValueError("Can only supply date or last; not both")
        if date is not None:
            if not bool(re.match(r"[0-9]{6}", str(date))):
                raise ValueError("Must specify date as YYYYMM")
            params = {'date': date}
        elif last is not None:
            if not 0 < last <= 90:
                raise ValueError("last must be between 1 and 90")
            params = {'last': last}
        return self._get("historical/daily", params=params)

    def __repr__(self):
        return f"<iex_stats>"


iex_stats = IexStats()
