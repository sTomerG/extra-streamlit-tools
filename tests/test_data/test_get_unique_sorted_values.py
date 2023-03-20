# test_get_unique_sorted_values.py

import pandas as pd
from extra_streamlit_tools.data import get_unique_sorted_values


def test_single_value_column():
    df = pd.DataFrame({"col1": ["hello"]})
    assert get_unique_sorted_values(df, "col1") == ["hello"]


def test_multiple_value_column():
    df = pd.DataFrame({"col1": ["hello", "world", "hello", "everyone"]})
    assert get_unique_sorted_values(df, "col1") == [
        "everyone",
        "hello",
        "world",
    ]


def test_numeric_column():
    df = pd.DataFrame({"col1": [1, 3, 2, 4, 2]})
    assert get_unique_sorted_values(df, "col1") == ["1", "2", "3", "4"]


def test_convert_to_int():
    df = pd.DataFrame({"col1": ["1", "3", "2", "4", "2"]})
    assert get_unique_sorted_values(df, "col1", int) == [1, 2, 3, 4]


def test_convert_to_float():
    df = pd.DataFrame({"col1": ["1.0", "3.5", "2.3", "4", "2.3"]})
    assert get_unique_sorted_values(df, "col1", float) == [1.0, 2.3, 3.5, 4.0]


def test_empty_dataframe():
    df = pd.DataFrame({"col1": []})
    assert get_unique_sorted_values(df, "col1") == []
