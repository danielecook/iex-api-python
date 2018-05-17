# IEX-API-Python

### Summary 

The `iex-api-python` module is a wrapper for the [IEX API](https://iextrading.com/developer/docs/#getting-started), and is designed to closely map to the organization of the original API while adding functionality. A few examples of the additional functionality are:

* Many queries are returned as [Pandas Dataframes](https://pandas.pydata.org/).
* Built-in support for websockets connections.
* Option to format timestamps as datetime objects or ISO-dates.

Before using __IEX-API-Python__ and the __IEX API__ you should read the [API terms of use](https://iextrading.com/api-terms/) and review the [documentation](https://iextrading.com/developer/docs/).

### Organization

The `IEX-API-Python` module is designed to map closely to the API from IEX. For many of the API calls, the resulting dataset is better represented in a tabular format. For these calls, data are returned as a [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html).
