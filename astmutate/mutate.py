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

    def visit_FunctionDef(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AsyncFunctionDef(self, node):
        return self.slightly_specific_visitor(node)
    def visit_ClassDef(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Return(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Delete(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Assign(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AnnAssign(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AugAssign(self, node):
        return self.slightly_specific_visitor(node)

    def visit_For(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AsyncFor(self, node):
        return self.slightly_specific_visitor(node)
    def visit_While(self, node):
        return self.slightly_specific_visitor(node)
    def visit_If(self, node):
        return self.slightly_specific_visitor(node)
    def visit_With(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AsyncWith(self, node):
        return self.slightly_specific_visitor(node)
    def visit_While(self, node):
        return self.slightly_specific_visitor(node)

    def visit_If(self, node):
        return self.slightly_specific_visitor(node)
    def visit_With(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AsyncWith(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Raise(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Try(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Assert(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Import(self, node):
        return self.slightly_specific_visitor(node)
    def visit_ImportFrom(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Global(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Nonlocal(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Expr(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Pass(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Break(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Continue(self, node):
        return self.slightly_specific_visitor(node)


class StmtMutator(ast.NodeTransformer):
    def __init__(self, mutate_lst):
        self.i = 0
        self.mutate_lst = mutate_lst

    def slightly_specific_visitor(self, node):
        self.i += 1
        if self.i in self.mutate_lst:
            return ast.Pass()
        return self.generic_visit(node)

    def visit_FunctionDef(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AsyncFunctionDef(self, node):
        return self.slightly_specific_visitor(node)
    def visit_ClassDef(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Return(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Delete(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Assign(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AnnAssign(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AugAssign(self, node):
        return self.slightly_specific_visitor(node)

    def visit_For(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AsyncFor(self, node):
        return self.slightly_specific_visitor(node)
    def visit_While(self, node):
        return self.slightly_specific_visitor(node)
    def visit_If(self, node):
        return self.slightly_specific_visitor(node)
    def visit_With(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AsyncWith(self, node):
        return self.slightly_specific_visitor(node)
    def visit_While(self, node):
        return self.slightly_specific_visitor(node)

    def visit_If(self, node):
        return self.slightly_specific_visitor(node)
    def visit_With(self, node):
        return self.slightly_specific_visitor(node)
    def visit_AsyncWith(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Raise(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Try(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Assert(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Import(self, node):
        return self.slightly_specific_visitor(node)
    def visit_ImportFrom(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Global(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Nonlocal(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Expr(self, node):
        return self.slightly_specific_visitor(node)

    def visit_Pass(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Break(self, node):
        return self.slightly_specific_visitor(node)
    def visit_Continue(self, node):
        return self.slightly_specific_visitor(node)

def parse(mysrc):
    s = StmtCounter()
    s.visit(ast.parse(mysrc))
    print(s.i, file=sys.stderr)
    num_statements = s.i
    num_statements_to_mutate = min(100, num_statements)
    print(num_statements_to_mutate, num_statements, file=sys.stderr)
    mutate_lst = random.sample(range(1, num_statements), num_statements_to_mutate)
    print(mutate_lst, file=sys.stderr)
    return StmtMutator(mutate_lst).visit(ast.parse(mysrc))


def main(args):
    print(astunparse.unparse(parse(open(args[0]).read())))

main(sys.argv[1:])
