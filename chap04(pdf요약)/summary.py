from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

def summarize_txt(file_path: str): # ①
    # 클라이언트 생성 (.env에서 GEMINI_API_KEY 자동 로드)
    client = genai.Client()

    # ② 주어진 텍스트 파일을 읽어들인다.
    with open(file_path, 'r', encoding='utf-8') as f:
        txt = f.read()

    # ③ 요약을 위한 시스템 프롬프트(지시사항)를 분리하여 작성한다.
    system_instruction = '''
    너는 문서를 요약하는 봇이다. 사용자가 제공하는 글을 읽고, 저자의 문제 인식과 주장을 파악하여 주요 내용을 요약하라. 

    작성해야 하는 포맷은 다음과 같다. 
    
    # 제목

    ## 저자의 문제 인식 및 주장 (15문장 이내)
    
    ## 저자 소개
    '''

    print("문서 분석을 시작합니다...")
    print('=========================================')

    # ④ Gemini API를 사용하여 요약을 생성한다.
    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",
        contents=txt, # 순수 텍스트 데이터만 사용자 입력으로 전달
        config=types.GenerateContentConfig(
            temperature=0.1, # ③ 사실 기반의 정확한 요약을 위해 온도를 낮춤
            system_instruction=system_instruction # 봇의 역할과 포맷 지시
        )
    )

    return response.text

if __name__ == '__main__':
    # 테스트를 위해 본인의 PC 환경에 맞는 경로로 수정해야 할 수 있습니다.
    file_path = 'chap04(pdf요약)\data\블록형 프로그래밍 언어와 텍스트형 프로그래밍 언어의 교육적 효과 비교 분석_with_preprocessing.txt'

    summary = summarize_txt(file_path)
    print(summary)

    # ⑤ 요약된 내용을 파일로 저장한다.
    # 저장할 폴더(output)가 미리 만들어져 있어야 에러가 나지 않습니다.
    with open('./chap04(pdf요약)/output/crop_model_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)