expectAST_content = r"""
from abc import ABC,abstractmethod,ABCMeta
from Visitor import Visitor
class AST(ABC):
        def __eq__(self,other):return self.__dict__==other.__dict__
        @abstractmethod
        def accept(self,v,param):return v.visit(self,param)
class Type(AST):__metaclass__=ABCMeta
class IntType(Type):
        def __str__(self):return'IntType()'
        def accept(self,v,param):return v.visitIntType(self,param)
class FloatType(Type):
        def __str__(self):return'FloatType()'
        def accept(self,v,param):return v.visitFloatType(self,param)
class BoolType(Type):
        def __str__(self):return'BoolType()'
        def accept(self,v,param):return v.visitBoolType(self,param)
class StringType(Type):
        def __str__(self):return'StringType()'
        def accept(self,v,param):return v.visitStringType(self,param)
class ArrayType(Type):
        def __init__(self,lower,upper,eleType):
                self.lower=lower;self.upper=upper;self.eleType=eleType
        def __str__(self):return'ArrayType('+str(self.lower)+ \
                    ','+str(self.upper)+','+str(self.eleType)+')'
        def accept(self,v,param):return v.visitArrayType(self,param)
class VoidType(Type):
        def __str__(self):return'VoidType()'
        def accept(self,v,param):return v.visitVoidType(self,param)
class Program(AST):
        def __init__(self,decl):self.decl=decl
        def __str__(
            self):return'Program(['+','.join((str(i)for i in(self.decl)))+'])'
        def accept(self,v,param):return v.visitProgram(self,param)
class Decl(AST):__metaclass__=ABCMeta
class VarDecl(Decl):
        def __init__(self,variable,varType):
                self.variable=variable;self.varType=varType
        def __str__(self):return'VarDecl('+ \
                    str(self.variable)+','+str(self.varType)+')'
        def accept(self,v,param):return v.visitVarDecl(self,param)
class FuncDecl(Decl):
        def __init__(self,name,param,local,body,returnType=VoidType()):
                self.name=name;self.param=param;self.returnType=returnType;self.local=local;self.body=body
        def __str__(self):return'FuncDecl('+str(self.name)+',['+','.join((str(i)for i in(self.param)))+'],['+','.join(
            (str(i)for i in(self.local)))+'],['+','.join((str(i)for i in(self.body)))+'],'+str(self.returnType)+')'
        def accept(self,v,param):return v.visitFuncDecl(self,param)
class Stmt(AST):__metaclass__=ABCMeta
class Assign(Stmt):
        def __init__(self,lhs,exp):
                self.lhs=lhs;self.exp=exp
        def __str__(self):return'Assign('+str(self.lhs)+','+str(self.exp)+')'
        def accept(self,v,param):return v.visitAssign(self,param)
class AssignStmt(Stmt):
        def __init__(self,lhs,exp):
                self.lhs=lhs;self.exp=exp
        def __str__(self):return'Assign('+str(self.lhs)+','+str(self.exp)+')'
        def accept(self,v,param):return v.visitAssign(self,param)
class If(Stmt):
        def __init__(self,expr,thenStmt,elseStmt=[]):
                self.expr=expr;self.thenStmt=thenStmt;self.elseStmt=elseStmt
        def __str__(self):return'If('+str(self.expr)+',['+','.join((str(i)for i in(
            self.thenStmt)))+'],['+','.join((str(i)for i in(self.elseStmt)))+'])'
        def accept(self,v,param):return v.visitIf(self,param)
class While(Stmt):
        def __init__(self,exp,sl):
                self.sl=sl;self.exp=exp
        def __str__(self):return'While('+str(self.exp)+ \
                    ',['+','.join((str(i)for i in(self.sl)))+'])'
        def accept(self,v,param):return v.visitWhile(self,param)
class For(Stmt):
        def __init__(self,id,expr1,expr2,up,loop):
                self.id=id;self.expr1=expr1;self.expr2=expr2;self.up=up;self.loop=loop
        def __str__(self):return'For('+str(self.id)+','+str(self.expr1)+','+ \
                    str(self.expr2)+','+str(self.up)+ \
                        ',['+','.join((str(i)for i in(self.loop)))+'])'
        def accept(self,v,param):return v.visitFor(self,param)
class Break(Stmt):
        def __str__(self):return'Break()'
        def accept(self,v,param):return v.visitBreak(self,param)
class Continue(Stmt):
        def __str__(self):return'Continue()'
        def accept(self,v,param):return v.visitContinue(self,param)
class Return(Stmt):
        def __init__(self,expr=None):self.expr=expr
        def __str__(self):return'Return('+ \
                    ('None'if self.expr is None else str(self.expr))+')'
        def accept(self,v,param):return v.visitReturn(self,param)
class With(Stmt):
        def __init__(self,decl,stmt):
                self.decl=decl;self.stmt=stmt
        def __str__(self):return'With(['+','.join(
            (str(i)for i in(self.decl)))+'],['+','.join((str(i)for i in(self.stmt)))+'])'
        def accept(self,v,param):return v.visitWith(self,param)
class CallStmt(Stmt):
        def __init__(self,method,param):
                self.method=method;self.param=param
        def __str__(self):return'CallStmt('+str(self.method)+ \
                    ',['+','.join((str(i)for i in(self.param)))+'])'
        def accept(self,v,param):return v.visitCallStmt(self,param)
class Expr(AST):__metaclass__=ABCMeta
class BinaryOp(Expr):
        def __init__(self,op,left,right):
                self.op=op;self.left=left;self.right=right
        def __str__(self):return"BinaryOp(r'"+self.op+"',"+ \
                    str(self.left)+','+str(self.right)+')'
        def accept(self,v,param):return v.visitBinaryOp(self,param)
class UnaryOp(Expr):
        def __init__(self,op,body):
                self.op=op;self.body=body
        def __str__(self):return"UnaryOp(r'"+self.op+"',"+str(self.body)+')'
        def accept(self,v,param):return v.visitUnaryOp(self,param)
class CallExpr(Expr):
        def __init__(self,method,param):
                self.method=method;self.param=param
        def __str__(self):return'CallExpr('+str(self.method)+ \
                    ',['+','.join((str(i)for i in(self.param)))+'])'
        def accept(self,v,param):return v.visitCallExpr(self,param)
class LHS(Expr):__metaclass__=ABCMeta
class Id(LHS):
        def __init__(self,name):self.name=name
        def __str__(self):return"Id(r'"+self.name+"')"
        def accept(self,v,param):return v.visitId(self,param)
class ArrayCell(LHS):
        def __init__(self,arr,idx):
                self.arr=arr;self.idx=idx
        def __str__(self):return'ArrayCell('+ \
                    str(self.arr)+','+str(self.idx)+')'
        def accept(self,v,param):return v.visitArrayCell(self,param)
class Literal(Expr):__metaclass__=ABCMeta
class IntLiteral(Literal):
        def __init__(self,value):self.value=value
        def __str__(self):return'IntLiteral('+str(self.value)+')'
        def accept(self,v,param):return v.visitIntLiteral(self,param)
class FloatLiteral(Literal):
        def __init__(self,value):self.value=value
        def __str__(self):return'FloatLiteral('+str(self.value)+')'
        def accept(self,v,param):return v.visitFloatLiteral(self,param)
class StringLiteral(Literal):
        def __init__(self,value):self.value=value
        def __str__(self):return"StringLiteral(r'"+self.value+"')"
        def accept(self,v,param):return v.visitStringLiteral(self,param)
class BooleanLiteral(Literal):
        def __init__(self,value):self.value=value
        def __str__(self):return'BooleanLiteral('+str(self.value)+')'
        def accept(self,v,param):return v.visitBooleanLiteral(self,param)
"""

