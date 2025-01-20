import streamlit as st
from auth import login, signup
from main_app import app
import auth

# Configure the page (tab name and icon)
# st.set_page_config(
#     page_title="EinsteinAI - Physics Assistant",
#     page_icon="🔬",
#     layout="wide",
# )
# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Show Login or App based on login status
if not st.session_state.logged_in:
    page_selection = st.radio("Select Page", ("Login", "Signup"))

    if page_selection == "Login":
        login()
    elif page_selection == "Signup":
        signup()
else:
    # Ensure loggedin_username exists before calling the app
    if "loggedin_username" in st.session_state:
        app(st.session_state.loggedin_username)
    else:
        st.error("Username not found in session state!")

