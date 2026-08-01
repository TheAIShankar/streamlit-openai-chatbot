import streamlit as st
from openai import OpenAI

# Page Configuration (Browser Tab Title & Favicon)
st.set_page_config(
    page_title="The Ai Shankar - ChatGPT Clone",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 ChatGPT Clone")
st.caption("🚀 Built by **The Ai Shankar** | Powered by OpenAI & Streamlit")

# 1. Initialize OpenAI client securely using Streamlit Secrets
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception as e:
    st.error("OpenAI API Key not found! Please configure .streamlit/secrets.toml.")
    st.stop()

# 2. Initialize Chat Memory in Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar branding & controls
with st.sidebar:
    st.title("📺 The Ai Shankar")
    st.markdown("Subscribe for more AI & Coding Tutorials!")
    st.divider()
    
    st.header("⚙️ Model Settings")
    model_choice = st.selectbox(
        "Select Model",
        ["gpt-4o-mini", "gpt-4o"],
        index=0
    )
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# 3. Render Existing Chat History on Page Reload
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle New User Input
prompt = st.chat_input("Ask me anything...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()

# 5. Generate Assistant Response (Runs after user message is rendered)
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant"):
        api_messages = [
            {"role": m["role"], "content": m["content"]} 
            for m in st.session_state.messages
        ]
        
        stream = client.chat.completions.create(
            model=model_choice,
            messages=api_messages,
            stream=True
        )
        
        response_text = st.write_stream(stream)
        
    st.session_state.messages.append({"role": "assistant", "content": response_text})