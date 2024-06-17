from pathlib import Path
image_path = Path("c:/Users/Maha Ahsla/Pictures/Saved Pictures/b4cf1efcecf26a5ce6b70d116e98f6f6.jpg")
target_path = Path.cwd() / "File_handling"

with open(image_path, "rb") as read_file:
    image = read_file.read()
    print(image)

with open(target_path / "tezla.jpg", "wb") as write_file:
    write_file.write(image)