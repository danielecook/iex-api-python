from datetime import date

from tests import *
from tests.helpers import *

from iex import stock

def test_stock_book():
    aapl = stock("AAPL")
    assert aapl.book()['symbol'] == 'AAPL'

