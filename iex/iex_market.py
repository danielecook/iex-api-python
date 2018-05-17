import json
import requests
import pandas as pd
from iex.utils import (parse_date,
                       validate_date_format,
                       validate_range_set,
                       validate_output_format,
                       timestamp_to_datetime,
                       timestamp_to_isoformat)

from iex.constants import (CHART_RANGES,
                           RANGES,
                           DATE_FIELDS,
                           BASE_URL,
                           BASE_SIO_URL,
                           BASE_SIO_VERSION)

from socketIO_client_nexus import (SocketIO,
                                   SocketIONamespace)

class feed_handler(SocketIONamespace):
    
    def on_connect(self):
        print("connected")

    def on_disconnect(self):
        print("disconnected")

    def on_message(self, msg):
        data = json.loads(msg)
        print(data)



class iex_market:

    def __init__(self, symbols = None, socket_handler = None, date_format='timestamp', output_format='dataframe'):
        """
            Args:
                socket_handler - Function for handling socket feed.
                date_format - Converts dates
                output_format - dataframe (pandas) or json

        """
        self.symbols = symbols
        self.socket_handler = socket_handler
        self.date_format = validate_date_format(date_format)
        self.output_format = validate_output_format(output_format)


    def _socket(self):
        socket = SocketIO('https://ws-api.iextrading.com', 443)
        namespace = socket.define(feed_handler, "/1.0/tops")
        symbols = "snap"
        namespace.emit('subscribe', 'firehose')
        socket.wait()


    def _get(self, url, params={}):
        request_url =f"{BASE_URL}"
        response = requests.get(f"{request_url}/{url}", params=params)
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

    def tops(self):
        params = {'symbols', ','.join(self.symbols)} if self.symbols else {}
        return self._get("tops")

    def __repr__(self):
        return f"<iex_market>"

