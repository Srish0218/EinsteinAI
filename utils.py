import streamlit as st

# Check login status
def check_login_status():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    return st.session_state.logged_in
