# MIT 6.034 Lab 1: Search

from tester import make_test, get_tests
from search import UndirectedGraph, Edge
from lab1 import (generic_dfs, generic_bfs, generic_hill_climbing,
                  generic_best_first, generic_branch_and_bound,
                  generic_branch_and_bound_with_heuristic,
                  generic_branch_and_bound_with_extended_set, generic_a_star,
                  is_admissible, is_consistent,
                  TEST_GENERIC_BEAM, TEST_HEURISTICS)

lab_number = 1
from read_graphs import get_graphs
all_graphs = get_graphs()
GRAPH_0 = all_graphs['GRAPH_0']
GRAPH_1 = all_graphs['GRAPH_1']
GRAPH_2 = all_graphs['GRAPH_2']
GRAPH_3 = all_graphs['GRAPH_3']
GRAPH_FOR_HEURISTICS = all_graphs['GRAPH_FOR_HEURISTICS']
GRAPH_FOR_HEURISTICS_TRICKY = all_graphs['GRAPH_FOR_HEURISTICS_TRICKY']

##########################################################################
### OFFLINE TESTS (HARDCODED ANSWERS)

#### PART 1: Helper Functions #########################################

make_test(type = 'FUNCTION',  #TEST 1
          getargs = [GRAPH_1, ['a', 'c', 'b', 'd']],
          testanswer = lambda val, original_val=None: val == 11,
          expected_val = 11,
          name = 'path_length')

make_test(type = 'FUNCTION',  #TEST 2
          getargs = [GRAPH_2, ['D', 'C', 'A', 'D', 'E', 'G', 'F']],
          testanswer = lambda val, original_val=None: val == 53,
          expected_val = 53,
          name = 'path_length')

make_test(type = 'FUNCTION',  #TEST 3
          getargs = [GRAPH_1, ['a']],
          testanswer = lambda val, original_val=None: val == 0,
          expected_val = 0,
          name = 'path_length')


make_test(type = 'FUNCTION',  #TEST 4
          getargs = [['node1', 'node3', 'node2']],
          testanswer = lambda val, original_val=None: val == False,
          expected_val = False,
          name = 'has_loops')

make_test(type = 'FUNCTION',  #TEST 5
          getargs = [['d', 'a', 'c', 'a', 'b']],
          testanswer = lambda val, original_val=None: val == True,
          expected_val = True,
          name = 'has_loops')

make_test(type = 'FUNCTION',  #TEST 6
          getargs = [list('SBCA')],
          testanswer = lambda val, original_val=None: val == False,
          expected_val = False,
          name = 'has_loops')

make_test(type = 'FUNCTION',  #TEST 7
          getargs = [['X']],
          testanswer = lambda val, original_val=None: val == False,
          expected_val = False,
          name = 'has_loops')


extensions_test1_answer = [['n2', 'n1'], ['n2', 'n3']]
make_test(type = 'FUNCTION',  #TEST 8
          getargs = [GRAPH_0, ['n2']],
          testanswer = lambda val, original_val=None: val == extensions_test1_answer,
          expected_val = extensions_test1_answer,
          name = 'extensions')

extensions_test2_answer = [['n2', 'n3', 'n4']]
make_test(type = 'FUNCTION',  #TEST 9
          getargs = [GRAPH_0, ['n2', 'n3']],
          testanswer = lambda val, original_val=None: val == extensions_test2_answer,
          expected_val = extensions_test2_answer,
          name = 'extensions')

extensions_test3_answer = [['S', 'A', 'C', 'E', 'D'],
                           ['S', 'A', 'C', 'E', 'F'],
                           ['S', 'A', 'C', 'E', 'G']]
make_test(type = 'FUNCTION',  #TEST 10
          getargs = [GRAPH_2, ['S', 'A', 'C', 'E']],
          testanswer = lambda val, original_val=None: val == extensions_test3_answer,
          expected_val = extensions_test3_answer,
          name = 'extensions')

