#!/usr/bin/env python3

import ast
import sys
import astunparse

print(astunparse.unparse(ast.parse(open(sys.argv[1]).read())))
