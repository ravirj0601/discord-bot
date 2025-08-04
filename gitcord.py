
import requests
from config import GITHUB_REPO

# url = f"https://api.github.com/repos/{GITHUB_REPO}/commits"

# try:
def fetch_gitinfo(git_username, git_repo_name):
    url = f"https://api.github.com/repos/{git_username}/{git_repo_name}/commits"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and data:
            latest = data[0]
            return latest
        else:
            return ""
    except Exception as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f" Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f" Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f" Other request error occurred: {req_err}")
    except ValueError as json_err:
        print(f" JSON decode error: {json_err}")
    except Exception as e:
        print(f"Unexpected error: {e}")   
    # print(Commit_datails)
