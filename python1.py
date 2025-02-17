import requests

# GitHub organization and repository name
ORG_NAME = 'python-script12'  # Your GitHub organization name
REPO_NAME = 'simple'          # Your GitHub repository name (remove the '.git')
GITHUB_TOKEN = ''  # Your updated GitHub personal access token

# GitHub API base URL
GITHUB_API_URL = 'https://api.github.com'

# Function to get collaborators
def get_collaborators():
    url = f'{GITHUB_API_URL}/repos/{ORG_NAME}/{REPO_NAME}/collaborators'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        collaborators = response.json()
        print(f'Collaborators with access to {REPO_NAME}:')
        for collaborator in collaborators:
            print(collaborator['login'])
    else:
        print(f'Failed to fetch collaborators: {response.status_code}, {response.text}')

# Function to get teams
def get_teams():
    url = f'{GITHUB_API_URL}/orgs/{ORG_NAME}/teams'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        teams = response.json()
        print(f'Teams with access to {REPO_NAME}:')
        for team in teams:
            print(team['name'])
    else:
        print(f'Failed to fetch teams: {response.status_code}, {response.text}')

# Main function
def main():
    get_collaborators()
    print()  # Just a newline for better readability
    get_teams()

if __name__ == '__main__':
    main()