# Checks intentionally-unordered neighbors in extensions
extensions_test4_graph = UndirectedGraph(list("abcdefgh"), edges=[Edge("a",l,0) for l in "hgfebcd"])
extensions_test4_answer = [["a",l] for l in "bcdefgh"]
make_test(type = 'FUNCTION',  #TEST 11
          getargs = [extensions_test4_graph, ["a"]],
          testanswer = lambda val, original_val=None: val == extensions_test4_answer,
          expected_val = extensions_test4_answer,
          name = 'extensions')

sortby_test1_answer = ['c', 'a', 'b', 'd']
make_test(type = 'FUNCTION',  #TEST 12
          getargs = [GRAPH_1, 'c', ['d', 'a', 'b', 'c']],
          testanswer = lambda val, original_val=None: val == sortby_test1_answer,
          expected_val = sortby_test1_answer,
          name = 'sort_by_heuristic')

sortby_test2_answer = ['H', 'D', 'F', 'C', 'C', 'A', 'B']
make_test(type = 'FUNCTION',  #TEST 13
          getargs = [GRAPH_2, 'G', ['D', 'C', 'B', 'H', 'A', 'F', 'C']],
          testanswer = lambda val, original_val=None: val == sortby_test2_answer,
          expected_val = sortby_test2_answer,
          name = 'sort_by_heuristic')

sortby_test3_answer = ['G', 'X', 'Y', 'F']
make_test(type = 'FUNCTION',  #TEST 14
          getargs = [GRAPH_2, 'G', ['X', 'Y', 'G', 'F']],
          testanswer = lambda val, original_val=None: val == sortby_test3_answer,
          expected_val = sortby_test3_answer,
          name = 'sort_by_heuristic')

#### PART 2: Basic Search #########################################

basic_dfs_1_answer = list('abcd')
make_test(type = 'FUNCTION',  #TEST 15
          getargs = [GRAPH_1, 'a', 'd'],
          testanswer = lambda val, original_val=None: val == basic_dfs_1_answer,
          expected_val = basic_dfs_1_answer,
          name = 'basic_dfs')

basic_dfs_2_answer = list('SACDEFG')
make_test(type = 'FUNCTION',  #TEST 16
          getargs = [GRAPH_2, 'S', 'G'],
          testanswer = lambda val, original_val=None: val == basic_dfs_2_answer,
          expected_val = basic_dfs_2_answer,
          name = 'basic_dfs')

basic_dfs_3_answer = list('HDACBY')
make_test(type = 'FUNCTION',  #TEST 17
          getargs = [GRAPH_2, 'H', 'Y'],
          testanswer = lambda val, original_val=None: val == basic_dfs_3_answer,
          expected_val = basic_dfs_3_answer,
          name = 'basic_dfs')

make_test(type = 'FUNCTION',  #TEST 18
          getargs = [GRAPH_1, 'a', 'z'],
          testanswer = lambda val, original_val=None: val == None,
          expected_val = None,
          name = 'basic_dfs')

basic_bfs_1_answer = list('abd')
make_test(type = 'FUNCTION',  #TEST 19
          getargs = [GRAPH_1, 'a', 'd'],
          testanswer = lambda val, original_val=None: val == basic_bfs_1_answer,
          expected_val = basic_bfs_1_answer,
          name = 'basic_bfs')

basic_bfs_2_answer = list('SACEG')
make_test(type = 'FUNCTION',  #TEST 20
          getargs = [GRAPH_2, 'S', 'G'],
          testanswer = lambda val, original_val=None: val == basic_bfs_2_answer,
          expected_val = basic_bfs_2_answer,
          name = 'basic_bfs')

basic_bfs_3_answer = list('HDCY')
make_test(type = 'FUNCTION',  #TEST 21
          getargs = [GRAPH_2, 'H', 'Y'],
          testanswer = lambda val, original_val=None: val == basic_bfs_3_answer,
          expected_val = basic_bfs_3_answer,
          name = 'basic_bfs')

make_test(type = 'FUNCTION',  #TEST 22
          getargs = [GRAPH_1, 'a', 'z'],
          testanswer = lambda val, original_val=None: val == None,
          expected_val = None,
          name = 'basic_bfs')

#### PART 3: Generic Search #######################################

