import requests
import json
import random
from datetime import datetime

def fetch_random_advice():
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        data = json.loads(response.text)
        advice = data['slip']['advice']
        return advice
    except Exception as e:
        print(f"API 호출 중 오류 발생: {e}")
        return None

now = datetime.now()

def save_advice_to_file(advice, filename="advice.txt"):
    with open(filename, "a") as file:
        file.write('[' + now.strftime('%Y-%m-%d %H:%M:%S') + '] ' + advice + ' ' + "\n")

def get_random_advice_from_file(filename="advice.txt"):
    try:
        with open(filename, "r") as file:
            advices = file.readlines()
            if advices:
                return advices
            else:
                return None
    except Exception as e:
        print(f"파일 읽기 중 오류 발생: {e}")
        return None

def number_and_save_advice(advice_list, filename="advice.txt"):
    if advice_list:
        numbered_advice_list = [f"{i + 1}. {advice.strip()}" for i, advice in enumerate(advice_list)]
        with open(filename, "w") as file:
            file.write("\n".join(numbered_advice_list))
        print("\nNumbered Advice saved to advice.txt.")
    else:
        print("No advice to number and save.")

def yes_or_no():
    print("Would you like to put this advice in advice.txt? ----- Press Y/N")
    value = input()
    if value.lower() == 'y':
        print("\nSave complete.")
        return 1
    else:
        return 0

if __name__ == "__main__":
    # 실행할 때마다 랜덤 명언 출력
    random_advice = fetch_random_advice()
    if random_advice:
        print("Random Advice from API:", random_advice, now.strftime('(%Y-%m-%d %H:%M:%S)\n'))
        if yes_or_no():
            save_advice_to_file(random_advice)
    else:
        print("Failed to get random advice from API")

    saved_advices = get_random_advice_from_file()
    if saved_advices:
        print("\nRandom Advice from advice.txt:")
        for i, advice in enumerate(saved_advices):
            print(f"{i + 1}. {advice.strip()[22:]}")
        
        number_and_save_advice(saved_advices)
    else:
        print("Failed to get random advice from advice.txt")
