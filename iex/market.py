import pandas as pd
import requests
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

class Market:

    def __init__(self, date_format='timestamp', output_format='dataframe'):
        """
            Args:
                date_format - Converts dates
                output_format - dataframe (pandas) or json
        """
        self.date_format = validate_date_format(date_format)
        self.output_format = validate_output_format(output_format)


    def _get(self, url, params={}):
        if not url:
            request_url = f"{BASE_URL}/market"
        else:
            request_url =f"{BASE_URL}/stock/market/{url}"
        response = requests.get(request_url, params=params)

        if response.status_code != 200:
            raise Exception(f"{response.status_code}: {response.content.decode('utf-8')}")
        result = response.json()

        if self.output_format =='dataframe':
            if url == 'previous':
                # Reorient previous result.
                result = pd.DataFrame.from_dict(result).transpose().reset_index()
                cols = ['symbol'] + [x for x in result.columns if x != 'symbol' and x != 'index']
                result = result.reindex(cols, axis=1)
                # previous has no date cols.
                return result

            result = pd.DataFrame.from_dict(result)
            if self.date_format:
                result = convert_pandas_datetimes(result, self.date_format)
            return result


    def threshold_securities(self, date=None):
        date = parse_date(date)
        url = f"threshold-securities/{date}" if date else "threshold-securities"
        return self._get(url)

    def short_interest(self, date=None):
        date = parse_date(date)
        url = f"short-interest/{date}" if date else "short-interest"
        return self._get(url)

    # List Items
    def mostactive(self):
        return self._get("list/mostactive")

    def gainers(self):
        return self._get("list/gainers")

    def losers(self):
        return self._get("list/losers")

    def iexvolume(self):
        return self._get("list/iexvolume")

    def iexpercent(self):
        return self._get("list/iexpercent")

    def news(self, last=10):
        if not 1 <= last <= 50:
            raise ValueError("Last must not be a value between 1 and 50.")
        url = f"news/last/{last}" if last else "news"
        return self._get(url)

    def ohlc(self):
        return self._get("ohlc")

    def previous(self):
        return self._get("previous")

    def market(self):
        # Returns /market - Gives near-realtime traded volume on markets
        return self._get("")

    def __repr__(self):
        return f"<market>"


market = Market()
