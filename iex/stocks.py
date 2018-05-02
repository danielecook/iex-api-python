import pandas as pd
import requests
import datetime
import arrow


BASE_URL = "https://api.iextrading.com/1.0"
CHART_RANGES = ['5y', '2y', '1y',
                'ytd', '6m', '3m',
                '1m', '1d', 'date',
                'dynamic']
DIVIDEND_RANGES = ['5y', '2y', '1y',
                   'ytd', '6m', '3m', '1m']


class stock:

    def __init__(self, symbol):
        self.symbol = symbol.upper()

    def _get(self, url):
        request_url = BASE_URL + '/stock/' + url
        print(request_url)
        response = requests.get(request_url)
        if response.status_code != 200:
            raise Exception(f"{response.status_code}: {response.content.decode('utf-8')}")
        return response.json()

    def book(self):
        return self._get(f"{self.symbol}/book").get('quote')

    def chart(self, range='1d'):
        """
            Args:
                range - what range of data to retrieve. The variable 'CHART_RANGES'
                        has possible values in addition to a date.
        """
        if range not in CHART_RANGES and type(range) not in [int, datetime.datetime]:
            err_msg = f"Invalid chart type '{range}'. Valid chart types are {', '.join(CHART_RANGES)}, YYYYMMDD (int), datetime"
            raise ValueError(err_msg)

        if type(range) == int:
            url = f"{self.symbol}/chart/date/{range}"
        elif type(range) == datetime.datetime:
            range = arrow.get(range).strftime("%Y%m%d")
            url = f"{self.symbol}/chart/date/{range}"
        else:
            url = f"{self.symbol}/chart/{range}"

        return self._get(url)

    def chart_table(self, range='1d'):
        chart_data = self.chart(range)
        return pd.DataFrame.from_dict(chart_data)

    def company(self):
        return self._get(f"{self.symbol}/company")

    def delayed_quote(self):
        dquote = self._get(f"{self.symbol}/delayed-quote")
        dquote['delayedPriceTime'] = arrow.get(
            dquote['delayedPriceTime'] / 1000.0).datetime
        dquote['processedTime'] = arrow.get(
            dquote['processedTime'] / 1000.0).datetime
        return dquote

    def dividends(self, range='1m'):
        """
            Args:
                range - what range of data to retrieve. The variable 'DIVIDEND_RANGES'
                        has possible values in addition to a date.
        """
        DIVIDEND_RANGES
        if range not in CHART_RANGES and type(range) not in [int, datetime.datetime]:
            err_msg = f"Invalid range: '{range}'. Valid chart types are {', '.join(CHART_RANGES)}, YYYYMMDD (int), datetime"
            raise ValueError(err_msg)
        else:
            url = f"{self.symbol}/chart/{range}"
        return self._get(url)

    def dividends_table(self, range='1m'):
        dividends_data = self.dividends(range)
        return pd.DataFrame.from_dict(dividends_data)

    def earnings(self):
        return self._get(f"{self.symbol}/earnings")

    def effective_spread(self):
        return self._get(f"{self.symbol}/effective-spread")

    def effective_spread_table(self):
        return pd.DataFrame.from_dict(self.effective_spread())

    def financials(self):
        return self._get(f"{self.symbol}/financials")['financials']

    def financials_table(self):
        return pd.DataFrame.from_dict(self.financials())

    def price(self):
        return self._get(f"{self.symbol}/price")

    def stats(self):
        return self._get(f"{self.symbol}/stats")

    @property
    def peers(self):
        return [stock(x) for x in self._get(f"/stock/{self.symbol}/peers")]

    def __repr__(self):
        return f"<stock:{self.symbol}>"


class batch:
    """
        The batch object is designed to fetch data
        from multiple stocks.
    """

    def __init__(self, symbols, format='dataframe'):
        """
            Args:
                symbols - a list of symbols.
                format - dataframe (pandas) or json
        """
        self.symbols = symbols
        self.symbols_list = ','.join(symbols)
        if format not in ['dataframe', 'json']:
            raise ValueError("batch format must be either 'dataframe' or 'json")
        self.format = format

    def _get(self, _type, params={}):
        request_url = BASE_URL + '/stock/market/batch'
        params.update({'symbols': self.symbols_list,
                       'types': _type})
        response = requests.get(request_url, params=params)
        print(response.url)
        # Check the response
        if response.status_code != 200:
            raise Exception(f"{response.status_code}: {response.content.decode('utf-8')}")

        if self.format == 'json':
            return response.json()
        result = response.json()

        if _type in ['delayed_quote',
                     'price']:
            for symbol, v in result.items():
                v.update({'symbol': symbol})
            result = pd.DataFrame.from_dict([v for k, v in result.items()])

        # Symbol --> List
        elif _type in ['peers']:
            for symbol, v in result.items():
                v.update({'symbol': symbol})
            result = pd.DataFrame.from_dict([v for k, v in result.items()])
            # Expand nested columns
            result = result.set_index('symbol') \
                           .apply(lambda x: x.apply(pd.Series).stack()) \
                           .reset_index() \
                           .drop('level_1', 1)

        # Nested result
        elif _type in ['book',
                       'company',
                       'quote',
                       'stats']:
            for symbol, item in result.items():
                item.update({'symbol': symbol})
            result = pd.DataFrame.from_dict([v[_type] for k, v in result.items()])

        # Nested multi-line
        elif _type in ['earnings', 'financials']:
            result_set = []
            for symbol, rows in result.items():
                for row in rows[_type][_type]:
                    row.update({'symbol': symbol})
                    result_set.append(row)
            #print([v[_type] for k, v in result.items()])
            result = pd.DataFrame.from_dict(result_set)


        # Move symbol to first column
        cols = ['symbol'] + [x for x in result.columns if x != 'symbol']
        result = result.reindex_axis(cols, axis=1)
        return result

    #def book(self):
    #    Complex structure
    #    return self._get("book")

    def company(self):
        return self._get("company")

    def delayed_quote(self):
        return self._get("delayed_quote")

    #def chart(self):
    #    return self._get('chart')

    def earnings(self):
        return self._get('earnings')

    def financials(self):
        return self._get('financials')

    def stats(self):
        return self._get('stats')

    def peers(self):
        return self._get('peers')

    def price(self):
        return self._get("price")

    def quote(self):
        return self._get("quote")



a = batch(["AAPL", "F", "TSLA", "MSFT", 'G', 'GOOG'])

print(a.quote())
