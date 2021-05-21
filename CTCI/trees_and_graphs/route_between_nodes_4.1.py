def route_between_nodes(g, node_one, node_two):

    if node_one == node_two:
        return True
    queue = []
    queue.append(node_one)
    while len(queue) != 0:
        curr_node = queue.pop(0)
        for neighbours in g[curr_node]:
            if node_two == neighbours:
                return True
            else:
                queue.append(neighbours)
    return False


print(route_between_nodes({
    1:[2, 3],
    2:[3, 4],
    3:[],
    4:[],
    5:[],
}, 1, 5))
