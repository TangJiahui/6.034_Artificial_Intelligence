# MIT 6.034 Lab 0: Getting Started

from tester import make_test, get_tests
from point_api import Point
import random
random.seed() # Change to "random.seed(n)" to make the random tests always return the same value

lab_number = 0


#### Multiple Choice ###########################################################

ANSWER_1_getargs = "ANSWER_1"  #TEST 1
def ANSWER_1_testanswer(val, original_val = None):
    if val == None or val == '':
        raise NotImplementedError
    return val == False
make_test(type = "VALUE",
          getargs = ANSWER_1_getargs,
          testanswer = ANSWER_1_testanswer,
          expected_val = ("(the correct answer, either True or False)"),
          name = ANSWER_1_getargs)

ANSWER_2_getargs = "ANSWER_2"  #TEST 2
def ANSWER_2_testanswer(val, original_val = None):
    if val == None or val == '':
        raise NotImplementedError
    return val == "D"
make_test(type = "VALUE",
          getargs = ANSWER_2_getargs,
          testanswer = ANSWER_2_testanswer,
          expected_val = ('(the correct letter "A", "B", "C", or "D")'),
          name = ANSWER_2_getargs)


#### Warmup ####################################################################

def is_even_0_getargs():  #TEST 3
    return [0]
def is_even_0_testanswer(val, original_val = None):
    return val == True
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_even_0_getargs,
          testanswer = is_even_0_testanswer,
          expected_val = "True",
          name = "is_even")

def is_even_1_getargs():  #TEST 4
    return [3]
def is_even_1_testanswer(val, original_val = None):
    return val == False
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_even_1_getargs,
          testanswer = is_even_1_testanswer,
          expected_val = "False",
          name = "is_even")

def is_even_2_getargs():  #TEST 5
    return [120]
def is_even_2_testanswer(val, original_val = None):
    return val == True
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_even_2_getargs,
          testanswer = is_even_2_testanswer,
          expected_val = "True",
          name = "is_even")

def is_even_3_getargs():  #TEST 6
    return [-3]
def is_even_3_testanswer(val, original_val = None):
    return val == False
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_even_3_getargs,
          testanswer = is_even_3_testanswer,
          expected_val = "False",
          name = "is_even")

def is_even_4_getargs():  #TEST 7
    return [-7.02]
def is_even_4_testanswer(val, original_val = None):
    return val == False
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_even_4_getargs,
          testanswer = is_even_4_testanswer,
          expected_val = "False",
          name = "is_even")

def approx_equal(a, b):
    return abs(a - b) < 0.001


def decrement_0_getargs():  #TEST 8
    return [2.5]
def decrement_0_testanswer(val, original_val = None):
    return approx_equal(val, 1.5)
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = decrement_0_getargs,
          testanswer = decrement_0_testanswer,
          expected_val = "1.5",
          name = "decrement")

def decrement_1_getargs():  #TEST 9
    return [1]
def decrement_1_testanswer(val, original_val = None):
    return approx_equal(val, 0)
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = decrement_1_getargs,
          testanswer = decrement_1_testanswer,
          expected_val = "0",
          name = "decrement")

def decrement_2_getargs():  #TEST 10
    return [-1.5]
def decrement_2_testanswer(val, original_val = None):
    return approx_equal(val, 0)
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = decrement_2_getargs,
          testanswer = decrement_2_testanswer,
          expected_val = "0",
          name = "decrement")

def cube_0_getargs():  #TEST 11
    return [10]
def cube_0_testanswer(val, original_val = None):
    return approx_equal(val, 1000)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = cube_0_getargs,
          testanswer = cube_0_testanswer,
          expected_val = "1000",
          name = 'cube')

def cube_1_getargs():  #TEST 12
    return [1]
def cube_1_testanswer(val, original_val = None):
    return approx_equal(val, 1)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = cube_1_getargs,
          testanswer = cube_1_testanswer,
          expected_val = "1",
          name = 'cube')

def cube_2_getargs():  #TEST 13
    return [-5]
def cube_2_testanswer(val, original_val = None):
    return approx_equal(val, -125)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = cube_2_getargs,
          testanswer = cube_2_testanswer,
          expected_val = "-125",
          name = 'cube')

