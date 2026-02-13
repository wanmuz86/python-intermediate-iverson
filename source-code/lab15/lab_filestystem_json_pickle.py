from pathlib import Path # To retrieve the path regardless of OS
from utils.file_utils import scan_directory
from utils.json_utils import save_to_json, load_from_json
print("=== Lab: File System + JSON + Pickle ===")


print("\n--- Part 1: Directory Scan ---")
base = Path(".")
# scan the files in the given directory (.)
# list of dict
file_data = scan_directory(base)
# how many files are there?
print("Files found:", len(file_data))
# get the first 2 files
print("Sample:", file_data[:2])

print("\n--- Part 2: JSON Serialization ---")
# filename is files.json
save_to_json(file_data, "files.json")

loaded_json = load_from_json("files.json")
print("Loaded from JSON:", len(loaded_json))

