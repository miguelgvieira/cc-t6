from enum import Enum

direction_types = {
    "<": "left",
    ">": "right",
    "<>": "bidirectional"    
}

def pretty_print(dictionary):
    import json
    print(json.dumps(dictionary, indent=4))