cube_3_arg = [-1]
def cube_3_getargs():  #TEST 14
    cube_3_arg[0] = random.randint(1,1000)
    return cube_3_arg
def cube_3_testanswer(val, original_val = None):
    return approx_equal(val, cube_3_arg[0]**3)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = cube_3_getargs,
          testanswer = cube_3_testanswer,
          expected_val = "a number between 1 and 1000000000 (this test is randomly generated)",
          name = 'cube')

def cube_4_getargs():  #TEST 15
    return [2.5]
def cube_4_testanswer(val, original_val = None):
    return approx_equal(val, 15.625)
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = cube_4_getargs,
          testanswer = cube_4_testanswer,
          expected_val = "~15.625",
          name = "cube")


#### Iteration #################################################################

def is_prime_0_getargs():  #TEST 16
    return [-3]
def is_prime_0_testanswer(val, original_val = None):
    return val == False
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_prime_0_getargs,
          testanswer = is_prime_0_testanswer,
          expected_val = "False",
          name = "is_prime")

def is_prime_1_getargs():  #TEST 17
    return [0]
def is_prime_1_testanswer(val, original_val = None):
    return val == False
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_prime_1_getargs,
          testanswer = is_prime_1_testanswer,
          expected_val = "False",
          name = "is_prime")

def is_prime_2_getargs():  #TEST 18
    return [1.5]
def is_prime_2_testanswer(val, original_val = None):
    return val == False
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_prime_2_getargs,
          testanswer = is_prime_2_testanswer,
          expected_val = "False",
          name = "is_prime")

def is_prime_3_getargs():  #TEST 19
    return [2]
def is_prime_3_testanswer(val, original_val = None):
    return val == True
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_prime_3_getargs,
          testanswer = is_prime_3_testanswer,
          expected_val = "True",
          name = "is_prime")

def is_prime_4_getargs():  #TEST 20
    return [5]
def is_prime_4_testanswer(val, original_val = None):
    return val == True
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_prime_4_getargs,
          testanswer = is_prime_4_testanswer,
          expected_val = "True",
          name = "is_prime")

def is_prime_5_getargs():  #TEST 21
    return [3323]
def is_prime_5_testanswer(val, original_val = None):
    return val == True
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_prime_5_getargs,
          testanswer = is_prime_5_testanswer,
          expected_val = "True",
          name = "is_prime")

def is_prime_6_getargs():  #TEST 22
    return [3400]
def is_prime_6_testanswer(val, original_val = None):
    return val == False
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = is_prime_6_getargs,
          testanswer = is_prime_6_testanswer,
          expected_val = "False",
          name = "is_prime")

def primes_up_to_0_getargs():  #TEST 23
    return [-2]
def primes_up_to_0_testanswer(val, original_val = None):
    return val == []
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = primes_up_to_0_getargs,
          testanswer = primes_up_to_0_testanswer,
          expected_val = "[]",
          name = "primes_up_to")

def primes_up_to_1_getargs():  #TEST 24
    return [1]
def primes_up_to_1_testanswer(val, original_val = None):
    return val == []
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = primes_up_to_1_getargs,
          testanswer = primes_up_to_1_testanswer,
          expected_val = "[]",
          name = "primes_up_to")

def primes_up_to_2_getargs():  #TEST 25
    return [2]
def primes_up_to_2_testanswer(val, original_val = None):
    return val == [2]
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = primes_up_to_2_getargs,
          testanswer = primes_up_to_2_testanswer,
          expected_val = "[2]",
          name = "primes_up_to")

def primes_up_to_3_getargs():  #TEST 26
    return [7.5]
def primes_up_to_3_testanswer(val, original_val = None):
    return val == [2, 3, 5, 7]
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = primes_up_to_3_getargs,
          testanswer = primes_up_to_3_testanswer,
          expected_val = "[2, 3, 5, 7]",
          name = "primes_up_to")

def primes_up_to_4_getargs():  #TEST 27
    return [11]
def primes_up_to_4_testanswer(val, original_val = None):
    return val == [2, 3, 5, 7, 11]
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = primes_up_to_4_getargs,
          testanswer = primes_up_to_4_testanswer,
          expected_val = "[2, 3, 5, 7, 11]",
          name = "primes_up_to")

