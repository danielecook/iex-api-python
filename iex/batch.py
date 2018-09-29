#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Daniel E. Cook

Batch

"""
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


class Batch:
    """
        The Batch object is designed to fetch data
        from multiple stocks.
    """

    def __init__(self, symbols, date_format='timestamp', output_format='dataframe'):
        """
            Args:
                symbols - a list of symbols.
                output_format - dataframe (pandas) or json
                convert_dates - Converts dates
        """
        self.symbols = symbols
        self.symbols_list = ','.join(symbols)
        self.date_format = validate_date_format(date_format)
        self.output_format = validate_output_format(output_format)

    def _get(self, _type, params={}):
        request_url = BASE_URL + '/stock/market/batch'
        params.update({'symbols': self.symbols_list,
                       'types': _type})
        response = requests.get(request_url, params=params)
        # Check the response
        if response.status_code != 200:
            raise Exception(f"{response.status_code}: {response.content.decode('utf-8')}")

        if self.output_format == 'json':
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
        elif _type in ['company',
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
            result = pd.DataFrame.from_dict(result_set)

        # Nested result list
        elif _type in ['book', 'chart']:
            result_set = []
            for symbol, rowset in result.items():
                for row in rowset[_type]:
                    row.update({'symbol': symbol})
                    result_set.append(row)
            result = pd.DataFrame.from_dict(result_set)

        # Convert columns with unix timestamps
        if self.date_format:
            date_field_conv = [x for x in result.columns if x in DATE_FIELDS]
            if date_field_conv:
                if self.date_format == 'datetime':
                    date_apply_func = timestamp_to_datetime
                elif self.date_format == 'isoformat':
                    date_apply_func = timestamp_to_isoformat
                result[date_field_conv] = result[date_field_conv].applymap(date_apply_func)

        # Move symbol to first column
        cols = ['symbol'] + [x for x in result.columns if x != 'symbol']
        result = result.reindex(cols, axis=1)

        return result

    def book(self):
        return self._get("book")


    def chart(self, range):
        if range not in CHART_RANGES:
            err_msg = f"Invalid range: '{range}'. Valid ranges are {', '.join(CHART_RANGES)}"
            raise ValueError(err_msg)
        return self._get("chart", params={'range': range})

    def company(self):
        return self._get("company")

    def delayed_quote(self):
        return self._get("delayed_quote")

    def dividends(self, range):
        if range not in DIVIDEND_RANGES:
            err_msg = f"Invalid range: '{range}'. Valid ranges are {', '.join(DIVIDEND_RANGES)}"
            raise ValueError(err_msg)

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

    def quote(self, displayPercent=False):
        displayPercent = param_bool(displayPercent)
        return self._get("quote", params={"displayPercent": displayPercent})

    def __repr__(self):
        return f"<Batch: {len(self.symbols)} symbols>"
