from brain_games.engine import run_game
from brain_games.games import brain_calc, brain_even

GAMES = {
    'brain_even': brain_even,
    'brain_calc': brain_calc,
}


def launch_game(game_name):
    game = GAMES.get(game_name)
    if game is None:
        raise ValueError(f'Игра {game_name!r} не найдена')

    run_game(game.DESCRIPTION, game.generate_round)
