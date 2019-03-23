#!/usr/bin/env python3

from copy import deepcopy
from nltk import Tree

from loadrules import loadrules
from debugutil import dprint
import transductionrule
#import sys, inspect
#clsmembers = inspect.getmembers(sys.modules[XTRule], inspect.isclass)


import sklearn
#import nltk
#nltk.download('punkt')

#print('The nltk version is {}.'.format(nltk.__version__))
#print('The scikit-learn version is {}.'.format(sklearn.__version__))

class SearchState:
    def __init__(self, tree, statemap, weight):
        self.tree = tree
        self.statemap = statemap
        self.weight = weight
    def __str__(self):
        return repr(self)
    def __repr__(self):
        return ("<search state.\n  tree: {0}\n  weight: {1}\n  statemap: {2}>".format(
            self.tree, self.weight, self.statemap))
    def __eq__(self, other):
        return (self.tree == other.tree
                and self.statemap == other.statemap
                and abs(self.weight - other.weight) < 0.001)

def transduce(tree, rules, initial):
    """Given a tree, a set of rules, and an initial state, return the list of
    all the trees that are produced by the transduction."""

    # list of the current generation of SearchStates
    current = []
    complete = []

    # give the root the initial state.
    statemap = {():'q'}
    current.append(SearchState(tree, statemap, 1.0))

    progress = True
    while progress:
        nextgen = []
        # for every tree that has a state: find every rule that applies to
        # that tree. apply that rule to that tree, put the results into the
        # nextgen.
        progress = False
        for ss in current: # (tr, statemap)
            if statemap != {}:
                for i,rule in enumerate(rules):
                    if rule.matches(ss.tree, ss.statemap):
                        results = rule.apply(ss.tree, ss.statemap)
                        for (newtr, newstatemap) in results:
                            w = rule.weight * ss.weight
                            newss = SearchState(newtr, newstatemap, w)
                            if newstatemap == {}:
                                complete.append(newss)
                            else:
                                nextgen.append(newss)
        if nextgen:
            dprint(nextgen)
            progress = True
            current = nextgen
    return complete

def create_data():
    rules = loadrules("deterministic.yaml")
    f = open('data.txt')
    input = open("input.txt","w+")
    output = open("output.txt","w+")
    line = f.readline()
    while line:
        tr = Tree.fromstring(line)
        theresults = transduce(tr, rules, "q")
        if(len(theresults) > 0):
            input.write(line)
            output.write(str(theresults[0].tree) + "\n")
        line = f.readline()
    f.close()
    input.close()
    output.close()

def main():
    create_data()
#    tr = Tree.fromstring("(1 (2 3 4) (5 (6 (7 8 9))))")
#    tr = Tree.fromstring("(1 (2 3 40) (5 (6 (7 8 20))))")
#    tr.pretty_print()
#    rules = loadrules("deterministic.yaml")
#    theresults = transduce(tr, rules, "q")
#    if(len(theresults) > 0):
#        print(tr)   
#        print(theresults[0].tree)
#    print("[[[done]]]")
    
#    for (i, result) in enumerate(theresults):
#        print("*** {0} ***".format(i))
#        print(result.tree)

if __name__ == "__main__": main()
