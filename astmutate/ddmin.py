import random
import string

# our use of ddmin.
# if the mutant fails in one of the test cases, we are happy 
#           (TODO: Threats -- we are not ensuring same test case fails.)
# we split the mutations in the mutants into two, and evaluate both.
# if at least one succeeds, then it is great, we descent into that.
# if both succeeds, then we have to descent into both.
# if none succeeds, then we do the ddmin thing and increase the coarseness

def complement(s, i, l): return s[:i] + s[i + l:]

def some_complement_is_failing(s, npartitions, testfn):
    subset_length = len(s) // npartitions
    items = range(0,len(s), subset_length)
    complements = [complement(s, i, subset_length) for i in items]
    for i in complements:
        if testfn(i):
            return i
    return None

def update_input(s, npartitions, fn):
    v = some_complement_is_failing(s, npartitions, fn)
    if v:
        return v, max(npartitions - 1, 2)
    else:
        return s, min(npartitions * 2, len(s))

def ddmin(s, fn):
    npartitions = 2
    while s:
        s, n1 = update_input(s, npartitions, fn)
        # npartitions is the number of partitions. We stop when the number of partitions
        # equal the number of individual elements.
        if npartitions == len(s): break
        npartitions = n1
    return s


