import datetime
import re
from pytest import raises
from tests import *
from tests.helpers import *

from iex import market

m = market()

def test_market_list():
    assert m.mostactive().empty == False
    m.gainers()
    m.losers()
    m.iexvolume()
    m.iexpercent()


def test_threshold_securities():
    m.threshold_securities()


def test_short_interest():
    m.short_interest()


def news():
    assert m.news(last=1).empty == False