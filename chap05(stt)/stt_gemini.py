from google import genai
from dotenv import load_dotenv
import os

# ① 환경 변수 로드 및 클라이언트 생성
load_dotenv()
client = genai.Client()

audio_file_path = 'chap05(stt)\\audio\\audio_1.mp3'

# ② 구글 서버에 미디어 파일 업로드 (File API 활용)
# 음성, 영상 등 용량이 큰 파일은 File API를 통해 업로드 후 사용하는 것이 정석입니다.
print("오디오 파일을 업로드 중입니다...")
uploaded_audio = client.files.upload(file=audio_file_path)

# ③ [실습 1] 음성 인식 (STT - 그대로 받아적기)
print("\n--- [1] 음성 인식 (Transcription) ---")
response_stt = client.models.generate_content(
    model="models/gemini-2.5-flash", # 멀티모달(음성/영상) 처리는 flash 모델을 권장합니다.
    contents=[
        uploaded_audio, 
        "이 음성 파일에서 들리는 말을 한국어 텍스트로 그대로 받아적어줘." # 프롬프트로 행동 지시
    ]
)
print(response_stt.text)

# ④ [실습 2] 음성 번역 (Translation - 영어로 번역하기)
print("\n--- [2] 영어로 번역 (Translation) ---")
response_trans = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents=[
        uploaded_audio, 
        "이 음성 파일에서 들리는 말을 영어(English)로 번역해서 텍스트로 적어줘." # 지시어만 변경!
    ]
)
print(response_trans.text)