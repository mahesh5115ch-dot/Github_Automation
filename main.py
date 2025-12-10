# import os
# import requests

# # GitHub Repository Information
# GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
# REPO = os.getenv('GITHUB_REPOSITORY')
# API_URL = f'https://api.github.com/repos/{REPO}/pulls'

# def get_latest_merged_pr():
#     headers = {'Authorization': f'token {GITHUB_TOKEN}'}
#     params = {'state': 'closed', 'sort': 'updated', 'direction': 'desc'}

#     response = requests.get(API_URL, headers=headers, params=params)
    
#     # Check if the response was successful
#     if response.status_code != 200:
#         print(f"Error fetching PRs: {response.status_code}, {response.text}")
#         return None

#     pr_list = response.json()

#     # Check if the response is a list and find the latest merged PR
#     if isinstance(pr_list, list):
#         for pr in pr_list:
#             if isinstance(pr, dict) and pr.get('merged_at'):
#                 return pr
#     else:
#         print("Unexpected response format:", pr_list)
    
#     return None

# def run_automation(folder):
#     script_path = os.path.join(folder, 'automation_script.py')
#     if os.path.exists(script_path):
#         os.system(f'python {script_path}')
#     else:
#         print(f"No automation script found in {folder}")

# def map_pr_to_folder(pr_title):
#     # This function dynamically maps PR titles to folders
#     # You can customize this function to match your folder naming conventions
#     folder_name = pr_title.lower().replace(' ', '_')  # Example: 'Feature A' becomes 'feature_a'
#     return folder_name

# def main():
#     latest_pr = get_latest_merged_pr()
    
#     if latest_pr:
#         pr_title = latest_pr['title']
#         print(f"Latest merged PR: {pr_title}")

#         folder = map_pr_to_folder(pr_title)
#         run_automation(folder)
#     else:
#         print("No merged PR found.")

# if __name__ == "__main__":
#     main()




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

    if response.status_code != 200:
        print(f"Error fetching PRs: {response.status_code}, {response.text}")
        return None

    pr_list = response.json()

    if isinstance(pr_list, list):
        for pr in pr_list:
            if isinstance(pr, dict) and pr.get('merged_at'):
                return pr
    else:
        print("Unexpected response format:", pr_list)

    return None

def map_pr_to_folder(pr_title):
    # Extract the prefix before any space or extra text
    folder_name = pr_title.split(' ')[0]  # Gets the first word or phrase before space
    # folder_name = folder_name.lower().replace(' ', '_')  # Convert to lowercase and replace spaces with underscores
    folder_name = folder_name.replace(' ', '_') 
    return folder_name

def run_automation(folder):
    script_path = os.path.join(folder, 'automation_script.py')
    if os.path.exists(script_path):
        os.system(f'python {script_path}')
    else:
        print(f"No automation script found in {folder}")

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