import datetime
import re
from pytest import raises
from iex import Stock


def test_error():
    aapl = Stock("AAPL")
    with raises(Exception):
        aapl._get("not_a_url")


def test_Stock_book():
    aapl = Stock("AAPL")
    assert aapl.book()['quote']['symbol'] == 'AAPL'


def test_Stock_chart():
    tsla = Stock("TSLA")
    # Sometimes these are returned as empty arrays; so don't
    # do much testing for now. Appears to be IEX bug.
    tsla.chart(range='20180514')
    tsla.chart(range='1d', chartReset=True) # Returns nothing?
    tsla.chart(range='1d', chartReset=False)
    tsla.chart(range='1d', chartSimplify=True)
    tsla.chart(range='1m', chartInterval=10)



def test_chart_range_error():
    msft = Stock("MSFT")
    with raises(ValueError):
        msft.chart(range="not_a_real_range")


def test_company():
    fb = Stock("FB")
    assert fb.company().get("companyName") == "Facebook Inc."


def test_delayed_quote():
    fb = Stock("FB")
    fb.delayed_quote()
    assert type(fb.delayed_quote().get("delayedPrice")) == float

def test_datetime_format_as_datetime():
    fb = Stock("FB", date_format="datetime")
    fb.delayed_quote()
    assert type(fb.delayed_quote().get("processedTime")) == datetime.datetime


def test_datetime_format_as_isoformat():
    fb = Stock("FB", date_format="isoformat")
    assert type(fb.delayed_quote().get("processedTime")) == str


def test_earnings():
    ibm = Stock("IBM")
    assert type(ibm.earnings()) == dict


def test_tables():
    ibm = Stock("IBM")
    assert ibm.chart_table().empty == False
    assert ibm.dividends_table().empty == False
    assert ibm.effective_spread_table().empty == False
    assert ibm.financials_table().empty == False
    assert ibm.volume_by_venue_table().empty == False


def test_stats():
    ibm = Stock("IBM")
    assert ibm.stats().get("companyName") == "International Business Machines Corporation"


def test_news():
    ibm = Stock("IBM")
    assert len(ibm.news(last=1)) == 1


def test_logo():
    ibm = Stock("IBM")
    assert bool(re.match('http.*.png', ibm.logo().get("url")))


def test_quote():
    amzn = Stock("amzn")
    assert bool(amzn.quote())


def test_ohlc():
    ibm = Stock("IBM")
    assert bool(ibm.ohlc().get('open'))

