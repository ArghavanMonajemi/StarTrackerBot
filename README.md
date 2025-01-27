# 🌟 StarTrackerBot

StarTrackerBot is a Python script that tracks GitHub repository stars and logs the count over time. It also sends a Telegram notification whenever the repository gains a new star.

## 🚀 Features
- Fetches the current star count of a GitHub repository
- Saves the star history to a CSV file
- Sends a Telegram notification when the star count increases

## 🛠 Setup

### 1️⃣ Prerequisites
- Python 3.x installed
- A Telegram bot and chat ID (for notifications)
- A GitHub repository to track

### 2️⃣ Install Dependencies
Clone the repository and install required packages:

```bash
git clone https://github.com/ArghavanMonajemi/StarTrackerBot.git
cd StarTrackerBot
pip install requests
```

### 3️⃣ Configure Your Bot
Replace these placeholders in the script with your actual credentials:
```python
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"
REPO = "torvalds/linux"  # Change to the GitHub repo you want to track
```

4️⃣ Run the Bot
```bash
python main.py
```

## ⏳ Scheduling the Bot
To automate the bot, you can set up a scheduler.

### 🐧 Linux/macOS (Using cron)
1. Open the terminal and type:
```bash
crontab -e
```
2. Add this line at the end (runs every hour):
```bash
0 * * * * /usr/bin/python3 /path/to/StarTrackerBot/main.py
```
* Replace /path/to/StarTrackerBot/star_tracker.py with the actual path.
3. Save and exit.

### 🖥 Windows (Using Task Scheduler)
1. Open Task Scheduler.
2. Click Create Basic Task.
3. Set a name like StarTrackerBot.
4. Select Daily or Hourly.
5. Choose Start a Program and browse for python.exe.
6. Add the script path (star_tracker.py) in the "Add arguments" field.
7. Click Finish.
* Now, the bot will run automatically at the scheduled time!

## 📂 How It Works
The script fetches the star count from the GitHub API.
It logs the count into a CSV file (stars_history.csv).
If the star count has increased, it sends a Telegram message.
