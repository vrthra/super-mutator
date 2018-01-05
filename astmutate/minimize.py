import random
import string

# if the mutant fails in one of the test cases, we are happy 
#           (TODO: Threats -- we are not ensuring same test case fails.)
# we split the mutations in the mutants into two, and evaluate both.
# if at least one succeeds, then it is great, we descent into that.
# if both succeeds, then we have to descent into both.
# if none succeeds, then we do the ddmin thing and increase the coarseness

def complement(s, i, l): return s[:i] + s[i + l:]

def split_into_two_and_check(s, fn):
    subset_length = len(s) // 2
    a1 = s[:subset_length]
    a2 = s[subset_length:]
    lst = [a1, a2]
    return [i for i in lst if fn(i)]

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
        # if both parts detected mutants, then we need to isolate mutants in both
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

