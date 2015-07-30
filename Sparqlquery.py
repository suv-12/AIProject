'''
Created on April 24, 2015

@author: SUV
'''
from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery
from rdflib import URIRef

parse = URIRef("http://www.semanticweb.org/suv/ontologies/2015/3/alfredowl/")       #creating a suitable PREFIX for the SPARQL queries
g = Graph()
g.parse("/Users/SUV/Desktop/AlfredOWL2.owl")                                        #loading and parsing the OWL file from local machine
optimal = []

def start(mood, status):                                                            #main query parser and passing function
    time = 0
    
    while mood != "Happy":
        optimal.append(mood)
        actionslist = actionquery(mood)
        print ("\nThe actions available for this mood are:")
        for items in actionslist:
            print actionslist.index(items), items
        choice = raw_input("Enter the index of the action you want to take:")
        
        print "The tasks involved in the action are:"
        taskquery(actionslist[int(choice)])
        mood = moodquery(actionslist[int(choice)])
        if status == 0:
            currtime = timequery(actionslist[int(choice)])
            print "The time taken in completing this action is", currtime
            time = time + currtime
            print "Time elapsed:", time
        print "The new mood is", mood.upper()
        del actionslist[:]
    
    optimal.append(mood)
    print ("\nMaster Wayne is happy. Target Achieved. Sir, Shall I power up the bat-cave??")
        
def actionquery(mood, actions=[]):                                                  #actions query function
    
    q = prepareQuery(
        'SELECT ?name WHERE { ?mood alfred:possible ?action . ?action alfred:named ?name .}',
        initNs = { "alfred": "http://www.semanticweb.org/suv/ontologies/2015/3/alfredowl/"})
    
    this = parse + mood
    for row in g.query(q, initBindings={'mood': this}):
        actions.append(row.name)
    return actions

def taskquery(action, tasks=[]):                                                    #tasks query function
    
    q = prepareQuery(
        'SELECT ?name WHERE { ?action alfred:involves ?task . ?task alfred:named ?name .}',
        initNs = { "alfred": "http://www.semanticweb.org/suv/ontologies/2015/3/alfredowl/"})
    
    this = parse + action
    for row in g.query(q, initBindings={'action': this}):
        print row.name

def moodquery(action):                                                              #mood query function
    
    q = prepareQuery(
        'SELECT ?name WHERE { ?action alfred:results ?mood . ?mood alfred:named ?name .}',
        initNs = { "alfred": "http://www.semanticweb.org/suv/ontologies/2015/3/alfredowl/"})
    
    this = parse + action
    for row in g.query(q, initBindings={'action': this}):
        return str(row.name)
    
def timequery(action):                                                              #time query function
    
    q = prepareQuery(
        'SELECT ?time WHERE { ?action alfred:takes ?time .}',
        initNs = { "alfred": "http://www.semanticweb.org/suv/ontologies/2015/3/alfredowl/"})
    
    this = parse + action
    for row in g.query(q, initBindings={'action': this}):
        return int(row.time)