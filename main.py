
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



################### Working ###################################

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

# def find_scripts_in_folder(folder):
#     # Check if folder exists
#     if os.path.exists(folder) and os.path.isdir(folder):
#         # List all files and folders in the folder
#         items = os.listdir(folder)
#         for item in items:
#             item_path = os.path.join(folder, item)
#             if os.path.isdir(item_path):
#                 print(f"{item} - Folder")
#             elif item.endswith('.py'):
#                 print(f"{item} - File")
#     else:
#         print(f"{folder} - Folder does not exist")

# def main():
#     latest_pr = get_latest_merged_pr()

#     if latest_pr:
#         pr_title = latest_pr['title']
#         print(f"Latest merged PR: {pr_title}")

#         folder = map_pr_to_folder(pr_title)
#         print(f"Checking folder: {folder}")

#         find_scripts_in_folder(folder)
#     else:
#         print("No merged PR found.")

# if __name__ == "__main__":
#     main()

#############################################################
# import os
# import requests
# import subprocess

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
#     # Extract the folder name from the PR title
#     folder_name = pr_title.split(' ')[0]  # Gets the first word or phrase before space
#     folder_name = folder_name.replace(' ', '_') 
#     return folder_name

# def find_scripts_in_folder(folder):
#     # Check if the folder exists
#     if os.path.exists(folder) and os.path.isdir(folder):
#         items = os.listdir(folder)
#         for item in items:
#             item_path = os.path.join(folder, item)
#             if os.path.isdir(item_path):
#                 print(f"{item} - Folder")
#                 # Check specifically for the 'venv' folder
#                 if item == 'venv':
#                     continue  # Skip printing the venv folder again
#             elif item.endswith('.py'):
#                 print(f"{item} - File")
#     else:
#         print(f"{folder} - Folder does not exist")

# def create_virtual_environment(folder, env_name):
#     # Create a virtual environment in the specified folder
#     env_path = os.path.join(folder, env_name)
#     subprocess.run(['python', '-m', 'venv', env_path], check=True)
#     print(f"Virtual environment '{env_name}' created in '{folder}'.")

# def main():
#     latest_pr = get_latest_merged_pr()
    
#     if latest_pr:
#         pr_title = latest_pr['title']
#         print(f"Latest merged PR: {pr_title}")

#         folder = map_pr_to_folder(pr_title)
#         print(f"Checking folder: {folder}")
        
#         # Only create the virtual environment if the folder exists
#         if os.path.exists(folder):
#             create_virtual_environment(folder, 'venv')
#             find_scripts_in_folder(folder)
#         else:
#             print(f"Folder '{folder}' does not exist. No virtual environment created.")
#     else:
#         print("No merged PR found.")

# if __name__ == "__main__":
#     main()




##################### Working 

# import os
# import requests
# import subprocess

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
#     folder_name = pr_title.split(' ')[0]  # Gets the first word or phrase before space
#     folder_name = folder_name.replace(' ', '_') 
#     return folder_name

# def get_size(path):
#     """Get the size of a file or directory in a human-readable format."""
#     if os.path.isdir(path):
#         total = 0
#         for dirpath, dirnames, filenames in os.walk(path):
#             total += sum(os.path.getsize(os.path.join(dirpath, f)) for f in filenames)
#         return total
#     else:
#         return os.path.getsize(path)

# def format_size(size):
#     """Format size in bytes to a human-readable string."""
#     for unit in ['B', 'Kb', 'Mb', 'Gb']:
#         if size < 1024:
#             return f"{size:.2f} {unit}"
#         size /= 1024
#     return f"{size:.2f} Tb"

# def find_scripts_in_folder(folder):
#     """Find and print files and folders in the specified directory with their sizes."""
#     if os.path.exists(folder) and os.path.isdir(folder):
#         items = os.listdir(folder)
#         for item in items:
#             item_path = os.path.join(folder, item)
#             item_size = get_size(item_path)

