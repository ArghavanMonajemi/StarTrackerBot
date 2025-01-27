import requests
import csv
from datetime import datetime

REPO = "torvalds/linux"
URL = f"https://api.github.com/repos/{REPO}"
CSV_FILE = "stars_history.csv"

def get_stars():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data['stargazers_count']
    else:
        print("Error fetching data:", response.status_code)
        return None

def save_to_csv(stars):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([now, stars])
    print(f"Saved: {now} - {stars} ⭐")

if __name__ == "__main__":
    stars = get_stars()
    if stars is not None:
        save_to_csv(stars)
