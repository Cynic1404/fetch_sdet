import requests


class Apis:
    BASE_URL="http://api.openweathermap.org/geo/1.0/"
    API_KEY = "..."
    @classmethod
    def api_get_coordinates_by_location_name(cls, city_state, is_api_key=True):
        api_key = "" if not is_api_key else cls.API_KEY
        url = f"{cls.BASE_URL}direct?q={city_state},US&limit=1&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                return {
                    "place_name": data[0].get("name"),
                    "state": data[0].get("state"),
                    "country": data[0].get("country"),
                    "latitude": data[0].get("lat"),
                    "longitude": data[0].get("lon")
                }
            else:
                return "Location not found"
        else:
            return response.status_code

    @classmethod
    def api_get_coordinates_by_zip(cls, zip_code, is_api_key=True):
        api_key = "" if not is_api_key else cls.API_KEY
        url = f"{cls.BASE_URL}zip?zip={zip_code},US&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                return {
                    "place_name": data.get("name"),
                    "state": data.get("state"),
                    "country": data.get("country"),
                    "latitude": data.get("lat"),
                    "longitude": data.get("lon")}
        else:
            return response.status_code
