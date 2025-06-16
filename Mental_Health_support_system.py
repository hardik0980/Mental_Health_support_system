
import streamlit as st
import base64
import re
from gtts import gTTS
import ollama

# -------------------- Page Setup --------------------
st.set_page_config(page_title="Mental Health Chatbot", layout="centered")

# -------------------- Background Image --------------------
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_base64(r"C:\Users\hardi\OneDrive\Desktop\ai-ml internship\Blue White Gradient Aesthetic Background Instagram Post.png")
logo_base64 = get_base64(r"C:\Users\hardi\OneDrive\Desktop\ai-ml internship\logo1.png")

# -------------------- Session Initialization --------------------
st.session_state.setdefault("conversation_history", [])
st.session_state.setdefault("stage", "intro")
st.session_state.setdefault("username", "")
st.session_state.setdefault("temp_input", "")

# -------------------- Custom CSS & Header --------------------
st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            font-family: 'Segoe UI', sans-serif;
        }}
        .header-title {{
            background-color: rgba(0, 123, 255, 0.95);
            padding: 15px 25px;
            display: flex;
            align-items: center;
            gap: 15px;
            font-size: 26px;
            font-weight: bold;
            color: white;
            border-radius: 0 0 15px 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }}
        .header-title img {{ height: 40px; border-radius: 50%; }}
        .message {{
            background-color: rgba(green);
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }}
        .chat-container {{
           
            align-items: center;
            gap: 10px;
            margin-top: 1rem;
        }}
        .chat-input {{
            flex: 1;
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #ccc;
            font-size: 16px;
        }}
        .send-button {{
            background-color: #007bff;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
        }}
        .send-button:hover {{
            background-color: #0056b3;
        }}
    </style>
    <div class="header-title">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo">
        Mental Health Support System
    </div>
  
""", unsafe_allow_html=True)

# -------------------- Helper Functions --------------------
def show_convo():
    for msg in st.session_state["conversation_history"]:
        sender = "You" if msg["role"] == "user" else "AI"
        st.markdown(f"""
            <div class="message">
                <strong>{sender}:</strong> {msg['content']}
            </div>
        """, unsafe_allow_html=True)

def extract_name(text):
    patterns = [
        r"my name is ([a-zA-Z]+)",
        r"i am ([a-zA-Z]+)",
        r"i'm ([a-zA-Z]+)",
        r"it's ([a-zA-Z]+)",
        r"(?:name[:\s]*)?([a-zA-Z]+)$"
    ]
    for pattern in patterns:
        match = re.search(pattern, text.lower())
        if match:
            return match.group(1).capitalize()
    return text.capitalize()

def generate_response(user_input):
    st.session_state["conversation_history"].append({"role": "user", "content": user_input})
    response = ollama.chat(model="llama3:8b", messages=st.session_state["conversation_history"])
    reply = response["message"]["content"]
    st.session_state["conversation_history"].append({"role": "assistant", "content": reply})
    return reply

def generate_affirmation():
    prompt = f"Give a short positive affirmation for {st.session_state['username']} who is feeling a bit low."
    response = ollama.chat(model="llama3:8b", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

def generate_meditation():
    prompt = f"Give a 5-minute guided meditation for {st.session_state['username']} to relax and feel calm."
    response = ollama.chat(model="llama3:8b", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

def play_audio(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    with open("response.mp3", "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        return f'<audio controls src="data:audio/mp3;base64,{b64}"></audio>'

# -------------------- Main Conversation Flow --------------------
if st.session_state["stage"] == "intro":
    st.session_state["conversation_history"].append({"role": "assistant", "content":
        "You are a compassionate, empathetic, and professional mental health support assistant. "
        "Your primary role is to offer emotional support, encouragement, and helpful information — without giving medical or clinical advice. "
        "Always respond with kindness, patience, and respect. Listen deeply to the user's feelings and concerns, validate their emotions, and create a safe, non-judgmental space for them to express themselves. "
        "Your goal is to be a calming, understanding presence during moments of emotional difficulty."
    })
    st.session_state["conversation_history"].append({"role": "assistant", "content": "Hi there! 😊 May I know your name?"})
    st.session_state["stage"] = "ask_name"
    st.rerun()




# ---------- Ask Name Stage ----------
if st.session_state["stage"] == "ask_name":
    show_convo()
    with st.form("name_form"):
        col1, col2 = st.columns([4, 1])
        with col1:
            name_input = st.text_input("Your Name", placeholder="Type something like: My name is Hardik", label_visibility="collapsed")
        with col2:
            submitted = st.form_submit_button("Send")

        if submitted and name_input:
            name = extract_name(name_input)
            st.session_state["username"] = name
            st.session_state["conversation_history"].append({"role": "user", "content": name_input})
            st.session_state["conversation_history"].append({"role": "assistant", "content": f"Hey {name}, how can I help you today? 😊"})
            st.session_state["stage"] = "chat"
            st.rerun()
if "temp_input" not in st.session_state:
    st.session_state["temp_input"] = ""
# ---------- Chat Stage ----------
elif st.session_state["stage"] == "chat":
    show_convo()
    with st.form("chat_form"):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.session_state["temp_input"] = st.text_input(
                "", 
                value=st.session_state["temp_input"], 
                placeholder="Type your message here...", 
                label_visibility="collapsed"
            )
        with col2:
            submitted = st.form_submit_button("Send")

        if submitted and st.session_state["temp_input"]:
            with st.spinner("Thinking..."):
                reply = generate_response(st.session_state["temp_input"])
                st.markdown(f'<div class="message"><strong>AI:</strong> {reply}</div>', unsafe_allow_html=True)
                st.markdown(play_audio(reply), unsafe_allow_html=True)
            st.session_state["temp_input"] = ""


# -------------------- Affirmation / Meditation Buttons --------------------
st.markdown('<div class="button-container center">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("Give me a positive Affirmation"):
        affirmation = generate_affirmation()
        st.markdown(f'<div class="message"><strong>AI:</strong> {affirmation}</div>', unsafe_allow_html=True)
        st.markdown(play_audio(affirmation), unsafe_allow_html=True)
with col2:
    if st.button("Give me a guided Meditation"):
        meditation = generate_meditation()
        st.markdown(f'<div class="message"><strong>AI:</strong> {meditation}</div>', unsafe_allow_html=True)
        st.markdown(play_audio(meditation), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
