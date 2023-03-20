# test_get_concat_columns.py

import pandas as pd
from extra_streamlit_tools.data import get_concat_columns


def test_single_column():
    df = pd.DataFrame({"col1": ["hello", "world"]})
    assert get_concat_columns(df, ["col1"], " ") == ["hello", "world"]


def test_multiple_columns():
    df = pd.DataFrame(
        {"col1": ["hello", "world"], "col2": ["python", "java"]}
    )
    assert get_concat_columns(df, ["col1", "col2"], " ") == [
        "hello python",
        "world java",
    ]


def test_empty_dataframe():
    df = pd.DataFrame({})
    assert get_concat_columns(df, [], " ") == []


def test_join_with_dot():
    df = pd.DataFrame(
        {"col1": ["hello", "world"], "col2": ["python", "java"]}
    )
    assert get_concat_columns(df, ["col1", "col2"], ".") == [
        "hello.python",
        "world.java",
    ]


def test_join_with_comma():
    df = pd.DataFrame(
        {"col1": ["hello", "world"], "col2": ["python", "java"]}
    )
    assert get_concat_columns(df, ["col1", "col2"], ",") == [
        "hello,python",
        "world,java",
    ]


def test_non_string_columns():
    df = pd.DataFrame(
        {"col1": [1, 2, 3], "col2": [4, 5, 6]}
    )
    assert get_concat_columns(df, ["col1", "col2"], " ") == [
        "1 4",
        "2 5",
        "3 6",
    ]

