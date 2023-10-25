# Make_Repository_Private.py

# Code for making a GitHub repository private
import requests
from requests.exceptions import RequestException

def make_repository_private(token, repo_name):
    try:
        headers = {"Authorization": f"token {token}"}
        data = {"private": True}
        response = requests.patch(f"https://api.github.com/repos/YourUsername/{repo_name}", headers=headers, json=data)

        if response.status_code == 200:
            print(f"Repository '{repo_name}' is now private.")
        else:
            print(f"Failed to make repository private. Status code: {response.status_code}")

    except RequestException as e:
        raise Exception(f"Request error: {str(e)}")

if __name__ == '__main__':
    try:
        github_token = "YourGitHubToken"
        repo_name = "RepositoryName"
        make_repository_private(github_token, repo_name)
    except Exception as e:
        print(f"Error: {str(e)}")
