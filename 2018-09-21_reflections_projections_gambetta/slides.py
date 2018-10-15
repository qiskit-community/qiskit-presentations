from IPython.display import HTML

import webbrowser

def lab():
    return HTML('''<img src="images/lab.jpg" width="1000 px">''')

def ibmqx():
    # generate an URL
    return webbrowser.open("https://quantumexperience.ng.bluemix.net/qx/editor", new=0)

def ibmq_qcc():
    return HTML('''<img src="images/ibmq_qcc.jpg" width="1000 px">''')

def devices():
    # generate an URL
    return webbrowser.open("https://quantumexperience.ng.bluemix.net/qx/devices", new=0)

def qiskit():
    return webbrowser.open("https://qiskit.org", new=0)

def git():
    return webbrowser.open("https://github.com/qiskit", new=0)

def elements():
    return HTML('''<img src="images/elements.jpg" width="1000 px">''')

def quantum():
    return HTML('<img src="https://66.media.tumblr.com/763756ea907e30b639da239618bbe2d3/tumblr_mlotjw0e2C1r4xjo2o1_500.gif" width="500 px" align="center">')


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
    <video src="images/executions_last_week_-_trace.mov" width="1000 px" autoplay>
    ''')

def thanks():
    return HTML('<img src="images/thanks.gif" width="1000 px" align="center">')

def system():
    return HTML('<img src="images/system.jpg" width="1000 px" align="center">')

def transmon():
    return HTML('<img src="images/transmon.jpg" width="1000 px" align="center">')


print("Hello Reflections|Projections ... ")
