"""
This module provides command-line argument parsing, processing, and execution functionalities for the application.

This module defines the main functions for setting up the argument parser, processing the arguments, and running the
main logic of the application. The module uses the argparse library to handle command-line arguments and the wolfsoftware.drawlines
module to draw lines for output formatting. It also utilizes the config module to create configurations from the parsed arguments.
"""

import argparse
import sys

from types import SimpleNamespace
from typing import Any, Dict

from .config import create_configuration_from_arguments
from .globals import ARG_PARSER_DESCRIPTION, ARG_PARSER_PROG_NAME, VERSION_STRING
from .token import validate_token, display_token


def setup_arg_parser() -> argparse.ArgumentParser:
    """
    Set up and returns the argument parser with all required flags, optional, and required arguments.

    This function creates an ArgumentParser object and defines the available command-line arguments, including flags for help,
    debug, verbose, and version information. It also sets up optional and required argument groups for additional parameters.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(prog=ARG_PARSER_PROG_NAME,
                                     add_help=False,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description=ARG_PARSER_DESCRIPTION)

    flags: argparse._ArgumentGroup = parser.add_argument_group(title='flags')
    optional: argparse._ArgumentGroup = parser.add_argument_group(title='optional')
    required: argparse._ArgumentGroup = parser.add_argument_group(title='required')

    flags.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="Show this help message and exit")
    flags.add_argument('-V', '--version', action="version", version=VERSION_STRING, help="Show program's version number and exit.")

    optional.add_argument("-T", "--timeout", type=int, default=10, help="Timeout value for GitHub API")

    required.add_argument("-t", "--token", type=str, required=True, help="The GitHub token to validate")

    return parser


def process_arguments(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """
    Process and validates the command-line arguments.

    This function uses the provided argument parser to parse the command-line arguments. It validates the parsed arguments
    and returns them in a Namespace object.

    Args:
        parser (argparse.ArgumentParser): The argument parser to use for parsing the command-line arguments.

    Returns:
        argparse.Namespace: The parsed and validated arguments.
    """
    args: argparse.Namespace = parser.parse_args()
    return args


def run() -> None:
    """
    Master controller function.

    This function sets up the argument parser, processes the command-line arguments, creates the configuration from
    the arguments, and executes the main functionality. It handles errors related to argument parsing and exits with
    an appropriate status code in case of failure.
    """
    parser: argparse.ArgumentParser = setup_arg_parser()
    try:
        args: argparse.Namespace = process_arguments(parser)
        config: SimpleNamespace = create_configuration_from_arguments(args)
        data: Dict[str, Any] = validate_token(config)
        display_token(data)
    except argparse.ArgumentTypeError as err:
        parser.print_usage()
        print(err)
        sys.exit(1)
