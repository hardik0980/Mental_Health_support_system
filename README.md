🧠 **Mental Health Support Agent**

A Streamlit-based mental health chatbot powered by Meta’s LLaMA 3 model via Ollama.
This project was developed under a 1-month internship with Elevate Labs in May 2025.


**🚀 How to Run the Project

Clone the repository
git clone https://github.com/<hardik0980>/mental-health-agent.git

Navigate to the folder
cd mental-health-agent

Install the dependencies
pip install -r requirements.txt

Start the app
streamlit run app.py

Make sure Ollama and the LLaMA 3 model are properly installed.
Use this to run the model locally:
ollama run llama3:8b**





**🌟 Project Highlights**

Empathetic, conversational AI agent

Name personalization using Regex

Audio responses via Google Text-to-Speech

Custom UI with chat bubbles, logo, and background

Special buttons: Positive affirmations & Guided meditations

**🛠️ Tools and Technologies Used**

Python
Used as the core language for backend logic, session management, and API integrations.

Streamlit
Built the interactive web interface, enabling real-time chat and state handling with minimal frontend code.

Ollama with LLaMA 3
Ollama is used to run Meta’s LLaMA 3 (8B) model locally, ensuring fast, secure, and offline response generation.

gTTS (Google Text-to-Speech)
Converted chatbot text replies into spoken audio, making the interaction more human and comforting.

Regex (re module)
Extracted user names from inputs like “My name is…” or “I’m…” to personalize the conversation.

HTML/CSS
Enhanced the default Streamlit UI with custom HTML and CSS for chat bubbles, buttons, and responsive layout.

Base64 Encoding
Embedded background images and audio clips directly within the app using base64 encoding to avoid external file dependencies.

Visual Studio Code (VS Code)
Used as the main development environment, taking advantage of its debugging, Git integration, and extensions.

GitHub
Hosted the project repository with version control for source code, assets, and documentation.

**🙏 Acknowledgment**
This project was created as part of a one-month internship with Elevate Labs in May 2025.
Special thanks to our mentors for their continuous guidance and support throughout the development phase.

**🔗 References**

Meta LLaMA 3 Model

Streamlit Documentation

Ollama Official Site

gTTS PyPI Package




