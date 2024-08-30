import streamlit as st
from config import uptdate_settings

def show():
    st.title("Settings")

    theme = st.selectbox("Select a theme", ["Light", "Dark"])
    data_source = st.text_input("Datas source", "https://example.com/data.csv")

    if st.button("Save"):
        uptdate_settings(theme, data_source)
        st.success("Settings saved successfully!")