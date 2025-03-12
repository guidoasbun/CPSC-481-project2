from games import *

class GameOfNim(Game):

    def __init__(self, board=None):
        if board is None:
            board = [7, 5, 3, 1]
        
        # Calculate and set the initial moves
        initial_moves = []
        for row in range(len(board)):
            for num_objects in range(1, board[row] + 1):
                initial_moves.append((row, num_objects))
                
        # Create the initial state with the calculated moves
        self.initial = GameState(to_move='MAX', 
                               utility=0, 
                               board=board, 
                               moves=initial_moves)

    def actions(self, state):
        moves = []
        for row in range(len(state.board)):
            for num_objects in range(1, state.board[row] + 1):
                moves.append((row, num_objects))
        return moves

    def result(self, state, move):
        board = state.board.copy()
        row, num_objects = move

        # Validate the move
        if row < 0 or row >= len(board) or num_objects > board[row]:
            return state
        
        # Apply the move
        board[row] -= num_objects

        # Calculate next player
        next_player = 'MIN' if state.to_move == 'MAX' else 'MAX'

        # Calculate utility
        utility = 0
        if sum(board) == 0:
            utility = -1 if next_player == 'MAX' else 1

        # Calculate new valid moves
        new_moves = []
        for row in range(len(board)):
            for num_objects in range(1, board[row] + 1):
                new_moves.append((row, num_objects))

        return GameState(to_move=next_player,
                        utility=utility,
                        board=board,
                        moves=new_moves)

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        # return state.utility if player == 'MAX' else -state.utility
        return 1 if state.utility == 1 and player == 'MAX' else -1 if state.utility == -1 and player == 'MIN' else 0

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return sum(state.board) == 0

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    #nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    result_state = nim.result(nim.initial, (1,2)) # computer moves first
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3)).board)
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if utility < 0:
        print("MIN won the game")
    else:
        print("MAX won the game")
