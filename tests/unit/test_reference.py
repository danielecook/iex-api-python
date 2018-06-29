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

from iex import reference

def test_json_return():
    symbols_json = reference(output_format='json').symbols()
    assert type(symbols_json) == list


def test_ref_symbols():
    assert reference.symbols().empty is False


def test_iex_corporate_actions():
    reference.iex_corporate_actions()


def test_iex_dividends():
    reference.iex_dividends()


def test_iex_next_day_ex_date():
    reference.iex_next_day_ex_date()


def test_iex_listed_symbol_directory():
    reference.iex_listed_symbol_directory()


def test_error():
    with raises(Exception):
        reference._get("not_a_url")
