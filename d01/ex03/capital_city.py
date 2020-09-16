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
        state = sys.argv[1]
        if state in states:
            stateShort = states[state]
            print(capital_cities[stateShort])
        else:
            print("Unknown state")
