import pandas as pd
import requests
from iex.utils import (parse_date,
                       validate_output_format)
from iex.constants import BASE_URL


class reference:

    def __init__(self, output_format='dataframe'):
        """
            Args:
                output_format - dataframe (pandas) or dict
        """
        self.output_format = validate_output_format(output_format)

    def _get(self, path):
        request_url = f"{BASE_URL}/ref-data/{path}"
        response = requests.get(request_url)
        if response.status_code != 200:
            raise Exception(f"{response.status_code}: {response.content.decode('utf-8')}")
        if self.output_format == 'json':
            return response.json()
        else:
            # Move symbol to first column
            result = pd.DataFrame.from_dict(response.json())
            cols = ['symbol'] + [x for x in result.columns if x != 'symbol']
            result = result.reindex(cols, axis=1)
            return result

    def symbols(self):
        return self._get("symbols")

    def iex_corporate_actions(self, date=None):
        date = parse_date(date)
        url = f"daily-list/corporate-actions/{date}" if date else "daily-list/corporate-actions"
        return self._get(url)

    def iex_dividends(self, date=None):
        date = parse_date(date)
        url = f"daily-list/dividends/{date}" if date else "daily-list/dividends"
        return self._get(url)

    def iex_next_day_ex_date(self, date=None):
        date = parse_date(date)
        url = f"daily-list/next-day-ex-date/{date}" if date else "daily-list/next-day-ex-date"
        return self._get(url)

    def iex_listed_symbol_directory(self, date=None):
        date = parse_date(date)
        url = f"daily-list/symbol-directory/{date}" if date else "daily-list/symbol-directory"
        return self._get(url)
