# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

import sys
sys.path.append('./demos/AI/')
from run_classify_local import classify
from presentation_helpers import *

mode = "offline"

if check_connection("https://www.qiskit.org")==1:
    mode = "online"
else:
    mode = "offline"

result_offline = ""

def execution_mode(status):
    global mode
    mode = status

def result_AI_inference():
    data = {}
    global mode
    global result_offline

    result = result_offline.split("\n")

    data["time"] = result[:1][0]
    data["metadata"] = result[1:-1]
    data["quality"] = 100

    data["labels"] = result[-1].replace("-1.", "B,").replace("1.", "A,").replace("[","").replace("]","").replace(" ","").split(",")[:-1]
    data["label"] = data["labels"][0]
    # print(data["labels"])
    data["inference"] = "cat" if result[-1] == "[-1. -1. -1. -1.]" else "dog"
    return data


def execute_AI(data):
    points = "0,0"
    global mode
    global result_offline
    if data == "🐱":
        points = "53,65,9,32,53,82,10,17"
    elif data == "🐶":
        points = "96,16,7,24,93,92,99,30"
    else:
        return "error in input data"

    result_offline = classify(points)

if __name__ == "__main__":
    # execute only if run as a script
    element = "🐱"
    execute_AI(element)
    print("--->", element)
    result = result_AI_inference()
    print("--->",result["inference"])
    print("===>",result["time"])
    print("===>",result["metadata"])
