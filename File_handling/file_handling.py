from pathlib import Path

cwd = Path.cwd()
new_file =  cwd / 'File_handling_new' / "new_floder" / 'new_file.txt'

# new_file.touch()

# try:
#     new_file.touch()
# except Exception as error:
#     print("File Error: {error}")
#     new_file.parent.mkdir(exist_ok=True)
#     new_file.touch()


new_file.parent.mkdir(parents=True, exist_ok=True)
new_file.touch()

with open(new_file, 'w') as file:
    text = "Hello, pathlib!"
    file.write(text)

new_rename_path = cwd / new_file.parent / "new_file_renamed_new.txt"



try:
    new_file.rename(new_rename_path)

except Exception :
    pass

new_delete_path = cwd / "new_delete_folder" / "new_delete_file.txt"
new_delete_path.unlink(missing_ok=True)