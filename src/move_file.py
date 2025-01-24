import shutil

def move_file(source:str, destination:str):
    # Move the file
    try:
        shutil.move(source, destination)
        # print(f"File moved successfully to {destination}")
    except FileNotFoundError:
        print(f"The file {source} does not exist.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")
