# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

# Checking the version of PYTHON; we only support 3 at the moment
import sys
if sys.version_info < (3,0):
    raise Exception("Please use Python version 3 or greater.")

import warnings

import numpy as np
from scipy import linalg as la
from functools import partial
import time
import itertools

import sys
import operator
import os

from qiskit import QuantumCircuit, QuantumProgram, QuantumRegister, ClassicalRegister, extensions

import math
from random import *
from cost_helpers import *


from python_helpers_local import *

warnings.simplefilter('ignore') 


#Experimental parameters
main_saving_directory = '/home/linus/qc_data/16Q_v2p0/Cooldown_180710/new_numbering/ErrorMit/ML/'
subdirectory = ''

saveshots = 1
#BLAH
n=2
my_zero_string = ''
for nq in range(n):
    my_zero_string += '0'
m=1
backend='local_qasm_simulator_cpp'
# backend=' "local_qasm_simulator"'

entangler_map = entangler_map_creator(n)
# the coupling_maps gates allowed on the device
coupling_map = None
# the layout of the qubits 
# initial_layout = {("q", 0): ("q", 3), ("q", 1): ("q", 4),("q", 2): ("q", 2)}
initial_layout = None

dataset = 'Ad_hoc'

def classify(datapoints):

    start = time.time()
    shots = 2000
    training_size = 2
    max_trials = 250
    class_labels = [r'A',r'B']

   
    N=100
   
    
    success_ratio_vec = np.zeros(1)
    for lind in range(1):
        tr = 0
        #Pool of A-points to choose: [96,7],[16,24],[93,99],[92,30],[86,89]
        #Pool of B-points to choose: [53,9],[65,32],[53,10],[82,17],[8,54]
        #Here we hard-code the points to classify
        # NA1 = [53,65]
        # NA2 = [9,32]
        datapoints =  [ int(ele) for ele in datapoints.split(",") ]
 
        NA1 = datapoints[:2]
        NA2 = datapoints[2:]
        label_train = np.zeros(2*training_size)
        sampleA = [[0 for x in range(n)] for y in range(training_size)]
        sampleB = [[0 for x in range(n)] for y in range(training_size)]

        for tr in range(training_size):
            draw1 = NA1[tr]
            draw2 = NA2[tr]
            sampleA[tr] = [2*np.pi*draw1/N,2*np.pi*draw2/N]

        # NB1 = [96,16]
        # NB2 = [7,24]

        NB1 = datapoints[-4:][:2]
        NB2 = datapoints[-2:]

        tr = 0
        for tr in range(training_size):
            draw1 = NB1[tr]
            draw2 = NB2[tr]
            sampleB[tr] = [2*np.pi*draw1/N,2*np.pi*draw2/N]

        sample_train = [sampleA,sampleB]
        for lindex in range(training_size):
            label_train[lindex]=0
        for lindex in range(training_size):
            label_train[training_size+lindex]=1
        label_train = label_train.astype(int)
        sample_train = np.reshape(sample_train,(2*training_size,n))
        test_input= {key: (sample_train[label_train==k,:])[:] for k,key in enumerate(class_labels)}
        
        m = 0
        mstring = '_d%s'%m
        
        #here input SVs
        svm = [[5.340707510000000,2.95309709000000],[5.152211950000000,4.649557130000000],\
              [0.691150380000000,0.753982240000000],[6.094689750000000,5.717698630000000],\
              [6.094689750000000,4.146902300000000],[2.638937830000000,4.838052690000000],\
              [4.146902300000000,2.073451150000000],[0.251327410000000,3.204424510000000],\
              [2.324778560000000,3.958406740000000],[4.146902300000000,6.220353450000000],\
              [2.638937830000000,1.696460030000000],[5.466371220000000,4.649557130000000],\
              [4.146902300000000,3.078760800000000]] 

        yin = [1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1]
        bias = -0.108977136917370
        alphas = [2.418525108568705,2.624798568677183,3.137930892104469,1.289096815981113,\
                 1.360365946297470,1.716334989598710,1.324193468646364,0.975747792672286,\
                 1.495259054044496,2.453623398504204,0.529308088060917,4.021266095027866,1.747654425140206]
        
        K_total  = eval_svm_function(entangler_map, coupling_map, initial_layout,n,m,svm,test_input,class_labels, \
                       backend,shots)

        test_label_0 =np.ones(len(test_input[class_labels[0]]))
        test_label_1 = -1*test_label_0
        test_label = np.concatenate((test_label_0,test_label_1))
        success_ratio = 0

        L = np.zeros(2*len(test_input[class_labels[0]]))
        Lsign = np.zeros(2*len(test_input[class_labels[0]]))
        for tin in range(2*len(test_input[class_labels[0]])):
            Ltot = 0
            for sin in range(len(svm)):
                L[tin] = yin[sin]*alphas[sin]*K_total[tin*len(svm)+sin]
                Ltot +=  L[tin]

            Lsign[tin] = np.sign(Ltot+bias)

            if Lsign[tin] == test_label[tin]:
                success_ratio += 1
        success_ratio_vec[lind] = success_ratio/(2*len(test_input[class_labels[0]]))

    end = time.time()
    result = "execution time: " + str(end - start)+"\n"+ str(success_ratio_vec)  +"\n" + str(success_ratio)+"\n" + str(Lsign)
    return result
