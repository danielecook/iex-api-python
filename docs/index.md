# IEX-API-Python

Welcome to the documentation for `iex-api-python`. This python module is a wrapper for the [IEX API](https://iextrading.com/developer/docs/#getting-started), and is designed to closely map to the organization of the original API. The goal is to avoid recreating the excellent API documentation that already exists, and only to provide additional details where new functionality has been added. A few examples of the additional functionality are:

* Batch queries are returned as Pandas Dataframes.
* Built-in support for websockets.

!! Important
    One notable difference between the Python module and the API is the use of the `format` parameter. For many of the API calls it is possible to return a CSV. However, the `iex-api-python` module will in these cases generate a Pandas DataFrame. The DataFrame can be exported as a CSV if desired. Alternatively, if you prefer to retrieve the json-to-python-dictionary object you can set an argument when creating a query object: `output_format = 'json'`.
