# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#decl.
    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_dec.
    def visitVar_dec(self, ctx:MPParser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_dec_list.
    def visitVar_dec_list(self, ctx:MPParser.Var_dec_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#one_var_dec.
    def visitOne_var_dec(self, ctx:MPParser.One_var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#id_list.
    def visitId_list(self, ctx:MPParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#main_type.
    def visitMain_type(self, ctx:MPParser.Main_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitive_type.
    def visitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#array_dec.
    def visitArray_dec(self, ctx:MPParser.Array_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#array_bound.
    def visitArray_bound(self, ctx:MPParser.Array_boundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_dec.
    def visitFunc_dec(self, ctx:MPParser.Func_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procedure_dec.
    def visitProcedure_dec(self, ctx:MPParser.Procedure_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp_element.
    def visitExp_element(self, ctx:MPParser.Exp_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#invo_exp.
    def visitInvo_exp(self, ctx:MPParser.Invo_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#index_exp.
    def visitIndex_exp(self, ctx:MPParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp_list.
    def visitExp_list(self, ctx:MPParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp5.
    def visitExp5(self, ctx:MPParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt.
    def visitStmt(self, ctx:MPParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_stmt.
    def visitAssign_stmt(self, ctx:MPParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lhs.
    def visitLhs(self, ctx:MPParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_stmt1.
    def visitAssign_stmt1(self, ctx:MPParser.Assign_stmt1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#if_stmt.
    def visitIf_stmt(self, ctx:MPParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#while_stmt.
    def visitWhile_stmt(self, ctx:MPParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#for_stmt.
    def visitFor_stmt(self, ctx:MPParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#break_stmt.
    def visitBreak_stmt(self, ctx:MPParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MPParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_stmt.
    def visitReturn_stmt(self, ctx:MPParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_stmt.
    def visitCompound_stmt(self, ctx:MPParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt_list.
    def visitStmt_list(self, ctx:MPParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#with_stmt.
    def visitWith_stmt(self, ctx:MPParser.With_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_stmt.
    def visitCall_stmt(self, ctx:MPParser.Call_stmtContext):
        return self.visitChildren(ctx)



del MPParser