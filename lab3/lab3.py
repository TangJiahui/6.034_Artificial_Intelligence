# MIT 6.034 Lab 3: Constraint Satisfaction Problems
# Written by 6.034 staff

from constraint_api import *
from test_problems import get_pokemon_problem


#### Part 1: Warmup ############################################################

def has_empty_domains(csp) :
    """Returns True if the problem has one or more empty domains, otherwise False"""
    for i in csp.domains:
        if csp.domains[i] == []:
            return True
    return False

def check_all_constraints(csp) :
    """Return False if the problem's assigned values violate some constraint,
    otherwise True"""
    # no value assigned
    if csp.assignments == {}:
        return True
    # check all constraints
    for c in csp.get_all_constraints():
        # get values of two variables and check constraints
        node1, node2 = csp.get_assignment(c.var1), csp.get_assignment(c.var2)
        if node1 is not None and node2 is not None:
            if not c.check(node1, node2):
                return False
    return True

#### Part 2: Depth-First Constraint Solver #####################################
def solve_constraint_dfs(problem) :
    """
    Solves the problem using depth-first search.  Returns a tuple containing:
    1. the solution (a dictionary mapping variables to assigned values)
    2. the number of extensions made (the number of problems popped off the agenda).
    If no solution was found, return None as the first element of the tuple.
    """
    if has_empty_domains(problem):
        return None, 1

    agenda = [problem]
    num_extensions = 0
    while agenda:
        csp = agenda.pop(0)
        num_extensions += 1
        if check_all_constraints(csp) and not has_empty_domains(csp):
            curr_var = csp.pop_next_unassigned_var()
            if curr_var is None:
                return csp.assignments, num_extensions
            new_problem_lst = []
            for possible_val in csp.get_domain(curr_var):
                # create a new problem
                new_problem_lst.append(csp.copy().set_assignment(curr_var, possible_val))
            agenda = new_problem_lst + agenda
    return None, num_extensions



# QUESTION 1: How many extensions does it take to solve the Pokemon problem
#    with DFS?

# Hint: Use get_pokemon_problem() to get a new copy of the Pokemon problem
#    each time you want to solve it with a different search method.

# print (solve_constraint_dfs(get_pokemon_problem()))
ANSWER_1 = 20


#### Part 3: Forward Checking ##################################################
def eliminate_from_neighbors(csp, var) :
    """
    Eliminates incompatible values from var's neighbors' domains, modifying
    the original csp.  Returns an alphabetically sorted list of the neighboring
    variables whose domains were reduced, with each variable appearing at most
    once. If no domains were reduced, returns empty list.
    If a domain is reduced to size 0, quits immediately and returns None.
    """
    reduced_domain = []
    for nbr in csp.get_neighbors(var):
        reduce_val = []
        cons = csp.constraints_between(var, nbr)
        for w in csp.get_domain(nbr):
            v_lst = csp.get_domain(var)
            for con in cons:
                flag = 0
                fineset = []
                # check neighbor w with every v
                for v in v_lst:
                    if con.check(v, w):
                        fineset += [v]
                        flag = 1
                v_lst = fineset
                if flag == 0:
                    reduce_val += [w]
                    break
        if reduce_val != []:
            reduced_domain += [nbr]
            for rval in reduce_val:
                csp.eliminate(nbr, rval)
            if csp.get_domain(nbr) == []:
                return None
    return sorted(reduced_domain)

# Because names give us power over things (you're free to use this alias)
forward_check = eliminate_from_neighbors

def solve_constraint_forward_checking(problem) :
    """
    Solves the problem using depth-first search with forward checking.
    Same return type as solve_constraint_dfs.
    """
    if has_empty_domains(problem):
        return None, 1
    agenda = [problem]
    num_extensions = 0
    while agenda:
        csp = agenda.pop(0)
        num_extensions += 1
        if check_all_constraints(csp) and not has_empty_domains(csp):
            curr_var = csp.pop_next_unassigned_var()
            if curr_var is None:
                return csp.assignments, num_extensions
            new_problem_lst = []
            for possible_val in csp.get_domain(curr_var):
                # create a new problem
                new_csp = csp.copy().set_assignment(curr_var, possible_val)
                forward_check(new_csp, curr_var)
                new_problem_lst.append(new_csp)
            agenda = new_problem_lst + agenda
    return None, num_extensions



# QUESTION 2: How many extensions does it take to solve the Pokemon problem
#    with DFS and forward checking?


#print (solve_constraint_forward_checking(get_pokemon_problem()))
ANSWER_2 = 9


#### Part 4: Domain Reduction ##################################################

def domain_reduction(csp, queue=None) :
    """
    Uses constraints to reduce domains, propagating the domain reduction
    to all neighbors whose domains are reduced during the process.
    If queue is None, initializes propagation queue by adding all variables in
    their default order. 
    Returns a list of all variables that were dequeued, in the order they
    were removed from the queue.  Variables may appear in the list multiple times.
    If a domain is reduced to size 0, quits immediately and returns None.
    This function modifies the original csp.
    """
    dequeue = []
    if queue is None:
        queue = csp.get_all_variables()
    while queue:
        var = queue.pop(0)
        reduced_domain = forward_check(csp, var)
        if reduced_domain is None:
            return None
        for reduced_d in reduced_domain:
            if reduced_d not in queue:
                queue.append(reduced_d)
        dequeue.append(var)
    return dequeue

