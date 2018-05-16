import datetime
import re
from pytest import raises
from tests import *
from tests.helpers import *

from iex import stock


def test_stock_book():
    aapl = stock("AAPL")
    assert aapl.book()['quote']['symbol'] == 'AAPL'


def test_stock_chart():
    tsla = stock("TSLA")
    assert tsla.chart(range='20180514')[0]['date'] == '20180514'


def test_chart_table():
    msft = stock("MSFT")
    msft_chart = msft.chart_table()
    assert msft_chart.empty == False


def test_chart_range_error():
    msft = stock("MSFT")
    with pytest.raises(ValueError):
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


def test_datetime_format_as_datetime():
    fb = stock("FB", date_format="isoformat")
    fb.delayed_quote()
    assert type(fb.delayed_quote().get("processedTime")) == str


def test_dividends():
    ibm = stock("IBM")
    assert len(ibm.dividends()) > 0
    assert ibm.dividends_table().empty is False


def test_earnings():
    ibm = stock("IBM")
    assert type(ibm.earnings()) == dict


def news():
    ibm = stock("IBM")
    assert len(ibm.news(last=1)) == 1
    assert len(ibm.news()) == 10

def test_logo():
    ibm = stock("IBM")
    assert bool(re.match('http.*.png', ibm.logo().get("url")))


def test_quote():
    amzn = stock("amzn")

