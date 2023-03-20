# test_get_values_based_on_other_value.py

import pandas as pd
from extra_streamlit_tools.data import get_values_based_on_other_value
import pytest


def test_single_match():
    df = pd.DataFrame(
        {"col1": ["hello", "world"], "col2": ["value1", "value2"]}
    )
    assert get_values_based_on_other_value(df, "col1", "hello", "col2") == [
        "value1"
    ]


def test_multiple_matches():
    df = pd.DataFrame(
        {
            "col1": ["hello", "world", "hello", "everyone"],
            "col2": ["value1", "value2", "value1", "value3"],
        }
    )
    assert get_values_based_on_other_value(df, "col1", "hello", "col2") == [
        "value1"
    ]


def test_empty_dataframe():
    df = pd.DataFrame({})
    with pytest.raises(KeyError):
        get_values_based_on_other_value(df, "col1", "hello", "col2")


def test_no_match():
    df = pd.DataFrame(
        {"col1": ["hello", "world"], "col2": ["value1", "value2"]}
    )
    assert (
        get_values_based_on_other_value(df, "col1", "everyone", "col2") == []
    )


def test_numeric_values():
    df = pd.DataFrame(
        {
            "col1": [1, 2, 3, 4],
            "col2": ["value1", "value2", "value1", "value3"],
        }
    )
    assert get_values_based_on_other_value(df, "col1", 2, "col2") == ["value2"]


def test_duplicate_values():
    df = pd.DataFrame(
        {
            "col1": ["hello", "world", "hello", "world"],
            "col2": ["value1", "value2", "value1", "value3"],
        }
    )
    assert get_values_based_on_other_value(df, "col1", "hello", "col2") == [
        "value1"
    ]
