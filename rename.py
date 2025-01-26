import os
import re

def rename_files(folder_path):
    """
    Renames files in a folder to a "Series - S##E### - Episode Title.ext" format.

    Args:
        folder_path: The path to the folder containing the files.
    """
    try:
        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                match = re.search(r"\[DBNL\] (.*?) - (\d+) - (.*?) \[.*?\].*", filename)
                if match:
                    series_name = match.group(1).strip()
                    episode_number = int(match.group(2))
                    episode_title = match.group(3).strip()
                    extension = os.path.splitext(filename)[1] #gets the extension
                    new_filename = f"{series_name} - S01E{episode_number:03} - {episode_title}{extension}"
                    try:
                        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
                        print(f"Renamed '{filename}' to '{new_filename}'")
                    except OSError as e:
                        print(f"Error renaming '{filename}': {e}")
                else:
                    print(f"Skipped '{filename}' as it does not match the expected pattern.")
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
    except NotADirectoryError:
        print(f"Error: '{folder_path}' is not a directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ")
    rename_files(folder_path)
    input("Press Enter to exit.")