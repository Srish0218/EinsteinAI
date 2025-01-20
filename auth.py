import streamlit as st
import mysql.connector
from mysql.connector import Error
import pymysql
from main_app import app

# Use pymysql as MySQLdb
pymysql.install_as_MySQLdb()

import MySQLdb

# Retrieve secrets from the secrets.toml
DB_HOST = st.secrets["DB_HOST"]
DB_USER = st.secrets["DB_USER"]
DB_PASSWORD = st.secrets["DB_PASSWORD"]
DB_NAME = st.secrets["DB_NAME"]


# Function to check if the username/email already exists in the database
def user_exists(username: str, email: str) -> bool:
    try:
        conn = MySQLdb.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        result = cursor.fetchone()
        conn.close()
        return result is not None
    except Error as e:
        st.error(f"Database error: {e}")
        return False


# Function to insert a new user into the database without hashing the password
def register_user(username: str, email: str, password: str):
    try:
        conn = MySQLdb.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password)  # Store the plain text password
        )
        conn.commit()
        conn.close()
        st.success("User registered successfully!")
    except Error as e:
        st.error(f"Database error: {e}")


# Function to authenticate user login without hashing the password
def authenticate_user(username: str, password: str) -> bool:
    try:
        conn = MySQLdb.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        conn.close()

        # Compare the password directly (plain text comparison)
        if result and result[0] == password:
            # Store username in session state
            st.session_state.loggedin_username = username
            return True
        return False
    except Error as e:
        st.error(f"Database error: {e}")
        return False


# Login page logic
def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.logged_in = True
            loggedin_username = username
            # app(loggedin_username)
            st.success("Logged in successfully!")

        else:
            st.error("Invalid username or password.")


# Signup page logic
def signup():
    st.subheader("Signup")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Signup"):
        if password != confirm_password:
            st.error("Passwords do not match!")
        elif user_exists(username, email):
            st.error("Username or email already exists.")
        else:
            register_user(username, email, password)  # Store plain text password
