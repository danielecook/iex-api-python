# Reference

<div class='code-def'>reference(output_format)</div>

__Parameters__

* __`output_format`__ - The format to output. Options:
    - __`dataframe` (default)__ - Return result as a pandas dataframe.
    - __`dict`__ - Return result as python dictionaries.


!!! note "The reference class"

    The `reference` class is designed to map closely to the [`Reference Data`](https://iextrading.com/developer/docs/#reference-data) section of the IEX API.

## Creating a new `reference` object

``` python
from iex import reference
ref = reference()
```

----


## Reference Methods

Below are the methods that can be invoked with a `reference` object. Beneath the listed method you will find a link that will take you to the corresponding IEX API documentation.

### `symbols()`

[IEX API - Book <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#symbols)

``` python
from iex import reference
ref = reference()
ref.symbols()
```

    # Output

         symbol        date  iexId  isEnabled  \
    0         A  2018-05-15      2       True   
    1        AA  2018-05-15  12042       True   
    2      AABA  2018-05-15   7653       True   
    ...

### `iex_corporate_actions()`

[IEX API - IEX Corporate Actions <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#iex-corporate-actions)

__Parameters__

* __`date`__ - Date specified as `YYYYMMDD` or a datetime object.

### `iex_dividends()`

[IEX API - IEX Dividends <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#iex-dividends)

__Parameters__

* __`date`__ - Date specified as `YYYYMMDD` or a datetime object.

### `iex_next_day_ex_date()`

[IEX API - IEX Next Day Ex Date <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#iex-next-day-ex-date)

__Parameters__

* __`date`__ - Date specified as `YYYYMMDD` or a datetime object.

### `iex_listed_symbol_directory()`

[IEX API - IEX Listed Symbol Directory <i class="material-icons md-16">
open_in_new
</i>](https://iextrading.com/developer/docs/#iex-listed-symbol-directory)

__Parameters__

* __`date`__ - Date specified as `YYYYMMDD` or a datetime object.
