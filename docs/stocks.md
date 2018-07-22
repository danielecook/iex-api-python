# Stock

<div class='code-def'>stock(symbol, date_format)</div>

__Parameters__

* __`symbol`__ - A stock symbol
* __`date_format` (default: timestamp)__ - Specifies how timestamps should be should be returned. Set to one of the following:
    * __`timestamp`__ - default; Does not alter IEX API output.
    * __`datetime`__ - Datetime object.
    * __`isoformat`__ - Converts to isoformat.

!!! note "The stock class"

    The `stock` class is useful for returning information for a specific stock, and is designed to map closely to the organization of the __[Stocks](https://iextrading.com/developer/docs/#stocks)__ section of the IEX API.

    One major difference between the stock class and the Stocks section of the IEX API is that the `stock` object is not designed to handle batch requests (multiple stocks) or market data. Batch requests are requests for data on multiple stocks at the same time. Market requests return data for all stocks or a set of stocks based on the request (_e.g._ gainers and losers). For batch requests, you should use the [`batch`](batch), and market requests should use the [`market`](market) object.

    Also note that the `stock` object most often returns data as a python dictionary or list - closely mimicking the returned JSON of the IEX API. However, in some cases there are additional methods (suffixed with `_table`) that will return a Pandas dataframe for convenience.


## Creating a new `stock` object

Provide a stock symbol to create a stock object. Stock symbols are case-insensitive.

``` python
from iex import stock
tsla = stock("tsla")
```

----

## Stock Methods

Below are the methods that can be invoked with a `stock` object. Beneath the listed method you will find a link that will take you to the corresponding IEX API documentation.

### `book()`

[IEX API - Book <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#book)

``` python
from iex import stock
goog = stock("goog")
goog.book()
```

    # Output
    {
     'quote': {...},
     'bids': [...],
     'asks': [...],
     'trades': [...],
     'systemEvent': {...}
    }

### `chart()`

[IEX API - Chart <i class="material-icons md-16">open_in_new</i>](https://iextrading.com/developer/docs/#chart)

__Parameters__

* __`range` (default: 1m)__ - Historical adjusted market-wide data or IEX-only data. See the [IEX API reference](https://iextrading.com/developer/docs/#chart) for further details.
    - `5y` `2y` `1y` `ytd` `6m` `3m` `1m` `YYYYMMDD (date)` `dynamic`
* __`chartReset` (bool; default: `None`)__ - 1d chart will reset at midnight instead of the default behavior of 9:30am ET.
* __`chartSimplify` (bool; default: `None`)__ -  If `True`, runs a polyline simplification using the Douglas-Peucker algorithm. This is useful if plotting sparkline charts.
* __`chartInterval` (bool: default: `None`)__ -  If passed, chart data will return every Nth element.

### `chart_table()`

Returns a pandas dataframe from chart data. If `range=dynamic`, a `range` column is appended to the returned dataframe indicating whether the data is for `1d` or `1m`. See the See the [IEX API documentation](https://iextrading.com/developer/docs/#chart) for further details.

__Parameters__

The same parameters are available as with [`chart()`](#chart).

__Example__

``` python
from iex import stock
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

[IEX API - Company <i class="material-icons md-16">open_in_new</i>](https://iextrading.com/developer/docs/#company)

### `delayed_quote()`

[IEX API - Delayed Quote <i class="material-icons md-16">open_in_new</i>](https://iextrading.com/developer/docs/#delayed-quote)

### `dividends()`

[IEX API - Dividends <i class="material-icons md-16">open_in_new</i>](https://iextrading.com/developer/docs/#dividends)

__parameters__

* __`range` (default: 1m)__ - Historical market data; range of data on dividends to return.

### `dividends_table()`

Returns a dataframe of [`dividend()`](#dividends())

__parameters__

* __`range` (default: 1m)__ - Historical market data; range of data on dividends to return.

__Example__

``` python
from iex import stock
F = stock("F")
f.dividends_table()
```

```
    # Output
    change  changeOverTime  changePercent    close        date   \
0   0.098676        0.000000          0.887  11.2293  2018-04-16 
1   0.000000        0.000000          0.000  11.2293  2018-04-17 
2  -0.049338       -0.004390         -0.439  11.1800  2018-04-18 
3  -0.220002       -0.023982         -1.968  10.9600  2018-04-19 
4  -0.140000       -0.036449         -1.277  10.8200  2018-04-20 
...
```

### `earnings()`

[IEX API - Earnings <i class="material-icons md-16">open_in_new</i>](https://iextrading.com/developer/docs/#earnings)

### `effective_spread()`

[IEX API - Effective Spread <i class="material-icons md-16">open_in_new</i>](https://iextrading.com/developer/docs/#effective-spread)

### `effective_spread_table()`

Returns a dataframe of [`effective_spread()`](#effective_spread)

### `financials()`


### `financials_table()`

### `ohlc()`

[IEX API - OHLC <i class="material-icons md-16">open_in_new</i>](https://iextrading.com/developer/docs/#ohlc)

!!! info
    If you are trying to return the official open/close for all stocks use [`market.ohlc()`](market#ohlc()).


### `price()`

### `peers()`

Returns a list of peer (competitor/related) companies. By default, the returned list is a set of `stock` objects. You can return a list of companies as strings by setting `as_string=True`.

__Parameters__

* __`as_string` (Default: `False`)__ - If set to `True`, return the list of peers as strings rather than `stock` objects.

__Example__

``` python
from iex import stock
tsla = stock("tsla")
tsla.peers()
```

    # Output
    [<stock:HMC>, <stock:TM>, <stock:F>, <stock:GM>]

### `previous()`

[IEX API - Previous <i class="material-icons md-16">open_in_new</i>](https://iextrading.com/developer/docs/#previous)

Returns the previous day adjusted stock price. The IEX API can also return the previous day prices for the entire market. For this query, use [`market.previous()`](market#previous()).

!!! info
    If you are trying to return the previous days market data, use [`market.previous()`](market#previous()).


### `price()`

[IEX API - Price <i class="material-icons md-16">open_in_new</i>](https://iextrading.com/developer/docs/#price)

Returns the stock price.

__Example__

``` python
tsla = stock("TSLA")
tsla.price()
```

    284.18

### `quote()`

### `stats()`



