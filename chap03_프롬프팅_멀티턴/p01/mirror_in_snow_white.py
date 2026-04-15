from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# ① .env 파일에서 환경 변수 불러오기
load_dotenv()

# 클라이언트 생성 (.env 파일의 'GEMINI_API_KEY'를 자동으로 찾아 적용합니다)
client = genai.Client()

# ② Gemini API 호출
response = client.models.generate_content(
    model = "models/gemini-2.5-flash-lite",
    contents="세상에서 누가 제일 아름답니?",  # ④ 사용자 질문 (User Prompt)
    config=types.GenerateContentConfig(
        temperature=0.1,  # ③ 창의성 조절
        system_instruction="너는 백설공주 이야기 속의 거울이야. 그 이야기 속의 마법 거울의 캐릭터에 부합하게 답변해줘."  # 시스템 프롬프트 (페르소나)
    )
)

print(response)

print('----') # ⑤
# 실제 생성된 텍스트 답변만 깔끔하게 출력
print(response.text)