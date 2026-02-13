import os # To perform os manipulation (read, write, append)


# scan the the given directory
def scan_directory(base_path):
    """
    Scan a directory tree and return file metadata.
    """
    files = []

    # for each of the file in the directory/path (os.walk)
    for root, dirs, filenames in os.walk(base_path):
        for name in filenames:
            # get the path
            full_path = os.path.join(root, name)
            # create a dictionary with the format
            # {"name","fole name", "path": "file path", "size":5kb}
            files.append({
                "name": name,
                "path": full_path,
                # os.path.getsize (return the file size)
                "size": os.path.getsize(full_path)
            })

    return files

