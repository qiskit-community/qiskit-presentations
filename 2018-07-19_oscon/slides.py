# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

from IPython.display import HTML

import webbrowser

def lab():
    return HTML('''<img src="images/lab.jpg" width="1000 px">''')

def ibmqx():
    # generate an URL
    return webbrowser.open("https://quantumexperience.ng.bluemix.net/qx/editor", new=0)

def ibmq_qcc():
    return HTML('''<img src="images/ibmq_qcc.jpg" width="1000 px">''')

def git():
    return webbrowser.open("https://github.com/qiskit", new=0)

def quantum():
    return HTML('<img src="images/cat.jpg" width="500 px" align="center">')

def model():
    return HTML('<img src="images/model.jpg" width="1000 px" align="center">')

def community():
    return HTML('<img src="images/community.jpg" width="1000 px" align="center">')

def entanglement():
    return HTML('<img src="images/entanglement.jpg" width="1000 px" align="center">')

def aqua():
    return HTML('<img src="images/aqua.jpg" width="1000 px" align="center">')

def papers():
    return HTML('<img src="images/papers.jpg" width="1000 px" align="center">')

def execution():
    return HTML('''
    <video src="images/executions-week.mp4" width="1000 px" autoplay>
    ''')

def thanks():
    return HTML('<img src="images/thanks.gif" width="1000 px" align="center">')

def system():
    return HTML('<img src="images/system.jpg" width="1000 px" align="center">')


print("Hello OSCON .... ")
