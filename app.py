import streamlit as st
import google.generativeai as genai

# Configure the page (tab name and icon)
st.set_page_config(
    page_title="EinsteinAI - Physics Assistant",
    page_icon="🔬",
    layout="wide",
)

# Configure API key
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
genai_model = genai.GenerativeModel('gemini-1.5-flash')

# Fixed Title using a container
st.markdown(
    """
    <style>
    .fixed-title {
        position: fixed;
        text-align: center;
        background-color: black;
        top: 20px;
        left: 0;
        width: 100%;
        color: white;
        padding: 15px 10px;
        z-index: 1000;
    }
    .main-content {
        margin-top: 80px;  /* Added space for the fixed title */
    }
    .fixed-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #1a1a1a;
        color: white;
        text-align: center;
        padding: 1px;
        z-index: 1000;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="fixed-title"><h1>EinsteinAI - Your Physics Assistant 🔬</h1></div>', unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant",
         "content": "Hi! I'm EinsteinAI, your physics assistant. Ask me anything related to physics!"}
    ]

# Display chat history
st.divider()
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# User input handling
if user_input := st.chat_input("Type your physics question here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing your question..."):
            try:
                linkedin_link = "https://www.linkedin.com/in/srishti-jaitly-6852b822b/"
                prompt = f"""
                You are EinsteinAI, a physics assistant created by Srishti Jaitly.
                Your purpose is to answer questions related to physics only. 
                If the question is not related to physics, respond:
                "I am EinsteinAI, a physics assistant created by [Srishti Jaitly]({linkedin_link}). 
                I answer only physics-related questions. Please ask me something related to physics."

                Question: {user_input}
                """
                response = genai_model.generate_content(prompt)
                assistant_response = response.text.strip()

                # Append response to chat history
                st.markdown(assistant_response)
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            except Exception as e:
                error_message = "Sorry, I couldn't process your question. Please try again later."
                st.error(f"{error_message} (Error: {e})")
                st.session_state.messages.append({"role": "assistant", "content": error_message})

# Fixed footer with contact info or additional links
st.markdown(
    """
    <div class="fixed-footer">
<p>&copy; 2025 EinsteinAI. All rights reserved. Created by <a href="https://www.linkedin.com/in/srishti-jaitly-6852b822b/" class="footer-link" target="_blank">Srishti Jaitly</a> Explore more at <a href="https://github.com/Srish0218" class="footer-link" target="_blank">GitHub</a> | <a href="mailto:srishtijaitly2002@gmail.com" class="footer-link" target="_blank">Send Email</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)