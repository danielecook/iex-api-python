# IEX Stats

<div class='code-def'>iex_stats(date_format, output_format)</div>

__Parameters__

* __`date_format` (default: timestamp)__ - Specifies how timestamps should be should be returned. Set to one of the following:
    * __`timestamp`__ - default; Does not alter IEX API output.
    * __`datetime`__ - Datetime object.
    * __`isoformat`__ - Converts to isoformat.
* __`output_format`__ - The format to output. Options:
    - __`dataframe` (default)__ - Return result as a pandas dataframe.
    - __`json`__ - Return raw result converted from JSON to a python data structure.

!!! note "The iex_stats class"

    The `iex_stats` class creates an object that can be used to fetch IEX aggregate data.

## Creating a new `iex_stats` object

Provide a stock symbol to create a stock object. Stock symbols are case-insensitive.

``` python
from iex import iex_stats
stats = iex_stats()
```

----

## IEX Stats Methods

### `intraday()`

[IEX API - Intraday <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#intraday)

``` python
from iex import iex_stats
iex_stats(date_format='datetime').intraday()
```
```
                                   lastUpdated         value
marketShare   2018-05-17 18:32:07.535000+00:00  2.661000e-02
notional      2018-05-17 18:32:07.472000+00:00  5.214433e+09
routedVolume  2018-05-17 18:32:06.999000+00:00  2.245174e+07
symbolsTraded 2018-05-17 18:32:07.472000+00:00  5.299000e+03
volume        2018-05-17 18:32:07.472000+00:00  1.141716e+08
```

### `recent()`

[IEX API - Recent <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#recent)

### `records()`

[IEX API - Records <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#records)

### `historical_summary()`

[IEX API - Historical Summary <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#historicaly-summary)


### `historical_daily()`

[IEX API - Historical Daily <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#historicaly-daily)


