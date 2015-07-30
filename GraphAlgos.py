'''
Created on April 10, 2015

@author: SUV
'''

from Queue import Queue
from heapq import heappush
from heapq import heappop


graph = {'A': {'B': 4, 'C': 1},
         'B': {'E': 4},
         'C': {'B': 2, 'D': 4},
         'D': {'E': 4},
         'E': {},
         }

visited = {'A': 0,
           'B': 0,
           'C': 0,
           'D': 0,
           'E': 0
          }

distance = {'A': 1000,
            'B': 1000,
            'C': 1000,
            'D': 1000,
            'E': 1000
           }
    
def depthfirst(graph, start):
    visited[start] = 1
    print start
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if not visited[node]:
            depthfirst(graph, node)
            
def find_shortest_path(graph, start, end, pathcost=0, path=[]):
    path = path + [start]
    if start == end:
        return path, pathcost
    if not graph.has_key(start):
        return None
    shortest = None
    optimumcost = 0
    for node in graph[start]:
        if node not in path:
            pathcost = pathcost + graph[start][node]
            newpath = find_shortest_path(graph, node, end, pathcost, path)
            if newpath:
                if not shortest or pathcost < optimumcost:
                    shortest = newpath
    return shortest, optimumcost
            
#print "Depth first search of the graph:"
#depthfirst(graph,'A')

def dijkstraalgo(graph, start, path={}, newd=0):
    q = []
    
    path[start] = 0
    distance[start] = 0
    
    for node in graph:
        heappush(q, (node, distance[node]))
        path[node] = -1
    
    while len(q):
        (minimum, minvalue) = heappop(q)

        for node in graph[minimum]:  
            newd = distance[minimum] + graph[minimum][node]
            
            if distance[node] > newd:
                distance[node] = newd
                heappush(q, (node, distance[node]))
                path.update({node:minimum})
    
    print "The shortest path:"
    for state in path:
        if (state != start):
            print path[state] + ' --> ' + state + ' : ' + str(distance[state] - distance[path[state]])
        
dijkstraalgo(graph,'A')

graph2 = {'7': ['11','8'],
          '5': ['11'],
          '3': ['8', '10'],
          '11': ['2', '9', '10'],
          '8': ['9'],
          '2': [],
          '9': [],
          '10': []
         }

def topolsort(graph, indegree ={}, path=[]):
    q = Queue()
    
    for node1 in graph:
        indegree[node1] = 0 
        for node2 in graph:
            if node1 in graph[node2]:
                indegree[node1] = indegree[node1] + 1
    
    print indegree
    
    for node in graph:
        if indegree[node] == 0:
            q.put(node)
            
    while not q.empty():
        currnode = q.get()
        path = path + [currnode]
        for node in graph[currnode]:
            indegree[node] = indegree[node] - 1
            if indegree[node] == 0:
                q.put(node)
    
    if len(path) != len(graph):
        print len(path)
        print path
        print 'Graph has a cycle. Topological Sorting is not possible'
    else:
        print 'Graph has no cycles.The Topological Sorting of the graph is as below'
        print path
            
#topolsort(graph2)