import matplotlib.pyplot as plt
import networkx as nx


# So I learned that, a node is basically a object that you may create another node(same object) inside of it and
# unival means if the upper node's value is the same with the objects' or not.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# this is for visualisation
def add_edges(G, node, parent_id=None, node_id=[0], labels={}):
    if node is None:
        return

    current_id = node_id[0]
    labels[current_id] = str(node.val)
    G.add_node(current_id)

    if parent_id is not None:
        G.add_edge(parent_id, current_id)

    node_id[0] += 1
    left_id = node_id[0]
    add_edges(G, node.left, current_id, node_id, labels)

    right_id = node_id[0]
    add_edges(G, node.right, current_id, node_id, labels)


def hierarchy_pos(G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    children = list(G.successors(root))
    if len(children) != 0:
        dx = width / len(children)
        nextx = xcenter - width / 2 - dx / 2
        for child in children:
            nextx += dx
            pos = hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                vert_loc=vert_loc - vert_gap, xcenter=nextx, pos=pos,
                                parent=root)
    return pos

def add_two(x):
    return x + 2



__all__ = ['Node', 'add_edges', 'hierarchy_pos']
