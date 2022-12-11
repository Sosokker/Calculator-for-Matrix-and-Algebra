import json
from json import JSONDecodeError
import os

def write_command(com, inp, out) -> None:
    filename = "history.json"
    try:
        with open(filename, "r") as file:
            number_dict = json.load(file)
        with open(filename, "w") as file1:
            lastest = 0
            for key in number_dict.keys():
                if int(key) >= int(lastest):
                    lastest = int(key)
            data = {}
            data["command"] = com
            data["input"] = inp
            data["output"] = out
            number_dict[lastest+1] = data
            json.dump(number_dict, file1, indent=4)
    except FileNotFoundError:
        data = {}
        number_dict = {}
        # {command: , input: , output}
        with open(filename, "w+") as file:
            data["command"] = com
            data["input"] = inp
            data["output"] = out
            number_dict[1] = data
            json.dump(number_dict, file, indent=4)

def clear() -> bool:
    filename = "history.json"
    try:
        open(filename, 'w').close()
        return True
    except FileNotFoundError:
        return False

def delete() -> bool:
    try:
        os.remove("history.json")
        return True
    except:
        return False

def read_history():
    filename = "history.json"
    try:
        with open(filename, "r") as file:
            number_dict = json.load(file)
            for line, data in number_dict.items():
                print(f"    ({line}) Command: {data['command']} | Input: {data['input']} | Output: {data['output']}")
    except FileNotFoundError:
        raise FileNotFoundError("History file not found! Maybe program hasn't been saved yet.")
    except JSONDecodeError:
        print("History is empty.")