"""Function to handle the actual HTTP request"""
import requests
from rich.console import Console

def handle_request(url:str, request_type:str, params:dict=None, headers:dict=None, data:dict=None, files:dict=None) -> requests.Response:
    if request_type == "GET":
        request = requests.get(url, params=params, headers=headers, data=data, files=files)
        # print status code to console
        response_code = request.status_code
        con = Console()
        # If its an information response print it in white
        if response_code >= 100 and response_code < 199:
            con.print(f"[white]{response_code}[/white] {request.url} in {round(request.elapsed.total_seconds() * 1000)} ms")
        # If it's OK print it in green
        elif response_code >= 200 and response_code < 299:
            con.print(f"[green]{response_code}[/green] {request.url} in {round(request.elapsed.total_seconds() * 1000)} ms")
        # If it's a redirect print in yellow
        elif response_code >= 300 and response_code < 399:
            con.print(f"[yellow]{response_code}[/yellow] {request.url} in {round(request.elapsed.total_seconds() * 1000)} ms")
        # If it's a client error print in red
        elif response_code >= 400 and response_code < 499:
            con.print(f"[red]{response_code}[/red] {request.url} in {round(request.elapsed.total_seconds() * 1000)} ms")
        # If it's server error print in bright red
        elif response_code >= 500 and response_code < 599:
            con.print(f"[bright-red]{response_code}[/bright-red] {request.url} in {round(request.elapsed.total_seconds() * 1000)} ms")
        return request