#             if os.path.isdir(item_path):
#                 print(f"{item:<15} - Folder     - {format_size(item_size)}")
#                 if item == 'venv':
#                     continue  # Skip printing the venv folder again
#             elif item.endswith('.py'):
#                 print(f"{item:<15} - File       - {format_size(item_size)}")
#     else:
#         print(f"{folder} - Folder does not exist")

# def create_virtual_environment(folder, env_name):
#     """Create a virtual environment in the specified folder."""
#     env_path = os.path.join(folder, env_name)
#     subprocess.run(['python', '-m', 'venv', env_path], check=True)
#     print(f"Virtual environment '{env_name}' created in '{folder}'.")

# def main():
#     latest_pr = get_latest_merged_pr()
    
#     if latest_pr:
#         pr_title = latest_pr['title']
#         print(f"Latest merged PR: {pr_title}")

#         folder = map_pr_to_folder(pr_title)
#         print(f"Checking folder: {folder}")
        
#         # Only create the virtual environment if the folder exists
#         if os.path.exists(folder):
#             create_virtual_environment(folder, 'venv')
#             find_scripts_in_folder(folder)
#         else:
#             print(f"Folder '{folder}' does not exist. No virtual environment created.")
#     else:
#         print("No merged PR found.")

# if __name__ == "__main__":
#     main()



############# working #######################

# import os
# import requests
# import subprocess

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
#     folder_name = pr_title.split(' ')[0]  # Gets the first word or phrase before space
#     folder_name = folder_name.replace(' ', '_') 
#     return folder_name

# def get_size(path):
#     """Get the size of a file or directory in a human-readable format."""
#     if os.path.isdir(path):
#         total = 0
#         for dirpath, dirnames, filenames in os.walk(path):
#             total += sum(os.path.getsize(os.path.join(dirpath, f)) for f in filenames)
#         return total
#     else:
#         return os.path.getsize(path)

# def format_size(size):
#     """Format size in bytes to a human-readable string."""
#     for unit in ['B', 'Kb', 'Mb', 'Gb']:
#         if size < 1024:
#             return f"{size:.2f} {unit}"
#         size /= 1024
#     return f"{size:.2f} Tb"

# def find_scripts_in_folder(folder):
#     """Find and print files and folders in the specified directory with their sizes."""
#     requirements_found = False
#     if os.path.exists(folder) and os.path.isdir(folder):
#         items = os.listdir(folder)
#         for item in items:
#             item_path = os.path.join(folder, item)
#             item_size = get_size(item_path)

#             if os.path.isdir(item_path):
#                 print(f"{item:<15} - Folder     - {format_size(item_size)}")
#                 if item == 'venv':
#                     continue  # Skip printing the venv folder again
#             elif item.endswith('.py'):
#                 print(f"{item:<15} - File       - {format_size(item_size)}")
#             elif item == 'requirements.txt':
#                 requirements_found = True  # Found requirements.txt
#                 print(f"{item:<15} - File       - {format_size(item_size)}")  # Print requirements.txt

#         return requirements_found  # Return True if requirements.txt is found
#     else:
#         print(f"{folder} - Folder does not exist")
#         return False

# def create_virtual_environment(folder, env_name):
#     """Create a virtual environment in the specified folder."""
#     env_path = os.path.join(folder, env_name)
#     subprocess.run(['python', '-m', 'venv', env_path], check=True)
#     print(f"Virtual environment '{env_name}' created in '{folder}'.")

# def install_requirements(folder):
#     """Install requirements from requirements.txt if it exists."""
#     requirements_path = os.path.join(folder, 'requirements.txt')
#     env_path = os.path.join(folder, 'venv', 'Scripts' if os.name == 'nt' else 'bin', 'pip')
    
#     if os.path.exists(requirements_path):
#         subprocess.run([env_path, 'install', '-r', requirements_path], check=True)
#         print("Requirements installed from requirements.txt.")
#     else:
#         print("No requirements.txt file found in the directory.")

