import os
import sys

# select the directory whose content you want to list
def list_directory_contents(path="."):
    try:
        entries = os.listdir(path)

        print(f"Directory Contents of: **{os.path.abspath(path)}**\n")
        
        if not entries:
            print("(The directory is empty.)")
            return

        print("--- Entries ---")
        for entry in entries:
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                print(f"**[DIR]** {entry}")
            else:
                print(f"    [FILE] {entry}")
        print("---------------")

    except FileNotFoundError:
        print(f"Error: Directory not found at path: {path}")
    except PermissionError:
        print(f"Error: Permission denied to access directory: {path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print("Listing current directory:")
list_directory_contents()