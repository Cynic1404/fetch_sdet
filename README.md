# Geolocation Utility

This is a command-line utility to get geolocation information for cities and zip codes in the United States. It fetches data from the OpenWeather Geocoding API.

## Features
- Get latitude and longitude for a given **city, state** or **zip code**.
- Handles multiple locations at once.
- Returns formatted results.
- Provides error messages for invalid inputs.
- Includes automated tests for functionality verification.

## Installation
### Prerequisites
- Python 3.x
- `pip` package manager

### Install Dependencies
Run the following command in the project root:
```sh
pip install -r requirements.txt
```

## Usage
### Command Line
Run the script with location inputs:
```sh
python main.py --locations "Madison, WI" "95126"
```
#### Example Output:
```
Madison, Wisconsin, US, 43.074761, -89.3837613
San Jose, US, 37.3249, -121.9153
```

## Running Tests
This project includes automated tests using `pytest`. To run them, execute:
```sh
pytest tests/tests.py
```

## Project Structure
```
root_folder/
│── main.py            # Main script
│── api/
│   ├── apis.py        # API calls to OpenWeather
│── helpers/
│   ├── helpers.py     # Helper functions for validation
│── tests/
│   ├── tests.py       # Test cases for the project
│── requirements.txt   # Required dependencies
│── README.md          # This file
```

## API Information
This utility uses the OpenWeather Geocoding API. An API key is required for requests.

## Error Handling
- If an invalid city or zip code is entered, the program will return an error message.
- If the API fails, it returns an appropriate response code.
