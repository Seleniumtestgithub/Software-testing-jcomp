# Create_Repository.py

# Code for creating a new GitHub repository
import requests
from requests.exceptions import RequestException

def create_github_repository(token, repo_name):

    try:
        headers = {"Authorization": f"token {token}"}
        data = {"name": repo_name}
        response = requests.post("https://api.github.com/user/repos", headers=headers, json=data)

        if response.status_code == 201:
            print(f"Repository '{repo_name}' created successfully.")
        else:
            print(f"Failed to create repository. Status code: {response.status_code}")

    except RequestException as e:
        raise Exception(f"Request error: {str(e)}")

if __name__ == '__main__':
    try:
        github_token = "YourGitHubToken"
        repo_name = "NewRepositoryName"
        create_github_repository(github_token, repo_name)
    except Exception as e:
        print(f"Error: {str(e)}")
