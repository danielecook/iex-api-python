import pandas as pd
import requests
import datetime
import arrow


BASE_URL = "https://api.iextrading.com/1.0"


class reference:

    def __init__(self, output_format='dataframe'):
        """
            Args:
                symbols - a list of symbols.
                format - dataframe (pandas) or json
        """
        self.output_format = output_format

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
        if date:
            url = f"daily-list/corporate-actions/{range}"
        else:
            url = "daily-list/corporate-actions"
        return self._get(url)

    def iex_dividends(self):
        pass

r = reference()

#print(r.symbols())