python = "python"

import os


def main(argv):
    if len(argv) >= 2:
        print("Usage: [<PYTHON_EXECUTABLE>] expect.py [<PYTHON_EXECUTABLE>]")
        exit()
    elif len(argv) == 1:
        global python
        python = argv[0]


if __name__ == "__main__":
    main(os.sys.argv[1:])

expectAST_file = open("main/mp/utils/ExpectAST.py", "w+")
expectAST_file.write(expectAST_content)
expectAST_file.close()

from shutil import copy
import time
t = time.time()
print("Creating backup file " + "ASTGeneration_backup_" + str(t) + ".py")
copy("main/mp/astgen/ASTGeneration.py",
     "main/mp/astgen/ASTGeneration_backup_" + str(t) + ".py")
print("Creating backup file " + "ASTGenSuite_backup_" + str(t) + ".py")
copy("test/ASTGenSuite.py", "test/ASTGenSuite_backup_" + str(t) + ".py")

ASTGeneration_file = open("main/mp/astgen/ASTGeneration.py", "r+")
new_ASTGeneration_content = ASTGeneration_file.read().replace(
    "from AST import *", "from ExpectAST import *")
ASTGeneration_file.close()
ASTGeneration_file = open("main/mp/astgen/ASTGeneration.py", "w+")
ASTGeneration_file.write(new_ASTGeneration_content)
ASTGeneration_file.close()