def primes_up_to_5_getargs():  #TEST 28
    return [102]
def primes_up_to_5_testanswer(val, original_val = None):
    return val == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = primes_up_to_5_getargs,
          testanswer = primes_up_to_5_testanswer,
          expected_val = "(list of primes, in order, up to 102)",
          name = "primes_up_to")


#### Recursion #################################################################

def fibonacci_0_getargs():  #TEST 29
    return [1]
def fibonacci_0_testanswer(val, original_val = None):
    return val == 1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = fibonacci_0_getargs,
          testanswer = fibonacci_0_testanswer,
          expected_val = "1",
          name = 'fibonacci')

def fibonacci_1_getargs():  #TEST 30
    return [2]
def fibonacci_1_testanswer(val, original_val = None):
    return val == 1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = fibonacci_1_getargs,
          testanswer = fibonacci_1_testanswer,
          expected_val = "1",
          name = 'fibonacci')

def fibonacci_2_getargs():  #TEST 31
    return [12]
def fibonacci_2_testanswer(val, original_val = None):
    return val == 144
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = fibonacci_2_getargs,
          testanswer = fibonacci_2_testanswer,
          expected_val = "144",
          name = 'fibonacci')

def fibonacci_3_getargs():  #TEST 32
    return [5]
def fibonacci_3_testanswer(val, original_val = None):
    return val == 5
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = fibonacci_3_getargs,
          testanswer = fibonacci_3_testanswer,
          expected_val = "5",
          name = 'fibonacci')


def expression_depth_0_getargs():  #TEST 33
    return ['x']
def expression_depth_0_testanswer(val, original_val = None):
    return val == 0
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = expression_depth_0_getargs,
          testanswer = expression_depth_0_testanswer,
          expected_val = "0",
          name = 'expression_depth')

def expression_depth_1_getargs():  #TEST 34
    return [['expt', 'x', 2]]
def expression_depth_1_testanswer(val, original_val = None):
    return val == 1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = expression_depth_1_getargs,
          testanswer = expression_depth_1_testanswer,
          expected_val = "1",
          name = 'expression_depth')

def expression_depth_2_getargs():  #TEST 35
    return [['+', ['expt', 'x', 2], ['expt', 'y', 2]]]
def expression_depth_2_testanswer(val, original_val = None):
    return val == 2
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = expression_depth_2_getargs,
          testanswer = expression_depth_2_testanswer,
          expected_val = "2",
          name = 'expression_depth')

def expression_depth_3_getargs():  #TEST 36
    return [['/', ['expt', 'x', 5], ['expt', ['-', ['expt', 'x', 2], '1'], ['+', 5, 2, 3, 'w', 4]]]]
def expression_depth_3_testanswer(val, original_val = None):
    return val == 4
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = expression_depth_3_getargs,
          testanswer = expression_depth_3_testanswer,
          expected_val = "4",
          name = 'expression_depth')


#### Built-in data types #######################################################

def remove_from_string_0_getargs():  #TEST 37
    return ["catapult", ""]
def remove_from_string_0_testanswer(val, original_val = None):
    return val == "catapult"
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = remove_from_string_0_getargs,
          testanswer = remove_from_string_0_testanswer,
          expected_val = "catapult",
          name = "remove_from_string")

def remove_from_string_1_getargs():  #TEST 38
    return ["catapult", "t"]
def remove_from_string_1_testanswer(val, original_val = None):
    return val == "caapul"
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = remove_from_string_1_getargs,
          testanswer = remove_from_string_1_testanswer,
          expected_val = "caapul",
          name = "remove_from_string")

def remove_from_string_2_getargs():  #TEST 39
    return ["catapult", "ata"]
def remove_from_string_2_testanswer(val, original_val = None):
    return val == "cpul"
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = remove_from_string_2_getargs,
          testanswer = remove_from_string_2_testanswer,
          expected_val = "cpul",
          name = "remove_from_string")

def remove_from_string_3_getargs():  #TEST 40
    return ["catapult", "xyz"]
