# Market

<div class='code-def'>market(date_format, output_format)</div>

__Parameters__

* __`date_format` (default: timestamp)__ - Specifies how timestamps should be should be returned. Set to one of the following:
    * __`timestamp`__ - default; Does not alter IEX API output.
    * __`datetime`__ - Datetime object.
    * __`isoformat`__ - Converts to isoformat.
* __`output_format`__ - The format to output. Options:
    - __`dataframe` (default)__ - Return result as a pandas dataframe.
    - __`json`__ - Return raw result converted from JSON to a python data structure.

!!! abstract "market"
    Certain API calls return market-wide data. For example, it might return data on stock prices for all stocks or a list of stocks based on a particular metric (_e.g._ performance, gainers, losers).

## Market Methods: List items

[IEX API - List <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#list)

### `mostactive()`

__Example__

``` python
from iex import market
market.mostactive()
```

       avgTotalVolume calculationPrice  change  changePercent    close  \
    0          494020              sip  0.0500        0.00126  39.8000
    1       124752351              sip -0.0052       -0.15249   0.0341
    2        50816723             tops  0.4100        0.03293  12.4500
    3         8446078             tops  3.0100        0.10057  29.9300
    4        44161998             tops  2.2050        0.04083  54.0100
    5        64003399             tops  0.6900        0.01485  46.4800

### `gainers()`
### `losers()`
### `iexvolume()`
### `iexpercent()`

## Market Methods: Additional

### `threshold_securities()`

[IEX API - IEX Regulation SHO Threshold Securities <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list)

### `short_interest()`

[IEX API - IEX Threshold Securities <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#iex-short-interest-list)

### `news()`

[IEX API - News <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#news)

__Parameters__

* __`last` (default: 10)__ - Number of stories to return between 1 and 50.

### `ohlc()`

[IEX API - News <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#ohlc)

### `previous()`

[IEX API - News <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#previous)

__Example__

``` python
from iex import market
market.previous()
```
```
     symbol  change changePercent   close        date     high     low  \
0         A   -6.71        -9.695    62.5  2018-05-15     64.1    60.7
1        AA   -1.79        -3.421   50.54  2018-05-15    51.95    50.4
2      AABA    -0.3        -0.391   76.44  2018-05-15    76.46    75.4
3       AAC    0.02         0.176    11.4  2018-05-15    11.52   11.19
4      AADR    0.52         0.888   59.08  2018-05-15  59.1785   58.02
5       AAL    0.73         1.719   43.19  2018-05-15     43.4    41.6
```

### `market()`

[IEX API - News <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#markets)

Returns near real time traded volume on the markets.
