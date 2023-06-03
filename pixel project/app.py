from utils import show_picture
import os

folder_path = "files"

files = os.listdir(folder_path)

for i, file in enumerate(files):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") :
        print(f"{i+1}. {file}")

choice = int(input("Which image would you like to choose? Enter the corresponding number: "))

choice = 0
while choice < 1 or choice > len(files):
    choice = int(input("Which image would you like to choose? Enter the corresponding number: "))
    if choice >= 1 and choice <= len(files):
        break
    print(f'You have to choose a number between 1 and {len(files)}')

chosen_picture = files[choice-1]
print(f"You chose: {chosen_picture}")

show_picture(chosen_picture)