def remove_from_string_3_testanswer(val, original_val = None):
    return val == "catapult"
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = remove_from_string_3_getargs,
          testanswer = remove_from_string_3_testanswer,
          expected_val = "catapult",
          name = "remove_from_string")

def remove_from_string_4_getargs():  #TEST 41
    return ["", "xyz"]
def remove_from_string_4_testanswer(val, original_val = None):
    return val == ""
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = remove_from_string_4_getargs,
          testanswer = remove_from_string_4_testanswer,
          expected_val = "(empty string)",
          name = "remove_from_string")

# "zyxw" -> (4, list("zyxw"), 4)
def compute_string_properties_0_getargs():  #TEST 42
    return ["zyxw"]
def compute_string_properties_0_testanswer(val, original_val = None):
    return val == (4, list("zyxw"), 4)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = compute_string_properties_0_getargs,
          testanswer = compute_string_properties_0_testanswer,
          expected_val = str((4, list("zyxw"), 4)),
          name = 'compute_string_properties')

# "xxx" -> (3, list("xxx"), 1)
def compute_string_properties_1_getargs():  #TEST 43
    return ["xxx"]
def compute_string_properties_1_testanswer(val, original_val = None):
    return val == (3, list("xxx"), 1)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = compute_string_properties_1_getargs,
          testanswer = compute_string_properties_1_testanswer,
          expected_val = str((3, list("xxx"), 1)),
          name = 'compute_string_properties')

# "artificialintelligence" -> (22, list("ttrnnllliiiiigfeeeccaa"), 10)
def compute_string_properties_2_getargs():  #TEST 44
    return ["artificialintelligence"]
def compute_string_properties_2_testanswer(val, original_val = None):
    return val == (22, list("ttrnnllliiiiigfeeeccaa"), 10)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = compute_string_properties_2_getargs,
          testanswer = compute_string_properties_2_testanswer,
          expected_val = str((22, list("ttrnnllliiiiigfeeeccaa"), 10)),
          name = 'compute_string_properties')

# "" -> (0, [], 0)
def compute_string_properties_3_getargs():  #TEST 45
    return [""]
def compute_string_properties_3_testanswer(val, original_val = None):
    return val == (0, [], 0)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = compute_string_properties_3_getargs,
          testanswer = compute_string_properties_3_testanswer,
          expected_val = "(0, [], 0)",
          name = 'compute_string_properties')

def tally_letters_0_getargs():  #TEST 46
    return ["hello"]
def tally_letters_0_testanswer(val, original_val = None):
    return val == {"h": 1, "e": 1, "l": 2, "o": 1}
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = tally_letters_0_getargs,
          testanswer = tally_letters_0_testanswer,
          expected_val = str({"h": 1, "e": 1, "l": 2, "o": 1}),
          name = 'tally_letters')

def tally_letters_1_getargs():  #TEST 47
    return ["artificialintelligence"]
def tally_letters_1_testanswer(val, original_val = None):
    return val == {"a": 2, "c": 2, "e": 3, "f": 1, "g": 1, "i": 5, "l": 3,
                   "n": 2, "r": 1, "t": 2}
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = tally_letters_1_getargs,
          testanswer = tally_letters_1_testanswer,
          expected_val = str({"a": 2, "c": 2, "e": 3, "f": 1, "g": 1, "i": 5, "l": 3, "n": 2, "r": 1, "t": 2}),
          name = 'tally_letters')

def tally_letters_2_getargs():  #TEST 48
    return ["zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"]
def tally_letters_2_testanswer(val, original_val = None):
    return val == {"z": 60}
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = tally_letters_2_getargs,
          testanswer = tally_letters_2_testanswer,
          expected_val = str({"z": 60}),
          name = 'tally_letters')

def tally_letters_3_getargs():  #TEST 49
    return [""]
def tally_letters_3_testanswer(val, original_val = None):
    return val == {}
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = tally_letters_3_getargs,
          testanswer = tally_letters_3_testanswer,
          expected_val = "{}",
          name = 'tally_letters')


#### Functions that return functions ###########################################

# create a function that multiplies numbers by 5
def create_multiplier_function_0_getargs():  #TEST 50
    return [5]
