import streamlit as st
from auth import login, signup
from main_app import app

# Initialize session state for login/signup
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

# Main logic to show login or signup forms
if not st.session_state.logged_in:
    if st.session_state.show_signup:
        signup()  # Show signup form
    else:
        login()  # Show login form
else:
    # Ensure loggedin_username exists before calling the app
    if "loggedin_username" in st.session_state:
        app()  # Main app if logged in
    else:
        st.error("Username not found in session state!")
