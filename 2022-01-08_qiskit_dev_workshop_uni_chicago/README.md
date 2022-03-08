# Qiskit workshop - University of Chicago / Chicago Quantum Exchange

This workshop was performed in University of Chicago, Jan 8th 2022. 

## Agenda

- Intro IBM Quantum Lab and Qiskit modules
- Circuits, backends, visualization
- Quantum info, circuit lib, algorithms
- Circuit compilation, pulse, opflow

## Notebooks

- [Lecturer notes](./qiskit-workshop-full.ipynb) 
- [Participant notes](./qiskit-workshop-lab-notebook.ipynb)

## Relevant Links

- https://quantum-computing.ibm.com/lab - Quantum lab
- https://qiskit.org/documentation/ - Qiskit documentation
- https://github.com/qiskit - Qiskit website

## Installation

#### Getting IBM Quantum account and token

1. Go to https://quantum-computing.ibm.com/
2. Register
3. On your welcome page you should see `API token` field which you can copy and use during lab

#### Local Jupyter + Qiskit setup

0. (if you do not have it already) [Install conda](https://www.anaconda.com/products/individual)
1. In terminal: create a new conda env
```shell
conda create --name qiskit-workshop python=3.7
```
2. In terminal: activate env
```shell
conda activate qiskit-workshop
```
3. In terminal: Install dependencies
```shell
conda install jupyter==1.0.0 matplotlib==3.5.1
pip install qiskit==0.34.0 pylatexenc==2.10
```
4. In terminal: launch jupyter
```shell
jupyter notebook
```