def create_multiplier_function_0_testanswer(val, original_val = None):
    return val(3) == 15 and val(-10) == -50
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = create_multiplier_function_0_getargs,
          testanswer = create_multiplier_function_0_testanswer,
          expected_val = "(function that multiplies numbers by 5)",
          name = 'create_multiplier_function')

# create a function that multiplies numbers by 0
def create_multiplier_function_1_getargs():  #TEST 51
    return [0]
def create_multiplier_function_1_testanswer(val, original_val = None):
    return val(random.randint(2,10000)) == 0
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = create_multiplier_function_1_getargs,
          testanswer = create_multiplier_function_1_testanswer,
          expected_val = "(function that multiplies numbers by 0)",
          name = 'create_multiplier_function')

# create a function that multiplies numbers by 73
def create_multiplier_function_2_getargs():  #TEST 52
    return [73]
def create_multiplier_function_2_testanswer(val, original_val = None):
    rand_nums = [random.randint(-100,-2), random.randint(2,100), 0, 1]
    return all([val(n) == n*73 for n in rand_nums])
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = create_multiplier_function_2_getargs,
          testanswer = create_multiplier_function_2_testanswer,
          expected_val = "(function that multiplies numbers by 73)",
          name = 'create_multiplier_function')

def create_length_comparer_function_0_getargs():  #TEST 53
    return [True]
def create_length_comparer_function_0_testanswer(val, original_val = None):
    return val([], []) == True and val([], [2, 3]) == False and val(["catapult", "dog"], [[2, 3, 4], []]) == True
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = create_length_comparer_function_0_getargs,
          testanswer = create_length_comparer_function_0_testanswer,
          expected_val = "(function that returns True when two input lists are of equal length)",
          name = "create_length_comparer_function")

def create_length_comparer_function_1_getargs():  #TEST 54
    return [False]
def create_length_comparer_function_1_testanswer(val, original_val = None):
    return val([], []) == False and val([], [2, 3]) == True and val([2], []) == True and val(["catapult"], [[2, 3]]) == False
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = create_length_comparer_function_1_getargs,
          testanswer = create_length_comparer_function_1_testanswer,
          expected_val = "(function that returns True when two input lists are of different lengths)",
          name = "create_length_comparer_function")


#### Objects and APIs: Copying and modifing objects ##########################

point_A = Point(4,9)
point_B = Point(-2,0)
point_C = Point(5,5)
point_D = Point(-1,-100)
all_points = [point_A, point_B, point_C, point_D]
for p in all_points:
    p._constructed = False

def sum_of_coordinates_0_getargs():  #TEST 55
    return [point_A.copy()]
def sum_of_coordinates_0_testanswer(val, original_val = None):
    return val == 13
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = sum_of_coordinates_0_getargs,
          testanswer = sum_of_coordinates_0_testanswer,
          expected_val = "13",
          name = "sum_of_coordinates")

def sum_of_coordinates_1_getargs():  #TEST 56
    return [point_D.copy()]
def sum_of_coordinates_1_testanswer(val, original_val = None):
    return val == -101
make_test(type = "FUNCTION_ENCODED_ARGS",
          getargs = sum_of_coordinates_1_getargs,
          testanswer = sum_of_coordinates_1_testanswer,
          expected_val = "-101",
          name = "sum_of_coordinates")

def points_lists_eq(p1, p2, eq_fn, ordered=False):
    if len(p1) != len(p2):
        return False

    if(not ordered):
        # Order both lists by a unique identifier; we use .ID
        p1 = sorted(p1, key=lambda p: (p.getX(), p.getY()))
        p2 = sorted(p2, key=lambda p: (p.getX(), p.getY()))
    for i in range(len(p1)):
        if(not eq_fn(p1[i], p2[i])):
            return False
    return True

def constructed_p(point):
    return point._constructed

get_neighbors_0_input = point_A.copy()
def get_neighbors_0_getargs():  #TEST 57
    return [get_neighbors_0_input]
get_neighbors_0_expected = [[p.copy().setX(p.getX()+x).setY(p.getY()+y)
                             for (x,y) in [(-1,0),(1,0),(0,-1),(0,1)]]
                            for p in [get_neighbors_0_input]][0]
