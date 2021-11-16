# MIT 6.034 Lab 7: Support Vector Machines
# Written by 6.034 staff

from svm_data import *
from functools import reduce


#### Part 1: Vector Math #######################################################

def dot_product(u, v):
    """Computes the dot product of two vectors u and v, each represented 
    as a tuple or list of coordinates. Assume the two vectors are the
    same length."""
    sum = 0
    for a, b in zip(u, v):
        sum += a*b
    return sum


def norm(v):
    """Computes the norm (length) of a vector v, represented
    as a tuple or list of coords."""
    return dot_product(v, v) ** 0.5


#### Part 2: Using the SVM Boundary Equations ##################################

def positiveness(svm, point):
    """Computes the expression (w dot x + b) for the given Point x."""
    return dot_product(svm.w, point) + svm.b

def classify(svm, point):
    """Uses the given SVM to classify a Point. Assume that the point's true
    classification is unknown.
    Returns +1 or -1, or 0 if point is on boundary."""
    if positiveness(svm, point) == 0:
        return 0
    elif positiveness(svm, point) > 0:
        return 1
    else:
        return -1

def margin_width(svm):
    """Calculate margin width based on the current boundary."""
    return 2/norm(svm.w)

def check_gutter_constraint(svm):
    """Returns the set of training points that violate one or both conditions:
        * gutter constraint (positiveness == classification, for support vectors)
        * training points must not be between the gutters
    Assumes that the SVM has support vectors assigned."""
    violate = []
    for point in svm.training_points:
        if point in svm.support_vectors and positiveness(svm, point) != point.classification:
            violate.append(point)
        elif abs(positiveness(svm, point)) < 1:
            violate.append(point)
    return set(violate)


#### Part 3: Supportiveness ####################################################

def check_alpha_signs(svm):
    """Returns the set of training points that violate either condition:
        * all non-support-vector training points have alpha = 0
        * all support vectors have alpha > 0
    Assumes that the SVM has support vectors assigned, and that all training
    points have alpha values assigned."""
    violate = []
    for point in svm.training_points:
        alpha = point.alpha
        if alpha < 0:
            violate.append(point)
        elif point in svm.support_vectors and alpha <= 0:
            violate.append(point)
        elif point not in svm.support_vectors and alpha != 0:
            violate.append(point)
    return set(violate)

def check_alpha_equations(svm):
    """Returns True if both Lagrange-multiplier equations are satisfied,
    otherwise False. Assumes that the SVM has support vectors assigned, and
    that all training points have alpha values assigned."""
    sum_equal4, sum_equal5 = 0, None
    for point in svm.training_points:
        sum_equal4 += point.classification * point.alpha
        if sum_equal5 is None:
            sum_equal5 = scalar_mult(point.classification * point.alpha, point.coords)
        else:
            sum_equal5 = vector_add(sum_equal5, scalar_mult(point.classification * point.alpha, point.coords))
    if sum_equal4 == 0 and svm.w == sum_equal5:
        return True
    else:
        return False

#### Part 4: Evaluating Accuracy ###############################################

def misclassified_training_points(svm):
    """Returns the set of training points that are classified incorrectly
    using the current decision boundary."""
    incorrect_points = []
    for point in svm.training_points:
        if classify(svm, point) != point.classification:
            incorrect_points.append(point)
    return set(incorrect_points)


#### Part 5: Training an SVM ###################################################
def update_svm_from_alphas(svm):
    """Given an SVM with training data and alpha values, use alpha values to
    update the SVM's support vectors, w, and b. Return the updated SVM."""
    support_vectors = []
    svm.w, svm.b = None, 0
    for point in svm.training_points:
        # support vector
        if point.alpha > 0:
            support_vectors.append(point)
        if svm.w is None:
            svm.w = scalar_mult(point.classification * point.alpha, point.coords)
        else:
            svm.w = vector_add(svm.w, scalar_mult(point.classification * point.alpha, point.coords))
    minb, maxb = None, None
    for point in support_vectors:
        value = point.classification - dot_product(svm.w, point.coords)
        if point.classification == -1:
            if minb is None:
                minb = value
            elif value < minb:
                minb = value
        elif point.classification == 1:
            if maxb is None:
                maxb = value
            elif value > maxb:
                maxb = value
    svm.b = (minb + maxb)/2
    svm.support_vectors = support_vectors
    return svm


#### Part 6: Multiple Choice ###################################################

##
# iterations: 11
# Training complete! SVM with decision boundary 0.000*x + -1.000*y + 2.000 >= 0 misclassified 0 points.

ANSWER_1 = 11
ANSWER_2 = 6
ANSWER_3 = 3
ANSWER_4 = 2

ANSWER_5 = ['A','D']
ANSWER_6 = ['A','B','D']
ANSWER_7 = ['A','B','D']
ANSWER_8 = []
ANSWER_9 = ['A','B','D']
ANSWER_10 = ['A','B','D']

ANSWER_11 = False
ANSWER_12 = True
ANSWER_13 = False
ANSWER_14 = False
ANSWER_15 = False
ANSWER_16 = True

ANSWER_17 = [1, 3, 6, 8]
ANSWER_18 = [1,2,4,5,6,7,8]
ANSWER_19 = [1,2,4,5,6,7,8]

ANSWER_20 = 6


#### SURVEY ####################################################################

NAME = 'Jiahui Tang'
COLLABORATORS = 'None'
HOW_MANY_HOURS_THIS_LAB_TOOK = '2'
WHAT_I_FOUND_INTERESTING = 'update SVM'
WHAT_I_FOUND_BORING = 'None'
SUGGESTIONS = 'None'
