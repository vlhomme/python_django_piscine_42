from django.shortcuts import render
import gameClass.game as gameUtils
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    action = request.GET.get('action', '')
    if (action == 'load_new_game'):
        # uncomment 3 lines behind to 
        # game = gameUtils.Game()
        # game.load_default_settings()
        # game.save()

        # CREATE SAVE FROM STATE
        # game = gameUtils.Game.readState()
        # game.saveToSavefile(1)

        # READ FROM SAVE
        game = gameUtils.Game.readSave(1)
        game.saveState()
        return HttpResponseRedirect("/worldmap")
    return render(request, "index.html")