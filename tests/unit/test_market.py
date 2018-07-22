import datetime
import re
from pytest import raises
from tests import *

from iex import market

def test_market_list():
    market.mostactive()
    market.gainers()
    market.losers()
    market.iexvolume()
    market.iexpercent()


def test_threshold_securities():
    market.threshold_securities()


def test_short_interest():
    market.short_interest()


def news():
    assert m.news(last=1).empty == False


def ohlc():
    pass
