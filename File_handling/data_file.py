from pathlib import Path
from datetime import datetime, timedelta

tezla_path = Path("File_handling/tezla.jpg")

if tezla_path.exists():
    state = tezla_path.stat()

    created_time = state.st_birthtime
    modified_time = state.st_mtime

    # print("Created time:", created_time)
    # print("Modified time:", modified_time)

    created_datetime = datetime.fromtimestamp(created_time)
    modified_datetime = datetime.fromtimestamp(modified_time)
    print("Created time: ", created_datetime)
    print("Modified time: ", modified_datetime)

    day_created = datetime.now() - created_datetime
    day_modified = datetime.now() - modified_datetime

    print("Days since created:", day_created)
    print("Days since modified: ", day_modified)

else:
    print("File not found!")

def get_file_ctime_m_time(day_input: datetime, target_path: Path):
    """ function return lsit od file that  created or modified 
    in specifie date Return list of files Path object
    [(File1, File2, File3)]
    """
    if target_path.exists():
        files = []
        for entry in target_path.iterdir():
            if entry.is_file():
                state = entry.stat()
                created_time = state.st_etime
                modified_time = state.st_mtime
                created_datetime = datetime.fromtimestamp(created_time)
                modified_datetime = datetime.fromtimestamp(modified_time)

                day_created = datetime.now() - created_datetime
                day_modified = datetime.now() - modified_time 

                if day_created >= day_input or day_modified >= day_input:
                    files.append(entry)
            else:
                files += get_file_ctime_m_time(day_input, entry)
        return files       
    else:
        return[]
cwd = Path.cwd()
list_files_greater_3_day = get_file_ctime_m_time(timedelta(days=3), cwd)   
for file in list_files_greater_3_day:
    name = file.name
    created_time = datetime.fromtimestamp(file.stat().st_ctime)
    modified_time = datetime.fromtimestamp(file.stat().st_mtime)
    print(f"File name: {name}, Created time: {created_time}, Modified time: {modified_time}")
