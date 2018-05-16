import pandas as pd
import requests
from iex.utils import (parse_date,
                       validate_date_format,
                       validate_range_set,
                       validate_output_format,
                       timestamp_to_datetime,
                       timestamp_to_isoformat)

from iex.constants import (BASE_URL,
                           CHART_RANGES,
                           RANGES,
                           DATE_FIELDS)

class iex_market:

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
        if self.output_format =='dataframe':
            if url == 'previous':
                # Reorient previous result.
                result = pd.DataFrame.from_dict(result).transpose().reset_index()
                cols = ['symbol'] + [x for x in result.columns if x != 'symbol' and x != 'index']
                result = result.reindex(cols, axis=1)
                return result
            return pd.DataFrame.from_dict(result)


    def __repr__(self):
        return f"<iex_market>"

