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
