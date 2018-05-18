import datetime
import re
from pytest import raises
from iex import stock


def test_error():
    aapl = stock("AAPL")
    with raises(Exception):
        aapl._get("not_a_url")


def test_stock_book():
    aapl = stock("AAPL")
    assert aapl.book()['quote']['symbol'] == 'AAPL'


def test_stock_chart():
    tsla = stock("TSLA")
    # Sometimes these are returned as empty arrays; so don't 
    # do much testing for now. Appears to be IEX bug.
    tsla.chart(range='20180514')
    tsla.chart(range='1d', chartReset=True) # Returns nothing?
    tsla.chart(range='1d', chartReset=False)
    tsla.chart(range='1d', chartSimplify=True)
    tsla.chart(range='1m', chartInterval=10)



def test_chart_range_error():
    msft = stock("MSFT")
    with raises(ValueError):
        msft.chart(range="not_a_real_range")


def test_company():
    fb = stock("FB")
    assert fb.company().get("companyName") == "Facebook Inc."


def test_delayed_quote():
    fb = stock("FB")
    fb.delayed_quote()
    assert type(fb.delayed_quote().get("delayedPrice")) == float

def test_datetime_format_as_datetime():
    fb = stock("FB", date_format="datetime")
    fb.delayed_quote()
    assert type(fb.delayed_quote().get("processedTime")) == datetime.datetime


def test_datetime_format_as_isoformat():
    fb = stock("FB", date_format="isoformat")
    assert type(fb.delayed_quote().get("processedTime")) == str


def test_earnings():
    ibm = stock("IBM")
    assert type(ibm.earnings()) == dict


def test_tables():
    ibm = stock("IBM")
    assert ibm.chart_table().empty == False
    assert ibm.dividends_table().empty == False
    assert ibm.effective_spread_table().empty == False
    assert ibm.financials_table().empty == False
    assert ibm.volume_by_venue_table().empty == False


def test_stats():
    ibm = stock("IBM")
    assert ibm.stats().get("companyName") == "International Business Machines Corporation"


def test_news():
    ibm = stock("IBM")
    assert len(ibm.news(last=1)) == 1
    assert len(ibm.news()) == 10


def test_logo():
    ibm = stock("IBM")
    assert bool(re.match('http.*.png', ibm.logo().get("url")))


def test_quote():
    amzn = stock("amzn")
    assert bool(amzn.quote())


def test_ohlc():
    ibm = stock("IBM")
    assert bool(ibm.ohlc().get('open'))

