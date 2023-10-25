# Add_Collaborator.py

# Code for adding a collaborator to a GitHub repository
import requests
from requests.exceptions import RequestException

def add_collaborator(token, repo_name, collaborator_username):
    
    try:
        headers = {"Authorization": f"token {token}"}
        response = requests.put(f"https://api.github.com/repos/YourUsername/{repo_name}/collaborators/{collaborator_username}", headers=headers)

        if response.status_code == 204:
            print(f"{collaborator_username} added as a collaborator to '{repo_name}'.")
        else:
            print(f"Failed to add collaborator. Status code: {response.status_code}")

    except RequestException as e:
        raise Exception(f"Request error: {str(e)}")

if __name__ == '__main__':
    try:
        github_token = "YourGitHubToken"
        repo_name = "RepositoryName"
        collaborator_username = "CollaboratorUsername"
        add_collaborator(github_token, repo_name, collaborator_username)
    except Exception as e:
        print(f"Error: {str(e)}")
