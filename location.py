import requests
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Get the current location of the user')

# Add the arguments
parser.add_argument('Info', metavar='info', type=str, help='the information to retrieve (city or country)')

# Parse the arguments
args = parser.parse_args()

try:
    response = requests.get('https://ipinfo.io/json')
    data = response.json()

    if args.Info.lower() == 'city':
        print(f"{data['city']}")
    elif args.Info.lower() == 'country':
        print(f"{'UK' if data['country'] == 'GB' else data['country']}")
    else:
        print("Invalid argument. Please enter 'city' or 'country'.")
except:
    print("No Location Found")