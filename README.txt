AI Powered Chatbot
Streamlit × OpenAI GPT-5.2

An interactive AI chatbot application built with Streamlit and OpenAI’s GPT-5.2 model. This project demonstrates how to create a conversational web interface that maintains context and delivers real-time AI responses.

Overview
This application allows users to chat with an AI model through a clean and intuitive web interface. It leverages Streamlit’s chat components and OpenAI’s Chat Completions API to deliver a seamless conversational experience.

Features
- Context-aware conversations using session state
- Real-time chat interface powered by Streamlit
- Integration with OpenAI GPT-5.2
- Persistent chat history during a session
- Lightweight and easy to extend

Tech Stack
- Python 3.9+
- Streamlit
- OpenAI Python SDK

Architecture & Flow
1. Streamlit initializes the chat UI.
2. Conversation history is stored in st.session_state.
3. User input is captured via st.chat_input().
4. Messages are sent to OpenAI’s Chat Completions API.
5. The AI response is rendered back in the chat interface.

Getting Started
1. Clone the repository
2. Install dependencies: pip install streamlit openai
3. Set the OPENAI_API_KEY as an environment variable
4. Run the app using: streamlit run app.py

Security Best Practices
- Do not hardcode API keys
- Use environment variables or secret managers
- Never commit API keys to version control

Project Structure
streamlit_conversational_chatbot.py
README.txt
requirements.txt

Possible Enhancements
- User authentication
- Multiple conversation threads
- Prompt customization
- Logging and analytics
- Cloud deployment

License
This project is intended for educational and demonstration purposes.
