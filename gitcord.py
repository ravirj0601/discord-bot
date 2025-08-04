import requests
from config import GITHUB_REPO

url = f"https://api.github.com/repos/{GITHUB_REPO}/commits"

# try:

response = requests.get(url)
response.raise_for_status()
data = response.json()

if isinstance(data, list) and data:
    latest = data[0]
    Commit_datails = {
        "Author" : latest["commit"]["author"]["name"],
        "Message" : latest["commit"]["message"],
        "Date" : latest["commit"]["author"]["date"][:10]
    }
    print(Commit_datails)

# except Exception as e:ll
