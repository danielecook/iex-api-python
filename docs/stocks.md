# Stocks

## The stock object

The `stock` object is useful for returning information for individual stocks, and is designed to map closely to the __[Stocks](https://iextrading.com/developer/docs/#stocks)__ section of the IEX API. One major difference is that the `stock` object is not designed to handle batch requests. Instead, batch requests can be handled using the [`batch`](batch) object.

Most of the `stock` methods return a python dictionary whereas `batch` methods tend to return Pandas dataframes. However, several `stock` methods have supplementary methods (suffixed with `_table`) that will return a Pandas dataframe.

```
stock(symbol, date_format)`
```

__Parameters__

* __`symbol`__ - A stock symbol
* __`date_format` (default: timestamp)__ - Specifies how timestamps should be should be returned. Set to one of the following:
    * `timestamp` - default; Does not alter IEX API output.
    * `datetime` - Datetime object.
    * `isoformat` - Converts to isoformat.

## Creating a new `stock` object

Provide a stock symbol to create a stock object.

``` python
tsla = stock("tsla")
```

----

## Stock Methods

Below are the methods that can be invoked with a `stock` object. After each method listed below is a `ref` link which will take you to the corresponding IEX API documentation.

### `book()`

[IEX API - Book](https://iextrading.com/developer/docs/#book)

``` python
goog = stock("goog")
goog.book()
```

    # Output
    {'symbol': 'GOOG',
     'companyName': 'Alphabet Inc.',
     ...
     'week52Low': 894.79,
     'ytdChange': 0.0312300469483568}

### `chart()`

[IEX API - Chart <i class="fa fa-external-link-square"></i>](https://iextrading.com/developer/docs/#chart)

__Parameters__

* __`range` (default: 1m)__ - Historical adjusted market-wide data or IEX-only data. See the [IEX API reference](https://iextrading.com/developer/docs/#chart) for further details.
    - `5y` `2y` `1y` `ytd` `6m` `3m` `1m` `YYYYMMDD (date)` `dynamic`
* __`chartReset` (bool; default: `None`)__ - 1d chart will reset at midnight instead of the default behavior of 9:30am ET.
* __`chartSimplify` (bool; default: `None`)__ -  If `True`, runs a polyline simplification using the Douglas-Peucker algorithm. This is useful if plotting sparkline charts.
* __`chartInterval` (bool: default: `None`)__ -  If passed, chart data will return every Nth element.

### `chart_table()`

Returns a pandas dataframe from chart data. If `range=dynamic`, a `range` column is appended to the returned dataframe indicating whether the data is for `1d` or `1m`. See the IEX API documentation for further details.

__Parameters__

The same parameters are available as with [`chart()`](#chart).

__Example__

``` python
goog = stock("goog")
goog.chart_table(range='1d')
```

    # Output
          average  changeOverTime     close      date      high  \
    0    1094.852        0.000000  1095.535  20180511  1095.535
    1      -1.000             NaN       NaN  20180511    -1.000
    2      -1.000             NaN       NaN  20180511    -1.000
    3    1093.145       -0.001559  1093.420  20180511  1093.630
    ...


### `company()`

[IEX API - Company <i class="fa fa-external-link-square"></i>](https://iextrading.com/developer/docs/#company)

### `delayed_quote()`

[IEX API - Delayed Quote <i class="fa fa-external-link-square"></i>](https://iextrading.com/developer/docs/#delayed-quote)

### `dividends()`

[IEX API - Dividends <i class="fa fa-external-link-square"></i>](https://iextrading.com/developer/docs/#dividends)

__parameters__

* __`range` (default: 1m)__ - Historical market data; range of data on dividends to return.

### `earnings()`

[IEX API - Earnings <i class="fa fa-external-link-square"></i>](https://iextrading.com/developer/docs/#earnings)

### `effective_spread()`

[IEX API - Effective Spread <i class="fa fa-external-link-square"></i>](https://iextrading.com/developer/docs/#effective-spread)

### `effective_spread_table()`

Returns a dataframe of [`effective_spread()`](#effective_spread)

### `financials()`


### `financials_table()`



