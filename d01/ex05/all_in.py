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
    if len(sys.argv) >= 2 and len(sys.argv) < 1000:
        bigStringOfArg = (''.join(sys.argv[1]))
        # print(bigStringOfArg)
        for getArg in bigStringOfArg.split(','):
            arg = getArg.strip()
            if len(arg) != 0:
                #we have a state
                if arg.lower() in (name.lower() for name in states):
                    theCapital = (capital_cities[states[arg.lower().title()]])
                    print(theCapital, " is the capital of ", arg.lower().title())
                #we have a city
                elif arg.lower() in (name.lower() for name in capital_cities.values()):
                    stateShort = ''
                    for key, value in capital_cities.items():
                        if value.lower() == arg.lower():
                            stateShort = key
                    state = ''
                    for key, value in states.items():
                        if value == stateShort:
                            state = key
                    print(arg.title(), " is the capital of", state)
                else:
                    print(arg, " is neither a capital city nor a state")
