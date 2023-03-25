""" Interactions with the random.org API. """

from pydantic import validate_arguments
import requests


class RandomOrgAPiException(Exception):
    """Exception for errors related with random.org API"""


@validate_arguments
def get_random_string(length: int) -> str:
    """
    Get a random (digits) string of determined length from the random.org API.

    :param int length: The length of the generated string
    :raises ValueError: Param length must be between 1 and 20
    :raises Exception: When the external API call fails
    :return str: Generated string
    """
    # Validate length
    if length <= 0 or length > 20:
        raise ValueError("Length of generated string must be between 1 and 20")

    # Define the API endpoint and parameters.
    url = "https://www.random.org/strings/"
    params = {
        "num": 1,  # Generate 1 string.
        "len": length,  # The length of each string.
        "digits": "on",  # Exclude digits.
        "unique": "on",  # Include uppercase letters.
        "format": "plain",  # Return plain text.
        "md": "new",
    }

    # Send the request and get the response.
    response = requests.get(url, params=params, timeout=5)
    if response.status_code != 200:
        raise RandomOrgAPiException(
            "Failed to get random string from random.org API: "
            f"{response.status_code} {response.reason}"
        )

    # Parse the response and return the random string.
    return response.text.strip()
