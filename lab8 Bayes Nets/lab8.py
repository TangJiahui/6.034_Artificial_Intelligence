# MIT 6.034 Lab 8: Bayesian Inference
# Written by 6.034 staff

from nets import *


#### Part 1: Warm-up; Ancestors, Descendents, and Non-descendents ##############

def get_ancestors(net, var):
    "Return a set containing the ancestors of var"
    ancestor_set = net.get_parents(var)
    for p in net.get_parents(var):
        ancestor_set.update(get_ancestors(net, p))
    return ancestor_set

def get_descendants(net, var):
    "Returns a set containing the descendants of var"
    descendant_set = net.get_children(var)
    for p in net.get_children(var):
        descendant_set.update(get_descendants(net, p))
    return descendant_set

def get_nondescendants(net, var):
    "Returns a set containing the non-descendants of var"
    non_desc = set(net.get_variables())
    desc = get_descendants(net,var)
    # taking diff to exclude descendants
    non_desc.difference_update(desc)
    # remove var itself
    non_desc.discard(var)
    return non_desc


#### Part 2: Computing Probability #############################################

def simplify_givens(net, var, givens):
    """
    If givens include every parent of var and no descendants, returns a
    simplified list of givens, keeping only parents.  Does not modify original
    givens.  Otherwise, if not all parents are given, or if a descendant is
    given, returns original givens.
    """
    desc = get_descendants(net,var)
    simplified_given = {}

    # check if any descendant is given
    for i in givens:
        if i in desc:
            return givens

    # check if all parents are given
    if not net.get_parents(var).issubset(givens):
        return givens

    # simplifying
    for i in givens:
        if i in net.get_parents(var):
            simplified_given[i] = givens[i]
    return simplified_given

    
def probability_lookup(net, hypothesis, givens=None):
    "Looks up a probability in the Bayes net, or raises LookupError"
    var = list(hypothesis)[0]
    try:
        if givens is None:
            return net.get_probability(hypothesis)
        else:
            return net.get_probability(hypothesis, simplify_givens(net, var, givens))
    except LookupError:
        raise LookupError
    except ValueError:
        raise LookupError

def probability_joint(net, hypothesis):
    "Uses the chain rule to compute a joint probability"
    v_lst = net.topological_sort()
    v_lst.reverse()
    conditionals = hypothesis.copy()
    prob = 1

    # calculate from child
    for v in v_lst:
        h = {v: conditionals.pop(v)}
        if conditionals == {}:
            term = probability_lookup(net, h, None)
        else:
            term = probability_lookup(net, h, conditionals)
        prob *= term
    return prob
    
def probability_marginal(net, hypothesis):
    "Computes a marginal probability as a sum of joint probabilities"
    joint_probs_lst = net.combinations(net.get_variables(), hypothesis)
    prob = 0
    for j in joint_probs_lst:
        prob += probability_joint(net, j)
    return prob

def probability_conditional(net, hypothesis, givens=None):
    "Computes a conditional probability as a ratio of marginal probabilities"
    # if givens is None, the "conditional" probability
    # is really just a marginal or joint probability.
    if givens is None:
        return probability_marginal(net, hypothesis)

    # edge case checking
    for i in hypothesis:
        if i in givens:
            if hypothesis[i] != givens[i]:
                return 0

    # ratio
    return probability_marginal(net, dict(hypothesis, **givens))/probability_marginal(net, givens)
    
def probability(net, hypothesis, givens=None):
    "Calls previous functions to compute any probability"
    return probability_conditional(net, hypothesis, givens)


#### Part 3: Counting Parameters ###############################################

def number_of_parameters(net):
    """
    Computes the minimum number of parameters required for the Bayes net.
    """
    params = 0
    for v in net.get_variables():
        if len(net.get_parents(v)) == 0:
            # we dont need all, as we can derive it by 1-the rest
            params += (len(net.get_domain(v)) - 1)

        else:
            s = 1
            # product of all parent domain
            for p in net.get_parents(v):
                s *= len(net.get_domain(p))
            params += (len(net.get_domain(v)) - 1) * s

    return params


#### Part 4: Independence ######################################################

def is_independent(net, var1, var2, givens=None):
    """
    Return True if var1, var2 are conditionally independent given givens,
    otherwise False. Uses numerical independence.
    """
    combinations = net.combinations([var1, var2])
    # for all combinations of values of two vars
    for c in combinations:
        if givens is None:
            # check marginally independent
            probA = probability(net, {var1: c[var1]}, None)
            probA_B = probability(net, {var1: c[var1]}, {var2: c[var2]})
        else:
            # check conditionally independent given givens
            probA = probability(net, {var1: c[var1]}, givens)
            probA_B = probability(net, {var1: c[var1]}, dict(givens, **{var2: c[var2]}))

        # if any P(A) != P(A|B,givens), return False
        if not approx_equal(probA, probA_B, epsilon=0.0000000001):
            return False
    return True


    
def is_structurally_independent(net, var1, var2, givens=None):
    """
    Return True if var1, var2 are conditionally independent given givens,
    based on the structure of the Bayes net, otherwise False.
    Uses structural independence only (not numerical independence).
    """
    # step 1: draw ancestral graph for all variables mentioned in the probability expression

    # ancestral graph for var 1, var 2
    ancestors_graph = get_ancestors(net, var1).union(get_ancestors(net, var2))

    # union ancestral graph for givens set
    if givens is not None:
        for v in givens:
            ancestors_graph = get_ancestors(net, v).union(ancestors_graph)
        givens_keys = list(givens.keys())
    else:
        givens_keys = []

    # add all variables mentioned in the probability expression to list
    ancestors_lst = list(ancestors_graph)
    simplified_net = net.subnet(ancestors_graph.union(set([var1, var2] + givens_keys)))


    # step 2: Link parents
    for a in ancestors_graph:
        children_a = simplified_net.get_children(a)
        # mark a as checked
        ancestors_lst.remove(a)
        # for the rest, check if a and b have common child
        # draw an undirected edge (line) between them
        for b in ancestors_lst:
            children_b = simplified_net.get_children(b)
            if len(children_a.intersection(children_b)) != 0:
                simplified_net.link(a, b)

    # step 3: Disorient
    bidir_net = simplified_net.make_bidirectional()

    # step 4: Delete givens
    if givens is not None:
        #erase givens
        for v in givens:
             bidir_net.remove_variable(v)

    # step 5: Read the answer off the graph.
    # if variables are disconnected, guarantee to be independent
    if bidir_net.find_path(var1, var2) is None:
        return True

    return False


#### SURVEY ####################################################################

NAME = 'Jiahui Tang'
COLLABORATORS = 'None'
HOW_MANY_HOURS_THIS_LAB_TOOK = '3'
WHAT_I_FOUND_INTERESTING = 'independence check'
WHAT_I_FOUND_BORING = 'None'
SUGGESTIONS = 'None'
