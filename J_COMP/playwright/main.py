# Driver.py

# Import each scenario and execute them one by one

import login
import signup
import create_repo
import private_repo
import pull_request
import add_collaborator

if __name__ == '__main__':
    # Execute the scenarios one by one
    login.main()
    signup.main()
    create_repo.main()
    private_repo.main()
    pull_request.main()
    add_collaborator.main()
