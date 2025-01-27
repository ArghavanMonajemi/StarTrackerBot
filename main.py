import requests

# change this to your repo
REPO = "torvalds/linux"  # Format: "owner/repository"
URL = f"https://api.github.com/repos/{REPO}"

def get_stars():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data['stargazers_count']
    else:
        print("Error fetching data:", response.status_code)
        return None

if __name__ == "__main__":
    stars = get_stars()
    if stars is not None:
        print(f"{REPO} has {stars} stars ⭐")
