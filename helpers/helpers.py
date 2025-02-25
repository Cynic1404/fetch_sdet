import re

from api.apis import Apis


class Helpers:

    @classmethod
    def get_coordinates_by_zip_code(cls, zip_code):
        result = Apis.api_get_coordinates_by_zip(zip_code)
        if result in [401,404]:
            return f"{zip_code} is a wrong zip code"
        else:
            return (f"{result['place_name']}, {result['state']+', ' if result['state'] else ''}"
                                        f"{result['country']},"
                                        f" {result['latitude']}, {result['longitude']}")

    @classmethod
    def get_coordinates_by_location_name(cls, location):
        result = Apis.api_get_coordinates_by_location_name(location)
        if result in [401,404, "Location not found"]:
            return(f"{location} is a wrong location")
        else:
            return (f"{result['place_name']}, {result['state'] + ', ' if result['state'] else ''}"
                    f"{result['country']},"
                    f" {result['latitude']}, {result['longitude']}")


    @classmethod
    def is_zip_code(cls, location):
        return bool(re.fullmatch(r"\d{5}", location))
