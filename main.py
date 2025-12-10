import os
import requests

# GitHub Repository Information
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO = os.getenv('GITHUB_REPOSITORY')
API_URL = f'https://api.github.com/repos/{REPO}/pulls'

def get_latest_merged_pr():
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    params = {'state': 'closed', 'sort': 'updated', 'direction': 'desc'}
    
    response = requests.get(API_URL, headers=headers, params=params)
    pr_list = response.json()
    
    # Find the latest merged PR
    for pr in pr_list:
        if pr.get('merged_at'):
            return pr
    return None

def run_automation(folder):
    script_path = os.path.join(folder, 'automation_script.py')
    if os.path.exists(script_path):
        os.system(f'python {script_path}')
    else:
        print(f"No automation script found in {folder}")

def map_pr_to_folder(pr_title):
    # This function dynamically maps PR titles to folders
    # You can customize this function to match your folder naming conventions
    folder_name = pr_title.lower().replace(' ', '_')  # Example: 'Feature A' becomes 'feature_a'
    return folder_name

def main():
    latest_pr = get_latest_merged_pr()
    
    if latest_pr:
        pr_title = latest_pr['title']
        print(f"Latest merged PR: {pr_title}")

        folder = map_pr_to_folder(pr_title)
        run_automation(folder)
    else:
        print("No merged PR found.")

if __name__ == "__main__":
    main()