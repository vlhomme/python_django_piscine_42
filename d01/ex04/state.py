import sys

if __name__ == '__main__':
    states = {
            "Oregon" : "OR",
            "Alabama" : "AL",
            "New Jersey": "NJ",
            "Colorado" : "CO"
            }
    capital_cities = {
            "OR": "Salem",
            "AL": "Montgomery",
            "NJ": "Trenton",
            "CO": "Denver"
            }
    if len(sys.argv) == 2:
        capital = sys.argv[1]
        if capital in capital_cities.values():
            stateShort = ''
            for key, value in capital_cities.items():
                if value == capital:
                    stateShort = key
            keyOfState = ''
            for key, value in states.items():
                if value == stateShort:
                    keyOfState = key
            print(keyOfState)
        else:
            print("Unknown state")
