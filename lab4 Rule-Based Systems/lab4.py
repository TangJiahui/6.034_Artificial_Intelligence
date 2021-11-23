# MIT 6.034 Lab 4: Rule-Based Systems
# Written by 6.034 staff

from production import IF, AND, OR, NOT, THEN, DELETE, forward_chain, pretty_goal_tree
from data import *
import pprint

pp = pprint.PrettyPrinter(indent=1)
pprint = pp.pprint

#### Part 1: Multiple Choice #########################################

ANSWER_1 = '2'

ANSWER_2 = '4'

ANSWER_3 = '2'

ANSWER_4 = '0'

ANSWER_5 = '3'

ANSWER_6 = '1'

ANSWER_7 = '0'

#### Part 2: Transitive Rule #########################################

# Fill this in with your rule 
transitive_rule = IF( AND('(?x) beats (?y)','(?y) beats (?z)'), THEN('(?x) beats (?z)'))

# You can test your rule by uncommenting these pretty print statements
#  and observing the results printed to your screen after executing lab1.py
#pprint(forward_chain([transitive_rule], abc_data))
#pprint(forward_chain([transitive_rule], poker_data))
# pprint(forward_chain([transitive_rule], minecraft_data))


#### Part 3: Family Relations #########################################

# Define your rules here. We've given you an example rule whose lead you can follow:
# friend_rule = IF( AND("person (?x)", "person (?y)"), THEN ("friend (?x) (?y)", "friend (?y) (?x)") )

self_rule = IF("person (?x)", THEN ("self (?x) (?x)"))

parent_child = IF( AND("parent (?x) (?y)"), THEN ("child (?y) (?x)") )
parent_child_rev = IF( AND("child (?x) (?y)"), THEN ("parent (?y) (?x)") )

# sibling
sib = IF( AND("parent (?x) (?y)", "parent (?x) (?z)", NOT ("self (?y) (?z)")), THEN ("sibling (?y) (?z)", "sibling (?z) (?y)") )
sib_rev = IF( "sibling (?y) (?z)", THEN ("sibling (?z) (?y)") )

# cousin
cou = IF( AND("parent (?a) (?x)", "parent (?b) (?y)", "sibling (?a) (?b)", NOT ("sibling (?x) (?y)"), NOT ("self (?x) (?y)")), THEN ("cousin (?x) (?y)", "cousin (?y) (?x)") )
cou_rev = IF("cousin (?y) (?z)", THEN ("cousin (?z) (?y)") )

# grand
grandparent = IF( AND("parent (?x) (?y)", "parent (?y) (?z)"), THEN ("grandparent (?x) (?z)") )
grandparent_rev = IF( AND("child (?x) (?y)", "child (?y) (?z)"), THEN ("grandchild (?x) (?z)") )
grandparent_ext = IF("grandparent (?x) (?y)", THEN ("grandchild (?y) (?x)") )


# Add your rules to this list:
family_rules = [ self_rule, parent_child, parent_child_rev, sib, sib_rev, cou, cou_rev, grandparent, grandparent_rev, grandparent_ext]

# Uncomment this to test your data on the Simpsons family:
# pprint(forward_chain(family_rules, simpsons_data, verbose=True))

# These smaller datasets might be helpful for debugging:
# pprint(forward_chain(family_rules, sibling_test_data, verbose=True))
# pprint(forward_chain(family_rules, grandparent_test_data, verbose=True))

# The following should generate 14 cousin relationships, representing 7 pairs
# of people who are cousins:
harry_potter_family_cousins = [
    relation for relation in
    forward_chain(family_rules, harry_potter_family_data, verbose=False)
    if "cousin" in relation ]

# To see if you found them all, uncomment this line:
# pprint(harry_potter_family_cousins)


#### Part 4: Backward Chaining #########################################

# Import additional methods for backchaining
from production import PASS, FAIL, match, populate, simplify, variables

