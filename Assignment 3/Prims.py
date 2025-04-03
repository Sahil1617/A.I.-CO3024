import sys, heapq
from collections import defaultdict
from math import inf

class PGraph:
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = graph

    def minKey(self, key, mstSet):
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)

            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u

        print(f'\n\nPrim’s Minimum Spanning Tree:\nEdge \tWeight')
        minimumCost = 0
        for i in range(1, self.V):
            print(f'{parent[i]} -- {i} == {self.graph[i][parent[i]]}')
            minimumCost += self.graph[i][parent[i]]
        print(f'Minimum cost = {minimumCost}')

if __name__ == '__main__':

    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0,11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9,14, 0, 0, 0],
        [0, 0, 0, 9, 0,10, 0, 0, 0],
        [0, 0, 4,14,10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8,11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]

    g = PGraph(9, graph)
    g.primMST()