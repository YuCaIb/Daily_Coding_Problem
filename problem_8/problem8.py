from utilty import node_create
import random
import matplotlib.pyplot as plt
import networkx as nx

tree = node_create.Node(random.randint(0, 1),
    node_create.Node(random.randint(0, 1)),
    node_create.Node(random.randint(0, 1),
        node_create.Node(random.randint(0, 1), node_create.Node(random.randint(0, 1)), node_create.Node(random.randint(0, 1))),
        node_create.Node(random.randint(0, 1))
    )
)

def unival_node_counter(root):
    count = [0]

    def is_unival(node):
        if node is None:
            return True

        left_unival = is_unival(node.left)
        right_unival = is_unival(node.right)

        if not left_unival or not right_unival:
            return False

        if node.left and node.left.val != node.val:
            return False

        if node.right and node.right.val != node.val:
            return False

        count[0] += 1
        return True

    is_unival(root)
    return count[0]




# plotting
G = nx.DiGraph()
labels = {}
node_create.add_edges(G, tree, labels=labels)
root_id = list(G.nodes)[0]
pos = node_create.hierarchy_pos(G, root=root_id)
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=False, arrows=False, node_size=1500, node_color='skyblue', edge_color='gray')
nx.draw_networkx_labels(G, pos, labels, font_size=14, font_color='black')
plt.title("Binary Tree Visualization (hierarchy layout)")
plt.axis('off')
plt.show()

print(unival_node_counter(tree))

