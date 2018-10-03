from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.decl()])

    def visitDecl(self,ctx:MPParser.DeclContext):
    # decl : var_dec | func_dec | procedure_dec
        return self.visitChildren(ctx)

    def visitVar_dec(self,ctx:MPParser.Var_decContext):
    #var_dec : VAR var_dec_list SM
        return self.visit(ctx.var_dec_list())
    
    def visitVar_dec_list(self,ctx:MPParser.Var_dec_listContext):
    # var_dec_list : one_var_dec var_dec_list
    #              | one_var_dec;
        if (ctx.var_dec_list()):
            return [self.visit(ctx.one_var_dec())] + [self.visit(ctx.var_dec_list())]
        else:
            return [self.visit(ctx.one_var_dec())]
    def visitId_list(self,ctx:MPParser.Id_listContext):
    # id_list : ID CM id_list
    #         | ID;
        if (ctx.id_list()):
            return [Id(ctx.ID().getText())] + [self.visit(ctx.id_list())]
        else:
            return [Id(ctx.ID().getText())]
  
    def visitOne_var_dec(self,ctx:MPParser.One_var_decContext):
    #one_var_dec: id_list COLON main_type SM;
        return VarDecl(self.visit(x), self.visit(ctx.main_type()))

    def visitMain_type(self,ctx:MPParser.Main_typeContext):
        return self.visitChildren(ctx)

    def visitPrimitive_type(self,ctx:MPParser.Primitive_typeContext):
    #primitive_type : (BOOLEAN | INTEGER | REAL | STRING)
        if ctx.BOOLEAN():
            return BoolType()
        elif ctx.INTEGER():
            return IntType()
        elif ctx.REAL():
            return FloatType()
        elif ctx.STRING():
            return StringType()
    
    def visitArray_dec(self,ctx:MPParser.Array_decContext):
    #array_dec : ARRAY LSB array_bound DOTDOT array_bound RSB OF primitive_type
        return ArrayType(self.visit(ctx.array_bound(0)),self.visit(ctx.array_bound(1)),self.visit(ctx.primitive_type()))

    def visitArray_bound(self, ctx:MPParser.Array_boundContext):
        return ctx.getText()
    
    def visitFunc_dec(self, ctx:MPParser.Func_decContext):
    # func_dec : FUNCTION ID LB var_dec_list? RB COLON main_type SM var_dec? compound_stmt
        param = self.visit(ctx.var_dec_list()) if ctx.var_dec_list() else []
        type = self.visit(ctx.main_type()) 
        var = self.visit(ctx.var_dec())if ctx.var_dec() else []
        cpstmt = self.visit(ctx.compound_stmt())
        return FuncDecl(Id(ctx.ID().getText()),param,var,cpstmt,type)

    def visitProcedure_dec(self, ctx:MPParser.Procedure_decContext):
    # procedure_dec : PROCEDURE ID LB var_dec_list? RB SM var_dec? compound_stmt
        param = self.visit(ctx.var_dec_list()) if ctx.var_dec_list() else []
        var = self.visit(ctx.var_dec())if ctx.var_dec() else []
        cpstmt = self.visit(ctx.compound_stmt())
        return FuncDecl(Id(ctx.ID().getText()),param,var,cpstmt)
    
    def visitExp_element(self, ctx:MPParser.Exp_elementContext):
    # exp_element: STRING_LIT | INT_LIT | FLOAT_LIT | BOOL_LIT | ID | invo_exp | index_exp
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        elif ctx.BOOL_LIT():
            return BoolLiteral(ctx.BOOL_LIT().getText())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.invo_exp():
            return self.visit(ctx.invo_exp())
        elif ctx.index_exp():
            return self.visit(ctx.index_exp())

    def visitInvo_exp(self, ctx:MPParser.Invo_expContext):
    #invo_exp : ID LB exp_list RB;
        if (ctx.exp_list()) :
            return CallStmt(Id(ctx.ID().getText()),self.visit(ctx.exp_list()))
        else:
            return CallStmt(Id(ctx.ID().getText()),[])
    def visitIndex_exp(self, ctx:MPParser.Index_expContext):
    #index_exp : (STRING_LIT | INT_LIT | FLOAT_LIT | BOOL_LIT | ID | invo_exp | LB exp RB) (LSB exp RSB)| index_exp LSB exp RSB;
        if (ctx.getChildCount() == 4): 
            if ctx.STRING_LIT():
                arr = StringLiteral(ctx.STRING_LIT().getText())
            elif ctx.INT_LIT():
                arr = IntLiteral(ctx.INT_LIT().getText())
            elif ctx.FLOAT_LIT():
                arr = FloatLiteral(ctx.FLOAT_LIT().getText())
            elif ctx.BOOL_LIT():
                arr = BoolLiteral(ctx.BOOL_LIT().getText())
            elif ctx.ID():
                arr = Id(ctx.ID().getText())
            elif ctx.invo_exp():
                arr = self.visit(ctx.invo_exp())
            elif ctx.index_exp():
                arr = self.visit(ctx.index_exp())
            index = self.visit(ctx.exp())
        else:
            arr = self.visit(ctx.exp(0))
            index = self.visit(ctx.exp(1))
        return ArrayCell(arr,index)
    
    def visitExp_list(self, ctx:MPParser.Exp_listContext):  
    #exp_list : exp CM exp_list | exp;
        if (ctx.exp_list()):
            return [self.visit(ctx.exp())] + [self.visit(ctx.exp_list())]
        else:
            return [self.visit(ctx.exp())]
    
    def visitExp(self, ctx:MPParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        if ctx.getChild(1) == ctx.ANDTHEN():
            op = "andthen"
        elif ctx.getChild(1) == ctx.ORELSE():
            op = "orelse"
        return BinaryOp(op,self.visit(ctx.exp()),self.visit(ctx.exp1()))
    
    def visitExp1(self, ctx:MPParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
    
    def visitExp2(self, ctx:MPParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))

    def visitExp3(self, ctx:MPParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
    
    def visitExp4(self, ctx:MPParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp4()))
    
    def visitExp5(self, ctx:MPParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return self.visit(ctx.exp())
    
    def visitStmt(self, ctx:MPParser.StmtContext):
        return self.visitChildren(ctx)
    
    def visitAssign_stmt(self, ctx:MPParser.Assign_stmtContext):
        #assign_stmt : lhs ASSIGN assign_stmt1;
        return Assign(self.visit(ctx.lhs()),self.visit(ctx.assign_stmt1()))
    
    def visitAssign_stmt1(self, ctx:MPParser.Assign_stmt1Context):
        #assign_stmt1 : exp SM| assign_stmt;
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            return self.visit(ctx.exp()) 

    def visitLhs(self, ctx:MPParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visitChildren(ctx)

    def visitIf_stmt(self, ctx:MPParser.If_stmtContext):
        #if_stmt : IF exp THEN stmt (ELSE stmt)?;
        if ctx.ELSE():
            return If(self.visit(ctx.exp()),self.visit(ctx.stmt(0)),self.visit(ctx.stmt(1)))
        else: 
            return If(self.visit(ctx.exp()),self.visit(ctx.stmt()))
    
    def visitWhile_stmt(self, ctx:MPParser.While_stmtContext):
        #while_stmt : WHILE exp DO stmt;
        return While(self.visit(ctx.exp()),self.visit(ctx.stmt()))
    
    def visitFor_stmt(self, ctx:MPParser.For_stmtContext):
    #for_stmt : FOR ID ASSIGN exp (TO | DOWNTO) exp DO stmt;
        if ctx.TO():
            up = True
        else: 
            up = False 
        return For(Id(ctx.ID().getText()),self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),up,self.visit(stmt()))
    
    def visitBreak_stmt(self, ctx:MPParser.Break_stmtContext):
        return Break()
    
    def visitContinue_stmt(self, ctx:MPParser.Continue_stmtContext):
        return Continue()
    
    def visitReturn_stmt(self, ctx:MPParser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        else:
            return Return()

    def visitCompound_stmt(self, ctx:MPParser.Compound_stmtContext):
        return self.visit(ctx.stmt_list())

    def visitStmt_list(self, ctx:MPParser.Stmt_listContext):
        #stmt_list : stmt stmt_list|;
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.stmt())] + [self.visit(ctx.stmt_list())]
 
    def visitWith_stmt(self, ctx:MPParser.With_stmtContext):
        return With(self.visit(ctx.var_dec_list()),self.visit(ctx.stmt()))

    def visitCall_stmt(self, ctx:MPParser.Call_stmtContext):
        if (ctx.exp_list()) :
            return CallStmt(Id(ctx.ID().getText()),self.visit(ctx.exp_list()))
        else:
            return CallStmt(Id(ctx.ID().getText()),[])

        
        