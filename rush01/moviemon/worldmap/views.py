from django.shortcuts import render
from django.conf import settings
import gameClass.game as gameUtils
import pickle

def updateposition(position):
    game = gameUtils.Game.readState()
    game.position = position
    game.saveState()

def updateData(case, game):
    if case == 'movieball':
        game.movieBalls = game.movieBalls + 1
        game.saveState()
    if case == 'moviemon':

# Create your views here.
def index(request):
    message = ''
    game = gameUtils.Game.readState()
    x, y = game.position
    action = request.GET.get('action', '')
    if (action == 'goUp') or (action == 'goDown') or (action == 'goLeft') or (action == 'goRight'):
        case = game.whatsinTheCell()
        message = 'you found ' + case + '.'
        updateData(case, game)
    if (action == 'goUp'):
        if (y - 1 in range(game.height + 1)) and y - 1 != 0:
            y = y - 1
            updateposition((x, y))
    elif (action == 'goDown'):
        if (y + 1 in range(game.height + 1)):
            y = y + 1
            updateposition((x, y))
    elif (action == 'goLeft'):
        if (x - 1 in range(game.width + 1)) and x - 1 != 0:
            x = x - 1
            updateposition((x, y))
    elif (action == 'goRight'):
        if (x + 1 in range(game.width + 1)):
            x = x + 1
            updateposition((x, y))
    return render(request, "worldmap.html", {
        'message' : message,
        'width' : range(game.width),
        'height' : range(game.height),
        'calculateSizeOfCells' : game.getStyleforSizeofCells(),
        'y' : y,
        'x' : x,
        'movieBalls' : str(game.movieBalls)
        })