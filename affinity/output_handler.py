"""Class to handle the output of the request result"""
from requests import Response
from requests.exceptions import JSONDecodeError
from rich.pretty import pprint
from rich.console import Console

class OutputHandler:
    def __init__(self, response:Response):
        self.con = Console()
        self.response:Response = response
        self.print_status()
        try:
            self.text = self.response.json()
        except JSONDecodeError:
            self.text = self.response.text
        
    def print_status(self):
        """Prints the result of the request"""
        code = self.response.status_code
        # The request had an informational response
        if code >= 100 and code < 199:
            self.con.print(f"[white]{code} {self.response.request.method} {self.response.url}[/white]")
        # The request was succesful
        elif code >= 200 and code < 299:
            self.con.print(f"[green]{code} {self.response.request.method} {self.response.url}[/green]")
        # The request got redirected
        elif code >= 300 and code < 399:
            self.con.print(f"[yellow]{code} {self.response.request.method} {self.response.url}[/yellow]")
        # Client Error
        elif code >= 400 and code < 499:
            self.con.print(f"[red]{code} {self.response.request.method} {self.response.url}[/red]")
        # Server Error
        elif code >= 500 and code < 599:
            self.con.print(f"[bright-red]{code} {self.response.request.method} {self.response.url}[/bright-red]")

    def print_result(self):
        """Prints the result of the response to the stdout. Tries to serialize the text into a dict but if it failes it will just print it as normal text"""
        pprint(self.text)
        
    def write_to_file(self, file_name:str, binary:bool):
        """Writes the response's data to a file"""
        if binary:
            with open(file_name, "wb") as f:
                f.write(self.response.content)
        else:
            with open(file_name, "w") as f:
                f.write(self.text)
