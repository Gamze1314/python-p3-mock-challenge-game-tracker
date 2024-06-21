# game and player has many-to-many relationship.
# Result belongs to a Player and to a Game.


class Game:  # Game class defined

    all = []

    def __init__(self, title):  # initialize w title attr, and assigns/attaches it to self.title
        self.title = title
        Game.all.append(self)

    @property
    def title(self):  # getter method returns the title
        # _title convention : a way to indicate that the variable is private.
        return self._title

    @title.setter  # setter method to validate the type of title
    # add logic to check if there is attr
    def title(self, value):
        if not hasattr(self, "title"):
            if not isinstance(value, str) or not len(value) > 0:
                raise ValueError("Title must be a non-empty string")
            # raises exception
            else:
                self._title = value

    def results(self):
        # returns a list of all results for that game
        # result must be type of Result class
        return [result for result in Result.all if result.game == self]

    def players(self):
        # returns a list of all players that played the game.
        # player must be type of Player class
        return list(set([result.player for result in Result.all if result.game == self]))

    def average_score(self, player):
        # how many scores in Result.all
        # total result player scores
        # total result player scores divided by how many scores in Result.all
        total = [result.score for result in Result.all if result.player == player]
        average = sum(total) / len(total)
        return average


class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not 2 <= len(value) <= 16:
            raise ValueError(
                "User name must be a string and not more than 16 characters.")
        else:
            self._username = value

    def results(self):
        # returns a list of all results for the player
        # result must be type of Result class
        return [result for result in Result.all if result.player == self]

    def games_played(self):  # review this
        # returns a list of all games played by the player
        # game must be type of Game class
        return list(set([result.game for result in Result.all if result.player == self]))

    def played_game(self, game):
        # returns true if the player has played the game
        # receives a game object
        # returns false otherwise
        return game in self.games_played()

    def num_times_played(self, game):
        # returns the number of times the player has played the game
        # self.results() == Result.all
        games_played = [result.game for result in self.results()]
        return games_played.count(game)


class Result:  # join table with unique players

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

# result property score returns the score, must be type of int, btw 1 and 5000 inclusive
# can not change

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not hasattr(value, 'score'):
            if not isinstance(value, int) or not 1 <= value <= 5000:
                raise ValueError("Score must be an integer and more than 1.")
            else:
                self._score = value

    @property
    def player(self):
        # make sure the player is unique
        return self._player

    @player.setter
    def player(self, value):
        if not isinstance(value, Player):
            raise ValueError("Player must be of type Player.")

        if value in Result.all:
            raise ValueError("Player already exists.")

        self._player = value

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        if not isinstance(value, Game):
            raise ValueError("Game must be of type Game.")

        if value in Result.all:
            raise ValueError("Game already exists.")

        self._game = value
