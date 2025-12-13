import os
import sys

def list_directory_contents(path="."):
    """
    Prints the contents (files and subdirectories) of the given path.

    :param path: The directory path to list. Defaults to the current directory (.).
    """
    try:
        # 1. Get the list of all entries (files and directories)
        entries = os.listdir(path)

        # 2. Print the results
        print(f"Directory Contents of: **{os.path.abspath(path)}**\n")
        
        if not entries:
            print("(The directory is empty.)")
            return

        print("--- Entries ---")
        for entry in entries:
            # Check if the entry is a directory or a file for better presentation
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

# --- Example Usage ---

# 1. List the contents of the current working directory
print("Listing current directory:")
list_directory_contents()

# 2. (Optional) List a specific directory, e.g., the parent directory
# list_directory_contents("..")

# 3. (Optional) List a directory you know exists on your system
# list_directory_contents("/Users/YourName/Documents/my_project")