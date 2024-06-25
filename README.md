# Finbot
This chatbot is designed to help you navigate the complex world of personal finance, investing, banking, taxes, and economics. With a focus on promoting financial literacy and responsible financial practices, the chatbot aims to educate and assist users in making informed financial decisions.

## Features
- General Financial Information: Get answers to your questions about personal finance, investing, banking, taxes, and economics.
- Clear Explanations: Financial concepts are explained in an easy-to-understand manner, avoiding jargon whenever possible.
- Risk Awareness: Learn about the risks associated with financial decisions and the importance of consulting with professional advisors.
- Promotion of Financial Literacy: The chatbot aims to improve your financial literacy and encourage responsible financial practices.
- Educational Assistance: The goal is to help you understand financial concepts to support your decision-making process.
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

## Disclaimer
The Financial Assistant Chatbot is intended for educational and informational purposes only. It is not a substitute for professional financial advice. Always consult with a certified financial advisor for specific financial advice and recommendations.
- Not a Certified Financial Advisor: The chatbot is not a certified financial advisor and cannot provide specific investment recommendations or predictions.
- Sensitive Information: Please do not share sensitive personal or financial information with the chatbot.
- Information Currency: The chatbot's knowledge is based on financial information up to April 2024. Users are advised to verify current rates and market conditions.