# QUESTION 3: How many extensions does it take to solve the Pokemon problem
#    with DFS (no forward checking) if you do domain reduction before solving it?

# csp = get_pokemon_problem()
# domain_reduction(csp)
# print(solve_constraint_dfs(csp))
ANSWER_3 = 6


def solve_constraint_propagate_reduced_domains(problem) :
    """
    Solves the problem using depth-first search with forward checking and
    propagation through all reduced domains.  Same return type as
    solve_constraint_dfs.
    """
    if has_empty_domains(problem):
        return None, 1
    agenda = [problem]
    num_extensions = 0
    while agenda:
        csp = agenda.pop(0)
        num_extensions += 1
        if check_all_constraints(csp) and not has_empty_domains(csp):
            curr_var = csp.pop_next_unassigned_var()
            if curr_var is None:
                return csp.assignments, num_extensions
            new_problem_lst = []
            for possible_val in csp.get_domain(curr_var):
                # create a new problem
                new_csp = csp.copy().set_assignment(curr_var, possible_val)
                domain_reduction(new_csp, queue=[curr_var])
                new_problem_lst.append(new_csp)
            agenda = new_problem_lst + agenda
    return None, num_extensions


# QUESTION 4: How many extensions does it take to solve the Pokemon problem
#    with forward checking and propagation through reduced domains?

# print(solve_constraint_propagate_reduced_domains(get_pokemon_problem()))
ANSWER_4 = 7


#### Part 5A: Generic Domain Reduction #########################################

def propagate(enqueue_condition_fn, csp, queue=None) :
    """
    Uses constraints to reduce domains, modifying the original csp.
    Uses enqueue_condition_fn to determine whether to enqueue a variable whose
    domain has been reduced. Same return type as domain_reduction.
    """
    dequeue = []
    if queue is None:
        queue = csp.get_all_variables()
    while queue:
        var = queue.pop(0)
        reduced_domain = forward_check(csp, var)
        if reduced_domain is None:
            return None
        for reduced_d in reduced_domain:
            if reduced_d not in queue and enqueue_condition_fn(csp, reduced_d):
                queue.append(reduced_d)
        dequeue.append(var)
    return dequeue

def condition_domain_reduction(csp, var) :
    """Returns True if var should be enqueued under the all-reduced-domains
    condition, otherwise False"""
    return True

def condition_singleton(csp, var) :
    """Returns True if var should be enqueued under the singleton-domains
    condition, otherwise False"""
    return len(csp.get_domain(var)) == 1

def condition_forward_checking(csp, var) :
    """Returns True if var should be enqueued under the forward-checking
    condition, otherwise False"""
    return False


#### Part 5B: Generic Constraint Solver ########################################

def solve_constraint_generic(problem, enqueue_condition=None) :
    """
    Solves the problem, calling propagate with the specified enqueue
    condition (a function). If enqueue_condition is None, uses DFS only.
    Same return type as solve_constraint_dfs.
    """
    if has_empty_domains(problem):
        return None, 1
    agenda = [problem]
    num_extensions = 0
    while agenda:
        csp = agenda.pop(0)
        num_extensions += 1
        if check_all_constraints(csp) and not has_empty_domains(csp):
            curr_var = csp.pop_next_unassigned_var()
            if curr_var is None:
                return csp.assignments, num_extensions
            new_problem_lst = []
            for possible_val in csp.get_domain(curr_var):
                # create a new problem
                new_csp = csp.copy().set_assignment(curr_var, possible_val)
                if enqueue_condition is not None:
                    propagate(enqueue_condition, new_csp, [curr_var])
                new_problem_lst.append(new_csp)
            agenda = new_problem_lst + agenda
    return None, num_extensions

# QUESTION 5: How many extensions does it take to solve the Pokemon problem
#    with forward checking and propagation through singleton domains? (Don't
#    use domain reduction before solving it.)

# print(solve_constraint_generic(get_pokemon_problem(), enqueue_condition = condition_singleton))
ANSWER_5 = 8


#### Part 6: Defining Custom Constraints #######################################

def constraint_adjacent(m, n) :
    """Returns True if m and n are adjacent, otherwise False.
    Assume m and n are ints."""
    return m-n == 1 or n-m == 1

def constraint_not_adjacent(m, n) :
    """Returns True if m and n are NOT adjacent, otherwise False.
    Assume m and n are ints."""
    return not constraint_adjacent(m, n)

def all_different(variables) :
    """Returns a list of constraints, with one difference constraint between
    each pair of variables."""
    con_lst = []
    for i in range(len(variables)):
        for j in range(i+1, len(variables)):
            con_lst.append(Constraint(variables[i], variables[j], constraint_different))
    return con_lst


#### SURVEY ####################################################################

NAME = 'Jiahui Tang'
COLLABORATORS = 'None'
HOW_MANY_HOURS_THIS_LAB_TOOK = '4'
WHAT_I_FOUND_INTERESTING = 'different cfs solve function'
WHAT_I_FOUND_BORING = 'eliminate_from_neighbors is challenging'
SUGGESTIONS = 'None'
