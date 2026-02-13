import json

def save_to_json(data, filename):
    # what is open? all the different modes
    # Open the file in write mode, utf-8 encoding
    # json.dump -> write the entire json in the file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_from_json(filename):
    # Open the file in read mode
    # retrieve all the json from the file
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


#look for example write in .txt