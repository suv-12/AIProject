'''
Created on April 25, 2015

@author: SUV
'''
from rdflib import Graph

g = Graph()
g.parse("/Users/SUV/Desktop/AlfredOWL2.owl")

#for s,p,o in g:
#    print s, p, o
    
q1 = g.query(""" SELECT ?name
                WHERE { alfredowl:Sad rdf:type alfredowl:Mood .
                        alfredowl:Sad alfredowl:possible ?action .
                        ?action alfredowl:named ?name}""")

for item in q1:
    print item.name