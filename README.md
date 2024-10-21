# Weather Forecast

This is a simple Python script that fetches and displays the current weather information for a specified city using the OpenWeatherMap API.

## Features

- Fetches current weather data for a specified city.
- Displays weather type, temperature in Celsius and Fahrenheit, maximum and minimum temperatures, and wind speed in miles and kilometers.
- Handles errors for invalid city names.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/Weather_Forecast.git
    cd Weather_Forecast
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. The `.env` file with the OpenWeatherMap API key is included in the repository. However, if you want to use your own API key, you can modify the `.env` file:
    ```sh
    echo "API_KEY=your_api_key_here" > .env
    ```

## Usage

1. Run the script:
    ```sh
    python Weather_Forecast.py
    ```

2. Enter the name of the city when prompted.


## License

This project is licensed under the MIT License. See the LICENSE file for details.
