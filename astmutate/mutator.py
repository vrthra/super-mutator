#!/usr/bin/env python3
import counter as counter
import mutate as mu
import minimize as m
import imp
import sys
import os.path
import timeout_decorator

def import_code(code, name):
    module = imp.new_module(name)
    exec(code, module.__dict__)
    return module

global nexecutions
nexecutions = 0

@timeout_decorator.timeout(1)
def evalmutant(mname, mutant, test):
    global nexecutions
    nexecutions += 1
    test.__dict__[mname] = mutant
    v = test.runTest() # Was test run successful? False -- Mutant Found
    return not v.wasSuccessful()

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
        try:
            mutant_src = mu.gen_mutant(mainsrc, lst_locations)
            mutant = import_code(mutant_src, mainname)
            r =  evalmutant(mainname, mutant, test_code)
            #if not r:
            #    with open(mainfile + '_mutant_' + '_'.join([str(i) for i in lst_locations]) + '.py', 'w+') as a:
            #        print(mutant_src,file=a)
            return r
        except SyntaxError:
            print('Syntax!', lst_locations)
            return True

    mutate_lst = sorted(list(range(1, num_statements+1)))
    r = m.minimize(mutate_lst, mytest)
    composite_list = [r[x:x+10] for x in range(0, len(r),10)]
    for i in composite_list:
        print(i)
    print('Total executions: ', nexecutions, ' for ', len(mutate_lst), ' muscore = ', len(r)/len(mutate_lst))

main(sys.argv[1:])
