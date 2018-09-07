# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

import os
from qiskit import *
import numpy as np
import time
import itertools
import math
from random import *

def inner_prod_circuit_ML(entangler_map, coupling_map, initial_layout,n, x_vec1, x_vec2, name = 'circuit',\
                     meas_string = None, measurement = True):

    # setup the circuit
    q = QuantumRegister("q", n)
    c = ClassicalRegister("c", n)
    trial_circuit = QuantumCircuit(q, c)

    # 0: Set the qubits in superposition
    #write input state from sample distribution
    for r in range(len(x_vec1)):
        trial_circuit.h(q[r])
        trial_circuit.u1(2*x_vec1[r], q[r])

    # 1: Using entanglement,map the training data to a quantum feature map
    for node in entangler_map:
        for j in entangler_map[node]:
            trial_circuit.cx(q[node], q[j])
            trial_circuit.u1(2*(np.pi-x_vec1[node])*(np.pi-x_vec1[j]), q[j])
            trial_circuit.cx(q[node], q[j])

    # 2: inference the quantum classifier.
    for r in range(len(x_vec1)):
        trial_circuit.h(q[r])
        trial_circuit.u1(2*x_vec1[r], q[r])

    for node in entangler_map:
        for j in entangler_map[node]:
            trial_circuit.cx(q[node], q[j])
            trial_circuit.u1(2*(np.pi-x_vec1[node])*(np.pi-x_vec1[j]), q[j])

    for node in entangler_map:
        for j in entangler_map[node]:
            trial_circuit.u1(-2*(np.pi-x_vec2[node])*(np.pi-x_vec2[j]), q[j])
            trial_circuit.cx(q[node], q[j])

    for r in range(len(x_vec2)):
        trial_circuit.u1(-2*x_vec2[r], q[r])
        trial_circuit.h(q[r])

    for node in entangler_map:
        for j in entangler_map[node]:
            trial_circuit.cx(q[node], q[j])
            trial_circuit.u1(-2*(np.pi-x_vec2[node])*(np.pi-x_vec2[j]), q[j])
            trial_circuit.cx(q[node], q[j])

    for r in range(len(x_vec2)):
        trial_circuit.u1(-2*x_vec2[r], q[r])
        trial_circuit.h(q[r])

    trial_circuit.measure(q,c)

    return name, trial_circuit
# ***************
# ***************
# ***************
def matrify(vector, dimension):

    mat = np.eye(dimension,dimension);
    for kk in range(dimension):
        a = int(dimension*kk - kk*(kk+1)/2)
        b = int(dimension*(kk+1)-((kk+1)*(kk+2)/2+1))
        mat[kk][kk+1:] = vector[a:b+1];
    for i in range(dimension):
        for j in range(i, dimension):
            mat[j][i] = mat[i][j]
    return mat

def eval_svm_function(entangler_map, coupling_map, initial_layout,n,m,svm,test_input,class_labels, \
                       backend,shots):
    sample_shots = 0

    c1 = 1
    c2 = 1.5
    c3 = 2
    my_zero_string = ''
    for nq in range(n):
        my_zero_string += '0'
    correct_povm = 0
    number_of_classes = len(class_labels)
    cost=0
    total_cost = 0
    std_cost = 0

    ### RUN CIRCUITS

    circuits = []
    cp = []
    cm = []
    sequencesp = []
    sequencesm = []

    first_array = test_input[class_labels[0]]
    second_array = test_input[class_labels[1]]
    total_test = np.concatenate([first_array,second_array])
    circuits = []

    ind = 0
    for a in range(len(total_test)):
        for b in range(len(svm)):
            cp, sequencesp = inner_prod_circuit_ML(entangler_map, coupling_map, initial_layout,n,\
                                                svm[b],total_test[a],'AB'+str(ind),None,True)

            circuits.append(sequencesp)
            ind +=1

    job_sim = execute(circuits, backend ,shots=shots)
    sim_result = job_sim.result()

    my_data = {}
    for index, circuit_to_get_result in enumerate(circuits):
        my_data[str(index)]=sim_result.get_counts(circuit_to_get_result)


    ind = iter(my_data.items())
    counts = dict(itertools.islice(ind,len(my_data)))

    K_total = []
    for v in range(len(counts)):
        K_total.append(counts[str(v)][my_zero_string]/shots)

    return K_total
