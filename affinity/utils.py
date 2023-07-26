"""General purpose utilities"""
import json
import os
from .output_handler import error

def get_data(params):
    """Either loads a file or reads key value pairs from the CLI"""
    if params:
        # If the user passed in a filename statring with *, read from it
        if params.startswith("*"):
            with open(params.replace("*", ""), "r") as f:
                params = json.load(f)
        else:
            # Otherwise read it as key value pairs
            values = params.split(" ")
            params = {}
            for value in values:
                key, v = value.split("=")
                params[key] = v
        return params

def get_files(files):
    """Converts a list of files into a format requests can use"""
    if not files: return
    file_data = []

    for file in files:
        if not os.path.exists(file): error("Could not find file")
        file_data.append(("files", (file, open(file, "rb"))))
    
    return file_data