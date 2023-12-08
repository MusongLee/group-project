import requests
from datetime import datetime
import json

now = datetime.now()

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
        file.write('[' + now.strftime('%Y-%m-%d %H:%M:%S') + '] ' + advice + ' ' + "\n")

def yes_or_no():
    print("Would you like to put this advice in advice.txt? ----- Press Y/N")
    value = input()
    if value == 'y' or value == 'Y':
      print("\nSave complete.")
      return 1
    else :
      return 0

random_advice = fetch_random_advice()

if random_advice:
    print("랜덤 명언:", random_advice, now.strftime('(%Y-%m-%d %H:%M:%S)\n'))
    if yes_or_no():
        save_advice_to_file(random_advice)
else:
    print("랜덤 명언을 불러오는 데 실패했습니다.")
