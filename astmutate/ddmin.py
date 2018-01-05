import random
import string

def complement(s, i, l): return s[:i] + s[i + l:]

def some_complement_is_failing(s, npartitions, testfn):
    subset_length = len(s) // npartitions
    items = range(0,len(s), subset_length)
    complements = (complement(s, i, subset_length) for i in items)
    return next((i for i in complements if testfn(i)), None)

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


