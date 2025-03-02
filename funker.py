import shutil
import os
import random
import string
import re
import datetime
import math

def copy_file(source_file, destination_folder):
    """
    Copy file to destanation folder

    :param source_file: Filename with path to copy
    :param destination_folder: Destanation folder
    """
    if not os.path.isfile(source_file):
        print(f"File {source_file} not found")
        return

    if not os.path.isdir(destination_folder):
        print(f"Folder {destination_folder} not found")
        return

    try:
        shutil.copy(source_file, destination_folder)
        print(f"File {source_file} copied to {destination_folder}.")
    except Exception as e:
        print(f"Error copying file: {e}")

def delete_file(file_path):
    """
    Delete file

    :param file_path: The full path of the file to delete
    """
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist")
        return

    try:
        os.remove(file_path)
        print(f"File {file_path} has been successfully deleted")
    except Exception as e:
        print(f"Error deleting file: {e}")

def count_files(folder, recursive=False):
    """
    Counts the number of files in the specified folder.

    :param folder: The folder to count files in.
    :param recursive: Whether to count files recursively.
    :return: The number of files.
    """
    if not os.path.isdir(folder):
        print(f"Folder {folder} does not exist.")
        return

    file_count = 0
    for root, dirs, files in os.walk(folder):
        file_count += len(files)
        if not recursive:
            break

    return file_count

def search_files(folder, pattern):
    """
    Searches for files in the specified folder that match the given regex pattern.

    :param folder: The folder to search in.
    :param pattern: The regex pattern to match file names.
    """
    if not os.path.isdir(folder):
        print(f"Folder {folder} does not exist.")
        return

    regex = re.compile(pattern)
    matched_files = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if regex.search(file):
                matched_files.append(os.path.join(root, file))

    if matched_files:
        print(f"Found {len(matched_files)} files matching pattern '{pattern}':")
        for file in matched_files:
            print(file)
        return matched_files
    else:
        print(f"No files matching pattern '{pattern}' found in {folder}.")
        return None

def add_creation_date_to_filename(folder, recursive=False):
    """
    Adds the creation date to the filenames in the specified folder.

    :param folder: The folder to process.
    :param recursive: Whether to process files recursively.
    """
    if not os.path.isdir(folder):
        print(f"Folder {folder} does not exist.")
        return

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            creation_time = os.path.getctime(file_path)
            creation_date = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
            new_file_name = f"{creation_date}_{file}"
            new_file_path = os.path.join(root, new_file_name)
            os.rename(file_path, new_file_path)
            print(f"Renamed {file_path} to {new_file_path}")

        if not recursive:
            break # Only analyse the top level if not recursive

def analyse_folder(folder):
    """
    Analyses the specified folder and prints the sizes of all files and subfolders.

    :param folder: The folder to analyse.
    """
    if not os.path.isdir(folder):
        print(f"Folder {folder} does not exist.")
        return

    total_size = 0
    sizes = []

    for root, dirs, files in os.walk(folder):
        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            total_size += file_size
            sizes.append((file_path, file_size))

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size = get_folder_size(dir_path)
            total_size += dir_size
            sizes.append((dir_path, dir_size))

        break  # Only analyse the top level

    print(f"Full size: {format_size(total_size)}")
    for path, size in sizes:
        print(f"  - {os.path.basename(path)} {format_size(size)}")

def get_folder_size(folder):
    """
    Gets the total size of the specified folder.

    :param folder: The folder to get the size of.
    :return: The total size of the folder in bytes.
    """
    total_size = 0
    for root, dirs, files in os.walk(folder):
        for name in files:
            file_path = os.path.join(root, name)
            total_size += os.path.getsize(file_path)
    return total_size

def format_size(size_bytes):
    """
    Formats the size in bytes to a human-readable string.

    :param size_bytes: The size in bytes.
    :return: The formatted size string.
    """
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def generate_random_content(size_kb):
    """
    Generates random content of the specified size in kilobytes.

    :param size_kb: Size of the content in kilobytes.
    :return: Random content as a string.
    """
    size_bytes = size_kb * 1024
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size_bytes))

def generate_data(destination_folder, count):
    """
    * For testing purposes *
    Generates test data - <count> number of folders with
    <count>*files in each folder<count>
    Regenerates a folder content if exists

    :param destination_folder: Destanation folder
    :param count: Number of folders to create
    """
    if destination_folder == "":
        print(f"Directory not set")
        return

    if os.path.exists(destination_folder):
        print(f"Test directory already exists, removing...")
        shutil.rmtree(destination_folder)

    os.makedirs(destination_folder)

    for i in range(1, count + 1):
        folder_name = os.path.join(destination_folder, f"folder{i}")
        os.mkdir(folder_name)

        for j in range(1, i + 1):
            file_name = os.path.join(folder_name, f"file{j}.txt")
            file_size_kb = 100 * j
            content = generate_random_content(file_size_kb)

            with open(file_name, 'w') as file:
                file.write(content)

    print(f"Created total {count_files(destination_folder, recursive=True)} files in {count} folders")
