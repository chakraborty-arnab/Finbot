# Chatbot
This is a Streamlit-based chatbot application that uses a local Language Model (LLM) to generate responses. The chatbot provides a user-friendly interface for interacting with an AI assistant.

## Features

- Interactive chat interface
- Integration with a local LLM
- Chat history management
- Clear conversation functionality
- Dark theme UI
- GitHub and LinkedIn profile links

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.7+
- pip (Python package manager)

## Getting Started
1. Clone this repository:
```
git clone https://github.com/chakraborty-arnab/Finbot.git
```

2. Download [Ollama](https://ollama.com/)

 **Note:** Ensure your local LLM is running and accessible at `http://localhost:11434/api/generate`.

3. Install Requirements
```
pip install -r requirements.txt
```
4. Launch the application
```
streamlit run chatbot.py
```
## How to Use

- Type your message in the input box and click "Send" or press Enter to submit.
- The AI assistant will generate a response based on the conversation history.
- Use the "Clear Chat" button to start a new conversation.
- Click on the GitHub or LinkedIn icons at the bottom of the page to visit the developer's profiles.

## Customization

- To modify the system prompt, edit the `system_prompt` variable in the `chatbot.py` file.
- To change the appearance, modify the CSS in the `st.markdown` section at the beginning of the script.
