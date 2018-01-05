#!/usr/bin/env python3
import counter as counter
import mutate as mu
import minimize as m
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
    r = m.minimize(mutate_lst, mytest)
    print(r)

main(sys.argv[1:])
