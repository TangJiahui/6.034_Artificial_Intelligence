# MIT 6.034 Lab 9: Boosting (Adaboost)
# Written by 6.034 staff

from math import log as ln
from utils import *


#### Part 1: Helper functions ##################################################

def initialize_weights(training_points):
    """Assigns every training point a weight equal to 1/N, where N is the number
    of training points.  Returns a dictionary mapping points to weights."""
    return {i: make_fraction(1, len(training_points)) for i in training_points}

def calculate_error_rates(point_to_weight, classifier_to_misclassified):
    """Given a dictionary mapping training points to their weights, and another
    dictionary mapping classifiers to the training points they misclassify,
    returns a dictionary mapping classifiers to their error rates."""
    result = {}
    for i in classifier_to_misclassified:
        error_rate = 0
        for j in classifier_to_misclassified[i]:
            error_rate += point_to_weight[j]
        result[i] = error_rate
    return result

def pick_best_classifier(classifier_to_error_rate, use_smallest_error=True):
    """Given a dictionary mapping classifiers to their error rates, returns the
    best* classifier, or raises NoGoodClassifiersError if best* classifier has
    error rate 1/2.  best* means 'smallest error rate' if use_smallest_error
    is True, otherwise 'error rate furthest from 1/2'."""
    if use_smallest_error:
        # add a secondary t[0] to break tie alphabetically, sorting by name of classifier as its secondary field
        best_c = min(classifier_to_error_rate.items(), key = lambda t: (t[1], t[0]))
    else:
        best_c = min(classifier_to_error_rate.items(), key = lambda t: (-abs(make_fraction(1,2) - make_fraction(t[1])),t[0]))
    
    # best_c = ('classifier', error_rate)
    if best_c is None or best_c[1] == make_fraction(1,2):
        raise NoGoodClassifiersError
    else:
        return best_c[0]


def calculate_voting_power(error_rate):
    """Given a classifier's error rate (a number), returns the voting power
    (aka alpha, or coefficient) for that classifier."""
    # flip decision if error_rate > 0.5
    e = error_rate
    # 1/2 * ln((1-ε)/ε)
    if e == 0:
        return INF
    elif e == 1:
        return -INF
    else:
        return 1/2 * ln((1-e)/e)


def get_overall_misclassifications(H, training_points, classifier_to_misclassified):
    """Given an overall classifier H, a list of all training points, and a
    dictionary mapping classifiers to the training points they misclassify,
    returns a set containing the training points that H misclassifies.
    H is represented as a list of (classifier, voting_power) tuples."""
    misclassifid = []
    for p in training_points:
        corr, wrong = 0, 0
        for i, j in H:
            # if p is misclassified by classifier i
            if p in classifier_to_misclassified[i]:
                wrong += j
            else:
                corr += j
        final_score_for_p = corr - wrong
        # tie or more wrong voting will be misclassfied
        if final_score_for_p <= 0:
            misclassifid.append(p)
    return set(misclassifid)
            
        
def is_good_enough(H, training_points, classifier_to_misclassified, mistake_tolerance=0):
    """Given an overall classifier H, a list of all training points, a
    dictionary mapping classifiers to the training points they misclassify, and
    a mistake tolerance (the maximum number of allowed misclassifications),
    returns False if H misclassifies more points than the tolerance allows,
    otherwise True.  H is represented as a list of (classifier, voting_power)
    tuples."""
    num = len(get_overall_misclassifications(H, training_points, classifier_to_misclassified))
    if num <= mistake_tolerance:
        return True
    else:
        return False


def update_weights(point_to_weight, misclassified_points, error_rate):
    """Given a dictionary mapping training points to their old weights, a list
    of training points misclassified by the current weak classifier, and the
    error rate of the current weak classifier, returns a dictionary mapping
    training points to their new weights.  This function is allowed (but not
    required) to modify the input dictionary point_to_weight."""
    new_weight = {}
    for p in point_to_weight:
        if p in misclassified_points:
            # 1/2 * 1/ε * (old weight)
            new_weight[p] = make_fraction(1,2) * make_fraction(1, error_rate) * point_to_weight[p]
        else:
            # 1/2 * 1/(1-ε) * (old weight)
            new_weight[p] = make_fraction(1,2) * make_fraction(1, 1-error_rate) * point_to_weight[p]
    return new_weight


#### Part 2: Adaboost ##########################################################

def adaboost(training_points, classifier_to_misclassified,
             use_smallest_error=True, mistake_tolerance=0, max_rounds=INF):
    """Performs the Adaboost algorithm for up to max_rounds rounds.
    Returns the resulting overall classifier H, represented as a list of
    (classifier, voting_power) tuples."""
    H = []
    round = 0
    #Initialize all training points' weights.
    point_to_weight = initialize_weights(training_points)

    while round < max_rounds:
        round += 1
        
        #Compute the error rate of each weak classifier.
        classifier_to_error_rate = calculate_error_rates(point_to_weight, classifier_to_misclassified)

        #Pick the "best" weak classifier h, by some definition of "best."
        # will throw error if no classifier remains
        try:
            h = pick_best_classifier(classifier_to_error_rate, use_smallest_error)
        except NoGoodClassifiersError:
            return H

        #Use the error rate of h to compute the voting power for h.
        voting_power_h = calculate_voting_power(classifier_to_error_rate[h])

        #Append h, along with its voting power, to the ensemble classifier H.
        H.append((h, voting_power_h))

        #Update weights in preparation for the next round.
        misclassified_points = classifier_to_misclassified[h]
        error_rate = classifier_to_error_rate[h]
        point_to_weight = update_weights(point_to_weight, misclassified_points, error_rate)

        #Repeat steps 2-7 until no good classifier remains, we have reached some max number of iterations, or H is "good enough."`
        if is_good_enough(H, training_points, classifier_to_misclassified, mistake_tolerance):
            return H
    return H


#### SURVEY ####################################################################

NAME = 'Jiahui Tang'
COLLABORATORS = 'None'
HOW_MANY_HOURS_THIS_LAB_TOOK = '3h'
WHAT_I_FOUND_INTERESTING = 'adaboost algorithm combining things together'
WHAT_I_FOUND_BORING = 'debug, break tie'
SUGGESTIONS = 'None'
