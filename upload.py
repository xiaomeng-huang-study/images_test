import os
import subprocess
import datetime
import pyperclip
import time

# Find the latest file in the current directory
files = [f for f in os.listdir() if f.startswith("Scrennshot")]
if not files:
    print("No files matching the criteria found. Program exiting.")
    exit()

# Get the latest modified file
latest_file = max(files, key=lambda f: os.path.getmtime(f))

# Execute git commands
try:
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "add", "."])

    # Extract the part of the filename excluding "Scrennshot_" as variable time_edited
    time_edited = latest_file.replace("Scrennshot_", "").replace(".png", "")

    commit_message = f"edited with autoscript at {time_edited}"
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push"])
    subprocess.run(["git", "pull"])

except Exception as e:
    print(f"Error occurred while executing git commands: {e}")
    exit()

# Form the string
current_directory = os.path.basename(os.getcwd())
# github_url = f"https://github.com/ICH-BIN-HXM/{current_directory}/blob/main/{latest_file}?raw="
github_url = f'<img src="https://github.com/ICH-BIN-HXM/{current_directory}/blob/main/{latest_file}?raw=" width="400" /> '

# Copy to clipboard
pyperclip.copy(github_url)

print(f"Generated GitHub link has been copied to the clipboard: {github_url}")

# Delay of 2 seconds 
time.sleep(2)

# Exit the program
exit()
