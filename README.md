# 💬 ChatGPT Clone by The Ai Shankar

A lightweight, real-time ChatGPT clone application built with **Python**, **Streamlit**, and the **OpenAI API**. This project features full conversational chat memory, model selection, real-time response streaming, and clean UI branding.

## 📺 Watch the Video Tutorial

Want to see how this app was built step-by-step? Watch the full video tutorial on YouTube!

[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch%20Tutorial-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=K9cz4PDuVkU)

> 🔔 **Subscribe to the channel:** [TheAIShankar](https://www.youtube.com/@TheAIShankar) for more AI projects, Python tutorials, and coding tips!

---


---

## ✨ Key Features

- **⚡ Live Response Streaming:** Powered by `st.write_stream` for a smooth, real-time typewriter output effect.
- **🧠 Full Chat Memory:** Retains multi-turn conversation context across interactions using `st.session_state`.
- **⚙️ Dynamic Model Switcher:** Instantly switch between `gpt-4o-mini` and `gpt-4o` from the sidebar.
- **🔒 Safe Credentials Management:** Stores sensitive keys securely using Streamlit's `.streamlit/secrets.toml`.
- **🎨 Custom UI Branding:** Includes dedicated headers and sidebar banners for channel promotion.
- **🧹 Instant Reset:** One-click conversation reset to clear session memory.

---

## 📁 Project Structure

```text
streamlit-openai-chatbot/
│
├── .streamlit/
│   ├── secrets.toml       # OpenAI API Key (OPENAI_API_KEY='API_KEY')
│
├── .gitignore             # Ignores .streamlit/secrets.toml, venv, cache
├── app.py                 # Main Streamlit application code
├── requirements.txt       # Dependencies list (streamlit, openai)
└── README.md              # Project description, installation & usage guide# streamlit-openai-chatbot
A lightweight, real-time ChatGPT clone built with Python, Streamlit, and OpenAI API featuring full chat memory and token streaming
