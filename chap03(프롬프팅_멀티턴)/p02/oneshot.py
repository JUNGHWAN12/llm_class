from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# ① .env 파일에서 환경 변수 불러오기
load_dotenv()

# 클라이언트 생성
client = genai.Client()

# ② Gemini API 호출
response = client.models.generate_content(
    model="models/gemini-2.5-flash-lite",
    # ④ 리스트 형태로 대화 기록(원샷 예시)과 질문을 전달합니다.
    contents=[
        # [원샷 예시 제공]
        types.Content(role="user", parts=[types.Part.from_text(text="참새")]),
        types.Content(role="model", parts=[types.Part.from_text(text="짹짹")]),
        
        # [실제 질문]
        types.Content(role="user", parts=[types.Part.from_text(text="오리")]),
    ],
    config=types.GenerateContentConfig(
        temperature=0.9,  # ③ 창의성 조절
        system_instruction="너는 유치원 학생이야. 유치원생처럼 답변해줘."  # 시스템 프롬프트
    )
)

print('----') # ⑤
# 실제 생성된 텍스트 답변 출력
print(response.text)