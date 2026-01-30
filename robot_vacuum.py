class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"<{self.value}>"


def dls_search(node, goal, limit, depth=0):
    """Поискс ограничением глубины в бинарном дереве"""
    if node is None:
        return False
    
    if node.value == goal:
        return True
    
    if depth >= limit:
        return False
    
    # Рекурсивно ищем в левом и правом поддеревьях
    if dls_search(node.left, goal, limit, depth + 1):
        return True
    
    if dls_search(node.right, goal, limit, depth + 1):
        return True
    
    return False


def main():
    root = BinaryTreeNode(
        1,
        BinaryTreeNode(2, None, BinaryTreeNode(4)),
        BinaryTreeNode(3, BinaryTreeNode(5), None)
    )
    
    goal = 4
    limit = 2
    
    # Выполняем поиск
    result = dls_search(root, goal, limit)
    print(f"Найден на глубине: {result}")

if __name__ == "__main__":
    main()