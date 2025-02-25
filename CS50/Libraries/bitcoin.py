import requests
import sys

def main():
    try:
        try:
            url = "https://api.coincap.io/v2/assets/bitcoin"
            response = requests.get(url).json()
            price = response["data"]["priceUsd"]
            multiplier = get_arg() * float(price)
            print(f"{multiplier:,.4f}")
        except requests.RequestException:
            print("Request failed")
    except TypeError:
        pass
def get_arg():
    try:
        try:
            value = float(sys.argv[1])
            if len(sys.argv) > 2:
                sys.exit("Please enter only 1 number")
            else:
                return value
        except ValueError:
            print("Invalid input please enter a number")
    except IndexError:
        print("Missing command-line argument")
main()