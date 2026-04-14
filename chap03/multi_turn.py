from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client()

# ① AI 응답을 받아오는 함수
def get_ai_response(history_list):
    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",
        contents=history_list,  # 누적된 대화 기록 리스트를 통째로 전달
        config=types.GenerateContentConfig(
            temperature=0.9,
            system_instruction="너는 사용자를 도와주는 상담사야."  # 시스템 프롬프트는 따로 분리
        )
    )
    return response.text

# Gemini는 시스템 프롬프트를 config에 따로 설정하므로, 대화 기록은 빈 리스트로 시작합니다.
messages = []

while True:
    user_input = input("사용자: ")

    if user_input.lower() == "exit":  # ② 종료 조건
        print("대화를 종료합니다.")
        break
    
    # 1. 사용자 메시지를 대화 기록 리스트에 추가 (역할: user)
    messages.append(
        types.Content(role="user", parts=[types.Part.from_text(text=user_input)])
    )
    
    # 2. 누적된 대화 기록을 보내서 AI 응답 받아오기
    ai_response = get_ai_response(messages)
    
    # 3. 받아온 AI 응답도 대화 기록 리스트에 추가 (역할: model)
    messages.append(
        types.Content(role="model", parts=[types.Part.from_text(text=ai_response)])
    )

    print("AI: " + ai_response)