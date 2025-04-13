# it is not the solution. Only a random node generator. I didn't have experience with the concept of "Node" before so I had to learn.

import random

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_random_tree(max_nodes=10, value_range=(1, 100)):
    """
    Rastgele sayıda düğüme sahip bir ikili ağaç oluşturur.

    Args:
        max_nodes (int): Oluşturulabilecek maksimum düğüm sayısı.
        value_range (tuple): Düğüm değerleri için aralık (min, max).

    Returns:
        Node: Rastgele oluşturulmuş ağacın kök düğümü veya None (eğer 0 düğüm oluşturulursa).
    """
    if max_nodes <= 0:
        return None

    num_nodes = random.randint(1, max_nodes)
    if num_nodes == 0:
        return None

    root_value = random.randint(value_range[0], value_range[1])
    root = Node(root_value)
    nodes_created = 1
    queue = [root]

    while nodes_created < num_nodes and queue:
        current_node = queue.pop(0)

        # Sol çocuk ekleme olasılığı
        if random.random() > 0.5 and nodes_created < num_nodes:
            left_value = random.randint(value_range[0], value_range[1])
            current_node.left = Node(left_value)
            queue.append(current_node.left)
            nodes_created += 1

        # Sağ çocuk ekleme olasılığı
        if random.random() > 0.5 and nodes_created < num_nodes:
            right_value = random.randint(value_range[0], value_range[1])
            current_node.right = Node(right_value)
            queue.append(current_node.right)
            nodes_created += 1

    return root

# Rastgele bir ağaç oluşturalım (maksimum 7 düğüm, değerler 1 ile 50 arasında)
random_tree = generate_random_tree(max_nodes=7, value_range=(1, 50))

# Oluşturulan ağacı görmek için (basit bir yazdırma fonksiyonu yazabiliriz)
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print("  " * level + prefix + str(root.val))
        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")

print("Rastgele Oluşturulan Ağaç:")
print_tree(random_tree)