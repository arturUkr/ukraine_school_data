import requests


def get_geocode(city_name, street_name, api_key):

    base_str = "https://api.visicom.ua/data-api/4.0/uk/geocode.json"
    address = f"{city_name}, {street_name}"
    request_str = f"{base_str}?text={address}&key={api_key}"

    response = requests.get(request_str)
    if response.status_code == 200:
        return response.json()
    else:
        return {}
