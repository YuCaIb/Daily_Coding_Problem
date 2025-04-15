import matplotlib.pyplot as plt
import networkx as nx


# So I learned that, a node is basically a object that you may create another node(same object) inside of it and
# unival means if the upper node's value is the same with the objects' or not.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# I created a node in here
tree = Node(0,
            Node(1),
            Node(0,
                 Node(1, Node(1), Node(1)),
                 Node(0)
                 )
            )


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


G = nx.DiGraph()
labels = {}
add_edges(G, tree, labels=labels)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=False, arrows=False, node_size=1500, node_color='skyblue', edge_color='gray')
nx.draw_networkx_labels(G, pos, labels, font_size=14, font_color='black')
plt.title("Binary Tree Visualization (spring layout)")
plt.axis('off')
plt.show()
