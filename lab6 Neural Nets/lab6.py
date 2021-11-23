# MIT 6.034 Lab 6: Neural Nets
# Written by 6.034 Staff

from nn_problems import *
from math import e
INF = float('inf')


#### Part 1: Wiring a Neural Net ###############################################

nn_half = [1]

nn_angle = [2,1]

nn_cross = [2,2,1]

nn_stripe = [3,1]

nn_hexagon = [6,1]

nn_grid = [4,2,1]


#### Part 2: Coding Warmup #####################################################

# Threshold functions
def stairstep(x, threshold=0):
    "Computes stairstep(x) using the given threshold (T)"
    return 1 if x >= threshold else 0

def sigmoid(x, steepness=1, midpoint=0):
    "Computes sigmoid(x) using the given steepness (S) and midpoint (M)"
    return (1 + e**(-steepness * (x-midpoint)))**-1

def ReLU(x):
    "Computes the threshold of an input using a rectified linear unit."
    return max(0,x)

# Accuracy function
def accuracy(desired_output, actual_output):
    "Computes accuracy. If output is binary, accuracy ranges from -0.5 to 0."
    return -0.5*(desired_output-actual_output)**2


#### Part 3: Forward Propagation ###############################################

def node_value(node, input_values, neuron_outputs):  # PROVIDED BY THE STAFF
    """
    Given
     * a node (as an input or as a neuron),
     * a dictionary mapping input names to their values, and
     * a dictionary mapping neuron names to their outputs
    returns the output value of the node.
    This function does NOT do any computation; it simply looks up
    values in the provided dictionaries.
    """
    if isinstance(node, str):
        # A string node (either an input or a neuron)
        if node in input_values:
            return input_values[node]
        if node in neuron_outputs:
            return neuron_outputs[node]
        raise KeyError("Node '{}' not found in either the input values or neuron outputs dictionary.".format(node))

    if isinstance(node, (int, float)):
        # A constant input, such as -1
        return node

    raise TypeError("Node argument is {}; should be either a string or a number.".format(node))


def forward_prop(net, input_values, threshold_fn=stairstep):
    """Given a neural net and dictionary of input values, performs forward
    propagation with the given threshold function to compute binary output.
    This function should not modify the input net.  Returns a tuple containing:
    (1) the final output of the neural net
    (2) a dictionary mapping neurons to their immediate outputs"""
    neuron_outputs = input_values
    neurons = net.topological_sort()
    for n in neurons:
        output = 0
        for w in net.get_wires(None, n):
            output += node_value(w.startNode,input_values,neuron_outputs)*w.get_weight()
        neuron_outputs[n] = threshold_fn(output)
    return neuron_outputs[net.get_output_neuron()], neuron_outputs

#### Part 4: Backward Propagation ##############################################

def gradient_ascent_step(func, inputs, step_size):
    """Given an unknown function of three variables and a list of three values
    representing the current inputs into the function, increments each variable
    by +/- step_size or 0, with the goal of maximizing the function output.
    After trying all possible variable assignments, returns a tuple containing:
    (1) the maximum function output found, and
    (2) the list of inputs that yielded the highest function output."""
    max_output, max_input_lst = func(inputs[0],inputs[1],inputs[2]), None
    input_extended = []
    for i in inputs:
        input_extended.append([i, i+step_size, i-step_size])
    for i in input_extended[0]:
        for j in input_extended[1]:
            for k in input_extended[2]:
                if func(i,j,k) >= max_output:
                    max_output = func(i,j,k)
                    max_input_lst = [i,j,k]
    return max_output, max_input_lst


def get_back_prop_dependencies(net, wire):
    """Given a wire in a neural network, returns a set of inputs, neurons, and
    Wires whose outputs/values are required to update this wire's weight."""
    dependency = set()
    dependency.update([wire, wire.startNode, wire.endNode])
    if net.is_output_neuron(wire.endNode):
        return dependency
    else:
        forward_wire = net.get_wires(startNode = wire.endNode)
        for w in forward_wire:
            dependency.update(get_back_prop_dependencies(net,w))
    return dependency


def calculate_deltas(net, desired_output, neuron_outputs):
    """Given a neural net and a dictionary of neuron outputs from forward-
    propagation, computes the update coefficient (delta_B) for each
    neuron in the net. Uses the sigmoid function to compute neuron output.
    Returns a dictionary mapping neuron names to update coefficient (the
    delta_B values). """
    delta_b = {}
    out_final = net.get_output_neuron()
    delta_b[out_final] = neuron_outputs[out_final]*(1-neuron_outputs[out_final])*(desired_output -neuron_outputs[out_final])

    neurons = net.topological_sort()
    # remove the last output
    neurons.pop()
    # update in reverse order
    while neurons:
        curr_update_node = neurons.pop()
        wire_a_b = net.get_wires(curr_update_node)
        outgoing = 0
        for w in wire_a_b:
            outgoing += w.get_weight() * delta_b[w.endNode]
        delta_b[curr_update_node] = neuron_outputs[curr_update_node] * (1-neuron_outputs[curr_update_node])*outgoing
    return delta_b

def update_weights(net, input_values, desired_output, neuron_outputs, r=1):
    """Performs a single step of back-propagation.  Computes delta_B values and
    weight updates for entire neural net, then updates all weights.  Uses the
    sigmoid function to compute neuron output.  Returns the modified neural net,
    with the updated weights."""
    delta_b = calculate_deltas(net, desired_output, neuron_outputs)
    # update all wires
    for w in net.get_wires():
        weight_prev = w.get_weight()
        delta_weight = r * node_value(w.startNode, input_values, neuron_outputs) * delta_b[w.endNode]
        w.set_weight(weight_prev + delta_weight)
    return net


def back_prop(net, input_values, desired_output, r=1, minimum_accuracy=-0.001):
    """Updates weights until accuracy surpasses minimum_accuracy.  Uses the
    sigmoid function to compute neuron output.  Returns a tuple containing:
    (1) the modified neural net, with trained weights
    (2) the number of iterations (that is, the number of weight updates)"""
    actual_output, neuron_outputs = forward_prop(net, input_values, threshold_fn=sigmoid)
    iter = 0
    while accuracy(desired_output, actual_output) <= minimum_accuracy:
        iter += 1
        net = update_weights(net, input_values, desired_output, neuron_outputs, r)
        actual_output, neuron_outputs = forward_prop(net, input_values, sigmoid)
    return net, iter

#### Part 5: Training a Neural Net #############################################

#  python3 training.py -data diagonal -net small
ANSWER_1 = 27
ANSWER_2 = 20
ANSWER_3 = 10
ANSWER_4 = 79
ANSWER_5 = 23

ANSWER_6 = 1
ANSWER_7 = 'checkerboard'
ANSWER_8 = ['small','medium','large']
ANSWER_9 = 'B'

ANSWER_10 = 'D'
ANSWER_11 = ['A','C']
ANSWER_12 =['A','E']


#### SURVEY ####################################################################

NAME = 'Jiahui Tang'
COLLABORATORS = 'None'
HOW_MANY_HOURS_THIS_LAB_TOOK = '4'
WHAT_I_FOUND_INTERESTING = 'NN with back and front'
WHAT_I_FOUND_BORING = 'None'
SUGGESTIONS = 'None'
