from django.conf import settings
from cryptography.fernet import Fernet
import requests
import json
import pickle
import random

def load_key():
    """
    Loads the key that was generated when settings ran
    """
    return open(settings.KEYFILE, "rb").read()
def encrypt(text: str, key):
    f = Fernet(key)
    return(f.encrypt(text.encode()))

SIZE_OF_SCREEN = 324 # should be constant because css padding and everything (screen is 400px square but inside is 324)

class Game:
    def __init__(self):
        self.position = (0, 0)
        self.movieBalls = 0
        self.width = 10
        self.height = 10
        self.size = 'small'
        self.playerStrength = 0
        self.moviemonNameList = []
        self.notCapturedYet = []
        self.captured = []
        self.movieDetails = {}
        self.key = load_key()

    def load(self, instanceAsObject):
        """
            Charge les données de jeu passés en paramètres dans l'instance de classe.
            Retourne l'instance courante.
        """
        self.position = instanceAsObject.position,
        self.movieBalls = instanceAsObject.movieBalls,
        self.width = instanceAsObject.width,
        self.height = instanceAsObject.height,
        self.size = instanceAsObject.size,
        self.playerStrength = instanceAsObject.playerStrength,
        self.moviemonNameList = instanceAsObject.moviemonNameList,
        self.notCapturedYet = instanceAsObject.notCapturedYet,
        self.captured = instanceAsObject.captured,
        self.movieDetails = instanceAsObject.movieDetails,
        self.key = instanceAsObject.key
        return(self)


    def saveState(self):
        """
            save instance in a tmp game state file
        """
        with open(settings.GAMESTATEFILE, 'wb') as f:
            pickle.dump(self, f)
    
    @staticmethod
    def readState():
        """
            return new instance base on the state file
        """
        with open(settings.GAMESTATEFILE, 'rb') as f:
            instance = pickle.load(f)
        return instance

    def saveToSavefile(self, numero):
        """
            save instance in a save file
        """
        with open(settings.SAVEFILEDIR + str(numero), 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def readSave(numero):
        """
            return new instance base on the specifiedSave file
        """
        with open(settings.SAVEFILEDIR + str(numero), 'rb') as f:
            instance = pickle.load(f)
        return instance

    def dump(self):
        """
            Retourne les données de jeu
        """
        return({
            'position': self.position,
            'movieBalls': self.movieBalls,
            'width': self.width,
            'height': self.height,
            'size': self.size,
            'playerStrength': self.playerStrength,
            'moviemonNameList': self.moviemonNameList,
            'notCapturedYet': self.notCapturedYet,
            'captured': self.captured,
            'movieDetails': self.movieDetails,
            'key': self.key,
        })

    @staticmethod
    def whatsinTheCell():
        randomRange = random.randint(0,100)
        if randomRange < 40:
            return 'nothing'
        elif randomRange < 70:
            return 'movieball'
        else:
            return 'moviemon'

    def get_random_movie(self):
        """
            Retourne un Moviemon au hasard parmi les Moviemons non capturés.
        """
        pass

    def load_default_settings(self):
        """ Charge les données de jeu dans l'instance de classe depuis les settings.
        Requête et stocke les détails de tous les Moviemons sur IMDB. Retourne l'instance courante. """
        # key = load_key()
        self.position = settings.STARTING_POS
        self.width = settings.MATRIX_WIDTH
        self.height = settings.MATRIX_HEIGHT
        self.size = settings.SIZE
        self.playerStrength = settings.PLAYER_STRENGTH
        self.moviemonNameList = settings.MOVIEMONS
        for movieName in self.moviemonNameList:
            r = requests.get("http://www.omdbapi.com/?t=" + movieName + '&apikey=2415147b')
            if (r.status_code == 200):
                movieDetails = r.json()
                # print(movieDetails)
                if (movieDetails['Response'] == 'True'):
                    encryptedID = encrypt(movieDetails['imdbID'], self.key)
                    movieDetails['id'] = str(encryptedID)
                    self.movieDetails[str(encryptedID)] = movieDetails
                    self.notCapturedYet.append(str(encryptedID))
                else:
                    print('request failed because the movie doesnt exist on IMDB ' + movieName)
            else:
                print('request failed' + movieName + ' with status ' + str(r.status_code))
        # log to a file
        self.notCapturedYet = list(dict.fromkeys(self.notCapturedYet))
        with open(settings.RANDOMLOGFILE, "w") as logfile:
            logfile.write(json.dumps([self.movieDetails, self.notCapturedYet]))

    def getStyleforSizeofCells(self):
        if self.width == self.height:
            tmp = SIZE_OF_SCREEN / self.width
            calculateSizeOfCells = 'width: ' + str(int(tmp)) + 'px; height: ' + str(int(tmp)) + 'px;'
        else:
            tmpWidth = SIZE_OF_SCREEN / self.width
            tmpHeight = SIZE_OF_SCREEN / self.height
            calculateSizeOfCells = 'width: ' + str(int(tmpWidth)) + 'px; height: ' + str(int(tmpHeight)) + 'px;'
        return calculateSizeOfCells

    def get_strength(self):
        """
            Retourne la force du joueur
        """
        pass
    def get_movie(self):
        """
            Retourne un dictionnaire Python contenant tous les détails
            depuis le nom du Moviemon passé en paramètre
            et nécessaires à la page Détail.
        """
        pass