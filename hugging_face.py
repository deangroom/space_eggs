import requests
import pandas as pd


"""
This script accesses public data from huggingface.co and prints the features of the dataset.
The features are then placed in a list and a pandas dataframe is created from the list.
The purpose of this is to demonstrate how to find a dataset online and then work out what the features are.
"""
url = "https://datasets-server.huggingface.co/rows?dataset=Hello-SimpleAI%2FHC3&config=all&split=train&offset=0&length=100"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the JSON response to a Python dictionary
    data = response.json()

    # Extract the 'features' list
    features = data['features']
    print(f'The features in this dataset are {features}')

    #access feature_idx_1
    feature_idx_1 = features[1]
    print(f'The first feature is {feature_idx_1}')
    print(f'The first feature is {feature_idx_1["name"]}')

    #access feature_idx_2
    feature_idx_2 = features[2]
    print(f'The second feature is {feature_idx_2}')
    print(f'The second feature is {feature_idx_2["name"]}')

    #access feature_idx_3
    feature_idx_3 = features[3]
    print(f'\nThe third feature is {feature_idx_3}')
    print(f'The third feature is {feature_idx_3["name"]}')

    #access feature_idx_4
    feature_idx_4 = features[4]
    print(f'\nThe fourth feature is {feature_idx_4}')
    print(f'\nThe fourth feature is {feature_idx_4["name"]}')

  
    #create a dataframe from the list
    df = pd.DataFrame(features)
    #print the first 5 rows of the dataframe
    print(f'\nThe first 5 rows of the dataframe are {df.head()}')

   #create a new data frame for each column in the dataframe
    df1 = df['name']


    #print the first 5 rows of each dataframe
    print(f'\nThe first 5 rows of the name dataframe are {df1.head()}')


    #print the first 5 rows of the dataframe
    print(f'\nThe first 5 rows of the dataframe are {df.head()}')

    #print the first 5 rows of the dataframe
    print(f'\nThe first 5 rows of the dataframe are {df.head()}')

    #print the first 5 rows of the dataframe
    print(f'\nThe first 5 rows of the dataframe are {df.head()}')

    #print the first 5 rows of the dataframe
    print(f'\nThe first 5 rows of the dataframe are {df.head()}')

    #print the first 5 rows of the dataframe
    print(f'\nThe first 5 rows of the dataframe are {df.head()}')





    

