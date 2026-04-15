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
    model="models/gemini-2.5-flash-lite",  # 👈 선생님께서 짚어주신 정확한 표준 모델 경로
    contents="오리",  
    config=types.GenerateContentConfig(
        temperature=0.9,  
        system_instruction="너는 유치원 학생이야. 유치원생처럼 답변해줘." 
    )
)

print('----') 
# 실제 생성된 텍스트 답변 출력
print(response.text)