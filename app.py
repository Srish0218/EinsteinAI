import streamlit as st
import google.generativeai as genai

# Configure the page (tab name and icon)
st.set_page_config(
    page_title="EinsteinAI - Physics Assistant",  # Tab name
    page_icon="🔬",  # Tab icon (you can use emojis or upload your own favicon)
)

# Get API key from Streamlit secrets, Configure the Gemini model with your API key
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
genai_model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant",
                                  "content": "Hi! I'm EinsteinAI, your physics assistant. Ask me anything related to physics!"}]

# Streamlit UI
st.title("EinsteinAI")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box for the user to type their question
if user_input := st.chat_input("Type your physics question here..."):
    # Append the user's message to the session
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate a response from the Gemini model
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Formulate the prompt
                linkedin_link = "https://www.linkedin.com/in/srishti-jaitly-6852b822b/"
                prompt = f"""
                You are EinsteinAI, a physics assistant created by Srishti Jaitly. 
                Your purpose is to answer questions related to physics only. 
                If the question is not related to physics, respond with:
                "I am EinsteinAI, a physics assistant created by Srishti Jaitly {linkedin_link}. 
                I am made to answer questions related to physics only. Please ask me something related to physics."

                Question: {user_input}
                """

                # Get response from the model
                response = genai_model.generate_content(prompt)
                assistant_response = response.text.strip()

                # Display and append the assistant's message
                st.markdown(assistant_response)
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            except Exception as e:
                error_message = "Sorry, I couldn't process your question. Please try again later."
                st.markdown(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})
