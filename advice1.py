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