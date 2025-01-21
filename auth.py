import streamlit as st
import pymysql
from pymysql.err import MySQLError

# Configure the page (tab name and icon)
st.set_page_config(
    page_title="EinsteinAI - Physics Assistant",
    page_icon="🔬",
    layout="wide",
)

# Retrieve secrets from the secrets.toml
DB_HOST = st.secrets["DB_HOST"]
DB_USER = st.secrets["DB_USER"]
DB_PASSWORD = st.secrets["DB_PASSWORD"]
DB_NAME = st.secrets["DB_NAME"]

# Function to check if the username/email already exists in the database
def user_exists(username: str, email: str) -> bool:
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME,port=3306)
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
            result = cursor.fetchone()
        conn.close()
        return result is not None
    except MySQLError as e:
        st.error(f"Database error: {e}")
        return False

# Function to insert a new user into the database
def register_user(username: str, email: str, password: str):
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME,port=3306)
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password)  # Store plain text password for now
            )
            conn.commit()
        conn.close()
        st.success("User registered successfully!")
    except MySQLError as e:
        st.error(f"Database error: {e}")

# Function to authenticate user login
def authenticate_user(username: str, password: str) -> bool:
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=3306)
        with conn.cursor() as cursor:
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
        conn.close()

        if result and result[0] == password:  # Plain text comparison
            st.session_state.loggedin_username = username
            return True
        return False
    except MySQLError as e:
        st.error(f"Database error: {e}")
        return False

# Login page logic
def login():
    st.subheader("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_button"):
        if authenticate_user(username, password):
            st.session_state.logged_in = True
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password.")

    st.markdown("---")
    st.markdown("Don't have an account?")
    if st.button("Switch to Signup", key="switch_to_signup"):
        st.session_state.show_signup = True

# Signup page logic
def signup():
    st.subheader("Signup")
    username = st.text_input("Username", key="signup_username")
    email = st.text_input("Email", key="signup_email")
    password = st.text_input("Password", type="password", key="signup_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password")

    if st.button("Signup", key="signup_button"):
        if password != confirm_password:
            st.error("Passwords do not match!")
        elif user_exists(username, email):
            st.error("Username or email already exists.")
        else:
            register_user(username, email, password)

    st.markdown("---")
    st.markdown("Already have an account?")
    if st.button("Back to Login", key="back_to_login_button"):
        st.session_state.show_signup = False
