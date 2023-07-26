"""Main CLI Interface for Affinity"""
import argparse
import requests
from .utils import get_data, get_files
from .output_handler import OutputHandler, error
from affinity import __version__

def main():
    # Set up the command line arguments
    parser = argparse.ArgumentParser(prog="Affinity", description="A simple CLI HTTP client")
    parser.add_argument('-v', '--version', action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("url", default=None)
    parser.add_argument("-t", "--type", default="GET", help="The type of request to make. Defaults to GET", type=str, 
                        choices=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE", "CONNECT"))
    parser.add_argument("-o", "--output", action="store_true", help="If used, the result of the request will be printed to the terminal")
    parser.add_argument("-p", "--params", default=None, help="Parameters to supply in the URL. Pass data as KEY=VALUE or to read from a JSON file use *FILE_NAME")
    parser.add_argument("--header", default=None, help="Header data to send with the request. Pass data as KEY=VALUE or to read from a JSON file use *FILE_NAME")
    parser.add_argument("-f", "--form", default=None, help="Form-encoded data to send. Pass data as KEY=VALUE or to read from a JSON file use *FILE_NAME")
    parser.add_argument("-e", "--encoding", default="utf-8", help="What encoding to use ")
    parser.add_argument("--files", default=None, help="Files to send with request", nargs="+")
    
    # Get the arguments passed in
    args = parser.parse_args()

    # Format the passed in data as dicts
    parameters = get_data(args.params)
    header = get_data(args.header)
    form = get_data(args.form)
    files = get_files(args.files)

    # Make the HTTP request with requests and handle any errors that may arise
    try:
        response = requests.request(args.type, args.url, params=parameters, headers=header, data=form, files=files)
        response.encoding = args.encoding
    except requests.exceptions.MissingSchema:
        error("Invalid URL. Make sure it starts with http/https")
    except requests.exceptions.Timeout:
        error("Connecttion timed out")
    except requests.exceptions.ConnectionError:
        error("Could not connect")
    except requests.exceptions.TooManyRedirects:
        error("Too many redirects")
    except requests.exceptions.RequestException:
        error("Could not send request")
    else:
        handler = OutputHandler(response)

    # If the user wants to display the result in the terminal
    if args.output:
        handler.print_result()