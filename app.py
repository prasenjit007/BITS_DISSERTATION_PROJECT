import streamlit as st
from intent import identify_intent
from llm_intent_detection import identify_intent_llm
from agent import handle_agentic_task
from event import handle_event
from run_command import run_command
from ollama_client import query_ollama
from ask_bot import askBot
import os
import re

from langsmith import traceable  

# --- LangSmith Setup ---
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "BITS_RAG_Ollama"
os.environ["LANGCHAIN_API_KEY"] = ""

def contains_html_tags(text):
    if not text or not isinstance(text, str):
        return False
    pattern = re.compile(r'<[^>]+>')
    return bool(pattern.search(text))

def contains_html_tags_old(text):
    pattern = re.compile(r'<[^>]+>')
    return bool(pattern.search(text))

os.environ["STREAMLIT_WATCHER_DISABLE"] = "true"

st.set_page_config(page_title="Ollama Chatbot with Custom Events", layout="centered")
st.title("🤖 Chatbot with Agentic & Events")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me to calculate or manage users...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    #intent = identify_intent(user_input)
    #st.write("Identifying Intent...")
    intent = identify_intent_llm(user_input)
    print('intent identified : ', intent)

    if intent in ['add', 'subtract', 'multiply', 'divide']:
        response = handle_agentic_task(intent, user_input)
    elif intent in ['create_user', 'delete_user', 'list_users',"create_camera", "delete_camera", "list_camera"]:
        response = handle_event(intent, user_input)
    elif intent in ['run_command']:
        response = run_command(intent, user_input)
    else:
        response = askBot(intent, user_input)
        #response = query_ollama(user_input)

    st.session_state.chat_history.append(("bot", response))

# Display chat history
for speaker, msg in st.session_state.chat_history:
    if not msg:
        continue  # Skip if msg is None or empty

    if speaker == "user":
        st.chat_message("user").markdown(msg)
    else:
        if contains_html_tags(msg):
            st.markdown(msg, unsafe_allow_html=True)
        else:
            st.chat_message("assistant").markdown(msg)

