class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, goal, limit, depth=0):
    """Поиск с ограничением глубины. Возвращает узел цели, если найден в пределах глубины limit, иначе None."""
    if node is None:
        return None
    
    if node.value == goal:
        return node
    
    if depth >= limit:
        return None
    
    # Рекурсивный поиск в левом поддереве
    left_result = depth_limited_search(node.left, goal, limit, depth + 1)
    if left_result:
        return left_result
    
    # Рекурсивный поиск в правом поддереве
    right_result = depth_limited_search(node.right, goal, limit, depth + 1)
    if right_result:
        return right_result
    
    return None


def main():
    root = BinaryTreeNode(
        1,
        BinaryTreeNode(2, None, BinaryTreeNode(4)),
        BinaryTreeNode(3, BinaryTreeNode(5), None)
    )
    
    goal = 4
    limit = 2
    
    # Поиск цели с ограничением глубины
    result = depth_limited_search(root, goal, limit)
    
    if result:
        print(f"Цель найдена: {result}")
    else:
        print("Цель не найдена")


if __name__ == "__main__":
    main()