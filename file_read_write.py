import json
import os

def read_write_command(com):
    filename = "history.json"
    file_data = {}

    try:
        with open(filename, "r") as file:
            file_data = json.load(file)
    except :
        pass

    file_data = {2:com}

    with open(filename, "w") as file:
        json.dump(file_data, file, indent = 4)

def delete():
    os.remove("history.json")