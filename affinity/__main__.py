"""Main CLI Interface for Affinity"""
import argparse
from .request import handle_request
from .output import write_output
from .parse_cli_dict import ParseDict

# Set up the command line arguments
parser = argparse.ArgumentParser(prog="Affinity", description="A simple CLI HTTP client")
parser.add_argument("url")
parser.add_argument("-t", "--type", default="GET", help="The type of request to make (GET, POST, PUT etc.) Defaults to GET", type=str)
parser.add_argument("-o", "--output", help="Whether or not Affinity should output the results", action="store_true")
parser.add_argument("-j", "--json", action="store_true", help="Whether or not to output the data in JSON")
parser.add_argument("-w", "--output-file", default=None, help="What file the data should be output to", type=str)
parser.add_argument("-p", "--params", default=None, help="Parameters to supply in the URL", nargs='*', action=ParseDict)

# Get the arguments passed in
args = parser.parse_args()
write_output(handle_request(args.url, args.type, args.params), args.output, args.json, args.output_file)