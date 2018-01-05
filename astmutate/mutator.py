#!/usr/bin/env python3
import counter as counter
import mutate as mu
import ddmin as dd
import imp
import sys
import os.path

def import_code(code, name):
    module = imp.new_module(name)
    exec(code, module.__dict__)
    return module

def evalmutant(mname, mutant, test):
    test.__dict__[mname] = mutant
    v = test.runTest() # Was test run successful? False -- Mutant Found
    # our use of ddmin.
    # if the mutant fails in one of the test cases, we are happy (TODO: Threats -- we are not ensuring same test case fails.)
    # we split the mutations in the mutants into two, and evaluate both.
    # if at least one succeeds, then it is great, we descent into that.
    # if both succeeds, then we have to descent into both.
    # if none succeeds, then we do the ddmin thing and increase the coarseness

    return not v

def main(args):
    mainfile = args[0]
    mainname = os.path.splitext(os.path.basename(mainfile))[0]
    mainsrc = open(mainfile).read()

    num_statements = counter.get_statements(mainsrc)

    testfile = args[1]
    testname = os.path.splitext(os.path.basename(testfile))[0]
    testsrc = open(testfile).read()
    test_code = import_code(testsrc, testname)

    def mytest(lst_locations):
        mutant_src = mu.gen_mutant(mainsrc, lst_locations)
        mutant = import_code(mutant_src, mainname)
        return evalmutant(mainname, mutant, test_code)

    mutate_lst = sorted(list(range(1, num_statements+1)))
    r = dd.ddmin(mutate_lst, mytest)
    print(r)

main(sys.argv[1:])