search_args = {"dfs": generic_dfs,
               "bfs": generic_bfs,
               "hill_climbing": generic_hill_climbing,
               "best_first": generic_best_first,
               "branch_and_bound": generic_branch_and_bound,
               "branch_and_bound_with_heuristic": generic_branch_and_bound_with_heuristic,
               "branch_and_bound_with_extended_set": generic_branch_and_bound_with_extended_set,
               "a_star": generic_a_star}

# Tests 23-42
search_tests = [['dfs', GRAPH_1, 'a', 'd', 'abcd'],
                ['dfs', GRAPH_2, 'S', 'G', 'SACDEFG'],
                ['bfs', GRAPH_1, 'a', 'd', 'abd'],
                ['bfs', GRAPH_2, 'S', 'G', 'SACEG'],
                ['hill_climbing', GRAPH_1, 'a', 'd', 'abcd'], # depends on lexicographic tie-breaking
                ['hill_climbing', GRAPH_2, 'S', 'G', 'SADHFG'],
                ['hill_climbing', GRAPH_3, 's', 'g', 'sywg'],
                ['best_first', GRAPH_1, 'a', 'd', 'abcd'], # depends on lexicographic tie-breaking
                ['best_first', GRAPH_2, 'S', 'G', 'SADEG'],
                ['best_first', GRAPH_3, 's', 'g', 'sywg'],
                ['branch_and_bound', GRAPH_1, 'a', 'd', 'acd'],
                ['branch_and_bound', GRAPH_2, 'S', 'G', 'SBCEG'],
                ['branch_and_bound', GRAPH_3, 's', 'g', 'sxwg'],
                ['branch_and_bound_with_heuristic', GRAPH_1, 'a', 'd', 'acd'],
                ['branch_and_bound_with_heuristic', GRAPH_2, 'S', 'G', 'SBCEG'],
                ['branch_and_bound_with_heuristic', GRAPH_3, 's', 'g', 'szwg'],
                ['branch_and_bound_with_extended_set', GRAPH_1, 'a', 'd', 'acd'],
                ['branch_and_bound_with_extended_set', GRAPH_2, 'S', 'G', 'SBCEG'],
                ['branch_and_bound_with_extended_set', GRAPH_3, 's', 'g', 'sxwg'],
                ['a_star', GRAPH_1, 'a', 'd', 'acd'],
                ['a_star', GRAPH_2, 'S', 'G', 'SBCEG'],
                ['a_star', GRAPH_3, 's', 'g', 'sywg']]

# Execute the tests
for arg_list in search_tests:
    if arg_list[0] != 'beam':
        (lambda method, graph, startNode, endNode, answer_string :
         make_test(type = 'NESTED_FUNCTION',
                   getargs = [search_args[method], [graph, startNode, endNode]],
                   testanswer = (lambda val, original_val=None:
                                 val == list(answer_string)),
                   expected_val = "({} search result) {}".format(method, list(answer_string)),
                   name = 'generic_search')
         )(*arg_list[:5])

bb_uses_extended_set_tests = [["generic_branch_and_bound", False],
                              ["generic_branch_and_bound_with_heuristic", False],
                              ["generic_branch_and_bound_with_extended_set", True]]
def get_bb_extended_testanswer_fn(answer):
    def bb_extended_testanswer(val, original_val=None):
        if val == [None, None, None, None]:
            raise NotImplementedError
        return val[3] == answer
    return bb_extended_testanswer

for arg_list in bb_uses_extended_set_tests:  #Tests 43-45
    (lambda method, answer :
     make_test(type = 'VALUE',
               getargs = method,
               testanswer = get_bb_extended_testanswer_fn(answer),
               expected_val = "Correct boolean value indicating whether search uses extended set",
               name = method)
     )(*arg_list)

# Checks that non-existent goal node --> no path found. 
for search_method in search_args: #Tests 46-53
    (lambda method :
        make_test(type = 'NESTED_FUNCTION',
                  getargs = [search_args[method], [GRAPH_1, 'a', 'z']],
                  testanswer = (lambda val, original_val=None: val == None),
                  expected_val = None,
                  name = "generic_search")
    )(search_method)