# def main():
#     latest_pr = get_latest_merged_pr()
    
#     if latest_pr:
#         pr_title = latest_pr['title']
#         print(f"Latest merged PR: {pr_title}")

#         folder = map_pr_to_folder(pr_title)
#         print(f"Checking folder: {folder}")
        
#         if os.path.exists(folder):
#             create_virtual_environment(folder, 'venv')
#             if find_scripts_in_folder(folder):
#                 install_requirements(folder)
#             else:
#                 print("No relevant files found in the directory.")
#         else:
#             print(f"Folder '{folder}' does not exist. No virtual environment created.")
#     else:
#         print("No merged PR found.")

# if __name__ == "__main__":
#     main()


#######################

import os
import requests
import subprocess

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
    folder_name = pr_title.split(' ')[0]  # Gets the first word or phrase before space
    folder_name = folder_name.replace(' ', '_') 
    return folder_name

def get_size(path):
    """Get the size of a file or directory in a human-readable format."""
    if os.path.isdir(path):
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            total += sum(os.path.getsize(os.path.join(dirpath, f)) for f in filenames)
        return total
    else:
        return os.path.getsize(path)

def format_size(size):
    """Format size in bytes to a human-readable string."""
    for unit in ['B', 'Kb', 'Mb', 'Gb']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} Tb"

def find_scripts_in_folder(folder):
    """Find and print files and folders in the specified directory with their sizes."""
    requirements_found = False
    if os.path.exists(folder) and os.path.isdir(folder):
        items = os.listdir(folder)
        for item in items:
            item_path = os.path.join(folder, item)
            item_size = get_size(item_path)

            if os.path.isdir(item_path):
                print(f"{item:<15} - Folder     - {format_size(item_size)}")
                if item == 'venv':
                    continue  # Skip printing the venv folder again
            elif item.endswith('.py'):
                print(f"{item:<15} - File       - {format_size(item_size)}")
            elif item == 'requirements.txt':
                requirements_found = True  # Found requirements.txt
                print(f"{item:<15} - File       - {format_size(item_size)}")  # Print requirements.txt

        return requirements_found  # Return True if requirements.txt is found
    else:
        print(f"{folder} - Folder does not exist")
        return False

def create_virtual_environment(folder, env_name):
    """Create a virtual environment in the specified folder."""
    env_path = os.path.join(folder, env_name)
    subprocess.run(['python', '-m', 'venv', env_path], check=True)
    print(f"Virtual environment '{env_name}' created in '{folder}'.")

def install_requirements(folder):
    """Install requirements from requirements.txt if it exists."""
    requirements_path = os.path.join(folder, 'requirements.txt')
    env_path = os.path.join(folder, 'venv', 'Scripts' if os.name == 'nt' else 'bin', 'pip')
    
    if os.path.exists(requirements_path):
        subprocess.run([env_path, 'install', '-r', requirements_path], check=True)
        print("Requirements installed from requirements.txt.")
        
        # Print the size of the venv folder after installation
        venv_size = get_size(os.path.join(folder, 'venv'))
        print(f"Size of venv after installing requirements: {format_size(venv_size)}")
    else:
        print("No requirements.txt file found in the directory.")

def main():
    latest_pr = get_latest_merged_pr()
    
    if latest_pr:
        pr_title = latest_pr['title']
        print(f"Latest merged PR: {pr_title}")

        folder = map_pr_to_folder(pr_title)
        print(f"Checking folder: {folder}")
        
        if os.path.exists(folder):
            create_virtual_environment(folder, 'venv')
            if find_scripts_in_folder(folder):
                install_requirements(folder)
            else:
                print("No relevant files found in the directory.")
        else:
            print(f"Folder '{folder}' does not exist. No virtual environment created.")
    else:
        print("No merged PR found.")

if __name__ == "__main__":
    main()