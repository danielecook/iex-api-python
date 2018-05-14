import pandas as pd
import requests
import re


BASE_URL = "https://api.iextrading.com/1.0"


class stats:

    def __init__(self, output_format='dataframe'):
        """
            Args:
                symbols - a list of symbols.
                format - dataframe (pandas) or json
        """
        self.output_format = output_format

    def _get(self, path, params={}):
        request_url = f"{BASE_URL}/stats/{path}"
        response = requests.get(request_url, params=params)
        if response.status_code != 200:
            raise Exception(f"{response.status_code}: {response.content.decode('utf-8')}")
        if self.output_format == 'json':
            return response.json()
        else:
            return pd.DataFrame.from_dict(response.json())

    def intraday(self):
        return self._get("intraday")

    def recent(self):
        return self._get("recent")

    def records(self):
        return self._get("records")

    def historical_summary(self, date=""):
        params = {}
        date_match = re.match('[0-9]{6}', str(date))
        if date and not date_match:
            raise ValueError("Date incorrectly specified. Must match YYYYMM")
        if date_match:
            params.update({'date': date})
        return self._get("historical", params)

    def historical_daily(self, last, date=""):
        params = {}
        date_match = re.match('[0-9]{6}', str(date))
        # Check for input errors
        if date and not date_match:
            raise ValueError("Date incorrectly specified. Must match YYYYMM")
        if date and last:
            raise ValueError("Cannot specify last and date parameters")
        if not isinstance(last, int):
            raise ValueError("last must be specified as an integer.")
        if date_match:
            params.update({'date': date})
        elif last:
            params.update({'last': last})
        return self._get("historical/daily", params)


r = stats()
print(r.records())
#print(r.symbols())