import streamlit as st

def show():
    with st.sidebar:
        st.title("Navigation")
        page = st.radio("Go to", ["Home", "Data Analysis", "Settings"])