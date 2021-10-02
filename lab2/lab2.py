# MIT 6.034 Lab 2: Games
# Written by 6.034 staff

from game_api import *
from boards import *
from toytree import GAME1

INF = float('inf')

# Please see wiki lab page for full description of functions and API.

#### Part 1: Utility Functions #################################################

def is_game_over_connectfour(board):
    """Returns True if game is over, otherwise False."""
    is_all_column_full = True
    is_game_over = False
    for chain in board.get_all_chains():
        if len(chain) >= 4:
            is_game_over = True
    for i in range(board.num_cols):
        if not board.is_column_full(i):
            is_all_column_full = False
            break
        else:
            continue
    return is_all_column_full or is_game_over

def next_boards_connectfour(board):
    """Returns a list of ConnectFourBoard objects that could result from the
    next move, or an empty list if no moves can be made."""
    list_of_boards = []
    if is_game_over_connectfour(board):
        return list_of_boards
    else:
        for i in range(board.num_cols):
            if not board.is_column_full(i):
                list_of_boards.append(board.add_piece(i))
        return list_of_boards

def tie(board):
    """Returns True if game is a tie (all column filled up but none four chain, otherwise False."""
    is_all_column_full = True
    is_game_over = False
    for chain in board.get_all_chains():
        if len(chain) >= 4:
            is_game_over = True
    for i in range(board.num_cols):
        if not board.is_column_full(i):
            is_all_column_full = False
            break
        else:
            continue
    return is_all_column_full and not is_game_over


def endgame_score_connectfour(board, is_current_player_maximizer):
    """Given an endgame board, returns 1000 if the maximizer has won,
    -1000 if the minimizer has won, or 0 in case of a tie."""
    if is_game_over_connectfour(board):
        # check if tie
        if tie(board):
            return 0
        else:
            if is_current_player_maximizer:
                return -1000
            return 1000

def endgame_score_connectfour_faster(board, is_current_player_maximizer):
    """Given an endgame board, returns an endgame score with abs(score) >= 1000,
    returning larger absolute scores for winning sooner."""
    score = endgame_score_connectfour(board, is_current_player_maximizer)
    # return last rounds' players winning piece, assign to a score
    multiplier = 4/board.count_pieces(current_player=False) + 1
    return score*multiplier

def heuristic_connectfour(board, is_current_player_maximizer):
    """Given a non-endgame board, returns a heuristic score with
    abs(score) < 1000, where higher numbers indicate that the board is better
    for the maximizer."""
    chains_curr = board.get_all_chains(current_player=True)
    chains_prev = board.get_all_chains(current_player=False)
    heuristic_score = 0
    for i, j in zip(chains_curr, chains_prev):
        if len(i) == 1:
            heuristic_score += 1
        elif len(i) == 2:
            heuristic_score += 10
        elif len(i) == 3:
            heuristic_score += 100
        if len(j) == 1:
            heuristic_score -= 1
        elif len(j) == 2:
            heuristic_score -= 10
        elif len(j) == 3:
            heuristic_score -= 100
    if is_current_player_maximizer:
        return heuristic_score
    else:
        return -heuristic_score


# Now we can create AbstractGameState objects for Connect Four, using some of
# the functions you implemented above.  You can use the following examples to
# test your dfs and minimax implementations in Part 2.

# This AbstractGameState represents a new ConnectFourBoard, before the game has started:
state_starting_connectfour = AbstractGameState(snapshot = ConnectFourBoard(),
                                 is_game_over_fn = is_game_over_connectfour,
                                 generate_next_states_fn = next_boards_connectfour,
                                 endgame_score_fn = endgame_score_connectfour_faster)

# This AbstractGameState represents the ConnectFourBoard "NEARLY_OVER" from boards.py:
state_NEARLY_OVER = AbstractGameState(snapshot = NEARLY_OVER,
                                 is_game_over_fn = is_game_over_connectfour,
                                 generate_next_states_fn = next_boards_connectfour,
                                 endgame_score_fn = endgame_score_connectfour_faster)