ASTGenSuite_file = open("test/ASTGenSuite.py", "r+")
new_ASTGenSuite_content = ASTGenSuite_file.read().replace(
    "from AST import *", "from ExpectAST import *")
ASTGenSuite_file.close()
ASTGenSuite_file = open("test/ASTGenSuite.py", "w+")
ASTGenSuite_file.write(new_ASTGenSuite_content)
ASTGenSuite_file.close()

import subprocess

os.chdir(os.path.dirname(os.path.realpath(__file__)))
subprocess.Popen([python, "run.py", "test", "ASTGenSuite"],
                 stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

import re
ASTGenSuite_file = open("test/ASTGenSuite.py", "r")
expect_assert_pattern = re.compile(
    r'(?P<expect_assert>expect\s*=.*?(?P<spaces>\s*)self.assertTrue\s*\(TestAST\.test\(\s*input\s*,\s*expect\s*,\s*(?P<num>[0-9]+)\s*\)\s*\))', re.DOTALL)
ASTGenSuite_content = ASTGenSuite_file.read()
matches = expect_assert_pattern.findall(ASTGenSuite_content)
ASTGenSuite_file.close()
for match in matches:
    print("Processing output " + match[2])
    output_file = open("test/solutions/" + match[2] + ".txt", "r")
    output = output_file.read()
    ASTGenSuite_content = ASTGenSuite_content.replace(
        match[0], 'expect = str(' + output + ')' + match[1] + 'self.assertTrue(TestAST.test(input,expect,' + match[2] + '))', 1)
    output_file.close()
ASTGenSuite_file = open("test/ASTGenSuite.py", "w+")
ASTGenSuite_file.write(ASTGenSuite_content)
ASTGenSuite_file.close()

if os.path.exists("main/mp/utils/ExpectAST.py"):
    os.remove("main/mp/utils/ExpectAST.py")

ASTGeneration_file = open("main/mp/astgen/ASTGeneration.py", "r+")
new_ASTGeneration_content = ASTGeneration_file.read().replace(
    "from ExpectAST import *", "from AST import *")
ASTGeneration_file.close()
ASTGeneration_file = open("main/mp/astgen/ASTGeneration.py", "w+")
ASTGeneration_file.write(new_ASTGeneration_content)
ASTGeneration_file.close()

ASTGenSuite_file = open("test/ASTGenSuite.py", "r+")
new_ASTGenSuite_content = ASTGenSuite_file.read().replace(
    "from ExpectAST import *", "from AST import *")
ASTGenSuite_file.close()
ASTGenSuite_file = open("test/ASTGenSuite.py", "w+")
ASTGenSuite_file.write(new_ASTGenSuite_content)
ASTGenSuite_file.close()

os.chdir(os.path.dirname(os.path.realpath(__file__)))
subprocess.Popen([python, "run.py", "test", "ASTGenSuite"],
                 stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

ASTGeneration_backup_pattern = re.compile(
    r"ASTGeneration_backup_[0-9]+\.[0-9]+\.py")
for root, dirs, files in os.walk("main/mp/astgen/"):
    for file_ in files:
        if ASTGeneration_backup_pattern.match(file_):
            print("Removing backup file " + file_)
            os.remove(os.path.join(root, file_))

print("Finished replacing expected outputs.")
