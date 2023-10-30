import requests

# Define the API URL
# url = "https://www.freetogame.com/api/games"

url="https://uselessfacts.jsph.pl/random.json?language=en"


# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    games_data = response.json()

    # Print the data
    for game in games_data:
        print(game)

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

'''
https://uselessfacts.jsph.pl/
'''