# This AbstractGameState represents the ConnectFourBoard "BOARD_UHOH" from boards.py:
state_UHOH = AbstractGameState(snapshot = BOARD_UHOH,
                                 is_game_over_fn = is_game_over_connectfour,
                                 generate_next_states_fn = next_boards_connectfour,
                                 endgame_score_fn = endgame_score_connectfour_faster)


#### Part 2: Searching a Game Tree #############################################

# Note: Functions in Part 2 use the AbstractGameState API, not ConnectFourBoard.

def dfs_maximizing(state) :
    """Performs depth-first search to find path with highest endgame score.
    Returns a tuple containing:
     0. the best path (a list of AbstractGameState objects),
     1. the score of the leaf node (a number), and
     2. the number of static evaluations performed (a number)"""
    agenda = [[state]]
    best_path, best_score, static_val = None, None, 0

    while agenda:
        firstPath = agenda.pop(0)
        node = firstPath[-1]
        child = node.generate_next_states()
        # reach leaf node
        if not child:
            curr_score = node.get_endgame_score(is_current_player_maximizer=True)
            static_val += 1
            if (best_score is None) or (curr_score > best_score):
                best_path, best_score = firstPath, curr_score
        # not reaching leaf node
        else:
            for n in child:
                if n not in firstPath:
                    agenda = ([firstPath + [n]]) + agenda
    return (best_path, best_score, static_val)


# Uncomment the line below to try your dfs_maximizing on an
# AbstractGameState representing the games tree "GAME1" from toytree.py:

# pretty_print_dfs_type(dfs_maximizing(GAME1))


def minimax_endgame_search(state, maximize=True) :
    """Performs minimax search, searching all leaf nodes and statically
    evaluating all endgame scores.  Same return type as dfs_maximizing."""
    agenda = [[state]]
    best_path, best_score, static_val = None, None, 0
    next_states = state.generate_next_states()

    if not next_states:
        return [state], state.get_endgame_score(is_current_player_maximizer=maximize), 1

    if maximize:
        for n in next_states:
            new_search_result = minimax_endgame_search(n, not maximize)
            static_val += new_search_result[-1]

            if (best_score is None) or new_search_result[-2] > best_score:
                best_path = [state] + new_search_result[-3]
                best_score = new_search_result[-2]
    else:
        for n in next_states:
            new_search_result = minimax_endgame_search(n, not maximize)
            static_val += new_search_result[-1]

            if (best_score is None) or new_search_result[-2] < best_score:
                best_path = [state] + new_search_result[-3]
                best_score = new_search_result[-2]
    return (best_path, best_score, static_val)


# Uncomment the line below to try your minimax_endgame_search on an
# AbstractGameState representing the ConnectFourBoard "NEARLY_OVER" from boards.py:

#pretty_print_dfs_type(minimax_endgame_search(state_NEARLY_OVER))


def minimax_search(state, heuristic_fn=always_zero, depth_limit=INF, maximize=True) :
    """Performs standard minimax search. Same return type as dfs_maximizing."""
    agenda = [[state]]
    best_path, best_score, static_val = None, None, 0
    next_states = state.generate_next_states()

    if not next_states:
        return [state], state.get_endgame_score(is_current_player_maximizer=maximize), 1

    if depth_limit == 0:
        return [state], heuristic_fn(state.get_snapshot(), maximize), 1

    if maximize:
        for n in next_states:
            new_search_result = minimax_search(n, heuristic_fn,  depth_limit-1, not maximize)
            static_val += new_search_result[-1]

            if (best_score is None) or new_search_result[-2] > best_score:
                best_path = [state] + new_search_result[-3]
                best_score = new_search_result[-2]
    else:
        for n in next_states:
            new_search_result = minimax_search(n, heuristic_fn,  depth_limit-1, not maximize)
            static_val += new_search_result[-1]

            if (best_score is None) or new_search_result[-2] < best_score:
                best_path = [state] + new_search_result[-3]
                best_score = new_search_result[-2]
    return (best_path, best_score, static_val)


# Uncomment the line below to try minimax_search with "BOARD_UHOH" and
# depth_limit=1. Try increasing the value of depth_limit to see what happens:

