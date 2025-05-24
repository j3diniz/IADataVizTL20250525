import pandas as pd
import streamlit as st
import time

### Dataframe Creation ###
# Create a sample DataFrame with random city
@st.cache_data
def ReturnDf(path: str, separator: str = ',', encoder: str = 'utf-8') -> pd.DataFrame:
    return pd.read_csv(
        filepath_or_buffer = path,
        sep = separator,
        encoding = encoder,
        # index_col = 0
    )




# For Excel Files
# def ReturnDf(io):
#     df = pd.read_excel(
#     # Specify the path to the Excel file
#     io = io,
#     # Specify the engine to use for reading the Excel file
#     # This is necessary for reading .xlsx files
#     engine='openpyxl',
#     # Specify the sheet name to read from the Excel file
#     sheet_name = 'Worksheet',
#     # Specify the header row to use for the DataFrame
#     # header = 0,
#     # Specify the columns to read from the Excel file                                                                                                                                                                                                                                                                                                                           '
#     # In this case, columns A to J (0 to 9 in zero-based index)
#     usecols="A:Q",
#     # skip 5 rows
#     skiprows = 5,
#     # Specify the number of rows to read from the Excel file
#     nrows=50,
#     )
#     return df
