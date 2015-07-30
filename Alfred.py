'''
Created on April 8, 2015

@author: SUV
'''

from heapq import heappush
from heapq import heappop
from sys import maxint
from Sparqlquery import start
import Sparqlquery

nodes = ['Sad', 'Sick', 'Lazy', 'Bad', 'Bored','Lucky','Excited',
         'Tired','Active','Hungry','Fun','Lonely','Homesick','Happy'] #All the involved moods

graph = {'Sad' : {'Sick':30, 'Lazy':5},
         'Sick' : {'Bad':15},
         'Lazy' : {'Bored':30},
         'Bad' : {'Lucky':30},
         'Bored' : {'Excited':60, 'Active':5},
         'Lucky' : {'Happy':60},
         'Excited' : {'Happy':60},
         'Tired' : {'Happy':60},
         'Active' : {'Tired':60, 'Hungry':30},
         'Hungry' : {'Fun':60},
         'Fun' : {'Happy':15},
         'Lonely' : {'Homesick':10},
         'Homesick' : {'Excited':15},
         'Happy' : {}}                                              #All the edges of the search space                                      

def dijkstraalgo(graph, start, end, distance={}, path={}, newd=0):  #for heuristic matrix
    
    for node in graph:
        distance[node] = maxint
    
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
    
    for state in path:
        if state == end:
            return distance[state]
        
def fill_matrix(graph, target, matrix={}):                          #filling the matrix
    
    for mood in graph:
        matrix[mood] = 0
        for node in matrix:
            matrix[node] = dijkstraalgo(graph, node, target)
                
    return matrix

def astar_algo(graph, start, end, solution={}, distance={}, pdistance={}, newd=0):
  
    for node in graph:                                              #performing a-star using heuristic matrix
        distance[node] = maxint
        pdistance[node] = maxint
    
    q = []
    distance[start] = 0
    pdistance[start] = 0
    matrix = fill_matrix(graph, end)
    
    for node in graph:
        heappush(q, (node, pdistance[node]))
        solution[node] = -1
    
    solution[start] = 0
        
    while len(q):
        (minimum, minvalue) = heappop(q)
        
        for node in graph[minimum]:
            newd = pdistance[minimum] + graph[minimum][node]
            if (pdistance[node]-matrix[node]) > newd:
                pdistance[node] = newd
                heappush(q, (node, pdistance[node]+matrix[node]))
                solution[node] = minimum
        
    currnode = end
    path = []
    while(solution[currnode] != 0):
        path.insert(0, currnode)
        currnode = solution[currnode]
    path.insert(0, currnode)    
    return path
    
def find_nodepath(graph, start, end, path=[]):          #algorithm for optimal path using second heuristic
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_nodepath(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    
    return shortest

def printgraph(pathsolution):
    print "The optimal path is:"
    for nodes in pathsolution:
        print nodes

def main():
    print "Hello, Master Wayne. Alfred at your service!"
    print nodes
    source = raw_input("Enter the current mood from the above list:")
    target = 'Happy'
    
    if source == 'Happy':
        print ("Excellent! You are as happy as you will ever be.")
    
    elif not (graph.has_key(source) or graph.has_key(target)):
        print ("Uhh, Master Wayne isn't that moody. You are an impostor!!")
    
    else:    
        print ("Heuristics available:\n1. Time cost taken to reach goal state\n2. Number of mood swings required to reach goal state")    
        option = raw_input("How would you like to proceed Master Wayne?:")    
        
        if option == '1':                                               #selecting first heuristic
            flag = 0
            foundpath = astar_algo(graph, source, target)
            printgraph(foundpath)
            start(source, flag)                                         #start the KB querying part
            if Sparqlquery.optimal == foundpath:                        #checking for optimality
                print "\nYou have taken the optimal path. Congratulations, You'd make a good Alfred!!"
            else:
                print "Not the optimal path. You wouldn't make a good Alfred!!"
        
        elif option == '2':                                             #selecting second heuristic
            flag = 1
            foundpath = find_nodepath(graph, source, target)
            printgraph(foundpath)
            start(source, flag)                                         #start the KB querying part
            if Sparqlquery.optimal == foundpath:                                #checking for optimality
                print "\nYou have taken the optimal path. Congratulations, You'd make a good Alfred!!"
            else:
                print "Not the optimal path. You wouldn't make a good Alfred!!"
        else:
            print("Nope. Only two heuristics available!!")
    
    return None

if __name__ == '__main__':
    main()