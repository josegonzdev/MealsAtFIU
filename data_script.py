import requests
import json

# url of website for data
url = "https://api.dineoncampus.com/v1/location/5b9fda57f3eeb60c6e592caf/periods/66c72eaec625af01b5d68ead?platform=0&date=2024-9-11"

#headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "Accept": "application/json",
}

try:
    # GET request to the API
    response = requests.get(url, headers=headers)

    # check if the request was successful
    if response.status_code == 200:
        # parse the JSON response
        data = response.json()

        # save the data to a JSON file everytime
        with open('menu_data.json', 'w') as file:
            json.dump(data, file, indent=4)

        print("Data has been successfully saved to 'menu_data.json'.")

    else:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
