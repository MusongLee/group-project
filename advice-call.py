import requests
import json

def fetch_random_advice():
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        data = json.loads(response.text)
        advice = data['slip']['advice']
        return advice
    except Exception as e:
        print(f"API 호출 중 오류 발생: {e}")
        return None

def save_advice_to_file(advice, filename="advice.txt"):
    with open(filename, "a") as file:
        file.write(advice + "\n")

random_advice = fetch_random_advice()

if random_advice:
    print("랜덤 명언:", random_advice)
    save_advice_to_file(random_advice)
else:
    print("랜덤 명언을 불러오는 데 실패했습니다.")