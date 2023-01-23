"""Handles outputting the data recieved"""

from rich.pretty import pprint
from requests import Response

def write_output(data:Response, output:bool, json:bool, file:str=None):
    if file != None:
        with open(file, "w") as f:
            f.write(data.text)
    if output:
        if json:
            pprint(data.json())
        else:
            pprint(data.text)