#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Daniel E. Cook

Static variables (constants)

"""

BASE_URL = "https://api.iextrading.com/1.0"
BASE_SIO_URL, BASE_SIO_VERSION = "https://ws-api.iextrading.com", "1.0"
CHART_RANGES = ['', '5y', '2y', '1y',
                'ytd', '6m', '3m',
                '1m', '1d', 'date',
                'dynamic']
RANGES = ['5y', '2y', '1y',
          'ytd', '6m', '3m', '1m']
DATE_FIELDS = ['openTime',
               'closeTime',
               'latestUpdate',
               'iexLastUpdated',
               'delayedPriceTime',
               'processedTime',
               'lastSaleTime',
               'lastUpdated']