import random
from game_search_algorithms import alfabeta_search, minimax_search
from base_game_class import Game


def convert_state_to_list(state_tuple):
    return [list(x) for x in state_tuple]


def convert_state_to_tuple(state_list):
    return tuple([tuple(x) for x in state_list])


# TIC-TAC TOE CLASS
class TicTacToe(Game):
    """3x3 version."""
    def __init__(self, h=3, w=3, k=3):
        """
        Base of the game. We will save states as dictionaries. We will save data in (idx, idx) = sign format.
        """
        pass
    def count_signs(self, state, sign):
        pass

    def check_triples(self, state):
        pass

    def next_player(self, state):
        pass

    def legal_steps(self, state):
        """We can step on every empty cell"""
        pass

    def goodness(self, state, player):
        """return 1 if player wins and -1 if player loses, and 0 otherwise"""
        pass

    def is_leaf(self, state):
        """If someone won or the table is full it will be the end of the game."""
        pass

    def take_step(self, step, state):
        """Effect of the step"""
        pass
    
    def print(self, state):
        """Let's see the current state."""
        for x in range(self.h):
            for y in range(self.w):
                if state[x][y] == 1:
                    sign = 'X'
                elif state[x][y] == 2:
                    sign = 'O'
                else:
                    sign = '.'
                print(sign, end=' ')
            print()
        print()

    


# PLAYERS
def random_player(game, state):
    """Randomly choose between options"""
    return random.choice(game.legal_steps(state))


def alfabeta_player(game, state):
    """Search in game tree"""
    return alfabeta_search(state, game)


def minimax_player(game, state):
    """Search in game tree"""
    return minimax_search(state, game)


def play_game(game, *players):
    """Play a game with players"""
    state = game.initial
    game.print(state)

    while True:
        for player in players:
            step = player(game, state)
            state = game.take_step(step, state)
            game.print(state)
            # print(game.legal_steps(state))
            if game.is_leaf(state):
                return game.goodness(state, 1)


tt = TicTacToe()

print('Result of the game: ', play_game(tt, random_player, minimax_player))
