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

def all_complements_failing(s, npartitions, testfn):
    subset_length = len(s) // npartitions
    items = range(0,len(s)-1, subset_length)
    complements = [complement(s, i, subset_length) for i in items]
    return [i for i in complements if testfn(i)] # return all complements, not just first

def update_input(s, npartitions, fn):
    v = all_complements_failing(s, npartitions, fn)
    if v:
        return v, max(npartitions - 1, 2)
    else:
        return [s], min(npartitions * 2, len(s))

def minimize(s, fn):
    # split the input into two, and check each.
    detected_mutations_llst = split_into_two_and_check(s, fn)

    if len(detected_mutations_llst) == 1:
        # if the detected is just one part, we are happy.
        # we can do a single track descent into that part.
        detected_mutations_lst = detected_mutations_llst[0]

        # if we are at single mutant level, return
        if len(detected_mutations_lst) == 1: return detected_mutations_lst

        # more to do. continue
        return minimize(detected_mutations_lst, fn)

    elif len(detected_mutations_llst) == 2:
        # if both parts detected mutants, then we need to
        # isolate mutants both
        detected_mutations_lst1, detected_mutations_lst2 = detected_mutations_llst
        r = list(sum([v if len(v) == 1 else minimize(v, fn) for v in detected_mutations_llst], []))
        return r
    elif len(detected_mutations_llst) == 0:
        # if a combined mutation mutant failed, but mutants with individual mutations did not.
        # Here, we may save the failed mutant for further analysis, because it
        # is more likely that the component mutations are non-equivalent but for
        # the purpose of mutation analysis, it is sufficient to note that the
        # children did not have failing faults, and hence their children are
        # also unlikely to have failing faults.
        return []
    else: assert False



    npartitions = 2
    lst = [s]
    collected = []
    while lst:
        s, *lst = lst
        newlst, n1 = update_input(s, npartitions, fn)
        # npartitions is the number of partitions. We stop when the number of partitions
        # equal the number of individual elements.
        if len(newlst) == 1 && npartitions == len(newlst[0]):
            collected.append(newlst[0])
            continue
        npartitions = n1
        lst.extend(newlst)
    return s