#### PART 4: Heuristics ###################################################

make_test(type = 'FUNCTION',  #TEST 54
          getargs = [GRAPH_1, 'd'],
          testanswer = lambda val, original_val=None: val == True,
          expected_val = True,
          name = 'is_admissible')

make_test(type = 'FUNCTION',  #TEST 55
          getargs = [GRAPH_1, 'c'],
          testanswer = lambda val, original_val=None: val == True,
          expected_val = True,
          name = 'is_admissible')

make_test(type = 'FUNCTION',  #TEST 56
          getargs = [GRAPH_2, 'G'],
          testanswer = lambda val, original_val=None: val == True,
          expected_val = True,
          name = 'is_admissible')

make_test(type = 'FUNCTION',  #TEST 57
          getargs = [GRAPH_3, 'g'],
          testanswer = lambda val, original_val=None: val == False,
          expected_val = False,
          name = 'is_admissible')

test_admissible_graph = GRAPH_FOR_HEURISTICS_TRICKY.copy()
test_admissible_graph.set_heuristic({'G': {'S': 0, 'A': 10, 'B': 5, 'C': 0, 'D': 0, 'G': 0}})
make_test(type = 'FUNCTION',  #TEST 58
          getargs = [test_admissible_graph, 'G'],
          testanswer = lambda val, original_val=None: val == False,
          expected_val = "{} (This one's tricky! How are you checking a node's admissibility?)".format(False),
          name = 'is_admissible')

make_test(type = 'FUNCTION',  #TEST 59
          getargs = [GRAPH_1, 'd'],
          testanswer = lambda val, original_val=None: val == True,
          expected_val = True,
          name = 'is_consistent')

make_test(type = 'FUNCTION',  #TEST 60
          getargs = [GRAPH_1, 'c'],
          testanswer = lambda val, original_val=None: val == True,
          expected_val = True,
          name = 'is_consistent')

make_test(type = 'FUNCTION',  #TEST 61
          getargs = [GRAPH_2, 'G'],
          testanswer = lambda val, original_val=None: val == False,
          expected_val = False,
          name = 'is_consistent')

make_test(type = 'FUNCTION',  #TEST 62
          getargs = [GRAPH_3, 'g'],
          testanswer = lambda val, original_val=None: val == False,
          expected_val = False,
          name = 'is_consistent')


#### PART 5: Multiple Choice ###################################################

# British Museum gives an exhaustive listing of all rooms in 
# the house. The other three algorithms would stop after
# finding one bedroom.
ANSWER_1_getargs = "ANSWER_1"
def ANSWER_1_testanswer(val, original_val = None):
    if val == '':
        raise NotImplementedError
    return str(val) == '2'
make_test(type = 'VALUE',  #TEST 63
          getargs = ANSWER_1_getargs,
          testanswer = ANSWER_1_testanswer,
          expected_val = "correct value of ANSWER_1 ('1', '2', '3', or '4')",
          name = ANSWER_1_getargs)

# Of 1, 2, and 4, Branch and Bound with Extended Set is the 
# winner here. Having access to an extended set is a massive
# advantage when stuck in a maze; BFS would just
# continually extend redundant nodes. 
# A* is out because we don't have access to a heuristic, and
# hence it's no better than BB with Extended Set. You could
# argue that the answer could be A* with a heuristic that is
# always 0; this is a true, but the simpler answer is BB with
# Extended Set. 
ANSWER_2_getargs = "ANSWER_2"
def ANSWER_2_testanswer(val, original_val = None):
    if val == '':
        raise NotImplementedError
    return str(val) == '4'
make_test(type = 'VALUE',  #TEST 64
          getargs = ANSWER_2_getargs,
          testanswer = ANSWER_2_testanswer,
          expected_val = "correct value of ANSWER_2 ('1', '2', '3', or '4')",
          name = ANSWER_2_getargs)

# "As few towns as possible" should stick out to you. Recall 
# that BFS always gives an optimal path in terms of the number
# of nodes visited (not in terms of path length).
ANSWER_3_getargs = "ANSWER_3"
def ANSWER_3_testanswer(val, original_val = None):
    if val == '':
        raise NotImplementedError
    return str(val) == '1'
