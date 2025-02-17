﻿# 🌌 EinsteinAI - Your Physics Assistant

Welcome to **EinsteinAI** — your go-to virtual assistant for all things physics! EinsteinAI is a state-of-the-art educational tool powered by **Google's Gemini AI model**, designed to provide accurate and concise answers to your physics-related questions. 🚀

✨ **Created by:** [Srishti Jaitly](https://www.linkedin.com/in/srishti-jaitly-6852b822b/) ✨

---

## 🧠 Features

🔍 **Physics-Centric Expertise**: EinsteinAI exclusively handles physics-related queries to ensure high-quality, focused responses.  
💬 **Smart Fallback Responses**: If your query is not physics-related, EinsteinAI will politely guide you back to its scope.  
🎨 **Interactive UI**: Experience an intuitive chat interface, powered by **Streamlit** for seamless interaction.  
⚡ **Gemini AI Power**: Utilizes the cutting-edge Gemini 1.5 Flash model for unparalleled accuracy.  
🔒 **Secure API Management**: API keys are safely managed using Streamlit secrets.  
🖌️ **Customizable**: Easily modify the app’s tab name and icon for a personalized touch.

---

## 🚀 How to Run the Project

### ✅ **Prerequisites**
1. Python 3.7 or above 🐍.
2. A Google Gemini API key 🔑.
3. Streamlit installed on your machine.

### ⚙️ **Installation**
1. Clone the repository:  
   ```bash
   git clone https://github.com/Srish0218/EinsteinAI.git
   cd EinsteinAI
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key:
   - Add your Google Gemini API key to the Streamlit secrets file.
   - Create a `.streamlit` directory in the root folder if it doesn’t exist:
     ```bash
     mkdir .streamlit
     ```
   - Inside `.streamlit`, create a `secrets.toml` file and add:
     ```toml
     GEMINI_API_KEY = "your-api-key"
     ```

### ▶️ **Running the Application**
1. Launch the Streamlit app:  
   ```bash
   streamlit run app.py
   ```
2. Open the URL displayed in your terminal to start chatting with EinsteinAI. 🌟

---

## 📂 Project Structure

```
EinsteinAI/
├── .streamlit/
│   └── secrets.toml       # Secure storage for API key
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── favicon.png            # Custom icon for the app (optional)
└── README.md              # Project documentation
```

---

## 🎨 Customization

🖋️ **Tab Name and Icon**: Modify the `st.set_page_config` section in `app.py` to update the tab title and favicon.  
🤖 **Fallback Behavior**: Customize the assistant’s response for non-physics questions in the prompt section of `app.py`.

---

## 📖 Example Usage

❓ **Physics Question**:  
*"What is Newton's second law of motion?"*  
✔️ **Response**:  
*"Newton's second law of motion states that the force acting on an object is equal to the mass of the object multiplied by its acceleration: F = ma."*

❓ **Non-Physics Question**:  
*"What is your name?"*  
✔️ **Response**:  
*"I am EinsteinAI, a physics assistant created by Srishti Jaitly. I am made to answer questions related to physics only. Please ask me something related to physics."*

---

## 🤝 Contribution

We welcome contributions! Fork the repository, make your changes, and submit a pull request. Let’s make EinsteinAI even better together! 🌟

---
## 🌐 Try It Now!

🌟 EinsteinAI is here to make physics engaging, accessible, and fun for everyone! 🌟

🔗 [Try EinsteinAI Here](https://einsteinai-srish0218.streamlit.app/)

---

## 💼 Creator

**Srishti Jaitly**  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/srishti-jaitly-6852b822b/)  

---

🌟 **EinsteinAI is here to make physics engaging, accessible, and fun for everyone!** 🌟

