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


def has_path_sum(root: Optional[Node], target: int) -> bool:
    # TODO: Dane jest drzewo binarne o korzeniem root raz liczba całkowita target.
    # Zwróć true, jeśli istnieje taka ścieżka w tym drzewie od korzenia do liścia,
    # taka że suma wszystkich wartości wzdłuż tej ścieżki jest równa target.
    if root == None:
        return False
    if target-root.val == 0 and root.left == None and root.right == None:
        return True
    else:
        return has_path_sum(root.left, target-root.val) or has_path_sum(root.right, target-root.val)


if __name__ == "__main__":
    target, node_values_str = input().strip().split(";")
    node_values = node_values_str.strip().split(" ")
    root = create_binary_tree(node_values)
    print(has_path_sum(root, int(target)))
