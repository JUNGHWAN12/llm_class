from google import genai

client = genai.Client(api_key = "AIzaSyB4hj13o_3Tv1lCpUgz8ABpXzX5DS4b0N4")

respense = client.models.generate_content(
    model = "models/gemini-2.5-flash-lite",
    contents="2022년 카타르 월드컵의 우승팀을 알려줘")

print(respense.text)