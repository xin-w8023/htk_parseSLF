import sys


class Node:
    def __init__(self, idx, value, isend=True):
        self.idx = idx
        self.value = value
        self.isend = isend

    def __repr__(self):
        if self.isend:
            return f'{self.idx} [label="{self.idx}", shape = doublecircle, style = bold, fontsize = 14];\n'
        else:
            return f'{self.idx} [label="{self.idx}", shape = circle, style = bold, fontsize = 14];\n'

class Arc:
    def __init__(self, idx, start: Node=None, end: Node=None, weight: float=1.0):
        self.start = start
        self.end = end
        self.weight = weight
        self.label = f'{self.end.value}:{self.end.value}/{self.weight}'
        self.idx = idx

    def __repr__(self):
        return f'{self.start.idx} -> {self.end.idx} [label="{self.label}", fontsize = 14];\n'


class Graph:
    def __init__(self, nodes, arcs):
        self.nodes = nodes
        self.arcs = arcs

    def __repr__(self):
        main_str = 'digraph FST { \n\
rankdir = LR; \n\
size = "85,110"; \n\
label = ""; \n\
center = 1; \n\
orientation = Landscape; \n\
ranksep = "0.4"; \n\
nodesep = "0.25"; \n\
'
        for node in self.nodes:
            main_str += node.__repr__()
        for arc in self.arcs:
            main_str += '\t' + arc.__repr__()
        main_str += '}\n'
        return main_str

def process_line(line):
    return [e.split('=')[1] for e in line.strip().split()]

def process_node(nodes):
    Nodes = []
    for node in nodes:
        n, w = process_line(node)
        Nodes += [Node(n, w)]
    return Nodes

def process_arc(arcs, nodes):
    Arcs = []
    for arc in arcs:
        i, s, e = process_line(arc)
        Arcs += [Arc(i, nodes[int(s)], nodes[int(e)])]
        nodes[int(s)].isend = False
    return Arcs



file_ = sys.argv[1];
f = open(file_, 'r')
f.readline();
N, L = process_line(f.readline())

lines = f.readlines()
nodes, arcs = lines[:int(N)], lines[int(N):]
f.close()
nodes = process_node(nodes)
arcs = process_arc(arcs, nodes)
graph = Graph(nodes, arcs)
print(graph)
