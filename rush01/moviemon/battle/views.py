from django.shortcuts import render
import gameClass.game as gameUtils

# Create your views here.
def index(request, moviemon_id):
    encryptedId = moviemon_id[1:]
    game = gameUtils.Game.readState()
    message = 'try to catch him by pressing A ! Or go back to map by pressing B. Movieballs left : ' + str(game.movieBalls)
    details = game.movieDetails[encryptedId]
    movieStrength = details['imdbRating']
    # print(details)

    action = request.GET.get('action', '')
    if (action == 'launch') or (game.movieBalls == 0):
        if game.movieBalls > 0:
            game.movieBalls = game.movieBalls - 1
            if game.catchSucceed(movieStrength):
                game.notCapturedYet.remove(encryptedId)
                game.captured.append(encryptedId)
                game.playerStrength = game.playerStrength + 1
                message = 'You just caught ' + details['Title'] + ' ! Go back to map by pressing B.'
            else:
                if game.movieBalls == 0:
                    message = "catch failed ! You have no more movieball. Go back to map by pressing B."
                else:
                    message = "catch failed ! Retry or back to map by pressing B. Movieballs left : " + str(game.movieBalls)
            game.saveState()
        else:
            message = "You have no more movieball. Go back to map by pressing B."

    return render(request, 'battle.html', {
      'title': details['Title'],
      'imdbRating': details['imdbRating'],
      'director': details['Director'],
      'poster': details['Poster'],
      'message': message
    })