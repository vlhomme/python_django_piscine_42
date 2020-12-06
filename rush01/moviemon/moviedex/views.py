from django.shortcuts import render
import gameClass.game as gameUtils


# Create your views here.
def detail(request, encryptedId):
    game = gameUtils.Game.readState()
    title = str(game.movieDetails[encryptedId]['Title'])
    director = str(game.movieDetails[encryptedId]['Director'])
    year = str(game.movieDetails[encryptedId]['Year'])
    rating = str(game.movieDetails[encryptedId]['imdbRating'])
    plot = str(game.movieDetails[encryptedId]['Plot'])
    actors = str(game.movieDetails[encryptedId]['Actors'])
    poster = str(game.movieDetails[encryptedId]['Poster'])
    return render(request, 'detail.html', {
        'title': title,
        'director': director,
        'year': year,
        'rating': rating,
        'plot': plot,
        'actors': actors,
        'poster': poster,
    })

def index(request):
    game = gameUtils.Game.readState()
    link = ''
    scrollStyleActivated = ''
    if len(game.captured) > 63:
        scrollStyleActivated = 'overflow: scroll;'
    movieSelected = 0
    action = request.GET.get('action', '')
    if 'next' in action:
        movieSelected = int(action.replace('next', '')) + 1
    elif 'previous' in action:
        movieSelected = int(action.replace('previous', '')) - 1
    if movieSelected < 0:
        movieSelected = 0
    elif movieSelected > len(game.captured) - 1:
        movieSelected = len(game.captured) - 1
    listForMoviedex = []
    i = 0
    for encryptedId in game.captured:
        if i == movieSelected:
            link = '/moviedex/' + encryptedId
        listForMoviedex.append(game.movieDetails[encryptedId]['Poster'])
        i = i + 1

    return render(request, 'moviedex.html', {'movieList': listForMoviedex, 'movieSelected': movieSelected, 'scrollStyleActivated' : scrollStyleActivated, 'link': link})