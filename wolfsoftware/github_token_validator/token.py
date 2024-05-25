"""
This module provides functions to validate a GitHub token and display its information in a table format.

It includes functionalities to make API requests, handle potential errors, and format the output.
"""

import sys
from datetime import datetime, timedelta
from typing import Any, Dict, Literal, Optional
from types import SimpleNamespace

import requests
from prettytable import PrettyTable
from wolfsoftware.notify import error_message


def pluralise(value) -> Literal['s'] | Literal['']:
    """
    Return 's' if the input value is 1, otherwise returns an empty string.

    Arguments:
        value (int or str): The value to be checked.

    Returns:
        Literal['s'] or Literal['']: 's' if value is 1, otherwise an empty string.
    """
    value = int(value)
    return 's' if value == 1 else ''


def validate_token(config: SimpleNamespace) -> Dict[str, Any]:
    """
    Validate the provided GitHub token by making an API request and returns token-related information.

    Arguments:
        config (SimpleNamespace): Configuration object containing the GitHub token and request timeout.

    Returns:
        Dict[str, Any]: Dictionary containing token scopes, rate limit information, and time until reset.

    Raises:
        SystemExit: If an error occurs during the API request or the token is invalid.
    """
    json_data: Dict[str, Any] = {}
    user_url = "https://api.github.com/user"

    headers: Dict[str, str] = {'Authorization': f'token {config.token}'}

    try:
        response: requests.Response = requests.get(user_url, headers=headers, timeout=config.timeout)
        response.raise_for_status()

        if response.status_code == 200:
            json_data['scopes'] = response.headers.get("X-OAuth-Scopes")
            json_data['rate_limit_limit'] = response.headers.get("X-RateLimit-Limit")
            json_data['rate_limit_remaining'] = response.headers.get("X-RateLimit-Remaining")
            json_data['rate_limit_used'] = response.headers.get("X-RateLimit-Used")

            rate_limit_reset: Optional[str] = response.headers.get("X-RateLimit-Reset")

            if rate_limit_reset:
                reset_time: datetime = datetime.fromtimestamp(int(rate_limit_reset))
                current_time: datetime = datetime.now()
                time_till_reset: timedelta = reset_time - current_time
                hours, remainder = divmod(time_till_reset.total_seconds(), 3600)
                minutes, seconds = divmod(remainder, 60)

                json_data['time_till_reset'] = (
                    f"{int(hours)} hour{pluralise(hours)}, "
                    f"{int(minutes)} minute{pluralise(minutes)}, "
                    f"{int(seconds)} second{pluralise(seconds)}"
                )
        else:
            print(error_message(f"Unable to fetch token info. Status code: {response.status_code}"))
            sys.exit(0)

    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            print(error_message("Authentication failed: Bad credentials"))
        if response.status_code == 403:
            print(error_message("Rate limit exceeded."))
        if response.status_code == 404:
            print(error_message(f"Resource not found for URL: {user_url}"))
        sys.exit(1)
    except requests.exceptions.Timeout:
        print(error_message(f"Request timed out after {config.timeout} seconds"))
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(error_message(f"An error occurred: {e}"))
        sys.exit(1)

    return json_data


def display_token(data: Any) -> None:
    """
    Display token information in a table format using PrettyTable.

    Arguments:
        data (Any): Dictionary containing token information to be displayed.
    """
    table = PrettyTable()

    table.field_names = ["Name", "Value"]
    table.add_row(["Token Scope", data['scopes']])
    table.add_row(["Rate Limit", data['rate_limit_limit']])
    table.add_row(["Rate Limit Used", data['rate_limit_used']])
    table.add_row(["Rate Limit Remaining", data['rate_limit_remaining']])
    table.add_row(["Time Till Reset", data['time_till_reset']])

    table.align["Name"] = "l"
    table.align["Value"] = "l"

    print(table)
