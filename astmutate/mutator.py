#!/usr/bin/env python3
import counter as counter
import mutate as mu
import ddmin as dd
import imp
import sys
import nayajson_test

def import_code(code, name):
    module = imp.new_module(name)
    exec(code, module.__dict__)
    return module

def evalmutant(mname, mutant, test):
    test.__dict__[mname] = mutant
    v = test.runTest()
    if len(v.errors) > 0 or len(v.failures) > 0:
        return True # Mutant Found
    else:
        return False # Mutant Not Found

def main(args):
    num_statements = counter.get_statements(open('example/nayajson.py').read())
    mynayajson_src = open('example/nayajson.py').read()
    nayajson_test = import_code(open('example/nayajson_test.py').read(), 'nayajson_test')

    def mytest(lst_locations):
        mutant_src = mu.gen_mutant(mynayajson_src, lst_locations)
        mutant = import_code(mutant_src, 'mynayajson')
        return evalmutant('mynayajson', mutant, nayajson_test)

    mutate_lst = list(range(1, num_statements+1))
    r = dd.ddmin(mutate_lst, mytest)
    print(r)

main(sys.argv)
