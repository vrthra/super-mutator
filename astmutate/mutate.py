#!/usr/bin/env python3
import sys
import ast
import astunparse
import random

class StmtMutator(ast.NodeTransformer):
    def __init__(self, mutate_lst):
        self.i = 0
        self.mutate_lst = mutate_lst

    def slightly_specific_visitor(self, node):
        self.i += 1
        if self.i in self.mutate_lst:
            return ast.Pass()
        return self.generic_visit(node)

    def visit_Return(self, node): return self.slightly_specific_visitor(node)
    def visit_Delete(self, node): return self.slightly_specific_visitor(node)

    def visit_Assign(self, node): return self.slightly_specific_visitor(node)
    def visit_AnnAssign(self, node): return self.slightly_specific_visitor(node)
    def visit_AugAssign(self, node): return self.slightly_specific_visitor(node)

    def visit_Raise(self, node): return self.slightly_specific_visitor(node)
    def visit_Assert(self, node): return self.slightly_specific_visitor(node)

    def visit_Global(self, node): return self.slightly_specific_visitor(node)
    def visit_Nonlocal(self, node): return self.slightly_specific_visitor(node)

    def visit_Expr(self, node): return self.slightly_specific_visitor(node)

    def visit_Pass(self, node): return self.slightly_specific_visitor(node)
    def visit_Break(self, node): return self.slightly_specific_visitor(node)
    def visit_Continue(self, node): return self.slightly_specific_visitor(node)

def parse(mysrc):
    s = StmtCounter()
    s.visit(ast.parse(mysrc))
    num_statements = s.i
    num_statements_to_mutate = num_statements
    mutate_lst = random.sample(range(1, num_statements+1), num_statements_to_mutate)
    v = StmtMutator(mutate_lst).visit(ast.parse(mysrc))
    return astunparse.unparse(parse(mysrc))


def gen_mutant(mysrc, mutate_lst):
    v = StmtMutator(mutate_lst).visit(ast.parse(mysrc))
    return astunparse.unparse(v)
