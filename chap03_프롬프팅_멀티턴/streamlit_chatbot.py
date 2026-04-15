import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv('GOOGLE_API_KEY')
client = genai.Client(api_key=gemini_api_key)

st.title("🤖 Gemini 멀티턴 챗봇")
st.write("Streamlit 화면에서 대화 이력을 기억하며(Multi-turn) 답변하는 챗봇입니다.")

# ① AI 응답을 받아오는 함수 (멀티턴)
def get_ai_response(messages_dict):
    # Streamlit의 딕셔너리 리스트를 Gemini의 types.Content 리스트로 변환
    history_list = []
    for msg in messages_dict:
        role = "model" if msg["role"] == "assistant" else "user"
        history_list.append(
            types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])])
        )
    
    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",
        contents=history_list,  # 누적된 대화 기록 리스트를 통째로 전달
        config=types.GenerateContentConfig(
            temperature=0.9,
            system_instruction="너는 사용자를 도와주는 상담사야."  # 시스템 프롬프트 설정
        )
    )
    return response.text

# Initialize chat history (대화 이력 초기화)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("메시지를 입력하세요..."):
    # 1. 사용자 메시지를 대화 기록에 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 화면에 사용자 메시지 표시
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. 누적된 대화 기록을 보내서 AI 응답 받아오기
    with st.chat_message("assistant"):
        with st.spinner("AI가 답변을 작성하고 있습니다..."):
            ai_response = get_ai_response(st.session_state.messages)
        st.markdown(ai_response)
        
    # 3. 받아온 AI 응답도 대화 기록 리스트에 추가
    st.session_state.messages.append({"role": "assistant", "content": ai_response})