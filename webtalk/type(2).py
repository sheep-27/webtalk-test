while True:
    new_text = input()

    with open(r"C:\Users\jhoward\Documents\programming\webtalk\see.html", "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if "<h4>computer b:" in lines[i]:
            lines[i] = f"<h4>computer b: {new_text}</h4>\n"

    with open(r"C:\Users\jhoward\Documents\programming\webtalk\see.html", "w") as file:
        file.writelines(lines)

# use this code instead if using one drive lets coputers tlk throw the cloud
'''
import os

def find_onedrive():
    home = os.path.expanduser("~")
    for folder in os.listdir(home):
        if folder.startswith("OneDrive"):
            full_path = os.path.join(home, folder)
            if os.path.isdir(full_path):
                return full_path
    return None

onedrive = find_onedrive()
if not onedrive:
    print("Could not find OneDrive folder.")
    exit()

file_path = os.path.join(
    onedrive, "Documents", "programming", "webtalk", "see.html"
)

print("Using file:", file_path)

while True:
    new_text = input("Computer B says: ")

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if "<h4>computer b:" in lines[i]:
            lines[i] = f"<h4>computer b: {new_text}</h4>\n"

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print("Updated Computer B section!")

'''