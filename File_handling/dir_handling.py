from pathlib import Path
cwd = Path.cwd()
dir_path = Path("File_handling")
total_size = 0
# if dir_path.exists():
#     print("Directory name:", dir_path.name)
#     for entry in dir_path.iterdir():
#         if entry.is_file():
#             total_size += entry.stat().st_size
#         else:
#             for sub_entry in entry.iterdir():
#                 if sub_entry.is_file():
#                     total_size += sub_entry.stat().st_size

# else:
#     print("Directory not found!")

# Create recursive function to get total size of a directory
def get_total_size(dir_path) -> int:
    total_size = 0
    if dir_path.exists():
        for entry in dir_path.iterdir():
            if entry.is_file():
                total_size += entry.stat().st_size
                if(entry.name == "password.txt"):
                    print("File name:", entry.name)
                    with open(entry, "r") as read_file:
                        print("File content:", read_file.read())
                    
            else:
                
                total_size += get_total_size(entry)
    
    return total_size
                
total_size = get_total_size(cwd)

kb = 1000
mb = kb*1000
gb = mb*1000

kb_size = total_size/kb
mb_size = total_size/mb
gb_size = total_size/gb

print("Total size (bytes):", total_size)
print ("Total size (KB):", kb_size)
print ("Total size (MB):", mb_size)
print ("Total size (GB):", gb_size)
