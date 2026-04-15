import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv('GOOGLE_API_KEY')

# (0) 사이드바에서 api_key 입력하는 부분 
with st.sidebar:
    "[Get a Gemini API key](https://aistudio.google.com/app/apikey)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot")

# (1) st.session_state에 "messages"가 없으면 초기값을 설정
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# (2) 대화 기록을 출력
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


def to_gemini_contents(messages):
    contents = []
    for msg in messages:
        role = "model" if msg["role"] == "assistant" else "user"
        contents.append(
            types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])])
        )
    return contents

# (3) 사용자 입력을 받아 대화 기록에 추가하고 AI 응답을 생성
if prompt := st.chat_input():
    if not gemini_api_key:
        st.info("Please add your Gemini API key to continue.")
        st.stop()

    client = genai.Client(api_key=gemini_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt}) 
    st.chat_message("user").write(prompt) 
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=to_gemini_contents(st.session_state.messages),
    )
    msg = response.text
    st.session_state.messages.append({"role": "assistant", "content": msg}) 
    st.chat_message("assistant").write(msg)
