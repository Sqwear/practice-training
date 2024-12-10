class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(game):
    if len(game) != 2:
        raise WrongNumberOfPlayersError("Wrong number of players")
    valid_strategies = ['R', 'P', 'S']
    if game[0][1] not in valid_strategies or game[1][1] not in valid_strategies:
        raise NoSuchStrategyError("No such strategy")
    
    rules = {'R': 'S', 'S': 'P', 'P': 'R'}
    if game[0][1] == game[1][1] or rules[game[0][1]] == game[1][1]:
        return f"{game[0][0]} {game[0][1]}"
    else:
        return f"{game[1][0]} {game[1][1]}"

# print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) WrongNumberOfPlayersError
# print(rps_game_winner([['player1', 'P'], ['player2', 'A']])) NoSuchStrategyError
print(rps_game_winner([['player1', 'P'], ['player2', 'S']])) # player2 S
print(rps_game_winner([['player1', 'P'], ['player2', 'P']])) # player1 P
