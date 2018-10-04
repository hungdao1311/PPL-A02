# Generated from /home/hungdao1311/Documents/PPL/assignment2/upload/src/main/mp/parser/MP.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete listener for a parse tree produced by MPParser.
class MPListener(ParseTreeListener):

    # Enter a parse tree produced by MPParser#program.
    def enterProgram(self, ctx:MPParser.ProgramContext):
        pass

    # Exit a parse tree produced by MPParser#program.
    def exitProgram(self, ctx:MPParser.ProgramContext):
        pass


    # Enter a parse tree produced by MPParser#decl.
    def enterDecl(self, ctx:MPParser.DeclContext):
        pass

    # Exit a parse tree produced by MPParser#decl.
    def exitDecl(self, ctx:MPParser.DeclContext):
        pass


    # Enter a parse tree produced by MPParser#var_dec.
    def enterVar_dec(self, ctx:MPParser.Var_decContext):
        pass

    # Exit a parse tree produced by MPParser#var_dec.
    def exitVar_dec(self, ctx:MPParser.Var_decContext):
        pass


    # Enter a parse tree produced by MPParser#var_dec_list.
    def enterVar_dec_list(self, ctx:MPParser.Var_dec_listContext):
        pass

    # Exit a parse tree produced by MPParser#var_dec_list.
    def exitVar_dec_list(self, ctx:MPParser.Var_dec_listContext):
        pass


    # Enter a parse tree produced by MPParser#one_var_dec.
    def enterOne_var_dec(self, ctx:MPParser.One_var_decContext):
        pass

    # Exit a parse tree produced by MPParser#one_var_dec.
    def exitOne_var_dec(self, ctx:MPParser.One_var_decContext):
        pass


    # Enter a parse tree produced by MPParser#id_list.
    def enterId_list(self, ctx:MPParser.Id_listContext):
        pass

    # Exit a parse tree produced by MPParser#id_list.
    def exitId_list(self, ctx:MPParser.Id_listContext):
        pass


    # Enter a parse tree produced by MPParser#main_type.
    def enterMain_type(self, ctx:MPParser.Main_typeContext):
        pass

    # Exit a parse tree produced by MPParser#main_type.
    def exitMain_type(self, ctx:MPParser.Main_typeContext):
        pass


    # Enter a parse tree produced by MPParser#primitive_type.
    def enterPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by MPParser#primitive_type.
    def exitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by MPParser#array_dec.
    def enterArray_dec(self, ctx:MPParser.Array_decContext):
        pass

    # Exit a parse tree produced by MPParser#array_dec.
    def exitArray_dec(self, ctx:MPParser.Array_decContext):
        pass


    # Enter a parse tree produced by MPParser#array_bound.
    def enterArray_bound(self, ctx:MPParser.Array_boundContext):
        pass

    # Exit a parse tree produced by MPParser#array_bound.
    def exitArray_bound(self, ctx:MPParser.Array_boundContext):
        pass


    # Enter a parse tree produced by MPParser#func_dec.
    def enterFunc_dec(self, ctx:MPParser.Func_decContext):
        pass

    # Exit a parse tree produced by MPParser#func_dec.
    def exitFunc_dec(self, ctx:MPParser.Func_decContext):
        pass


    # Enter a parse tree produced by MPParser#procedure_dec.
    def enterProcedure_dec(self, ctx:MPParser.Procedure_decContext):
        pass

    # Exit a parse tree produced by MPParser#procedure_dec.
    def exitProcedure_dec(self, ctx:MPParser.Procedure_decContext):
        pass


    # Enter a parse tree produced by MPParser#exp_element.
    def enterExp_element(self, ctx:MPParser.Exp_elementContext):
        pass

    # Exit a parse tree produced by MPParser#exp_element.
    def exitExp_element(self, ctx:MPParser.Exp_elementContext):
        pass


    # Enter a parse tree produced by MPParser#invo_exp.
    def enterInvo_exp(self, ctx:MPParser.Invo_expContext):
        pass

    # Exit a parse tree produced by MPParser#invo_exp.
    def exitInvo_exp(self, ctx:MPParser.Invo_expContext):
        pass


    # Enter a parse tree produced by MPParser#index_exp.
    def enterIndex_exp(self, ctx:MPParser.Index_expContext):
        pass

    # Exit a parse tree produced by MPParser#index_exp.
    def exitIndex_exp(self, ctx:MPParser.Index_expContext):
        pass


    # Enter a parse tree produced by MPParser#exp_list.
    def enterExp_list(self, ctx:MPParser.Exp_listContext):
        pass

    # Exit a parse tree produced by MPParser#exp_list.
    def exitExp_list(self, ctx:MPParser.Exp_listContext):
        pass


    # Enter a parse tree produced by MPParser#exp.
    def enterExp(self, ctx:MPParser.ExpContext):
        pass

    # Exit a parse tree produced by MPParser#exp.
    def exitExp(self, ctx:MPParser.ExpContext):
        pass


    # Enter a parse tree produced by MPParser#exp1.
    def enterExp1(self, ctx:MPParser.Exp1Context):
        pass

    # Exit a parse tree produced by MPParser#exp1.
    def exitExp1(self, ctx:MPParser.Exp1Context):
        pass


    # Enter a parse tree produced by MPParser#exp2.
    def enterExp2(self, ctx:MPParser.Exp2Context):
        pass

    # Exit a parse tree produced by MPParser#exp2.
    def exitExp2(self, ctx:MPParser.Exp2Context):
        pass


    # Enter a parse tree produced by MPParser#exp3.
    def enterExp3(self, ctx:MPParser.Exp3Context):
        pass

    # Exit a parse tree produced by MPParser#exp3.
    def exitExp3(self, ctx:MPParser.Exp3Context):
        pass


    # Enter a parse tree produced by MPParser#exp4.
    def enterExp4(self, ctx:MPParser.Exp4Context):
        pass

    # Exit a parse tree produced by MPParser#exp4.
    def exitExp4(self, ctx:MPParser.Exp4Context):
        pass


    # Enter a parse tree produced by MPParser#exp5.
    def enterExp5(self, ctx:MPParser.Exp5Context):
        pass

    # Exit a parse tree produced by MPParser#exp5.
    def exitExp5(self, ctx:MPParser.Exp5Context):
        pass


    # Enter a parse tree produced by MPParser#stmt.
    def enterStmt(self, ctx:MPParser.StmtContext):
        pass

    # Exit a parse tree produced by MPParser#stmt.
    def exitStmt(self, ctx:MPParser.StmtContext):
        pass


    # Enter a parse tree produced by MPParser#assign_stmt.
    def enterAssign_stmt(self, ctx:MPParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by MPParser#assign_stmt.
    def exitAssign_stmt(self, ctx:MPParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by MPParser#lhs.
    def enterLhs(self, ctx:MPParser.LhsContext):
        pass

    # Exit a parse tree produced by MPParser#lhs.
    def exitLhs(self, ctx:MPParser.LhsContext):
        pass


    # Enter a parse tree produced by MPParser#assign_stmt1.
    def enterAssign_stmt1(self, ctx:MPParser.Assign_stmt1Context):
        pass

    # Exit a parse tree produced by MPParser#assign_stmt1.
    def exitAssign_stmt1(self, ctx:MPParser.Assign_stmt1Context):
        pass


    # Enter a parse tree produced by MPParser#if_stmt.
    def enterIf_stmt(self, ctx:MPParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MPParser#if_stmt.
    def exitIf_stmt(self, ctx:MPParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MPParser#while_stmt.
    def enterWhile_stmt(self, ctx:MPParser.While_stmtContext):
        pass

    # Exit a parse tree produced by MPParser#while_stmt.
    def exitWhile_stmt(self, ctx:MPParser.While_stmtContext):
        pass


    # Enter a parse tree produced by MPParser#for_stmt.
    def enterFor_stmt(self, ctx:MPParser.For_stmtContext):
        pass

    # Exit a parse tree produced by MPParser#for_stmt.
    def exitFor_stmt(self, ctx:MPParser.For_stmtContext):
        pass


    # Enter a parse tree produced by MPParser#break_stmt.
    def enterBreak_stmt(self, ctx:MPParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by MPParser#break_stmt.
    def exitBreak_stmt(self, ctx:MPParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by MPParser#continue_stmt.
    def enterContinue_stmt(self, ctx:MPParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by MPParser#continue_stmt.
    def exitContinue_stmt(self, ctx:MPParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by MPParser#return_stmt.
    def enterReturn_stmt(self, ctx:MPParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MPParser#return_stmt.
    def exitReturn_stmt(self, ctx:MPParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MPParser#compound_stmt.
    def enterCompound_stmt(self, ctx:MPParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by MPParser#compound_stmt.
    def exitCompound_stmt(self, ctx:MPParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by MPParser#stmt_list.
    def enterStmt_list(self, ctx:MPParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by MPParser#stmt_list.
    def exitStmt_list(self, ctx:MPParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by MPParser#with_stmt.
    def enterWith_stmt(self, ctx:MPParser.With_stmtContext):
        pass

    # Exit a parse tree produced by MPParser#with_stmt.
    def exitWith_stmt(self, ctx:MPParser.With_stmtContext):
        pass


    # Enter a parse tree produced by MPParser#call_stmt.
    def enterCall_stmt(self, ctx:MPParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by MPParser#call_stmt.
    def exitCall_stmt(self, ctx:MPParser.Call_stmtContext):
        pass


