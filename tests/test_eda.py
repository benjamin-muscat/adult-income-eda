import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from eda import load_data, drop_missing_data, quantify_missing_data

def test_load_data_pass():
    df = load_data("adult.data", "adult.test")
    assert df.shape == (48842, 15)

def test_missing_data_detected_pass():
    df = load_data("adult.data", "adult.test")
    missing_df = quantify_missing_data(df)

    assert missing_df.loc["occupation", "missing_count"] == 2809
    assert missing_df.loc["workclass", "missing_count"] == 2799
    assert missing_df.loc["native_country", "missing_count"] == 857

def test_drop_missing_data_pass():
    df = load_data("adult.data", "adult.test")
    cleaned_df = drop_missing_data(df)

    assert cleaned_df.shape[0] == 45222
    assert cleaned_df.isnull().sum().sum() == 0

def test_fail_wrong_shape():
    df = load_data("adult.data", "adult.test")
    assert df.shape == (50000, 15)

def test_fail_no_missing_before_cleaning():
    df = load_data("adult.data", "adult.test")
    assert df.isnull().sum().sum() == 0