import argparse
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description="CLI program to make HTTP requests")

    parser.add_argument("url", help="URL for the HTTP request")

    parser.add_argument("--method", default="GET", help="HTTP method (default: GET)")
    parser.add_argument("--params", type=json.loads, help="Parameters for the request (JSON format)")
    parser.add_argument("--files", type=json.loads, help="Files to upload with the request (JSON format)")
    parser.add_argument("--proxies", type=json.loads, help="Proxies for the request (JSON format)")
    parser.add_argument("--data", type=json.loads, help="Data for the request (JSON format)")
    parser.add_argument("--headers", type=json.loads, help="Headers for the request (JSON format)")
    parser.add_argument("--timeout", type=float, help="Timeout for the request")
    parser.add_argument("--auth", type=tuple, help="Authentication credentials (username, password)")
    parser.add_argument("--cookies", type=json.loads, help="Cookies for the request (JSON format)")
    parser.add_argument("--verify", type=bool, default=True, help="Verify SSL certificate (default: True)")
    parser.add_argument("--cert", help="Path to SSL certificate file")
    parser.add_argument("--allow-redirects", type=bool, default=True, help="Allow redirects (default: True)")
    parser.add_argument("--nocolor", action="store_true", help="Disable colored output")

    parser.add_argument("--status-code", action="store_true", help="Show the status code")
    parser.add_argument("--headers-content", action="store_true", help="Show the headers")
    parser.add_argument("--text-content", action="store_true", help="Show the text content")
    parser.add_argument("--binary-content", action="store_true", help="Show the binary content")
    parser.add_argument("--json-content", action="store_true", help="Show the JSON content")
    parser.add_argument("--final-url", action="store_true", help="Show the final URL")
    parser.add_argument("--elapsed-time", action="store_true", help="Show the elapsed time")
    parser.add_argument("--cookies-content", action="store_true", help="Show the cookies")

    parser.add_argument("--load-config", help="Load configuration from a JSON file")
    parser.add_argument("--output-file", help="Save the output to a file")

    args = parser.parse_args()

    if args.load_config:
        with open(args.load_config, 'r') as config_file:
            config = json.load(config_file)
            for key, value in config.items():
                setattr(args, key, value)

    return args