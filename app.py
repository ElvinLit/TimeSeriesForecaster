import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title
import yfinance as yf

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

st.header("Time Series Forecaster")
