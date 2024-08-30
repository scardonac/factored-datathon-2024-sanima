import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

home = st.Page(
    "pages\\home.py", title="Home", icon=":material/home:", default=True
)

data_analysis = st.Page(
    "pages\\data_analysis.py", title="Data analysis", icon=":material/dashboard:"
)

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [home, data_analysis],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()