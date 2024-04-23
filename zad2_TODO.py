"""
Uzupełnij 1 funkcje poniżej oznaczoną jako "TODO". 
Nie modyfikuj kodu, który już istnieje.
Można tworzyć własne funkcje pomocnicze.
Po zaimplementowaniu rozwiązania komendy `pass` powinny być usunięte.
"""

from typing import Optional, List


class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(node_values: List[str]):
    if (
        not node_values
        or len(node_values) == 0
        or node_values[0].strip() == ""
        or node_values[0] == "null"
    ):
        return None
    root = Node(int(node_values[0]))
    queue = [(root, 0)]
    while queue:
        current_node, idx = queue.pop()
        left_idx = idx * 2 + 1
        right_idx = idx * 2 + 2
        if left_idx < len(node_values):  # left child
            value = node_values[left_idx]
            if value != "null":
                current_node.left = Node(int(value))
                if left_idx <= len(node_values) // 2:  # is not a leaf
                    queue.append((current_node.left, left_idx))

        if right_idx < len(node_values):  # right child
            value = node_values[right_idx]
            if value != "null":
                current_node.right = Node(int(value))
                if right_idx <= len(node_values) // 2:  # is not a leaf
                    queue.append((current_node.right, right_idx))

    return root


def get_level_order(root: Optional[Node]) -> List[List[int]]:
    # TODO: Dane jest drzewo binarne z korzeniem  root. 
    # Zadanie polega na przejściu drzewa poziomami od korzenia w dół, 
    # od lewej do prawej i zapisać proces przechodzenia drzewa.
    if root is not None:
        left_arr = get_level_order(root.left) if root.left else []
        right_arr = get_level_order(root.right) if root.right else []
        max_len = max(len(left_arr), len(right_arr))
        new_arr = [(left_arr[i] if i < len(left_arr) else []) + (right_arr[i] if i < len(right_arr) else []) for i in range(max_len)]
        new_arr.insert(0, [root.val])
        return new_arr
    return []

# nie zmieniaj poniższego kodu
if __name__ == "__main__":
    node_values = input().strip().split(" ")
    root = create_binary_tree(node_values)
    print(get_level_order(root))
