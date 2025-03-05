def edge_list():
    N,M = input().split()
    edge_list = []
    for i in range(M):
        x, y = (int(x) for x in input().split())
        edge_list.append((x, y))
    return edge_list


def adj_matrix(N,edge_list):
    adj_matrix = [[0 for i in range(N)] for i in range(N)]
    for x,y in edge_list:
        adj_matrix[x][y] = 1
        adj_matrix[y][x] = 1
    return adj_matrix

def reversed_matrix(adj_matrix):
    A = []
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if  (i,j) not in A:
                adj_matrix[i][j], adj_matrix[j][i] = adj_matrix[j][i], adj_matrix[i][j]
                A.append((j,i))
    return adj_matrix

def components( adj_list, visited = None):
    d = 0
    if visited is None:
        visited = set()
    for i in range(len(adj_list)):
        if i not in visited:
            queue = [i]
            while len(queue) > 0:
                curr_node = queue.pop(0)
                visited.add(curr_node)
                for adj_node in adj_list[curr_node]:
                    if adj_node not in visited:
                        queue.append(adj_node)
            d+=1
    return d

def DFS_print(start_node, adj_list, visited = None):
    if visited is None:
        visited = set()
    print(start_node)
    visited.add(start_node)
    for node in adj_list[start_node]:
        if node not in visited:
            DFS_print(node, adj_list, visited)
    print(start_node)


def Ford_Bellman(adj_list, start_node):
    dist = {i: float("inf") for i in range(len(adj_list))}
    dist[start_node] = 0

    for j in range(len(adj_list) - 1):
        for i in range(len(adj_list)):
            for node, weight in adj_list[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight
    for j in range(len(adj_list)):
        for i in range(len(adj_list)):
            for node, weight in adj_list[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = float('-inf')

    return dist
