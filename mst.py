#################################################################################################################################################
# The code below is a single file of Python code that can be used to determine the maximum saving that can be achieved from a given input network. 
# Inside this file, the code calls a function that has the following boilerplate format as shown below:
##################################################################################################################################################

def maximum_saving(input_network: str) -> int:
    lines = [line.strip() for line in input_network.strip().splitlines()]
    n = len(lines)

    edges = []
    total_cost = 0

    # This section of code is to read matrix and collect edges
    for i in range(n):
        values = lines[i].split(',')
        for j in range(i + 1, n):
            if values[j] != '-':
                weight = int(values[j])
                edges.append((weight, i, j))
                total_cost += weight

    # I sort edges by weight
    edges.sort()

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False

    mst_cost = 0
    edges_used = 0

    for weight, u, v in edges:
        if union(u, v):
            mst_cost += weight
            edges_used += 1
            if edges_used == n - 1:
                break

    return total_cost - mst_cost


# This part of the code is to test the input
input_network = '''
-,14,10,19,-,-,-
14,-,-,15,18,-,-
10,-,-,26,-,29,-
19,15,26,-,16,17,21
-,18,-,16,-,-,9
-,-,29,17,-,-,25
-,-,-,21,9,25,-
'''

print(maximum_saving(input_network))
