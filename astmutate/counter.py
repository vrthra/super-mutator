#!/usr/bin/env python3
import sys
import ast
import astunparse
import random

class StmtCounter(ast.NodeVisitor):
    def __init__(self):
        self.i = 0

    def slightly_specific_visitor(self, node):
        self.i += 1
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


def get_statements(mysrc):
    s = StmtCounter()
    s.visit(ast.parse(mysrc))
    return s.i
