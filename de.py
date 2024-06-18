import os
from pathlib import Path

# Path to your desktop
desktop_path = Path.home() / 'Desktop'

# Loop through all files on the desktop
for file in desktop_path.glob('*.*'):
    if file.is_file():
        # Get the file extension and create a custom folder name
        extension = file.suffix[1:].lower()
        if extension in ['jpg', 'png', 'jpeg', 'psd']:
            folder_name = 'Images'
        elif extension in ['docx', 'pdf']:
            folder_name = 'Documents'
        elif extension in ['mp4', 'mkv']:
            folder_name = 'Videos'
        elif extension in ['mp3']:
            folder_name = 'Audio'
        elif extension in ['py', 'php','exe','c++','html','js']:
            folder_name = 'Code'
        # Add more conditions for other file types as needed
        else:
            folder_name = 'Other Files'

        # Create the folder if it does not exist
        folder_path = desktop_path / folder_name
        folder_path.mkdir(exist_ok=True)
        
        # Move the file into the corresponding folder
        file.rename(folder_path / file.name)

print('Desktop organized!')
