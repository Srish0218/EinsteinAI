import streamlit as st
from auth import login, signup
from main_app import app

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

# Main logic to show login or signup forms
try:
    if not st.session_state.logged_in:
        # Display button to switch between login and signup forms
        if st.session_state.show_signup:
            # If we are showing the signup form, show the login button
            # if st.button("Switch to Login"):
            #     st.session_state.show_signup = False
            signup()  # Show signup form
        else:
            # If we are showing the login form, show the signup button
            # if st.button("Switch to Sign Up"):
            #     st.session_state.show_signup = True
            login()  # Show login form
    else:
        # Ensure loggedin_username exists before calling the app
        if "loggedin_username" in st.session_state:
            app()  # Main app if logged in
        else:
            st.error("Username not found in session state!")
except Exception as e:
    st.error(f"An error occurred: {e}")
