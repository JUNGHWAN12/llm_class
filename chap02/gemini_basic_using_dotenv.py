from google import genai
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일에서 환경 변수 로드
api_key = os.getenv("GOOGLE_API_KEY")  # 환경 변수에서 API 키 가져오기
client = genai.Client(api_key = api_key)

respense = client.models.generate_content(
    model = "models/gemini-2.5-flash-lite",
    contents="2022년 카타르 월드컵의 우승팀을 알려줘")

print(respense.text)