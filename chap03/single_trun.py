from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# ① 환경 변수 로드 및 클라이언트 생성
load_dotenv()
client = genai.Client()

print("봇: 안녕하세요! 무엇이든 물어보세요. (종료하려면 'exit' 입력)")
print("-" * 50)

# ② 무한 루프 시작
while True:
    user_input = input("사용자: ")

    # 종료 조건
    if user_input.lower() == "exit":
        print("봇: 대화를 종료합니다.")
        break

    # ③ 매번 독립적으로 API를 호출합니다 (채팅 기록을 유지하지 않음)
    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",
        contents=user_input,  # 매번 방금 입력한 질문 하나만 보냅니다.
        config=types.GenerateContentConfig(
            temperature=0.9,
            system_instruction="너는 사용자를 도와주는 상담사야."
        )
    )
    
    print("AI: " + response.text)