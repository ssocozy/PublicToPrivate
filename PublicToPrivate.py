import requests

# Replace these values with your GitHub username and personal access token
username = "" 
token = ""

print(f'Created by cozy')
# Get the list of repositories
response = requests.get(f"https://api.github.com/users/{username}/repos", auth=(username, token))

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        if not repo['private']:
            # Update the repository to be private
            repo_name = repo['name']
            update_response = requests.patch(
                f"https://api.github.com/repos/{username}/{repo_name}",
                json={"private": True},
                auth=(username, token)
            )
            
            if update_response.status_code == 200:
                print(f"Repository '{repo_name}' updated to private.")
            else:
                print(f"Failed to update repository '{repo_name}'.")
else:
    print("Failed to fetch repositories.")


