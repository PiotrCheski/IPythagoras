# IP Geolocation Information Retrieval Script

## Overview

This script is designed to extract and retrieve geolocation information for IP addresses found in a given file. It utilizes the IP Geolocation API to gather information about each IP address and displays the results.

Before using the script, ensure you have obtained an API key from [IPGeolocation.io](https://ipgeolocation.io/).


![obraz](https://github.com/PiotrCheski/IPythagoras/assets/61555492/eeef9a29-6b25-49ba-bb68-a83081ab7537)


## Usage

To use this script, follow these steps:

1. Obtain an API key from [IPGeolocation.io](https://ipgeolocation.io/).

2. Create a `config.py` file in the same directory as the script and add your API key as follows:

    ```python
    # config.py

    # Define your API key here
    API_KEY = "your_api_key_here"
    ```

3. Run the script using the following command:

    ```
    python main.py <file_path_or_directory>
    ```

   Replace `<file_path_or_directory>` with the path to a text file containing IP addresses or a directory containing multiple text files. The script will extract and retrieve geolocation information for the IP addresses found in the specified file(s) and display the results.

## Notes

- IP addresses are processed only once, even if they appear multiple times in the specified file(s).





