import requests

def get_iss_location():
    """Fetches the current location of the International Space Station (ISS).

    This function makes a request to the Open Notify API to retrieve the real-time
    location data of the ISS. It includes checks to ensure a successful request
    and valid data format.

    Returns:
        dict: A dictionary containing the ISS location information, including:
            - "timestamp": (int) Unix timestamp of when the data was fetched

    Raises:
        requests.exceptions.RequestException: If the API request fails.
        ValueError: If the response data is not in the expected format.
        KeyError: If the expected keys ('timestamp', 'iss_position') are missing.
    """
    try:
        response = requests.get('http://api.open-notify.org/iss-now.json')
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)

        data = response.json()

        # Check if the expected keys are present in the response
        if "timestamp" not in data or "iss_position" not in data:
            raise KeyError("Missing keys 'timestamp' or 'iss_position' in the response")

    except requests.exceptions.RequestException as e:
        # Handle network errors or API issues (log, return default values, etc.)
        raise  # Re-raise the exception for the caller to handle

    return data
