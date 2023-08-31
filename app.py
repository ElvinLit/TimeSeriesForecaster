import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

import yfinance as yf

import datetime as dt
import numpy as np
import pandas as pd
import seaborn as sns

from packages.methods import line_plot

st.set_page_config(
    page_title="Time Series Forecaster",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

show_pages(
    [
        Page("app.py", "Time Series Forecaster", "📈"),
        Page("about.py", "About", "❓")
    ]
)

st.header("Stock Time Series Forecaster")

col1, col2 = st.columns([1,1])

with col1:
    starting_date = st.date_input("Starting Date", value=dt.datetime(2023, 6, 1))
    ending_date = st.date_input("Ending Date", value=dt.datetime(2023, 6, 25))
    company = st.text_input('Company Ticker Symbol', value='AAPL')
    model = st.multiselect('Choose a model', ('ARIMA', 'GARCH'))
    graph_display = st.selectbox('Choose a graph to display', ('ARIMA', 'GARCH'))

stock = yf.Ticker(company)
stock_data = stock.history(start=starting_date, end=ending_date)

with col2:
    st.pyplot(line_plot(company, stock_data, 'Date', 'Close'))
