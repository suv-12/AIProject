'''
Created on April 27, 2015

@author: SUV
'''

import rdflib
from rdflib.plugins.sparql import prepareQuery 

q = prepareQuery(
        'SELECT ?action WHERE { ?mood alfred:takes ?action .}',
        initNs = { "alfred": "http://www.semanticweb.org/suv/ontologies/2015/3/alfredowl/"})

g = rdflib.Graph()
g.parse("/Users/SUV/Desktop/AlfredOWL2.owl")

start = "Browse_Facebook"

tim = rdflib.URIRef("http://www.semanticweb.org/suv/ontologies/2015/3/alfredowl/")

tim = tim + start

for row in g.query(q, initBindings={'mood': tim}):
        print int(row.action)