def backchain_to_goal_tree(rules, hypothesis):
    """
    Takes a hypothesis (string) and a list of rules (list
    of IF objects), returning an AND/OR tree representing the
    backchain of possible statements we may need to test
    to determine if this hypothesis is reachable or not.

    This method should return an AND/OR tree, that is, an
    AND or OR object, whose constituents are the subgoals that
    need to be tested. The leaves of this tree should be strings
    (possibly with unbound variables), *not* AND or OR objects.
    Make sure to use simplify(...) to flatten trees where appropriate.
    """
    # hypothesis itself be added in OR node
    statement = OR([hypothesis])
    for r in rules:
        possible_options = match(r.consequent(), hypothesis)
        #print(possible_options)
        condition = None
        if possible_options is not None:
            antec = r.antecedent()
            if len(possible_options) > 0:
                condition = populate(antec, possible_options)
            else:
                condition = antec

        if isinstance(condition, str):
            statement.append(simplify(backchain_to_goal_tree(rules, condition)))
        elif isinstance(condition, AND):
            antec_matches = []
            # instantiate those same variables in the antecedent
            for ant in condition:
                antec_matches.append(backchain_to_goal_tree(rules, ant))
            statement.append(simplify(AND(antec_matches)))
        elif isinstance(condition, OR):
            antec_matches = []
            for ant in condition:
                antec_matches.append(backchain_to_goal_tree(rules, ant))
            statement.append(simplify(OR(antec_matches)))
    return simplify(OR(statement))


# Uncomment this to test out your backward chainer:
# pretty_goal_tree(backchain_to_goal_tree(zookeeper_rules, 'opus is a penguin'))

test11_rule = (
                  IF(AND('(?x) has (?y)', '(?x) has (?z)'),
                     THEN('(?x) has (?y) and (?z)'), []),
                  IF('(?x) has rhythm and music',
                     THEN('(?x) could not ask for anything more'), []))
test11_hypo = "gershwin could not ask for anything more"
#backchain_to_goal_tree(test11_rule, test11_hypo)
#pretty_goal_tree(backchain_to_goal_tree(test11_rule, test11_hypo))


test13_rule = ( [IF('a', THEN('b'), []),
                 IF('b', THEN('c i'), []),
                 IF(OR('c (?x)', 'd (?x)'), THEN('e (?x)'), []),
                 IF(AND('c (?x)', 'e (?x)'), THEN('f (?x) j'), []),
                 IF(OR('f (?x) (?y)', 'f (?y) (?x)'), THEN('g (?x) (?y)'), [])])
test13_hypo = "g i j"

#pretty_goal_tree(backchain_to_goal_tree(test13_rule, test13_hypo))


#### Survey #########################################

NAME = 'Jiahui Tang'
COLLABORATORS = 'None'
HOW_MANY_HOURS_THIS_LAB_TOOK = '3'
WHAT_I_FOUND_INTERESTING = 'family tree, backward chaining'
WHAT_I_FOUND_BORING = ''
SUGGESTIONS = 'None'


###########################################################
### Ignore everything below this line; for testing only ###
###########################################################

# The following lines are used in the tester. DO NOT CHANGE!
print("(Doing forward chaining. This may take a minute.)")
transitive_rule_poker = forward_chain([transitive_rule], poker_data)
transitive_rule_abc = forward_chain([transitive_rule], abc_data)
transitive_rule_minecraft = forward_chain([transitive_rule], minecraft_data)
family_rules_simpsons = forward_chain(family_rules, simpsons_data)
family_rules_harry_potter_family = forward_chain(family_rules, harry_potter_family_data)
family_rules_sibling = forward_chain(family_rules, sibling_test_data)
family_rules_grandparent = forward_chain(family_rules, grandparent_test_data)
family_rules_anonymous_family = forward_chain(family_rules, anonymous_family_test_data)
family_rules_black = forward_chain(family_rules, black_data)
