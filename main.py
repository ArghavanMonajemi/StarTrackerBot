import requests
import csv
from datetime import datetime

#change this to your repo
REPO = "torvalds/linux" # Format: "owner/repository"
URL = f"https://api.github.com/repos/{REPO}"
CSV_FILE = "stars_history.csv"
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"

def get_stars():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data['stargazers_count']
    else:
        print("Error fetching data:", response.status_code)
        return None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)

def save_and_check_stars(stars):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_stars = None

    try:
        with open(CSV_FILE, "r") as file:
            last_stars = list(csv.reader(file))[-1][1]
    except (FileNotFoundError, IndexError):
        pass

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([now, stars])

    print(f"Saved: {now} - {stars} ⭐")

    if last_stars and int(stars) > int(last_stars):
        message = f"🎉 {REPO} gained a new star! Total: {stars} ⭐"
        send_telegram_message(message)

if __name__ == "__main__":
    stars = get_stars()
    if stars is not None:
        save_and_check_stars(stars)
