import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file_path = "../data/annotated_data.csv") -> pd.DataFrame:
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    return pd.read_csv(file_path)