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

#     if response.status_code != 200:
#         print(f"Error fetching PRs: {response.status_code}, {response.text}")
#         return None

#     pr_list = response.json()

#     if isinstance(pr_list, list):
#         for pr in pr_list:
#             if isinstance(pr, dict) and pr.get('merged_at'):
#                 return pr
#     else:
#         print("Unexpected response format:", pr_list)

#     return None

# def map_pr_to_folder(pr_title):
#     # Extract the prefix before any space or extra text
#     folder_name = pr_title.split(' ')[0]  # Gets the first word or phrase before space
#     # folder_name = folder_name.lower().replace(' ', '_')  # Convert to lowercase and replace spaces with underscores
#     folder_name = folder_name.replace(' ', '_') 
#     return folder_name

# def run_automation(folder):
#     script_path = os.path.join(folder, 'automation_script.py')
#     if os.path.exists(script_path):
#         os.system(f'python {script_path}')
#     else:
#         print(f"No automation script found in {folder}")

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

#################################################################

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

#     if response.status_code != 200:
#         print(f"Error fetching PRs: {response.status_code}, {response.text}")
#         return None

#     pr_list = response.json()

#     if isinstance(pr_list, list):
#         for pr in pr_list:
#             if isinstance(pr, dict) and pr.get('merged_at'):
#                 return pr
#     else:
#         print("Unexpected response format:", pr_list)

#     return None


# def map_pr_to_folder(pr_title):
#     # Extract the prefix before any space or extra text
#     folder_name = pr_title.split(' ')[0]  # Gets the first word or phrase before space
#     folder_name = folder_name.replace(' ', '_') 
#     return folder_name

# def find_script_in_folder(folder):
#     # Check if folder exists
#     if os.path.exists(folder) and os.path.isdir(folder):
#         # List all files in the folder
#         for filename in os.listdir(folder):
#             if filename.endswith('.py'):  # Looking for Python scripts only
#                 return os.path.join(folder, filename)  # Return the first Python script found
#     return None

# def main():
#     latest_pr = get_latest_merged_pr()

#     if latest_pr:
#         pr_title = latest_pr['title']
#         print(f"Latest merged PR: {pr_title}")

#         folder = map_pr_to_folder(pr_title)
#         script_to_run = find_script_in_folder(folder)

#         if script_to_run:
#             print(f"Running script: {script_to_run}")
#             os.system(f'python {script_to_run}')
#         else:
#             print(f"No automation script found in {folder}")
#     else:
#         print("No merged PR found.")

# if __name__ == "__main__":
#     main()



######################################################

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
    folder_name = folder_name.replace(' ', '_') 
    return folder_name

def find_scripts_in_folder(folder):
    # Check if folder exists
    if os.path.exists(folder) and os.path.isdir(folder):
        # List all files and folders in the folder
        items = os.listdir(folder)
        for item in items:
            item_path = os.path.join(folder, item)
            if os.path.isdir(item_path):
                print(f"{item} - Folder")
            elif item.endswith('.py'):
                print(f"{item} - File")
    else:
        print(f"{folder} - Folder does not exist")

def main():
    latest_pr = get_latest_merged_pr()

    if latest_pr:
        pr_title = latest_pr['title']
        print(f"Latest merged PR: {pr_title}")

        folder = map_pr_to_folder(pr_title)
        print(f"Checking folder: {folder}")

        find_scripts_in_folder(folder)
    else:
        print("No merged PR found.")

if __name__ == "__main__":
    main()