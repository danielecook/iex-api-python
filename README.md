[![Build Status](https://travis-ci.org/danielecook/iex-api-python.svg?branch=master)](https://travis-ci.org/danielecook/iex-api-python) [![Coverage Status](https://coveralls.io/repos/github/danielecook/iex-api-python/badge.svg)](https://coveralls.io/github/danielecook/iex-api-python)

# IEX-API-Python - [Documentation](http://www.danielecook.com/iex-api-python/stocks/)

__Python >=3.6__

![under construction](https://countspooky.neocities.org/construction.gif)

This module is currently being actively developed. Feedback is welcomed.

### Summary

The `iex-api-python` module is a wrapper for the [IEX API](https://iextrading.com/developer/docs/#getting-started), and is designed to closely map to the organization of the original API while adding functionality. A few examples of the additional functionality are:

* Many queries are returned as [Pandas Dataframes](https://pandas.pydata.org/).
* Built-in support for websockets connections.
* Option to format timestamps as datetime objects or ISO-dates.

Before using __IEX-API-Python__ and the __IEX API__ you should read the [API terms of use](https://iextrading.com/api-terms/) and review the [documentation](https://iextrading.com/developer/docs/).

### Organization

The `IEX-API-Python` module is designed to map closely to the API from IEX. For many of the API calls, the resulting dataset is better represented in a tabular format. For these calls, data are returned as a [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html).

### Examples

To illustrate a few things you can do with `iex-api-python`, take a look at the examples below.

__Fetch all stock symbols__

```
from iex import reference
ref = reference()
ref.symbols() # Returns a Pandas Dataframe of all stock symbols, names, and more.
```
```
     symbol        date  iexId  isEnabled  \
0         A  2018-05-16      2       True
1        AA  2018-05-16  12042       True
2      AABA  2018-05-16   7653       True
3       AAC  2018-05-16   9169       True
```

__Get a stocks price__

```
from iex import stock
stock("F").price()
```
```
11.4
```

__Get a stocks price for the last year__
```
from iex import stock
stock("F").chart_table(range="1y")
```
```
       change  changeOverTime  changePercent    close        date     high  \
0    0.000000        0.000000          0.000  10.2760  2017-05-16  10.3982
1   -0.169075       -0.016446         -1.645  10.1070  2017-05-17  10.2854
2    0.028180       -0.013712          0.279  10.1351  2017-05-18  10.1633
3    0.075144       -0.006394          0.741  10.2103  2017-05-19  10.2760
4    0.216042        0.014626          2.116  10.4263  2017-05-22  10.4545
5   -0.046966        0.010062         -0.450  10.3794  2017-05-23  10.4874
6   -0.084539        0.001830         -0.814  10.2948  2017-05-24  10.3888
...
```

__Fetch 