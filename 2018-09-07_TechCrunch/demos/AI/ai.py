# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

from run_classify_local import classify
import time

def run_ai_experiment(data):
  result = classify(data)
  return result
  # return classify(data)
