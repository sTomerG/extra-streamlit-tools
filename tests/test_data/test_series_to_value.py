import pandas as pd
import numpy as np
import pytest
from extra_streamlit_tools.data import series_to_value


def test_single_value():
    test_series = pd.Series([42])
    assert series_to_value(test_series) == 42


def test_single_string_value():
    test_series = pd.Series(["Hello"])
    assert series_to_value(test_series) == "Hello"


def test_hashtag_removal():
    test_series = pd.Series(["#Hello"])
    assert series_to_value(test_series) == "Hello"


def test_single_float_value():
    test_series = pd.Series([42.0])
    assert series_to_value(test_series) == 42


def test_single_nan_value():
    test_series = pd.Series([np.nan])
    assert series_to_value(test_series) == ""


def test_single_none_value():
    test_series = pd.Series([None])
    assert series_to_value(test_series) == ""


def test_more_than_one_row():
    test_series = pd.Series([1, 2])
    with pytest.raises(ValueError) as exc_info:
        series_to_value(test_series)
    assert "Found more than one row" in str(exc_info.value)
