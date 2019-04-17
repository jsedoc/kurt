#!/usr/bin/env python3

from copy import deepcopy
from nltk import Tree

from loadrules import loadrules
from debugutil import dprint
import transductionrule
import sys, inspect
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
                        break

        if nextgen:
            dprint(nextgen)
            progress = True
            current = nextgen
    return complete

def create_data(tree_file, rule_file, input_file, output_file):
    count = 0
    tried = 0
    rules = loadrules(rule_file)
    f = open(tree_file)
    input = open(input_file,"w+")
    output = open(output_file,"w+")
    line = f.readline()
    while line:
        tried = tried+1
        tr = Tree.fromstring(line)
        theresults = transduce(tr, rules, "q")
        if(tried%1000 ==0):
            print("Tried: " + str(tried))
            print("Generated: " + str(count))
            
        if(len(theresults) > 0):
            count = count+1
            input.write(line)
            output.write(str(theresults[0].tree) + "\n")
        line = f.readline()
    print("Generated: " + str(count))
    f.close()
    input.close()
    output.close()

def main():
    tree_file = sys.argv[1]
    rule_file = sys.argv[2]
    input_file = sys.argv[3]
    output_file = sys.argv[4]
    create_data(tree_file, rule_file, input_file, output_file)

if __name__ == "__main__": main()
