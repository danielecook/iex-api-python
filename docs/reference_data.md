# Reference

<div class='code-def'>ReferenceData(output_format)</div>

__Parameters__

* __`output_format`__ - The format to output. Options:
    - __`dataframe` (default)__ - Return result as a pandas dataframe.
    - __`json`__ - Return raw result converted from JSON to a python data structure.

!!! note "The `reference` instance"

    The `reference` object is designed to map closely to the [`Reference Data`](https://iextrading.com/developer/docs/#reference-data) section of the IEX API.

    You can import either `ReferenceData` (the class) or `reference` from iex. The `reference` import is an instance of `ReferenceData` that can be used without having to instantiate a new object. 

## Importing the `reference` object

``` python
from iex import reference
```

#### Setting the output format using the instance

To update the output format, set the `output_format` attribute:

```python
reference.output_format = 'json'
```

----

## Reference Methods

Below are the methods that can be invoked with a `reference` object. Beneath the listed method you will find a link that will take you to the corresponding IEX API documentation.

### `symbols()`

[IEX API - symbols](https://iextrading.com/developer/docs/#symbols)

``` python
from iex import reference
reference.symbols()
```

    # Output

         symbol        date  iexId  isEnabled  \
    0         A  2018-05-15      2       True   
    1        AA  2018-05-15  12042       True   
    2      AABA  2018-05-15   7653       True   
    ...

### `iex_corporate_actions()`

[IEX API - IEX Corporate Actions](https://iextrading.com/developer/docs/#iex-corporate-actions)

__Parameters__

* __`date`__ - Date specified as `YYYYMMDD` or a datetime object.

### `iex_dividends()`

[IEX API - IEX Dividends](https://iextrading.com/developer/docs/#iex-dividends)

__Parameters__

* __`date`__ - Date specified as `YYYYMMDD` or a datetime object.

### `iex_next_day_ex_date()`

[IEX API - IEX Next Day Ex Date](https://iextrading.com/developer/docs/#iex-next-day-ex-date)

__Parameters__

* __`date`__ - Date specified as `YYYYMMDD` or a datetime object.

### `iex_listed_symbol_directory()`

[IEX API - IEX Listed Symbol Directory](https://iextrading.com/developer/docs/#iex-listed-symbol-directory)

__Parameters__

* __`date`__ - Date specified as `YYYYMMDD` or a datetime object.
