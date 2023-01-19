import requests
import json
import re
import sys

def main(country, postcode):
    # send api get request
    data = requests.get('https://restcountries.com/v3.1/name/{}'.format(country))
    
    # initialise result variable
    result = ""
    
    # check for a response from server
    if data.status_code == 200:    
        # convert json to list
        country_list = json.loads(data.text) 
        # loop through country list
        for country in country_list:
            # stores regex for comparison
            postcode_regex = country['postalCode']['regex']

            # checks for valid postcode
            if re.match(postcode_regex, postcode):
                result = result + ("This postcode is valid for {} \n".format(country['name']['common']))
            else:
                result = result + ("This postcode is invalid for {} \n".format(country['name']['common']))

    # error handling if incorrect input for country
    else:
        result = result + ("Country does not exist or incorrect input of country name.")
    
    # print results
    return print(result)

# initialise python program and retrieve 2 arguements
if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])

