import requests

BASE_URL = "https://passiogo.com"


def to_int_incl_none(to_int):
    if to_int is None:
        return to_int
    return int(to_int)


def send_api_request(url, body):
    response = requests.post(url, json=body)

    try:
        response = response.json()
    except Exception as e:
        raise Exception(
            f"Error converting API response to JSON! Here is the response received: {response}"
        ) from e

    if "error" in response and response["error"] != "":
        raise Exception(f"Error in Response! Here is the received response: {response}")

    return response