#pretty_print_dfs_type(minimax_search(state_UHOH, heuristic_fn=heuristic_connectfour, depth_limit=5))


def minimax_search_alphabeta(state, alpha=-INF, beta=INF, heuristic_fn=always_zero,
                             depth_limit=INF, maximize=True) :
    """"Performs minimax with alpha-beta pruning. Same return type 
    as dfs_maximizing."""
    agenda = [[state]]
    best_path, best_score, static_val = None, None, 0
    next_states = state.generate_next_states()

    if not next_states:
        return [state], state.get_endgame_score(is_current_player_maximizer=maximize), 1

    if depth_limit == 0:
        return [state], heuristic_fn(state.get_snapshot(), maximize), 1

    if maximize:
        for n in next_states:
            new_search_result = minimax_search_alphabeta(n, alpha, beta, heuristic_fn,  depth_limit-1, not maximize)
            static_val += new_search_result[-1]

            if (best_score is None) or new_search_result[-2] > best_score:
                best_path = [state] + new_search_result[-3]
                best_score = new_search_result[-2]
                # add pruning
                alpha = max(best_score, alpha)
                if alpha >= beta:
                    return (best_path, alpha, static_val)
    else:
        for n in next_states:
            new_search_result = minimax_search_alphabeta(n,alpha, beta, heuristic_fn,  depth_limit-1, not maximize)
            static_val += new_search_result[-1]

            if (best_score is None) or new_search_result[-2] < best_score:
                best_path = [state] + new_search_result[-3]
                best_score = new_search_result[-2]
                beta = min(best_score, beta)
                # add pruning
                if alpha >= beta:
                    return (best_path, beta, static_val)
    return (best_path, best_score, static_val)


# Uncomment the line below to try minimax_search_alphabeta with "BOARD_UHOH" and
# depth_limit=4. Compare with the number of evaluations from minimax_search for
# different values of depth_limit.

# pretty_print_dfs_type(minimax_search_alphabeta(state_UHOH, heuristic_fn=heuristic_connectfour, depth_limit=4))


def progressive_deepening(state, heuristic_fn=always_zero, depth_limit=INF,
                          maximize=True) :
    """Runs minimax with alpha-beta pruning. At each level, updates anytime_value
    with the tuple returned from minimax_search_alphabeta. Returns anytime_value."""
    anytime = AnytimeValue()
    #make iterative calls to minimax_search_alphabeta, increasing the depth each time
    for depth in range(1, depth_limit+1):
        res = minimax_search_alphabeta(state, alpha=-INF, beta=INF, heuristic_fn =heuristic_fn , depth_limit= depth, maximize=maximize)
        anytime.set_value(res)
    return anytime

# Uncomment the line below to try progressive_deepening with "BOARD_UHOH" and
# depth_limit=4. Compare the total number of evaluations with the number of
# evaluations from minimax_search or minimax_search_alphabeta.

# progressive_deepening(state_UHOH, heuristic_fn=heuristic_connectfour, depth_limit=4).pretty_print()


# Progressive deepening is NOT optional. However, you may find that 
#  the tests for progressive deepening take a long time. If you would
#  like to temporarily bypass them, set this variable False. You will,
#  of course, need to set this back to True to pass all of the local
#  and online tests.
TEST_PROGRESSIVE_DEEPENING = True
if not TEST_PROGRESSIVE_DEEPENING:
    def not_implemented(*args): raise NotImplementedError
    progressive_deepening = not_implemented


#### Part 3: Multiple Choice ###################################################

ANSWER_1 = '4'

ANSWER_2 = '1'

ANSWER_3 = '4'

ANSWER_4 = '5'


#### SURVEY ###################################################

NAME = 'Jiahui Tang'
COLLABORATORS = 'N/A'
HOW_MANY_HOURS_THIS_LAB_TOOK = '4'
WHAT_I_FOUND_INTERESTING = 'building each minmax search algorithm on top of each other'
WHAT_I_FOUND_BORING = 'implementation and debug, it\'s challenging'
SUGGESTIONS = 'N/A'
