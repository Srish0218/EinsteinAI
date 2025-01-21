import streamlit as st

def logout():
    st.session_state.logged_in = False
    st.session_state.loggedin_username = None
    st.success("You have logged out successfully!")