make_test(type = 'VALUE',  #TEST 65
          getargs = ANSWER_3_getargs,
          testanswer = ANSWER_3_testanswer,
          expected_val = "correct value of ANSWER_3 ('1', '2', '3', or '4')",
          name = ANSWER_3_getargs)

# A* is the clear winner, because you have access to a heuristic 
# and can remember how far you've travelled.
ANSWER_4_getargs = "ANSWER_4"
def ANSWER_4_testanswer(val, original_val = None):
    if val == '':
        raise NotImplementedError
    return str(val) == '3'
make_test(type = 'VALUE',  #TEST 66
          getargs = ANSWER_4_getargs,
          testanswer = ANSWER_4_testanswer,
          expected_val = "correct value of ANSWER_4 ('1', '2', '3', or '4')",
          name = ANSWER_4_getargs)


#### Optional tests ############################################################

beam_search_tests = [['beam', GRAPH_2, 'S', 'G', 2, 'SBYCEG'],
                     # ['beam', GRAPH_1, 'a', 'd', 2, 'abd'], #depends on lexicographic tie-breaking
                     ['beam', GRAPH_2, 'S', 'G', 1, 'SADHFG'],
                     ['beam', GRAPH_2, 'S', 'G', 3, 'SADEG']]

if TEST_GENERIC_BEAM:
    from lab1 import generic_beam, beam
    # no-path-found test for beam:
    make_test(type = 'FUNCTION',
              getargs = [GRAPH_2, 'C', 'G', 1],
              testanswer = (lambda val, original_val=None: val == None),
              expected_val = None,
              name = 'beam')

    for arg_list in beam_search_tests:
        (lambda method, graph, startNode, endNode, beam_width, answer_string :
         make_test(type = 'NESTED_FUNCTION',
                   getargs = [generic_beam,
                              [graph, startNode, endNode, beam_width]],
                   testanswer = (lambda val, original_val=None:
                                 val == list(answer_string)),
                   expected_val = list(answer_string),
                   name = 'generic_search')
         )(*arg_list[:6])


if TEST_HEURISTICS:
    from lab1 import a_star

    def test_heuristic(heuristic_dict, should_be_admissible, should_be_consistent,
                       should_be_optimal_a_star):
        if None in list(heuristic_dict['G'].values()): return False
        shortest_path = ['S', 'A', 'C', 'G']
        GRAPH_FOR_HEURISTICS.set_heuristic(heuristic_dict)
        match_adm = should_be_admissible == None or should_be_admissible == is_admissible(GRAPH_FOR_HEURISTICS, 'G')
        match_con = should_be_consistent == None or should_be_consistent == is_consistent(GRAPH_FOR_HEURISTICS, 'G')
        a_star_result = a_star(GRAPH_FOR_HEURISTICS, 'S', 'G')
        match_opt = should_be_optimal_a_star == None \
            or (should_be_optimal_a_star == (a_star_result == shortest_path))
        return match_adm and match_con and match_opt 

    make_test(type = 'VALUE',
              getargs = 'heuristic_1',
              testanswer = (lambda val, original_val=None:
                            test_heuristic(val, True, True, None)),
              expected_val = 'Correct numerical values for heuristic to fit specifications',
              name = 'heuristic_1')

    make_test(type = 'VALUE',
              getargs = 'heuristic_2',
              testanswer = (lambda val, original_val=None:
                            test_heuristic(val, True, False, None)),
              expected_val = 'Correct numerical values for heuristic to fit specifications',
              name = 'heuristic_2')

    make_test(type = 'VALUE',
              getargs = 'heuristic_3',
              testanswer = (lambda val, original_val=None:
                            test_heuristic(val, True, None, False)),
              expected_val = 'Correct numerical values for heuristic to fit specifications',
              name = 'heuristic_3')

    make_test(type = 'VALUE',
              getargs = 'heuristic_4',
              testanswer = (lambda val, original_val=None:
                            test_heuristic(val, True, False, True)),
              expected_val = 'Correct numerical values for heuristic to fit specifications',
              name = 'heuristic_4')