def get_neighbors_0_testanswer(val, original_val = None):
    return (points_lists_eq(val, get_neighbors_0_expected, Point.coords_equal)
      and get_neighbors_0_input.coords_equal(point_A)
      and all([not constructed_p(p) for p in val]))
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_neighbors_0_getargs,
          testanswer = get_neighbors_0_testanswer,
          expected_val = (str(get_neighbors_0_expected) + " (any order).\n"
            "Be sure not to call Point(__) directly or mutate the input!"),
          name = 'get_neighbors')

get_neighbors_1_input = point_B.copy()
def get_neighbors_1_getargs():  #TEST 58
    return [get_neighbors_1_input]
get_neighbors_1_expected = [[p.copy().setX(p.getX()+x).setY(p.getY()+y)
                             for (x,y) in [(-1,0),(1,0),(0,-1),(0,1)]]
                            for p in [get_neighbors_1_input]][0]
def get_neighbors_1_testanswer(val, original_val = None):
    return (points_lists_eq(val, get_neighbors_1_expected, Point.coords_equal)
      and get_neighbors_1_input.coords_equal(point_B)
      and all([not constructed_p(p) for p in val]))
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_neighbors_1_getargs,
          testanswer = get_neighbors_1_testanswer,
          expected_val = (str(get_neighbors_1_expected) + " (any order).\n"
            "Be sure not to call Point(__) directly or mutate the input!"),
          name = 'get_neighbors')

get_neighbors_2_input = point_C.copy()
def get_neighbors_2_getargs():  #TEST 59
    return [get_neighbors_2_input]
get_neighbors_2_expected = [[p.copy().setX(p.getX()+x).setY(p.getY()+y)
                             for (x,y) in [(-1,0),(1,0),(0,-1),(0,1)]]
                            for p in [get_neighbors_2_input]][0]
def get_neighbors_2_testanswer(val, original_val = None):
    return (points_lists_eq(val, get_neighbors_2_expected, Point.coords_equal)
      and get_neighbors_2_input.coords_equal(point_C)
      and all([not constructed_p(p) for p in val]))
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_neighbors_2_getargs,
          testanswer = get_neighbors_2_testanswer,
          expected_val = (str(get_neighbors_2_expected) + " (any order).\n"
            "Be sure not to call Point(__) directly or mutate the input!"),
          name = 'get_neighbors')


#### Using the "key" argument ##################################################

sort_points_by_Y_0_input = [p.copy() for p in [point_C, point_A]]
sort_points_by_Y_0_expected = sort_points_by_Y_0_input[::-1] # it just "happens" to work!
def sort_points_by_Y_0_getargs():  #TEST 60
    return [sort_points_by_Y_0_input]
def sort_points_by_Y_0_testanswer(val, original_val = None):
    return (len(val) == len(sort_points_by_Y_0_expected)
      and all([val[i].identical(sort_points_by_Y_0_expected[i]) for i in range(len(val))])
      and points_lists_eq(sort_points_by_Y_0_input, [point_C, point_A], Point.coords_equal, True)
      and all([not constructed_p(p) for p in val]))
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = sort_points_by_Y_0_getargs,
          testanswer = sort_points_by_Y_0_testanswer,
          expected_val = str(sort_points_by_Y_0_expected),
          name = 'sort_points_by_Y')

sort_points_by_Y_1_input = [p.copy() for p in all_points]
sort_points_by_Y_1_expected = sort_points_by_Y_1_input[:]
temp = sort_points_by_Y_1_expected[1]
sort_points_by_Y_1_expected[1] = sort_points_by_Y_1_expected[2]
sort_points_by_Y_1_expected[2] = temp
def sort_points_by_Y_1_getargs():  #TEST 61
    return [sort_points_by_Y_1_input]
def sort_points_by_Y_1_testanswer(val, original_val = None):
    return (len(val) == len(sort_points_by_Y_1_expected)
      and all([val[i].identical(sort_points_by_Y_1_expected[i]) for i in range(len(val))])
      and points_lists_eq(sort_points_by_Y_1_input, all_points, Point.coords_equal, True)
      and all([not constructed_p(p) for p in val]))
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = sort_points_by_Y_1_getargs,
          testanswer = sort_points_by_Y_1_testanswer,
          expected_val = str(sort_points_by_Y_1_expected),
          name = 'sort_points_by_Y')

