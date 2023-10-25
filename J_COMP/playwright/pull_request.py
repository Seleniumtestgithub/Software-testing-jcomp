# Create_Pull_Request.py

# Code for creating a GitHub pull request
import subprocess
from subprocess import CalledProcessError

def create_pull_request():

    try:
        subprocess.run(["git", "checkout", "-b", "feature-branch"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Adding new feature"])
        subprocess.run(["git", "push", "origin", "feature-branch"])
        subprocess.run(["gh", "pr", "create", "--base", "main", "--head", "feature-branch"])

        print("Pull request created successfully!")

    except CalledProcessError as e:
        raise Exception(f"Error running Git or GitHub CLI: {str(e)}")

if __name__ == '__main__':
    try:
        create_pull_request()
    except Exception as e:
        print(f"Error: {str(e)}")
