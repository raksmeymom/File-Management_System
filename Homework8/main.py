from pathlib import Path
from datetime import datetime, timedelta

def back_files(source_dir: Path, input_days: timedelta, target_dir: Path):
    """ Function to back-up files from source directory to target directory.
    `source_dir`: this is the source directory where the files are located.
    `input_dir`: this is the number of days to chck if the files are older. 
    `target_dir`: this is the target directory where the files will be  back-up.
    """
    try:
        if source_dir.exists():
            target_dir.mkdir(parents=True, exist_ok=True)
            for entry in source_dir.iterdir():
                if entry.is_file():
                    file_state = entry.stat()
                    created_time = file_state.st_ctime
                    created_datetime = datetime.fromtimestamp(created_time)
                    day_created = datetime.now() - created_datetime
                    if day_created >= input_days:
                         with open(entry, 'rb') as file:
                              with open(target_dir / entry.name, 'wb') as target_file:
                                   target_dir.write(file.read())
            
            else: 
                 back_files(entry, input_days, target_dir)
        else:
            print(f"Source directory{source_dir} does not exist.")
    except Exception as e:
            pass
back_files(Path.cwd(), timedelta(days=7), Path.cwd() / 'backup')


def delete_files(source_dir: Path, file_names: str):
    try:
        if source_dir.exists():
               for entry in source_dir.iterdir():
                    if entry.is_file():
                        if file_names in entry.name:
                              print("Are you sure you want to delete the file? (y/n):")
                              print(entry)
                              opts = input("Enter your choice (y/n):")
                              if opts.lower() == 'y':
                                   entry.unlink()
                              else:
                                   print("File not deleted.")
                                

                    else:
                         delete_files(entry, file_names)
        else:
                print(f"Source directory{source_dir} does not exist.")
    except Exception:
         pass
delete_files(Path.cwd(), 'password')


# list_files = []
# def delete_files_all(source_dir: Path, file_names: str):
#     list_files: list[Path] = []
#     try:
#         if source_dir.exists():
#                for entry in source_dir.iterdir():
#                     if entry.is_file():
#                         if file_names in entry.name:
#                               list_files.append(entry)
                             
#                         else:
#                             list_files.extend (delete_files_all(entry, file_names))
                        
#         else:
#             print(f"Source directory{source_dir} does not exist.")
#         return list_files
       
#     except Exception:
#          pass
# list_files = delete_files_all(Path.cwd(), 'Restau')
# if list_files:
#     for index,file in enumerate(list_files):
#         print(f"{index+1}. {file}")
#         print("Are you sure you want to delete the files? (y/n): ")
#         opts = input("Enter your choice (y/n): ")
#         if opts.lower() == 'y':
#             for file in list_files:
#                 file.unlink()
#         else:
#             print("File not deleted.")
# delete_files_all(Path.cwd(), 'Restau')



def search_file_by_name(source_dir: Path, file_names: str):
    try:
        if source_dir.exists():
               for entry in source_dir.iterdir():
                    if entry.is_file():
                         print(entry)
                       

                    else:
                         search_file_by_name(entry, file_names)
        else:
                print(f"Source directory{source_dir} does not exist.")
    except Exception:
         pass
search_file_by_name(Path.cwd(), 'copy')




         
         

            
                        
           