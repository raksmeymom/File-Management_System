from pathlib import Path

cwd = Path.cwd()
print(cwd)
new_folder = cwd / "File_handling_new" / 'new_folder2'
new_folder.mkdir(parents=True, exist_ok=True)

new_file = Path.joinpath(new_folder, "File1_txt")
new_file.touch()

 