import datetime
import re
from pytest import raises
from tests import *
from tests.helpers import *

from iex import iex_stats

stats = iex_stats()

def test_intraday():
    assert stats.intraday().empty == False

def test_recent():
    assert stats.recent().empty == False

def test_records():
    assert stats.records().empty == False

def test_historical_summary():
    assert stats.historical_summary().empty == False
    assert stats.historical_summary(date='201705').empty == False

def test_historical_daily():
    assert stats.historical_daily().empty == False
    assert stats.historical_daily(date='201704').empty == False
    assert len(stats.historical_daily(last=20).index) == 20
    # Test last out of range.
    with raises(ValueError):
        stats.historical_daily(last=0)
    with raises(ValueError):
        stats.historical(date="not_a_date")
