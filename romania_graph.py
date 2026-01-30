romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
    
    def __repr__(self):
        return f"<Node {self.state}>"
    
    def __len__(self):
        return 0 if self.parent is None else (1 + len(self.parent))


failure = Node('failure', path_cost=float('inf'))
cutoff = Node('cutoff', path_cost=float('inf'))


class LIFOQueue:
    def __init__(self):
        self.queue = []
    
    def append(self, item):
        self.queue.append(item)
    
    def pop(self):
        return self.queue.pop()
    
    def __len__(self):
        return len(self.queue)
    
    def __bool__(self):
        return len(self.queue) > 0


class GraphProblem:
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph
    
    def actions(self, state):
        return [city for city, _ in self.graph.get(state, [])]
    
    def result(self, state, action):
        return action
    
    def is_goal(self, state):
        return state == self.goal
    
    def action_cost(self, s, a, s1):
        for city, cost in self.graph[s]:
            if city == s1:
                return cost
        return float('inf')


def expand(problem, node):
    s = node.state
    for action in problem.actions(s):
        s1 = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s1)
        yield Node(s1, node, action, cost)


def is_cycle(node):
    state = node.state
    ancestor = node.parent
    while ancestor is not None:
        if ancestor.state == state:
            return True
        ancestor = ancestor.parent
    return False


def depth_limited_search(problem, limit=10):
    frontier = LIFOQueue()
    frontier.append(Node(problem.initial))
    result = failure
    
    while frontier:
        node = frontier.pop()
        
        if problem.is_goal(node.state):
            return node
        elif len(node) >= limit:
            result = cutoff
        elif not is_cycle(node):
            for child in expand(problem, node):
                frontier.append(child)
    
    return result


def path_states(node):
    if node in (cutoff, failure):
        return []
    
    path = []
    current = node
    while current is not None:
        path.append(current.state)
        current = current.parent
    path.reverse()
    return path


def main():
    print("Анализ графа Румынии поиск с ограничением глубины (DLS)")
    
    start_city = 'Arad'
    goal_city = 'Bucharest'
    
    problem = GraphProblem(start_city, goal_city, romania_map)
    
    print(f"Начальный город: {start_city}")
    print(f"Целевой город: {goal_city}")
    
    print("\nЭксперимент 1: Ограничение глубины = 3")
    result = depth_limited_search(problem, limit=3)
    if result == cutoff:
        print("Результат: cutoff (решение не найдено на глубине 3)")
    elif result == failure:
        print("Результат: failure")
    else:
        path = path_states(result)
        print(f"Путь найден: {' -> '.join(path)}")
        print(f"Стоимость: {result.path_cost} км")
        print(f"Глубина: {len(result)}")
    
    print("\nЭксперимент 2: Ограничение глубины = 4")
    result = depth_limited_search(problem, limit=4)
    if result == cutoff:
        print("Результат: cutoff (решение не найдено на глубине 4)")
    elif result == failure:
        print("Результат: failure")
    else:
        path = path_states(result)
        print(f"Путь найден: {' -> '.join(path)}")
        print(f"Стоимость: {result.path_cost} км")
        print(f"Глубина: {len(result)}")
    
    print("\nЭксперимент 3: Ограничение глубины = 5")
    result = depth_limited_search(problem, limit=5)
    if result == cutoff:
        print("Результат: cutoff (решение не найдено на глубине 5)")
    elif result == failure:
        print("Результат: failure")
    else:
        path = path_states(result)
        print(f"Путь найден: {' -> '.join(path)}")
        print(f"Стоимость: {result.path_cost} км")
        print(f"Глубина: {len(result)}")
    
    print("Сравнение с ручным решением:")
    
    manual_path = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
    manual_cost = 0
    for i in range(len(manual_path) - 1):
        current = manual_path[i]
        next_city = manual_path[i + 1]
        for city, cost in romania_map[current]:
            if city == next_city:
                manual_cost += cost
                break
    
    print(f"Ручное решение (A* алгоритм):")
    print(f"  Путь: {' -> '.join(manual_path)}")
    print(f"  Стоимость: {manual_cost} км")
    print(f"  Длина пути: {len(manual_path)} городов")
    
    if result != cutoff and result != failure:
        dls_path = path_states(result)
        dls_cost = result.path_cost
        
        print(f"\nРешение DLS:")
        print(f"  Путь: {' -> '.join(dls_path)}")
        print(f"  Стоимость: {dls_cost} км")
        print(f"  Длина пути: {len(dls_path)} городов")
        
        print(f"\nСравнение:")
        print(f"  Разница в стоимости: {abs(dls_cost - manual_cost)} км")
        
        if dls_cost == manual_cost:
            print("  Алгоритм DLS нашел оптимальное решение!")
        elif dls_cost < manual_cost:
            print("  Алгоритм DLS нашел решение дешевле")
        else:
            print("  Алгоритм DLS нашел более дорогое решение")
    else:
        print("\nПримечание: DLS не нашел решение в пределах заданной глубины")

if __name__ == "__main__":
    main()