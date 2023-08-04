import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

st.set_page_config(
    page_title="About",
    page_icon="❓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.header("About")
