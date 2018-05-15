from pytest import raises
from tests import *
from tests.helpers import *

from iex import stock


def test_stock_book():
    aapl = stock("AAPL")
    assert aapl.book()['quote']['symbol'] == 'AAPL'


def test_stock_chart():
    tsla = stock("TSLA")
    tsla.chart(range='1d')
    assert tsla.chart(range='20180514')[0]['date'] == '20180514'


def test_chart_table():
    msft = stock("MSFT")
    msft_chart = msft.chart_table()
    assert msft_chart.empty == False


def test_chart_range():
    msft = stock("MSFT")
    with pytest.raises(ValueError):
        msft.chart(range="not_a_real_range")
