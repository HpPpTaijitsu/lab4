class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"<{self.value}>"


def find_max_at_depth(node, limit, current_depth=0):
    """Находим максимальное значение на указанной глубине в бинарном дереве"""
    if node is None:
        # Возвращаем минус бесконечность для пустых узлов чтобы не влиять на стравнение
        return float('-inf')
    
    if current_depth == limit:
        return node.value
    
    left_max = find_max_at_depth(node.left, limit, current_depth + 1)
    right_max = find_max_at_depth(node.right, limit, current_depth + 1)
    
    # Возвращаем максимальное значение из поддеревьев
    return max(left_max, right_max)

def main():
    root = BinaryTreeNode(
        3,
        BinaryTreeNode(1, BinaryTreeNode(0), None),
        BinaryTreeNode(5, BinaryTreeNode(4), BinaryTreeNode(6))
    )
    
    limit = 2
    
    max_value = find_max_at_depth(root, limit)
    
    print(f"Максимальное значение на указанной глубине: {max_value}")


if __name__ == "__main__":
    main()