import datetime
import re
from pytest import raises
from tests import *

from iex import iex_stats, IexStats

def test_intraday():
    assert iex_stats.intraday().empty == False

def test_recent():
    assert iex_stats.recent().empty == False

def test_records():
    assert iex_stats.records().empty == False

def test_historical_summary():
    assert iex_stats.historical_summary().empty == False
    assert iex_stats.historical_summary(date='201704').empty == False
    with raises(ValueError):
        iex_stats.historical_summary(date="not_a_date")

def test_historical_daily():
    assert iex_stats.historical_daily().empty == False
    assert iex_stats.historical_daily(date='201704').empty == False
    assert len(iex_stats.historical_daily(last=20).index) == 20
    # Test last out of range.
    with raises(ValueError):
        iex_stats.historical_daily(date="201704", last=0)
    with raises(ValueError):
        iex_stats.historical_daily(last=0)
    with raises(ValueError):
        iex_stats.historical_daily(date="not_a_date")


def test_error():
    with raises(Exception):
        iex_stats._get("not_a_url")

def test_print():
    assert IexStats().__repr__() == '<iex_stats>'

