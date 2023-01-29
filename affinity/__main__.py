"""Main CLI Interface for Affinity"""
import argparse, requests
from .parse_cli_dict import ParseDict
from .output_handler import OutputHandler
from affinity import __version__

def main():
    # Set up the command line arguments
    parser = argparse.ArgumentParser(prog="Affinity", description="A simple CLI HTTP client")
    parser.add_argument('-v', '--version', action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("url", default=None)
    parser.add_argument("-t", "--type", default="GET", help="The type of request to make (GET, POST, PUT etc.) Defaults to GET", type=str)
    parser.add_argument("-o", "--output", action="store_true", help="If used, the result of the request will be printed to the terminal")
    parser.add_argument("-f", "--output-file", default=None, help="What file the data should be output to", type=str)
    parser.add_argument("-p", "--params", default=None, help="Parameters to supply in the URL", nargs='*', action=ParseDict)
    parser.add_argument("--header", default=None, help="Header data to send with the request", nargs='*', action=ParseDict)
    parser.add_argument("-d", "--debug", action="store_true", help="Shows debug information about the request")
    parser.add_argument("--form", default=None, help="Form-encoded data to send", nargs="*", action=ParseDict)
    
    # Get the arguments passed in
    args = parser.parse_args()

    # Make the HTTP request with requests
    response = requests.request(args.type, args.url, params=args.params, headers=args.header, data=args.form)
    handler = OutputHandler(response)

    # If the user wants to display the result in the terminal
    if args.output:
        handler.print_result()

    # If the user wants to display debug info
    if args.debug:
        handler.write_debug_info()

    # If the user wants to write the results to a file
    if args.output_file != None:
        handler.write_to_file(args.output_file, args.binary)