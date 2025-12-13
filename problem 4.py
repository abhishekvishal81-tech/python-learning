import os

def list_directory(path='.'):
    """
    Print the contents of the directory given by path.
    If no path is provided, it lists the current working directory.
    """
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage — replace '.' with any directory path you like
    list_directory('.')
