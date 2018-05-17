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
    with raises(ValueError):
        stats.historical_summary(date="not_a_date", last=0)

def test_historical_daily():
    assert stats.historical_daily().empty == False
    assert stats.historical_daily(date='201704').empty == False
    assert len(stats.historical_daily(last=20).index) == 20
    # Test last out of range.
    with raises(ValueError):
        stats.historical_daily(date="201704", last=0)
    with raises(ValueError):
        stats.historical_daily(last=0)
    with raises(ValueError):
        stats.historical_daily(date="not_a_date")


def test_error():
    with raises(Exception):
        stats._get("not_a_url")

def test_print():
    assert iex_stats().__repr__() == '<iex_stats>'

