import readchar
from custom_types.round_result import RoundResult
from services.game import Game
from services.game_controller import GameController
from services.board import Board
from utils.print import pretty_print


board = Board()
game_controller = GameController(board)
game = Game(game_controller)

terminal_results = [RoundResult.LOST, RoundResult.WON]
pretty_print(board.values)

result = None
while result not in terminal_results:
    key = readchar.readkey()
    result, recommendation = game.start_round(key)

    if recommendation:
        print("AI recommendation:", recommendation, "\n")
        continue

    if result == RoundResult.WRONG_INPUT:
        print("Wrong input, try again!")
    elif result == RoundResult.LOST:
        print("You have lost!")
    elif result == RoundResult.WON:
        print("You have won!")

    pretty_print(board.values)
