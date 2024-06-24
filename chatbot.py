import streamlit as st
import requests
import json

# Set page config
# st.set_page_config(page_title="Arnab's AI Chatbot", page_icon="🤖", layout="centered")
st.set_page_config(page_title="Arnab's AI Chatbot", page_icon="🤖", layout="centered", initial_sidebar_state="auto", menu_items=None)

# Custom CSS
st.markdown("""
<style>
.stTextInput > div > div > input {
    font-size: 16px;
}
.stButton > button {
    font-size: 16px;
    font-weight: bold;
    width: 100%;
}
.chat-message {
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
}
.chat-message.user {
    background-color: #1c2e4a;
    align-items: flex-end;
    color: white;
}
.chat-message.assistant {
    background-color: #2f2f2f;
    align-items: flex-start;
    color: white;
}
.chat-message .message-content {
    word-wrap: break-word;
    max-width: 80%;
}
.chat-message .message-role {
    font-size: 0.8rem;
    color: #888;
    margin-bottom: 0.2rem;
}
.social-links {
    display: flex;
    justify-content: center;
    gap: 20px;
}
.social-button {
    text-decoration: none;
    color: white;
    background-color: #0e1117;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 5px 10px;
    font-size: 14px;
    transition: background-color 0.3s;
}
.social-button:hover {
    background-color: #30363d;
}
</style>
""", unsafe_allow_html=True)

# Set up the Streamlit app
st.title("Chatbot 💬")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# System prompt
system_prompt = """You are an AI assistant created by Arnab. You always provide accurate and relevant information. If you're unsure about something, you'll say so. You're here to assist users with their questions and tasks to the best of your ability."""

# Function to clear conversation
def clear_conversation():
    st.session_state.messages = []

# Function to generate prompt with history
def generate_prompt(new_message):
    conversation = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
    return f"{system_prompt}\n\n{conversation}\nUser: {new_message}\nAssistant:"

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.container():
        st.markdown(f"""
        <div class="chat-message {message['role'].lower()}">
            <div class="message-role">{message['role']}</div>
            <div class="message-content">{message['content']}</div>
        </div>
        """, unsafe_allow_html=True)

# Create two columns for input and clear button
col1, col2 = st.columns([3, 1])

# Accept user input in the first (wider) column
with col1:
    prompt = st.text_input("Ask me anything:", key="user_input")

# Add clear button in the second (narrower) column
with col2:
    st.write('\n\n\n\n')
    st.write('\n\n\n\n')
    if st.button("Clear Chat", key="clear_button"):
        clear_conversation()
        st.experimental_rerun()

if st.button("Send", key="send_button") and prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "User", "content": prompt})
    
    # Generate full prompt with history
    full_prompt = generate_prompt(prompt)
    
    # Send request to local LLM
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": full_prompt
    }
    
    try:
        with st.spinner("Thinking..."):
            response = requests.post(url, json=payload, stream=True)
            response.raise_for_status()
            
            # Parse the streaming response
            full_response = ""
            for line in response.iter_lines():
                if line:
                    try:
                        json_line = json.loads(line)
                        if 'response' in json_line:
                            full_response += json_line['response']
                    except json.JSONDecodeError:
                        continue  # Skip lines that aren't valid JSON
            
            if not full_response:
                full_response = "Sorry, I couldn't generate a response."
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "Assistant", "content": full_response})
        
        # Display the updated conversation
        st.experimental_rerun()
    
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")

import streamlit as st

# ... (rest of your code remains the same)

# At the end of your script, add:

# Add some space at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)

# Add GitHub and LinkedIn icons
st.markdown("""
    <style>
    .social-links {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    .social-btn {
        display: inline-flex;
        width: 40px;
        height: 40px;
        background-color: #ffffff;
        color: #000000;
        border-radius: 50%;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        font-size: 24px;
        transition: 0.3s;
    }
    .social-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }
    </style>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    
    <div class="social-links">
        <a href="https://github.com/chakraborty-arnab" target="_blank" class="social-btn">
            <i class="fab fa-github"></i>
        </a>
        <a href="https://www.linkedin.com/in/arnab-chakraborty13/" target="_blank" class="social-btn">
            <i class="fab fa-linkedin-in"></i>
        </a>
    </div>
""", unsafe_allow_html=True)