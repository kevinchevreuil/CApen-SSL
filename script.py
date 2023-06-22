import os

def add_gitkeep(folder):
    gitkeep_path = os.path.join(folder, '.gitkeep')

    # Check if the folder is empty
    if not os.listdir(folder):
        # Check if .gitkeep file doesn't exist already
        if not os.path.exists(gitkeep_path):
            # Create the .gitkeep file
            with open(gitkeep_path, 'w'):
                pass
            print(f'.gitkeep added to {folder}')
        else:
            print(f'{gitkeep_path} already exists in {folder}')
    else:
        print(f'{folder} is not empty')

def add_gitkeep_recursive(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for d in dirs:
            folder_path = os.path.join(root, d)
            add_gitkeep(folder_path)

# Provide the root folder path here
root_folder = './'

add_gitkeep_recursive(root_folder)

