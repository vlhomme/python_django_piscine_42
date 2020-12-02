from django.shortcuts import render
from colour import Color

# Create your views here.
def index(request):
    black = Color("black")
    blacklist = list(black.range_to(Color("white"),50))
    red = Color("red")
    redlist = list(red.range_to(Color("white"),50))
    blue = Color("blue")
    bluelist = list(blue.range_to(Color("white"),50))
    green = Color("green")
    greenlist = list(green.range_to(Color("white"),50))

    listOfColors = []
    i = 0
    for color in blacklist:
        line = {
            'black' : blacklist[i].hex_l,
            'red' : redlist[i].hex_l,
            'blue' : bluelist[i].hex_l,
            'green' : greenlist[i].hex_l,
        }
        listOfColors.append(line)
        i = i + 1

    return render(request, "indexo.html", {'listOfColors' : listOfColors})