# levels/__init__.py
import json

def load_level(path):
    """
    Given an absolute path (or relative) to a JSON file,
    load it and return the parsed dict.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
