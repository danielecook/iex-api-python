#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Daniel E. Cook


Testing the IEX items can be difficult because
they only show data for part of the day. Returning an empty result
is O.K.

"""
import datetime
import re
from pytest import raises
from tests import *
from tests.helpers import *

from iex import reference

ref = reference()


def test_json_return():
    symbols_json = reference(output_format='json').symbols()
    assert type(symbols_json) == list


def test_ref_symbols():
    assert ref.symbols().empty is False


def test_iex_corporate_actions():
    ref.iex_corporate_actions()


def test_iex_dividends():
    ref.iex_dividends()


def test_iex_next_day_ex_date():
    ref.iex_next_day_ex_date()


def test_iex_listed_symbol_directory():
    ref.iex_listed_symbol_directory()


def test_error():
    with raises(Exception):
        ref._get("not_a_url")
