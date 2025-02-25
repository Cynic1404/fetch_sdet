import argparse
from helpers.helpers import Helpers


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--locations", nargs='+', required=True)
    args = parser.parse_args()


    results = []

    for user_input in args.locations:
        if user_input == "":
            results.append("Location/zip code is required")
        else:
            if Helpers.is_zip_code(user_input):
                result = Helpers.get_coordinates_by_zip_code(user_input)
            else:
                result = Helpers.get_coordinates_by_location_name(user_input)
            results.append(result)

    return results



if __name__ == "__main__":
    results = main()
    for result in results:
        print(result, end="\n")