furthest_right_point_0_input = [p.copy() for p in all_points]
def furthest_right_point_0_getargs():  #TEST 62
    return [furthest_right_point_0_input]
def furthest_right_point_0_testanswer(val, original_val = None):
    return (val.identical(furthest_right_point_0_input[2])
            and points_lists_eq(furthest_right_point_0_input, all_points, Point.coords_equal)
            and (not constructed_p(val)))
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = furthest_right_point_0_getargs,
          testanswer = furthest_right_point_0_testanswer,
          expected_val = str(point_C),
          name = 'furthest_right_point')

furthest_right_point_1_input = [p.copy() for p in [point_B, point_D]]
def furthest_right_point_1_getargs():  #TEST 63
    return [furthest_right_point_1_input]
def furthest_right_point_1_testanswer(val, original_val = None):
    return (val.identical(furthest_right_point_1_input[1])
            and points_lists_eq(furthest_right_point_1_input, [point_B, point_D], Point.coords_equal)
            and (not constructed_p(val)))
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = furthest_right_point_1_getargs,
          testanswer = furthest_right_point_1_testanswer,
          expected_val = str(point_D),
          name = 'furthest_right_point')


#### SURVEY ####################################################################

PYTHON_EXPERIENCE_getargs = 'PYTHON_EXPERIENCE'  #TEST 64
def PYTHON_EXPERIENCE_testanswer(val, original_val = None):
    if val == '':
        raise NotImplementedError
    return val in list("ABCDE")
make_test(type = 'VALUE',
          getargs = PYTHON_EXPERIENCE_getargs,
          testanswer = PYTHON_EXPERIENCE_testanswer,
          expected_val = '(a capital letter A, B, C, D, or E, as a string)',
          name = PYTHON_EXPERIENCE_getargs)

PROGRAMMING_EXPERIENCE_getargs = 'PROGRAMMING_EXPERIENCE'  #TEST 65
def PROGRAMMING_EXPERIENCE_testanswer(val, original_val = None):
    if val == '':
        raise NotImplementedError
    return val in list("ABCDE")
make_test(type = 'VALUE',
          getargs = PROGRAMMING_EXPERIENCE_getargs,
          testanswer = PROGRAMMING_EXPERIENCE_testanswer,
          expected_val = '(a capital letter A, B, C, D, or E, as a string)',
          name = PROGRAMMING_EXPERIENCE_getargs)

NAME_getargs = 'NAME'  #TEST 66
def NAME_testanswer(val, original_val = None):
    if val == None:
        raise NotImplementedError
    return ( isinstance(val, str) and val != '')
make_test(type = 'VALUE',
          getargs = NAME_getargs,
          testanswer = NAME_testanswer,
          expected_val = '(your name, as a string)',
          name = NAME_getargs)

COLLABORATORS_getargs = 'COLLABORATORS'  #TEST 67
def COLLABORATORS_testanswer(val, original_val = None):
    if val == None:
        raise NotImplementedError
    return isinstance(val, str)
make_test(type = 'VALUE',
          getargs = COLLABORATORS_getargs,
          testanswer = COLLABORATORS_testanswer,
          expected_val = ("(names of people you worked with, as a string, or "
                          + "empty string if you worked alone)"),
          name = COLLABORATORS_getargs)

HOW_MANY_HOURS_THIS_LAB_TOOK_getargs = 'HOW_MANY_HOURS_THIS_LAB_TOOK'  #TEST 68
def HOW_MANY_HOURS_THIS_LAB_TOOK_testanswer(val, original_val = None):
    if val == None:
        raise NotImplementedError
    return isinstance(val, (int, float, str)) and val != ''
make_test(type = 'VALUE',
          getargs = HOW_MANY_HOURS_THIS_LAB_TOOK_getargs,
          testanswer = HOW_MANY_HOURS_THIS_LAB_TOOK_testanswer,
          expected_val = ('(number of hours you spent on this lab, as a number '
                          +'or string)'),
          name = HOW_MANY_HOURS_THIS_LAB_TOOK_getargs)
