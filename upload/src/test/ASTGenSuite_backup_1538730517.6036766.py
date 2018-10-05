import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_proc300(self):
        input = """ procedure main();
        begin
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,300))
        

    def test_var301(self):
        input = """var a,b : integer;"""
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))
        
    def test_built_in302(self):
        input = """procedure foo(a : integer);
            begin
            putIntLn(4);
            end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType())],[],[CallStmt(Id(r'putIntLn'),[IntLiteral(4)])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_array303(self):
        input = """procedure foo(a : integer;b : real);
    begin
        e := (3+4)/3;
        putint(a);
        a := b[4];
    return;
    end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType())],[],[Assign(Id(r'e'),BinaryOp(r'/',BinaryOp(r'+',IntLiteral(3),IntLiteral(4)),IntLiteral(3))),CallStmt(Id(r'putint'),[Id(r'a')]),Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(4))),Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_assign304(self):
        input = """procedure foo(a : integer;b : real);
    begin
        d := a[b] := b + 5;
    return;
    end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType())],[],[Assign(Id(r'd'),Assign(ArrayCell(Id(r'a'),Id(r'b')),BinaryOp(r'+',Id(r'b'),IntLiteral(5)))),Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_if305(self):
        input = """procedure main();
            begin
                 if a>b then a := b; else b:=a ;
            end
        """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'>',Id(r'a'),Id(r'b')),[Assign(Id(r'a'),Id(r'b'))],[Assign(Id(r'b'),Id(r'a'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_var_306(self):
        input = """
Var name, surname: String;
Procedure main();
Begin
	write("Enter your name:");
	readln(name);
	writeln("Your name is: ",name);
	readln();
End
        """
        expect = str(Program([VarDecl(Id(r'name'),StringType()),VarDecl(Id(r'surname'),StringType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'Enter your name:')]),CallStmt(Id(r'readln'),[Id(r'name')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Your name is: '),Id(r'name')]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_index307(self):
        input = """function foo(a : integer;b : real): array [1 .. 5] of real;
             begin
                 foo(2)[3+x] := a[b[2]] + 3;
                 return a;
            end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType())],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(2)]),BinaryOp(r'+',IntLiteral(3),Id(r'x'))),BinaryOp(r'+',ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))),IntLiteral(3))),Return(Id(r'a'))],ArrayType(1,5,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_complex_308(self):
        input = """
Var Sel: String;
    N1,N2, Total : Real;
    YN : String;  { this is a character variable type, which holds single characters ONLY }
procedure main();
Begin
	Total := 0;  { always initialise integer/real variables }
	GotoXy(4,3);
	Writeln("1.Addition");
	GotoXy(4,4);
	Writeln("2.Subtraction");
	GotoXy(4,5);
	Writeln("3.Exit");
	GotoXy(6,8);
	Write("Select: ");
	Sel := Readkey();

	If Sel = "1" {condition} Then 
	Begin  {more than one statement}
		ClrScr();
		Write("Input No.1:");
		Readln(N1);
		Write("Input No.2:");
		Readln(N2);
		Total := N1 + N2;
		Writeln("Addition: ",N1," + ",N2," = ",Total);
		Write("Press any key to continue...");
		Readkey();
	end { Closing the if statement }

	If Sel = "2" Then { note that here we do not use an assignment statement } 
	Begin 
		ClrScr();
		Write("Input No.1:");
		Readln(N1);
		Write("Input No.2:");
		Readln(N2);
		Total := N1 - N2;
		Write("Subtraction: ");
		Write(N1," - ",N2," = ",Total);
		Write("Press any key to continue...");
		Readkey();
	end  { Closing the if statement }

	If Sel = "3" Then 
	Begin
		ClrScr();
		Write("Are you sure?(Y/N)");
		YN := Readkey();
		If YN = "y" Then Halt(); { 1 instruction, so no need of Begin..End }
		If YN = "n" Then Goto1(); { the goto statement is not recommended for frequent use }
	End
End
        """
        expect = str(Program([VarDecl(Id(r'Sel'),StringType()),VarDecl(Id(r'N1'),FloatType()),VarDecl(Id(r'N2'),FloatType()),VarDecl(Id(r'Total'),FloatType()),VarDecl(Id(r'YN'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'Total'),IntLiteral(0)),CallStmt(Id(r'GotoXy'),[IntLiteral(4),IntLiteral(3)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'1.Addition')]),CallStmt(Id(r'GotoXy'),[IntLiteral(4),IntLiteral(4)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'2.Subtraction')]),CallStmt(Id(r'GotoXy'),[IntLiteral(4),IntLiteral(5)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'3.Exit')]),CallStmt(Id(r'GotoXy'),[IntLiteral(6),IntLiteral(8)]),CallStmt(Id(r'Write'),[StringLiteral(r'Select: ')]),Assign(Id(r'Sel'),CallExpr(Id(r'Readkey'),[])),If(BinaryOp(r'=',Id(r'Sel'),StringLiteral(r'1')),[CallStmt(Id(r'ClrScr'),[]),CallStmt(Id(r'Write'),[StringLiteral(r'Input No.1:')]),CallStmt(Id(r'Readln'),[Id(r'N1')]),CallStmt(Id(r'Write'),[StringLiteral(r'Input No.2:')]),CallStmt(Id(r'Readln'),[Id(r'N2')]),Assign(Id(r'Total'),BinaryOp(r'+',Id(r'N1'),Id(r'N2'))),CallStmt(Id(r'Writeln'),[StringLiteral(r'Addition: '),Id(r'N1'),StringLiteral(r' + '),Id(r'N2'),StringLiteral(r' = '),Id(r'Total')]),CallStmt(Id(r'Write'),[StringLiteral(r'Press any key to continue...')]),CallStmt(Id(r'Readkey'),[])],[]),If(BinaryOp(r'=',Id(r'Sel'),StringLiteral(r'2')),[CallStmt(Id(r'ClrScr'),[]),CallStmt(Id(r'Write'),[StringLiteral(r'Input No.1:')]),CallStmt(Id(r'Readln'),[Id(r'N1')]),CallStmt(Id(r'Write'),[StringLiteral(r'Input No.2:')]),CallStmt(Id(r'Readln'),[Id(r'N2')]),Assign(Id(r'Total'),BinaryOp(r'-',Id(r'N1'),Id(r'N2'))),CallStmt(Id(r'Write'),[StringLiteral(r'Subtraction: ')]),CallStmt(Id(r'Write'),[Id(r'N1'),StringLiteral(r' - '),Id(r'N2'),StringLiteral(r' = '),Id(r'Total')]),CallStmt(Id(r'Write'),[StringLiteral(r'Press any key to continue...')]),CallStmt(Id(r'Readkey'),[])],[]),If(BinaryOp(r'=',Id(r'Sel'),StringLiteral(r'3')),[CallStmt(Id(r'ClrScr'),[]),CallStmt(Id(r'Write'),[StringLiteral(r'Are you sure?(Y/N)')]),Assign(Id(r'YN'),CallExpr(Id(r'Readkey'),[])),If(BinaryOp(r'=',Id(r'YN'),StringLiteral(r'y')),[CallStmt(Id(r'Halt'),[])],[]),If(BinaryOp(r'=',Id(r'YN'),StringLiteral(r'n')),[CallStmt(Id(r'Goto1'),[])],[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,308))
        
    def test_if309(self):
        input = """procedure main();
            begin
                 if a>b then a := b; else b:=a ;
            end
        """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'>',Id(r'a'),Id(r'b')),[Assign(Id(r'a'),Id(r'b'))],[Assign(Id(r'b'),Id(r'a'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_expr310(self):
        input = """procedure foo(a:integer);
                begin
                    while true do putstring(a);
                end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType())],[],[While(BooleanLiteral(True),[CallStmt(Id(r'putstring'),[Id(r'a')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_with311(self):
        input = """var i : integer;
        function f(): integer;
        begin
        return 200;
        end
        procedure main();
        var
            main: integer;
        begin
            main := f;
            foo();
            putintln(main);
            with 
                i: integer;
                main: integer;
                f: integer;
            do  begin 
                main := f := i := 100;
                putIntLn(main);
                putIntLn(f);
                putIntLn(i);
                end
                putintlN(main);
        end
            var g: real;

        """
        expect = str(Program([VarDecl(Id(r'i'),IntType()),FuncDecl(Id(r'f'),[],[],[Return(IntLiteral(200))],IntType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'main'),IntType())],[Assign(Id(r'main'),Id(r'f')),CallStmt(Id(r'foo'),[]),CallStmt(Id(r'putintln'),[Id(r'main')]),With([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'main'),IntType()),VarDecl(Id(r'f'),IntType())],[Assign(Id(r'main'),Assign(Id(r'f'),Assign(Id(r'i'),IntLiteral(100)))),CallStmt(Id(r'putIntLn'),[Id(r'main')]),CallStmt(Id(r'putIntLn'),[Id(r'f')]),CallStmt(Id(r'putIntLn'),[Id(r'i')])]),CallStmt(Id(r'putintlN'),[Id(r'main')])],VoidType()),VarDecl(Id(r'g'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_if_312(self):
        input = """
Var
	SEL : Integer;
	YN : String;
procedure main();
Begin
	Writeln("[1]. PLAY GAME");
	WRITELN("[2]. LOAD GAME");
	WRITELN("[3]. MULTIPLAYER");
	WRITELN("[4]. EXIT GAME");
	Writeln("note: Do not press anything except");
	Writeln("numbers; otherwise an error occurs!");
	Readln(SEL);
	
	If SEL = 1 Then
	Begin
		Writeln("You will soon be able to create");
		Writeln("games using Pascal Programming :-)");
		Delay(3000);
		Goto(Ret);
	end

	If SEL = 2 Then
	Begin
		Writeln("Ahhh... no saved games");
		Delay(3000);
		Goto(Ret);
	end

	If SEL = 3 Then
	Begin
		Writeln("networking or 2 players?");
		Delay(3000);
		Goto(Ret);
	end

	If SEL = 4 Then
	Begin
		Writeln("Are you sure you want to Exit?");
		YN := Readkey;
		If YN = "y" Then
		Begin
			Writeln("Good Bye...");
			Delay(1000);
			Halt(); {EXIT PROGRAM}
		end

		If YN = "n" Then
			Goto(Ret);
	end
end
        """
        expect = str(Program([VarDecl(Id(r'SEL'),IntType()),VarDecl(Id(r'YN'),StringType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Writeln'),[StringLiteral(r'[1]. PLAY GAME')]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'[2]. LOAD GAME')]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'[3]. MULTIPLAYER')]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'[4]. EXIT GAME')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'note: Do not press anything except')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'numbers; otherwise an error occurs!')]),CallStmt(Id(r'Readln'),[Id(r'SEL')]),If(BinaryOp(r'=',Id(r'SEL'),IntLiteral(1)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'You will soon be able to create')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'games using Pascal Programming :-)')]),CallStmt(Id(r'Delay'),[IntLiteral(3000)]),CallStmt(Id(r'Goto'),[Id(r'Ret')])],[]),If(BinaryOp(r'=',Id(r'SEL'),IntLiteral(2)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'Ahhh... no saved games')]),CallStmt(Id(r'Delay'),[IntLiteral(3000)]),CallStmt(Id(r'Goto'),[Id(r'Ret')])],[]),If(BinaryOp(r'=',Id(r'SEL'),IntLiteral(3)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'networking or 2 players?')]),CallStmt(Id(r'Delay'),[IntLiteral(3000)]),CallStmt(Id(r'Goto'),[Id(r'Ret')])],[]),If(BinaryOp(r'=',Id(r'SEL'),IntLiteral(4)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'Are you sure you want to Exit?')]),Assign(Id(r'YN'),Id(r'Readkey')),If(BinaryOp(r'=',Id(r'YN'),StringLiteral(r'y')),[CallStmt(Id(r'Writeln'),[StringLiteral(r'Good Bye...')]),CallStmt(Id(r'Delay'),[IntLiteral(1000)]),CallStmt(Id(r'Halt'),[])],[]),If(BinaryOp(r'=',Id(r'YN'),StringLiteral(r'n')),[CallStmt(Id(r'Goto'),[Id(r'Ret')])],[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,312))
        

    def test_func313(self):
        input = """
        fUnCTiOn foo(): integer;
        var a,b: integer;
        begin
            a := a+b;
            bar(a);
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[Assign(Id(r'a'),BinaryOp(r'+',Id(r'a'),Id(r'b'))),CallStmt(Id(r'bar'),[Id(r'a')])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,313))
        
    def test_break314(self):
        input = """
var
   d: real;
procedure main();
begin
   while  a = true do
   begin   
      if( a > 15) then       
      break;
   end
end
        """
        expect = str(Program([VarDecl(Id(r'd'),FloatType()),FuncDecl(Id(r'main'),[],[],[While(BinaryOp(r'=',Id(r'a'),BooleanLiteral(True)),[If(BinaryOp(r'>',Id(r'a'),IntLiteral(15)),[Break()],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,314))
    
    def test_index_exp315(self):
        input = """
procedure main();
begin
    a := a[2] := 1[2] := a[b[2]];
end
        """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),Assign(ArrayCell(Id(r'a'),IntLiteral(2)),Assign(ArrayCell(IntLiteral(1),IntLiteral(2)),ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_array_dec316(self):
        input = """
        var  a: array [4 .. 9] of real ;          
        """
        expect = str(Program([VarDecl(Id(r'a'),ArrayType(4,9,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_array_dec317(self):
        input = """
        var  a: array [-4 .. 2] of integer ;          
        """
        expect = str(Program([VarDecl(Id(r'a'),ArrayType(-4,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_assign318(self):
        input = """procedurE inndeeexxx();
        begin
            (e>d)[5] := abc+a[1][2]; 
            foo(2)[a+3] := 5;
            ca[1][10] := 123;
        end"""
        expect = str(Program([FuncDecl(Id(r'inndeeexxx'),[],[],[Assign(ArrayCell(BinaryOp(r'>',Id(r'e'),Id(r'd')),IntLiteral(5)),BinaryOp(r'+',Id(r'abc'),ArrayCell(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(2)))),Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(2)]),BinaryOp(r'+',Id(r'a'),IntLiteral(3))),IntLiteral(5)),Assign(ArrayCell(ArrayCell(Id(r'ca'),IntLiteral(1)),IntLiteral(10)),IntLiteral(123))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,318))
    
    def test_complex319(self):
        input = """
        procedure Camelcase();

        var
            text, cc: string;
            c: string;
            i: integer;
            lastSpace: boolean;

        begin
            readln(text);
            lastSpace := true;
            cc := " ";
            for i := 1 to Length(text) do
            begin
                c := text[i];
                if ((c >= "65") and (c <= "90")) or ((c >= "97") and (c <= "122")) then
                begin
                    if (lastSpace) then
                    begin
                        if ((c >= "97") and (c <= "122")) then
                            c := chr(ord(c) - 32);
                    end
                    else
                        if ((c >= "65") and (c <= "90")) then
                            c := chr(ord(c) + 32);
                    cc := cc + c;
                    lastSpace := false;
                end
                else
                    lastSpace := true;
            end
            writeln(cc);
        end
        """
        expect = str(Program([FuncDecl(Id(r'Camelcase'),[],[VarDecl(Id(r'text'),StringType()),VarDecl(Id(r'cc'),StringType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'lastSpace'),BoolType())],[CallStmt(Id(r'readln'),[Id(r'text')]),Assign(Id(r'lastSpace'),BooleanLiteral(True)),Assign(Id(r'cc'),StringLiteral(r' ')),For(Id(r'i'),IntLiteral(1),CallExpr(Id(r'Length'),[Id(r'text')]),True,[Assign(Id(r'c'),ArrayCell(Id(r'text'),Id(r'i'))),If(BinaryOp(r'or',BinaryOp(r'and',BinaryOp(r'>=',Id(r'c'),StringLiteral(r'65')),BinaryOp(r'<=',Id(r'c'),StringLiteral(r'90'))),BinaryOp(r'and',BinaryOp(r'>=',Id(r'c'),StringLiteral(r'97')),BinaryOp(r'<=',Id(r'c'),StringLiteral(r'122')))),[If(Id(r'lastSpace'),[If(BinaryOp(r'and',BinaryOp(r'>=',Id(r'c'),StringLiteral(r'97')),BinaryOp(r'<=',Id(r'c'),StringLiteral(r'122'))),[Assign(Id(r'c'),CallExpr(Id(r'chr'),[BinaryOp(r'-',CallExpr(Id(r'ord'),[Id(r'c')]),IntLiteral(32))]))],[])],[If(BinaryOp(r'and',BinaryOp(r'>=',Id(r'c'),StringLiteral(r'65')),BinaryOp(r'<=',Id(r'c'),StringLiteral(r'90'))),[Assign(Id(r'c'),CallExpr(Id(r'chr'),[BinaryOp(r'+',CallExpr(Id(r'ord'),[Id(r'c')]),IntLiteral(32))]))],[])]),Assign(Id(r'cc'),BinaryOp(r'+',Id(r'cc'),Id(r'c'))),Assign(Id(r'lastSpace'),BooleanLiteral(False))],[Assign(Id(r'lastSpace'),BooleanLiteral(True))])]),CallStmt(Id(r'writeln'),[Id(r'cc')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_for320(self):
        input = """
Procedure DrawLine(X : Integer; Y : Integer);
    
    Begin 
        For count := 1 to 10 do
        Write(chr(196));
    End


        """
        expect = str(Program([FuncDecl(Id(r'DrawLine'),[VarDecl(Id(r'X'),IntType()),VarDecl(Id(r'Y'),IntType())],[],[For(Id(r'count'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'chr'),[IntLiteral(196)])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_proc321(self):
        input = """
Procedure Square(Index : Integer; Result : Integer);
Begin
    Result := Index * Index;
End

Procedure Main();
Begin
    Writeln("The square of 2 is: ");
    Square(2, Result);
End
        """
        expect = str(Program([FuncDecl(Id(r'Square'),[VarDecl(Id(r'Index'),IntType()),VarDecl(Id(r'Result'),IntType())],[],[Assign(Id(r'Result'),BinaryOp(r'*',Id(r'Index'),Id(r'Index')))],VoidType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'Writeln'),[StringLiteral(r'The square of 2 is: ')]),CallStmt(Id(r'Square'),[IntLiteral(2),Id(r'Result')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_stringlit322(self):
        input = """procedure main();
                beGin
                    a := "abcede";
                end

            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),StringLiteral(r'abcede'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_compound323(self):
        input = """procedure foo();
                   BEGIN
                    while (true) do begin begin end eND
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BooleanLiteral(True),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,323))
    
    def test_bool324(self):
        input = """
var check : Boolean;
    abc   : String;
Procedure main();
Begin
    While (check = True) Do
    Begin
        reAdLn(abc);
    End
End
        """
        expect = str(Program([VarDecl(Id(r'check'),BoolType()),VarDecl(Id(r'abc'),StringType()),FuncDecl(Id(r'main'),[],[],[While(BinaryOp(r'=',Id(r'check'),BooleanLiteral(True)),[CallStmt(Id(r'reAdLn'),[Id(r'abc')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_or_325(self):
        input = """
Var n1, n2 : string;
procedure main();
Begin
	Writeln("Enter two numbers: to exit)");
	While not ((n1 = "0") OR (n2 = "0")) do
    Begin
		Write("No.1: ");
		Readln(n1);
		Write("No.2: ");
		Readln(n2);
		If (n1 = "0") OR (n2 = "0") Then Halt(0);
    End
End
        """
        expect = str(Program([VarDecl(Id(r'n1'),StringType()),VarDecl(Id(r'n2'),StringType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Writeln'),[StringLiteral(r'Enter two numbers: to exit)')]),While(UnaryOp(r'not',BinaryOp(r'OR',BinaryOp(r'=',Id(r'n1'),StringLiteral(r'0')),BinaryOp(r'=',Id(r'n2'),StringLiteral(r'0')))),[CallStmt(Id(r'Write'),[StringLiteral(r'No.1: ')]),CallStmt(Id(r'Readln'),[Id(r'n1')]),CallStmt(Id(r'Write'),[StringLiteral(r'No.2: ')]),CallStmt(Id(r'Readln'),[Id(r'n2')]),If(BinaryOp(r'OR',BinaryOp(r'=',Id(r'n1'),StringLiteral(r'0')),BinaryOp(r'=',Id(r'n2'),StringLiteral(r'0'))),[CallStmt(Id(r'Halt'),[IntLiteral(0)])],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,325))  

    def test_CallExpr326(self):
        input = """function foo(): integer;
                   BEGIN
                    foo();
                    bar(a);
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'foo'),[]),CallStmt(Id(r'bar'),[Id(r'a')])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_CallExpr327(self):
        input = """function foo(): integer;
                   BEGIN
                    foo(a+2);
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'foo'),[BinaryOp(r'+',Id(r'a'),IntLiteral(2))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_CallExpr328(self):
        input = """function foo(): integer;
                   BEGIN
                    foo(foo(2));
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'foo'),[CallExpr(Id(r'foo'),[IntLiteral(2)])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_fun329(self):
        input = """
        PROCEDURE test_err();
        begin
            foo := a[b[2]];
        end
        """
        expect = str(Program([FuncDecl(Id(r'test_err'),[],[],[Assign(Id(r'foo'),ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,329))

        
    def test_and_330(self):
        input = """
Var age : Integer;
procedure main();
Begin
	While (age > 0) AND (age <= 100) Do
    Begin
		Write("Enter age (1 - 100): ");
		Readln(age);
		If (age < 1) Then
			Writeln("Age cannot be less than 1...");
		Else If (age > 100) Then
			Writeln("Age cannot be greater than 100...");
    End
End
        """
        expect = str(Program([VarDecl(Id(r'age'),IntType()),FuncDecl(Id(r'main'),[],[],[While(BinaryOp(r'AND',BinaryOp(r'>',Id(r'age'),IntLiteral(0)),BinaryOp(r'<=',Id(r'age'),IntLiteral(100))),[CallStmt(Id(r'Write'),[StringLiteral(r'Enter age (1 - 100): ')]),CallStmt(Id(r'Readln'),[Id(r'age')]),If(BinaryOp(r'<',Id(r'age'),IntLiteral(1)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'Age cannot be less than 1...')])],[If(BinaryOp(r'>',Id(r'age'),IntLiteral(100)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'Age cannot be greater than 100...')])],[])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,330))
    
    def test_fun314(self):
        input = """function  foo () :  real ;
        begin
        if ( true )  then return 2;     
        else return 2;     
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[Return(IntLiteral(2))],[Return(IntLiteral(2))])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_string332(self):
        input = """
Var
    NewDir : String; 
    F : String;

Procedure Main();
Begin
    NewDir := FSearch("C:\\\\Pascal Programming", GetEnv("")); 
    If NewDir = "" Then
    CreateDir("C:\\\\Pascal Programming"); 
    Assign(F,"C:\\\\Pascal Programming\\\\pascal-programming.txt");
    ReWrite(F);
    Writeln(F,"http://pascal-programming.info/"); 
    Close(F); 
End
        """
        expect = str(Program([VarDecl(Id(r'NewDir'),StringType()),VarDecl(Id(r'F'),StringType()),FuncDecl(Id(r'Main'),[],[],[Assign(Id(r'NewDir'),CallExpr(Id(r'FSearch'),[StringLiteral(r'C:\\Pascal Programming'),CallExpr(Id(r'GetEnv'),[StringLiteral(r'')])])),If(BinaryOp(r'=',Id(r'NewDir'),StringLiteral(r'')),[CallStmt(Id(r'CreateDir'),[StringLiteral(r'C:\\Pascal Programming')])],[]),CallStmt(Id(r'Assign'),[Id(r'F'),StringLiteral(r'C:\\Pascal Programming\\pascal-programming.txt')]),CallStmt(Id(r'ReWrite'),[Id(r'F')]),CallStmt(Id(r'Writeln'),[Id(r'F'),StringLiteral(r'http://pascal-programming.info/')]),CallStmt(Id(r'Close'),[Id(r'F')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,332))
    
    def test_string333(self):
        input = """
Var
    f : String; { file var of type byte }
    sz : Integer;  { var for the size }

Procedure Main();
Begin
    Assign(f,"C:\\\\anyfile.txt");
    {$I-} Reset(f); {$I+}
    If (IOResult <> 0) Then
    Begin     { file found? }
        Writeln("File not found.. exiting");
        Readln();
    End Else
    Begin
            { Return the file size in Kilobytes }
        sz := Round(FileSize(f)/1024);
        Writeln("Size of the file in Kilobytes: ",sz," Kb");
        Readln();
        Close(f); 
    End
End
        """
        expect = str(Program([VarDecl(Id(r'f'),StringType()),VarDecl(Id(r'sz'),IntType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'Assign'),[Id(r'f'),StringLiteral(r'C:\\anyfile.txt')]),CallStmt(Id(r'Reset'),[Id(r'f')]),If(BinaryOp(r'<>',Id(r'IOResult'),IntLiteral(0)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'File not found.. exiting')]),CallStmt(Id(r'Readln'),[])],[Assign(Id(r'sz'),CallExpr(Id(r'Round'),[BinaryOp(r'/',CallExpr(Id(r'FileSize'),[Id(r'f')]),IntLiteral(1024))])),CallStmt(Id(r'Writeln'),[StringLiteral(r'Size of the file in Kilobytes: '),Id(r'sz'),StringLiteral(r' Kb')]),CallStmt(Id(r'Readln'),[]),CallStmt(Id(r'Close'),[Id(r'f')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_proc334(self):
        input = """
                procedure foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                    return;
                  END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,334))
    
    def test_proc335(self):
        input = """proCeduRe foo(c: real) ;
                  var x,y: real ;
                  BEGIN
                  END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_func336(self):
        input = """
                FUNcTION foo(a, b: integer ; c: real): real;
                  BEGIN
                    return a[1];
                  END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[],[Return(ArrayCell(Id(r'a'),IntLiteral(1)))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_bool_337(self):
        input = """
Var 
	bool : Boolean;
	A, B : Integer;
Procedure main();
Begin
	A := 10;
	B := 30;
	bool := False;
	bool := (A = 10) OR (B = 10);
	Writeln(bool); { outputs TRUE }
	bool := (A = 10) AND (B = 10);
	Writeln(bool); { outputs FALSE }
End
        """
        expect = str(Program([VarDecl(Id(r'bool'),BoolType()),VarDecl(Id(r'A'),IntType()),VarDecl(Id(r'B'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),IntLiteral(10)),Assign(Id(r'B'),IntLiteral(30)),Assign(Id(r'bool'),BooleanLiteral(False)),Assign(Id(r'bool'),BinaryOp(r'OR',BinaryOp(r'=',Id(r'A'),IntLiteral(10)),BinaryOp(r'=',Id(r'B'),IntLiteral(10)))),CallStmt(Id(r'Writeln'),[Id(r'bool')]),Assign(Id(r'bool'),BinaryOp(r'AND',BinaryOp(r'=',Id(r'A'),IntLiteral(10)),BinaryOp(r'=',Id(r'B'),IntLiteral(10)))),CallStmt(Id(r'Writeln'),[Id(r'bool')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,337))
        
    def test_string338(self):
        input = """
Var
    UFile : String; { or it could be of "file" type}

Procedure Main();
Begin
    Assign(UFile, "C:\\\\ADDTEXT.TXT");
    Erase(UFile); 
End
        """
        expect = str(Program([VarDecl(Id(r'UFile'),StringType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'Assign'),[Id(r'UFile'),StringLiteral(r'C:\\ADDTEXT.TXT')]),CallStmt(Id(r'Erase'),[Id(r'UFile')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_array339(self):
        input = """
Var
    i : Integer;
    myIntArray : Array[1 .. 20] of Integer;
    myBoolArray : Array[1 .. 20] of Boolean;

Procedure Main();
Begin
    For i := 1 to Length(myIntArray) do
    Begin
        myIntArray[i] := 1;
        myBoolArray[i] := True;
    End
End
        """
        expect = str(Program([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'myIntArray'),ArrayType(1,20,IntType())),VarDecl(Id(r'myBoolArray'),ArrayType(1,20,BoolType())),FuncDecl(Id(r'Main'),[],[],[For(Id(r'i'),IntLiteral(1),CallExpr(Id(r'Length'),[Id(r'myIntArray')]),True,[Assign(ArrayCell(Id(r'myIntArray'),Id(r'i')),IntLiteral(1)),Assign(ArrayCell(Id(r'myBoolArray'),Id(r'i')),BooleanLiteral(True))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_bool_340(self):
        input = """
Var quit : Boolean;
    a    : String;
Procedure main();
Begin
	While NOT (quit = True) Do
    Begin
		Writeln("Type \\\"\\\"exit\\\"\\\" to quit:");
		Readln(a);
		If a = "exit" Then 
			quit := True;
    End
End
        """
        expect = str(Program([VarDecl(Id(r'quit'),BoolType()),VarDecl(Id(r'a'),StringType()),FuncDecl(Id(r'main'),[],[],[While(UnaryOp(r'NOT',BinaryOp(r'=',Id(r'quit'),BooleanLiteral(True))),[CallStmt(Id(r'Writeln'),[StringLiteral(r'Type \"\"exit\"\" to quit:')]),CallStmt(Id(r'Readln'),[Id(r'a')]),If(BinaryOp(r'=',Id(r'a'),StringLiteral(r'exit')),[Assign(Id(r'quit'),BooleanLiteral(True))],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,340))
        
    def test_for_341(self):
        input = """
Procedure DrawLine(); 
{This procedure helps me to avoid the rewriting the for loops}
Var Counter : Integer;
Begin
	textcolor(green);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196)); 
	End
End

Procedure Main();
Begin
	GotoXy(10,5);
	DrawLine();
	GotoXy(10,6);
	DrawLine();
	GotoXy(10,7);
	DrawLine();
	GotoXy(10,10);
	DrawLine();
	Readkey();
End
        """
        expect = str(Program([FuncDecl(Id(r'DrawLine'),[],[VarDecl(Id(r'Counter'),IntType())],[CallStmt(Id(r'textcolor'),[Id(r'green')]),For(Id(r'Counter'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'chr'),[IntLiteral(196)])])])],VoidType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'GotoXy'),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id(r'DrawLine'),[]),CallStmt(Id(r'GotoXy'),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id(r'DrawLine'),[]),CallStmt(Id(r'GotoXy'),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id(r'DrawLine'),[]),CallStmt(Id(r'GotoXy'),[IntLiteral(10),IntLiteral(10)]),CallStmt(Id(r'DrawLine'),[]),CallStmt(Id(r'Readkey'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,341))
    
    def test_string342(self):
        input = """
Var 
    S : String;

Procedure main();
Begin
    S := "Hey there! How are you?";
    S := Copy(S, 5, 6); { "there!" }
    Write(S);
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S'),StringLiteral(r'Hey there! How are you?')),Assign(Id(r'S'),CallExpr(Id(r'Copy'),[Id(r'S'),IntLiteral(5),IntLiteral(6)])),CallStmt(Id(r'Write'),[Id(r'S')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_string343(self):
        input = """
Var 
    S : String;

Procedure main();
Begin
    S := "Hey! It's Me, your best friend?";
    Write(S);

End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S'),StringLiteral(r'Hey! It\'s Me, your best friend?')),CallStmt(Id(r'Write'),[Id(r'S')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_for_344(self):
        input = """
Procedure DrawLine(X : Integer; Y : Integer);
{ the declaration of the variables in brackets are called parameters }
Var Counter : Integer; { this is called a local variable }
Begin
	GotoXy(X,Y); {here I use the arguments of X and Y}
	textcolor(green);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196));
	End
End

Procedure main();
Begin
	DrawLine(10,5);
	DrawLine(10,6);
	DrawLine(10,7);
	DrawLine(10,10);
	Readkey();
End
        """
        expect = str(Program([FuncDecl(Id(r'DrawLine'),[VarDecl(Id(r'X'),IntType()),VarDecl(Id(r'Y'),IntType())],[VarDecl(Id(r'Counter'),IntType())],[CallStmt(Id(r'GotoXy'),[Id(r'X'),Id(r'Y')]),CallStmt(Id(r'textcolor'),[Id(r'green')]),For(Id(r'Counter'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'chr'),[IntLiteral(196)])])])],VoidType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'DrawLine'),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id(r'DrawLine'),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id(r'DrawLine'),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id(r'DrawLine'),[IntLiteral(10),IntLiteral(10)]),CallStmt(Id(r'Readkey'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,344))
    
    def test_simple_program345(self):
        input = """
        procedurE foo () ;
            begin
            End          
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_procedure_346(self):
        input = """
Procedure Square(Index : Integer; Result : Integer);
Begin
	Result := Index * Index;
End

Var
	Res : Integer;

Procedure Main();
Begin
	Writeln("The square of 5 is: ");
	Square(5, Res);
	Writeln(Res);
End
        """
        expect = str(Program([FuncDecl(Id(r'Square'),[VarDecl(Id(r'Index'),IntType()),VarDecl(Id(r'Result'),IntType())],[],[Assign(Id(r'Result'),BinaryOp(r'*',Id(r'Index'),Id(r'Index')))],VoidType()),VarDecl(Id(r'Res'),IntType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'Writeln'),[StringLiteral(r'The square of 5 is: ')]),CallStmt(Id(r'Square'),[IntLiteral(5),Id(r'Res')]),CallStmt(Id(r'Writeln'),[Id(r'Res')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,346))
        
    def test_while347(self):
        input = """
        function foo(): real;
        var a,b: integer;
        begin
        while (a>b) do  
        a := a/b;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[While(BinaryOp(r'>',Id(r'a'),Id(r'b')),[Assign(Id(r'a'),BinaryOp(r'/',Id(r'a'),Id(r'b')))])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,347))
    
    def test_for348(self):
        input = """
        procedure main();
        var a : integer;
        begin
        for x:= 1 to 10 do 
        a := a*a + x;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),IntType())],[For(Id(r'x'),IntLiteral(1),IntLiteral(10),True,[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'*',Id(r'a'),Id(r'a')),Id(r'x')))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,348))
    
    def test_simple269(self):
        input = """
Var 
    S     : String;
    error : Integer;
    R     : Real;

Procedure main();
Begin
    S := "-0.563"; 
    Val(S, R, error);
    If error > 0 Then
    Write("Error in conversion.");
    Else
        Write(R); 
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),VarDecl(Id(r'error'),IntType()),VarDecl(Id(r'R'),FloatType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S'),StringLiteral(r'-0.563')),CallStmt(Id(r'Val'),[Id(r'S'),Id(r'R'),Id(r'error')]),If(BinaryOp(r'>',Id(r'error'),IntLiteral(0)),[CallStmt(Id(r'Write'),[StringLiteral(r'Error in conversion.')])],[CallStmt(Id(r'Write'),[Id(r'R')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,349))
    
    def test_string_350(self):
        input = """
Var
	UserFile : String;
	FileName, TFile : String;

Procedure Main();
Begin
	Writeln("Enter the file name (including its full path) of the text file (without the extension):");
	Readln(FileName); { A .txt file will be assigned to a text variable }
	Assign(UserFile, FileName + ".txt");
	Reset(UserFile); { "Reset(x)" - means open the file x and reset cursor to the beginning of file }
	While NOT Eof(UserFile) Do
    Begin
		Readln(UserFile,TFile);
		Writeln(TFile);
	End
	Close(UserFile);
	Readln();
End
        """
        expect = str(Program([VarDecl(Id(r'UserFile'),StringType()),VarDecl(Id(r'FileName'),StringType()),VarDecl(Id(r'TFile'),StringType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'Writeln'),[StringLiteral(r'Enter the file name (including its full path) of the text file (without the extension):')]),CallStmt(Id(r'Readln'),[Id(r'FileName')]),CallStmt(Id(r'Assign'),[Id(r'UserFile'),BinaryOp(r'+',Id(r'FileName'),StringLiteral(r'.txt'))]),CallStmt(Id(r'Reset'),[Id(r'UserFile')]),While(UnaryOp(r'NOT',CallExpr(Id(r'Eof'),[Id(r'UserFile')])),[CallStmt(Id(r'Readln'),[Id(r'UserFile'),Id(r'TFile')]),CallStmt(Id(r'Writeln'),[Id(r'TFile')])]),CallStmt(Id(r'Close'),[Id(r'UserFile')]),CallStmt(Id(r'Readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,350))
        

    def test_string_351(self):
        input = """
Var
	FName, Txt : String;
	UserFile   : String; 

Procedure Main();
Begin
	FName := "Textfile";
	Assign(UserFile, "C:\\\\" + FName + ".txt"); {assign a text file}
	Rewrite(UserFile); {open the file "fname" for writing}
	Writeln(UserFile, "PASCAL PROGRAMMING");
	Writeln(UserFile, "if you did not understand something,");
	Writeln(UserFile, "please send me an email to:");
	Writeln(UserFile, "victorsaliba@hotmail.com");
	Writeln("Write some text to the file:");
	Readln(Txt);
	Writeln(UserFile, "");
	Writeln(UserFile, "The user entered this text:");
	Writeln(UserFile, Txt);
	Close(UserFile);
End
        """
        expect = str(Program([VarDecl(Id(r'FName'),StringType()),VarDecl(Id(r'Txt'),StringType()),VarDecl(Id(r'UserFile'),StringType()),FuncDecl(Id(r'Main'),[],[],[Assign(Id(r'FName'),StringLiteral(r'Textfile')),CallStmt(Id(r'Assign'),[Id(r'UserFile'),BinaryOp(r'+',BinaryOp(r'+',StringLiteral(r'C:\\'),Id(r'FName')),StringLiteral(r'.txt'))]),CallStmt(Id(r'Rewrite'),[Id(r'UserFile')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'PASCAL PROGRAMMING')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'if you did not understand something,')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'please send me an email to:')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'victorsaliba@hotmail.com')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'Write some text to the file:')]),CallStmt(Id(r'Readln'),[Id(r'Txt')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'The user entered this text:')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),Id(r'Txt')]),CallStmt(Id(r'Close'),[Id(r'UserFile')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,351))
    
    def test_string352(self):
        input = """
Var 
    S     : String;
   
Procedure main();
Begin
    S := "day la mot \\n string"; 
    Write(S); 
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S'),StringLiteral(r'day la mot \n string')),CallStmt(Id(r'Write'),[Id(r'S')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_bool353(self):
        input = """
Var 
    bool : Boolean;
    A, B : Integer;
Procedure main();
Begin
    A := 10;
    B := 20;
    bool := False;
    bool := (A = 10) OR (B = 10);
    Writeln(bool);
    bool := (A = 10) AND (B = 10);
    Writeln(bool); 
End
        """
        expect = str(Program([VarDecl(Id(r'bool'),BoolType()),VarDecl(Id(r'A'),IntType()),VarDecl(Id(r'B'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),IntLiteral(10)),Assign(Id(r'B'),IntLiteral(20)),Assign(Id(r'bool'),BooleanLiteral(False)),Assign(Id(r'bool'),BinaryOp(r'OR',BinaryOp(r'=',Id(r'A'),IntLiteral(10)),BinaryOp(r'=',Id(r'B'),IntLiteral(10)))),CallStmt(Id(r'Writeln'),[Id(r'bool')]),Assign(Id(r'bool'),BinaryOp(r'AND',BinaryOp(r'=',Id(r'A'),IntLiteral(10)),BinaryOp(r'=',Id(r'B'),IntLiteral(10)))),CallStmt(Id(r'Writeln'),[Id(r'bool')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,353))
    
    def test_simple354(self):
        input = """
Var
	UFile : String; { or it could be of "file" type}

Procedure Main();
Begin
	Assign(UFile, "C:\\\\abasdcasdcT.TXT");
	Erase(UFile); 
End
        """
        expect = str(Program([VarDecl(Id(r'UFile'),StringType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'Assign'),[Id(r'UFile'),StringLiteral(r'C:\\abasdcasdcT.TXT')]),CallStmt(Id(r'Erase'),[Id(r'UFile')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,354))
        
    def test_string_355(self):
        input = """
Var
	t : String;
	s : String;

Procedure main();
Begin
	Assign(t, "C:\\\\ABC.DEF");
	{$I-}   { disable i/o error checking }
	Reset(t);
	{$I+}   { enable again i/o error checking - important }
	If (IOResult <> 0) Then
	Begin
		Writeln("The file required to be opened is not found!");
		Readln();
	End Else 
	Begin
		Readln(t,s);
		Writeln("The first line of the file reads: ",s);
		Close(t);
	End
End
        """
        expect = str(Program([VarDecl(Id(r't'),StringType()),VarDecl(Id(r's'),StringType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Assign'),[Id(r't'),StringLiteral(r'C:\\ABC.DEF')]),CallStmt(Id(r'Reset'),[Id(r't')]),If(BinaryOp(r'<>',Id(r'IOResult'),IntLiteral(0)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'The file required to be opened is not found!')]),CallStmt(Id(r'Readln'),[])],[CallStmt(Id(r'Readln'),[Id(r't'),Id(r's')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'The first line of the file reads: '),Id(r's')]),CallStmt(Id(r'Close'),[Id(r't')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_func356(self):
        input = """function IsPrintable(aCharacter: string): Boolean;
        begin
        result := (aCharacter <> "7") and    //bell (beeps)
                    (aCharacter <> "8") and    //Backspace 
                    (aCharacter <> "10") and   //Carrage return
                    (aCharacter <> "13");      //Line feed
        end
                """
        expect = str(Program([FuncDecl(Id(r'IsPrintable'),[VarDecl(Id(r'aCharacter'),StringType())],[],[Assign(Id(r'result'),BinaryOp(r'and',BinaryOp(r'and',BinaryOp(r'and',BinaryOp(r'<>',Id(r'aCharacter'),StringLiteral(r'7')),BinaryOp(r'<>',Id(r'aCharacter'),StringLiteral(r'8'))),BinaryOp(r'<>',Id(r'aCharacter'),StringLiteral(r'10'))),BinaryOp(r'<>',Id(r'aCharacter'),StringLiteral(r'13'))))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,356))     

    def test_string357(self):
        input = """
Var
	f : String; { file var of type byte }
	sz : Integer;  { var for the size }

Procedure Main();
Begin
	Assign(f,"C:\\\\anyfile.txt");
	{$I-} Reset(f); {$I+}
	If (IOResult <> 0) Then
 	Begin     { file found? }
  		Writeln("File not found.. exiting");
  		Readln();
 	End Else
 	Begin
			{ Return the file size in Kilobytes }
  		sz := Round(FileSize(f)/1024);
  		Writeln("Size of the file in Kilobytes: ",sz," Kb");
  		Readln();
  		Close(f); 
 	End
End
        """
        expect = str(Program([VarDecl(Id(r'f'),StringType()),VarDecl(Id(r'sz'),IntType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'Assign'),[Id(r'f'),StringLiteral(r'C:\\anyfile.txt')]),CallStmt(Id(r'Reset'),[Id(r'f')]),If(BinaryOp(r'<>',Id(r'IOResult'),IntLiteral(0)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'File not found.. exiting')]),CallStmt(Id(r'Readln'),[])],[Assign(Id(r'sz'),CallExpr(Id(r'Round'),[BinaryOp(r'/',CallExpr(Id(r'FileSize'),[Id(r'f')]),IntLiteral(1024))])),CallStmt(Id(r'Writeln'),[StringLiteral(r'Size of the file in Kilobytes: '),Id(r'sz'),StringLiteral(r' Kb')]),CallStmt(Id(r'Readln'),[]),CallStmt(Id(r'Close'),[Id(r'f')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,357))
        

    def test_array358(self):
        input = """
Var
	myVar : Integer;
	myArray : Array[1 .. 5] of Integer;

Procedure Main();
Begin
	myArray[2] := 25;
	myVar := myArray[2];
End
        """
        expect = str(Program([VarDecl(Id(r'myVar'),IntType()),VarDecl(Id(r'myArray'),ArrayType(1,5,IntType())),FuncDecl(Id(r'Main'),[],[],[Assign(ArrayCell(Id(r'myArray'),IntLiteral(2)),IntLiteral(25)),Assign(Id(r'myVar'),ArrayCell(Id(r'myArray'),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,358))
    
    def test_or359(self):
        input = """
Var n1, n2 : string;
procedure main();
Begin
    Writeln("Enter two numbers to exit");
    While not ((n1 = "0") OR (n2 = "0")) do
    Begin
        write(n1);
        write(n2);
    End
End
        """
        expect = str(Program([VarDecl(Id(r'n1'),StringType()),VarDecl(Id(r'n2'),StringType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Writeln'),[StringLiteral(r'Enter two numbers to exit')]),While(UnaryOp(r'not',BinaryOp(r'OR',BinaryOp(r'=',Id(r'n1'),StringLiteral(r'0')),BinaryOp(r'=',Id(r'n2'),StringLiteral(r'0')))),[CallStmt(Id(r'write'),[Id(r'n1')]),CallStmt(Id(r'write'),[Id(r'n2')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_complex360(self):
        input = """procedure PrintArea();
                    var
                    radius, area : real;
                    begin
                    radius := GetRadius();
                    area := PI * radius * radius;
                    WriteLn("The area is ", area);
                    end
                """
        expect = str(Program([FuncDecl(Id(r'PrintArea'),[],[VarDecl(Id(r'radius'),FloatType()),VarDecl(Id(r'area'),FloatType())],[Assign(Id(r'radius'),CallExpr(Id(r'GetRadius'),[])),Assign(Id(r'area'),BinaryOp(r'*',BinaryOp(r'*',Id(r'PI'),Id(r'radius')),Id(r'radius'))),CallStmt(Id(r'WriteLn'),[StringLiteral(r'The area is '),Id(r'area')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,360))
    
    def test_complex361(self):
        input = """
                function fibo(x: integer): integer;
                begin
                    if x<=2 then return 1;
                    else return fibo(x-2)+ fibo(x-1);
                end
                """
        expect = str(Program([FuncDecl(Id(r'fibo'),[VarDecl(Id(r'x'),IntType())],[],[If(BinaryOp(r'<=',Id(r'x'),IntLiteral(2)),[Return(IntLiteral(1))],[Return(BinaryOp(r'+',CallExpr(Id(r'fibo'),[BinaryOp(r'-',Id(r'x'),IntLiteral(2))]),CallExpr(Id(r'fibo'),[BinaryOp(r'-',Id(r'x'),IntLiteral(1))])))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test_array_362(self):
        input = """
Var
	i : Integer;
	myIntArray : Array[1 .. 20] of Integer;
	myBoolArray : Array[1 .. 20] of Boolean;

Procedure Main();
Begin
	For i := 1 to Length(myIntArray) do
	Begin
		myIntArray[i] := 1;
		myBoolArray[i] := True;
	End
End
        """
        expect = str(Program([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'myIntArray'),ArrayType(1,20,IntType())),VarDecl(Id(r'myBoolArray'),ArrayType(1,20,BoolType())),FuncDecl(Id(r'Main'),[],[],[For(Id(r'i'),IntLiteral(1),CallExpr(Id(r'Length'),[Id(r'myIntArray')]),True,[Assign(ArrayCell(Id(r'myIntArray'),Id(r'i')),IntLiteral(1)),Assign(ArrayCell(Id(r'myBoolArray'),Id(r'i')),BooleanLiteral(True))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,362))
        
    def test_complex363(self):
        input = """
                procedure qsort_recur();
                BEGIN { QuicksortRecur }
                { If there's anything to do... }
                IF start < stop THEN 
                    BEGIN
                        splitpt := Split(start, stop);
                        QuicksortRecur(start, splitpt-1);
                        QuicksortRecur(splitpt+1, stop);
                    END
                END
                """
        expect = str(Program([FuncDecl(Id(r'qsort_recur'),[],[],[If(BinaryOp(r'<',Id(r'start'),Id(r'stop')),[Assign(Id(r'splitpt'),CallExpr(Id(r'Split'),[Id(r'start'),Id(r'stop')])),CallStmt(Id(r'QuicksortRecur'),[Id(r'start'),BinaryOp(r'-',Id(r'splitpt'),IntLiteral(1))]),CallStmt(Id(r'QuicksortRecur'),[BinaryOp(r'+',Id(r'splitpt'),IntLiteral(1)),Id(r'stop')])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test_string364(self):
        input = """
Var
    myString : String;

Procedure Main();
Begin
	myString := "Hey! How are you?";
	Writeln("The length of the string is ", byte(myString[0]));
	Write(myString[byte(myString[0])]);
	Write(" is the last character.");
End
        """
        expect = str(Program([VarDecl(Id(r'myString'),StringType()),FuncDecl(Id(r'Main'),[],[],[Assign(Id(r'myString'),StringLiteral(r'Hey! How are you?')),CallStmt(Id(r'Writeln'),[StringLiteral(r'The length of the string is '),CallExpr(Id(r'byte'),[ArrayCell(Id(r'myString'),IntLiteral(0))])]),CallStmt(Id(r'Write'),[ArrayCell(Id(r'myString'),CallExpr(Id(r'byte'),[ArrayCell(Id(r'myString'),IntLiteral(0))]))]),CallStmt(Id(r'Write'),[StringLiteral(r' is the last character.')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_string365(self):
        input = """
Var
	S : String;

Procedure main();
Begin
	S := "Hey there! How are you?";
	Write("The word \\"How\\" is found at char index ");
	Writeln(Pos("How", S));
	If Pos("Why", S) <= 0 Then
		Writeln("\\"Why\\" is not found.");
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S'),StringLiteral(r'Hey there! How are you?')),CallStmt(Id(r'Write'),[StringLiteral(r'The word \"How\" is found at char index ')]),CallStmt(Id(r'Writeln'),[CallExpr(Id(r'Pos'),[StringLiteral(r'How'),Id(r'S')])]),If(BinaryOp(r'<=',CallExpr(Id(r'Pos'),[StringLiteral(r'Why'),Id(r'S')]),IntLiteral(0)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'\"Why\" is not found.')])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,365))
        
    def test_assign366(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	S := "Hey there! How are you?";
	S := Copy(S, 5, 6); { "there!" }
	Write(S);
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S'),StringLiteral(r'Hey there! How are you?')),Assign(Id(r'S'),CallExpr(Id(r'Copy'),[Id(r'S'),IntLiteral(5),IntLiteral(6)])),CallStmt(Id(r'Write'),[Id(r'S')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,366))
       
    def test_complex367(self):
        input = """
Var 
   S : String;
   i : Integer;

Procedure main();
Begin
	S := "Hey! How are you?";
	For i := 1 to length(S) do
		S[i] := UpCase(S[i]);
	Write(S); { "HEY! HOW ARE YOU?" }
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),VarDecl(Id(r'i'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S'),StringLiteral(r'Hey! How are you?')),For(Id(r'i'),IntLiteral(1),CallExpr(Id(r'length'),[Id(r'S')]),True,[Assign(ArrayCell(Id(r'S'),Id(r'i')),CallExpr(Id(r'UpCase'),[ArrayCell(Id(r'S'),Id(r'i'))]))]),CallStmt(Id(r'Write'),[Id(r'S')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,367))
        
    def test_complex368(self):
        input = """
Procedure BubbleSort(numbers : Array[1 .. 100] of Integer; size : Integer);
Var
	i, j, temp : Integer;

Begin
	For i := size-1 DownTo 1 do
		For j := 2 to i do
			If (numbers[j-1] > numbers[j]) Then
			Begin
				temp := numbers[j-1];
				numbers[j-1] := numbers[j];
				numbers[j] := temp;
			End

End
        """
        expect = str(Program([FuncDecl(Id(r'BubbleSort'),[VarDecl(Id(r'numbers'),ArrayType(1,100,IntType())),VarDecl(Id(r'size'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'temp'),IntType())],[For(Id(r'i'),BinaryOp(r'-',Id(r'size'),IntLiteral(1)),IntLiteral(1),False,[For(Id(r'j'),IntLiteral(2),Id(r'i'),True,[If(BinaryOp(r'>',ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1))),ArrayCell(Id(r'numbers'),Id(r'j'))),[Assign(Id(r'temp'),ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1)))),Assign(ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1))),ArrayCell(Id(r'numbers'),Id(r'j'))),Assign(ArrayCell(Id(r'numbers'),Id(r'j')),Id(r'temp'))],[])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,368))
        

    def test_complex369(self):
        input = """
Procedure InsertionSort(numbers : Array[1 .. 100] of Integer; size : Integer);
Var
	i, j, index : Integer;


Begin
	For i := 2 to size-1 do
	Begin
		index := numbers[i];
		j := i;
		While ((j > 1) AND (numbers[j-1] > index)) do
		Begin
			numbers[j] := numbers[j-1];
			j := j - 1;
		End
		numbers[j] := index;
	End
End
        """
        expect = str(Program([FuncDecl(Id(r'InsertionSort'),[VarDecl(Id(r'numbers'),ArrayType(1,100,IntType())),VarDecl(Id(r'size'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'index'),IntType())],[For(Id(r'i'),IntLiteral(2),BinaryOp(r'-',Id(r'size'),IntLiteral(1)),True,[Assign(Id(r'index'),ArrayCell(Id(r'numbers'),Id(r'i'))),Assign(Id(r'j'),Id(r'i')),While(BinaryOp(r'AND',BinaryOp(r'>',Id(r'j'),IntLiteral(1)),BinaryOp(r'>',ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1))),Id(r'index'))),[Assign(ArrayCell(Id(r'numbers'),Id(r'j')),ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1)))),Assign(Id(r'j'),BinaryOp(r'-',Id(r'j'),IntLiteral(1)))]),Assign(ArrayCell(Id(r'numbers'),Id(r'j')),Id(r'index'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,369))
        

    def test_complex370(self):
        input = """
Procedure QSort(numbers : Array [1 .. 100] of Integer; left : Integer; right : Integer);
Var 
	pivot, l_ptr, r_ptr : Integer;

Begin
	l_ptr := left;
	r_ptr := right;
	pivot := numbers[left];

	While (left < right) do
	Begin
		While ((numbers[right] >= pivot) AND (left < right)) do
			right := right - 1;

		If (left <> right) Then
		Begin
			numbers[left] := numbers[right];
			left := left + 1;
		End

		While ((numbers[left] <= pivot) AND (left < right)) do
			left := left + 1;

		If (left <> right) Then
		Begin
			numbers[right] := numbers[left];
			right := right - 1;
		End
	End

	numbers[left] := pivot;
	pivot := left;
	left := l_ptr;
	right := r_ptr;

	If (left < pivot) Then
		QSort(numbers, left, pivot-1);

	If (right > pivot) Then
		QSort(numbers, pivot+1, right);
End

Procedure QuickSort(numbers : Array [1 .. 100] of Integer; size : Integer);
Begin
	QSort(numbers, 0, size-1);
End
        """
        expect = str(Program([FuncDecl(Id(r'QSort'),[VarDecl(Id(r'numbers'),ArrayType(1,100,IntType())),VarDecl(Id(r'left'),IntType()),VarDecl(Id(r'right'),IntType())],[VarDecl(Id(r'pivot'),IntType()),VarDecl(Id(r'l_ptr'),IntType()),VarDecl(Id(r'r_ptr'),IntType())],[Assign(Id(r'l_ptr'),Id(r'left')),Assign(Id(r'r_ptr'),Id(r'right')),Assign(Id(r'pivot'),ArrayCell(Id(r'numbers'),Id(r'left'))),While(BinaryOp(r'<',Id(r'left'),Id(r'right')),[While(BinaryOp(r'AND',BinaryOp(r'>=',ArrayCell(Id(r'numbers'),Id(r'right')),Id(r'pivot')),BinaryOp(r'<',Id(r'left'),Id(r'right'))),[Assign(Id(r'right'),BinaryOp(r'-',Id(r'right'),IntLiteral(1)))]),If(BinaryOp(r'<>',Id(r'left'),Id(r'right')),[Assign(ArrayCell(Id(r'numbers'),Id(r'left')),ArrayCell(Id(r'numbers'),Id(r'right'))),Assign(Id(r'left'),BinaryOp(r'+',Id(r'left'),IntLiteral(1)))],[]),While(BinaryOp(r'AND',BinaryOp(r'<=',ArrayCell(Id(r'numbers'),Id(r'left')),Id(r'pivot')),BinaryOp(r'<',Id(r'left'),Id(r'right'))),[Assign(Id(r'left'),BinaryOp(r'+',Id(r'left'),IntLiteral(1)))]),If(BinaryOp(r'<>',Id(r'left'),Id(r'right')),[Assign(ArrayCell(Id(r'numbers'),Id(r'right')),ArrayCell(Id(r'numbers'),Id(r'left'))),Assign(Id(r'right'),BinaryOp(r'-',Id(r'right'),IntLiteral(1)))],[])]),Assign(ArrayCell(Id(r'numbers'),Id(r'left')),Id(r'pivot')),Assign(Id(r'pivot'),Id(r'left')),Assign(Id(r'left'),Id(r'l_ptr')),Assign(Id(r'right'),Id(r'r_ptr')),If(BinaryOp(r'<',Id(r'left'),Id(r'pivot')),[CallStmt(Id(r'QSort'),[Id(r'numbers'),Id(r'left'),BinaryOp(r'-',Id(r'pivot'),IntLiteral(1))])],[]),If(BinaryOp(r'>',Id(r'right'),Id(r'pivot')),[CallStmt(Id(r'QSort'),[Id(r'numbers'),BinaryOp(r'+',Id(r'pivot'),IntLiteral(1)),Id(r'right')])],[])],VoidType()),FuncDecl(Id(r'QuickSort'),[VarDecl(Id(r'numbers'),ArrayType(1,100,IntType())),VarDecl(Id(r'size'),IntType())],[],[CallStmt(Id(r'QSort'),[Id(r'numbers'),IntLiteral(0),BinaryOp(r'-',Id(r'size'),IntLiteral(1))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,370))
    
    def test_complex371(self):
        input = """
                Procedure DrawLine(X : Integer; Y : Integer);
{ the declaration of the variables in brackets are called parameters }
Var Counter : Integer; { this is called a local variable }
Begin
    GotoXy(X,Y); {here I use the arguments of X and Y}
    textcolor(green);
    For Counter := 1 to 10 do
    Begin 
        Write(chr(196));
    End
End

            """
        expect = str(Program([FuncDecl(Id(r'DrawLine'),[VarDecl(Id(r'X'),IntType()),VarDecl(Id(r'Y'),IntType())],[VarDecl(Id(r'Counter'),IntType())],[CallStmt(Id(r'GotoXy'),[Id(r'X'),Id(r'Y')]),CallStmt(Id(r'textcolor'),[Id(r'green')]),For(Id(r'Counter'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'chr'),[IntLiteral(196)])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,371))
    
    def test_complex372(self):
        input = """
                procedure Rectangle();
var 
   i, j: integer;
begin
   for i:= 1 to length do
   begin
     for j:= 1 to width do
        write(" * ");
        writeln();
   end
end

            """
        expect = str(Program([FuncDecl(Id(r'Rectangle'),[],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType())],[For(Id(r'i'),IntLiteral(1),Id(r'length'),True,[For(Id(r'j'),IntLiteral(1),Id(r'width'),True,[CallStmt(Id(r'write'),[StringLiteral(r' * ')])]),CallStmt(Id(r'writeln'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,372))
    
    def test_complex373(self):
        input = """
                procedure calculator();
var
a,b,c : integer;
d: real;

begin
   a:=21;
   b:=10;
   c := a + b;
   c := a - b;

   c := a * b;
   
   d := a / b;
   
   c := a mod b;
   
   c := a div b;
   
      writeln("Line 6 - Value of c is ", c );
end

            """
        expect = str(Program([FuncDecl(Id(r'calculator'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),FloatType())],[Assign(Id(r'a'),IntLiteral(21)),Assign(Id(r'b'),IntLiteral(10)),Assign(Id(r'c'),BinaryOp(r'+',Id(r'a'),Id(r'b'))),Assign(Id(r'c'),BinaryOp(r'-',Id(r'a'),Id(r'b'))),Assign(Id(r'c'),BinaryOp(r'*',Id(r'a'),Id(r'b'))),Assign(Id(r'd'),BinaryOp(r'/',Id(r'a'),Id(r'b'))),Assign(Id(r'c'),BinaryOp(r'mod',Id(r'a'),Id(r'b'))),Assign(Id(r'c'),BinaryOp(r'div',Id(r'a'),Id(r'b'))),CallStmt(Id(r'writeln'),[StringLiteral(r'Line 6 - Value of c is '),Id(r'c')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,373))
    
    def test_complex374(self):
        input = """procedure ifelseChecking();
var
   { local variable definition }
   a : integer;

begin
   a := 100;
   (* check the boolean condition *)
   if( a < 20 ) then
      (* if condition is true then print the following *)
      writeln("a is less than 20" );
   
   else
      (* if condition is false then print the following *) 
      writeln("a is not less than 20");
      writeln("value of a is : ", a);
end
            """
        expect = str(Program([FuncDecl(Id(r'ifelseChecking'),[],[VarDecl(Id(r'a'),IntType())],[Assign(Id(r'a'),IntLiteral(100)),If(BinaryOp(r'<',Id(r'a'),IntLiteral(20)),[CallStmt(Id(r'writeln'),[StringLiteral(r'a is less than 20')])],[CallStmt(Id(r'writeln'),[StringLiteral(r'a is not less than 20')])]),CallStmt(Id(r'writeln'),[StringLiteral(r'value of a is : '),Id(r'a')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,374))
    
    def test_complex375(self):
        input = """
Var
	myStack : Array[1 .. 100] of Integer;
	topPointer : Integer;


Procedure InitStack();
Begin
	topPointer := 0;
End
//We now implemement the IsEmpty() and IsFull() functions.

Function IsEmpty() : Boolean;
Begin
	IsEmpty := False;
	If (topPointer = 0) Then
		IsEmpty := true;
End

Function IsFull() : Boolean;
Begin
	IsFull := False;
	If ((topPointer + 1) = STACK_SIZE) Then
		IsFull := True;
End
//Here are the implementations of the Pop() and Push() functions and making use of the functions that we have just implemented.

Function Pop() : Integer;

Begin
	Pop := nil;

	If not IsEmpty Then
	Begin
		Pop := myStack[topPointer];
		topPointer := topPointer - 1; 
	End
End

Procedure Push(item : Integer);
Begin
	If not IsFull Then
	Begin
		myStack[topPointer+1] := item;
		topPointer := topPointer + 1;
	End
End

//Finally, we implement the utility function GetSize(). Although one can access the current size of the stack using the global variable topPointer, it is of good practice to make use of functions instead of global variables.

Function GetSize() : Integer;
Begin
	GetSize := topPointer;
End
        """
        expect = str(Program([VarDecl(Id(r'myStack'),ArrayType(1,100,IntType())),VarDecl(Id(r'topPointer'),IntType()),FuncDecl(Id(r'InitStack'),[],[],[Assign(Id(r'topPointer'),IntLiteral(0))],VoidType()),FuncDecl(Id(r'IsEmpty'),[],[],[Assign(Id(r'IsEmpty'),BooleanLiteral(False)),If(BinaryOp(r'=',Id(r'topPointer'),IntLiteral(0)),[Assign(Id(r'IsEmpty'),BooleanLiteral(True))],[])],BoolType()),FuncDecl(Id(r'IsFull'),[],[],[Assign(Id(r'IsFull'),BooleanLiteral(False)),If(BinaryOp(r'=',BinaryOp(r'+',Id(r'topPointer'),IntLiteral(1)),Id(r'STACK_SIZE')),[Assign(Id(r'IsFull'),BooleanLiteral(True))],[])],BoolType()),FuncDecl(Id(r'Pop'),[],[],[Assign(Id(r'Pop'),Id(r'nil')),If(UnaryOp(r'not',Id(r'IsEmpty')),[Assign(Id(r'Pop'),ArrayCell(Id(r'myStack'),Id(r'topPointer'))),Assign(Id(r'topPointer'),BinaryOp(r'-',Id(r'topPointer'),IntLiteral(1)))],[])],IntType()),FuncDecl(Id(r'Push'),[VarDecl(Id(r'item'),IntType())],[],[If(UnaryOp(r'not',Id(r'IsFull')),[Assign(ArrayCell(Id(r'myStack'),BinaryOp(r'+',Id(r'topPointer'),IntLiteral(1))),Id(r'item')),Assign(Id(r'topPointer'),BinaryOp(r'+',Id(r'topPointer'),IntLiteral(1)))],[])],VoidType()),FuncDecl(Id(r'GetSize'),[],[],[Assign(Id(r'GetSize'),Id(r'topPointer'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,375))
        
    def test_complex_376(self):
        input = """
Var 
	Counter : Integer;  { will be used as a loop counter }

Procedure main();
Begin

	For Counter := 1 to 5 do 
	Begin      
		gotoxy(25, 5 + Counter);
		Writeln("I");
	End

	For Counter := 5 Downto 1 do
	Begin  {an example of "downto" instead of "to", note the "gotoxy(_,_)"}
		gotoxy(32, 11 - Counter);
		Writeln("I");
	End

	For Counter := 1 to 6 do
	Begin
		gotoxy(25 + Counter, 11);
		Writeln("-");
	End

	For Counter := 6 Downto 1 do
	Begin
		gotoxy(32 - Counter, 5);
		Writeln("-");
	End

	{--------------The Corners(+)---------------}
	Gotoxy(25,5);
	Writeln("+");
	GotoXy(25,11);
	Writeln("+");
	GotoXy(32,5);
	Writeln("+");
	GotoXy(32,11);
	Writeln("+");
	GotoXy(45,7); 
	Write("Made with For Loops :)");
	Readln();
End
        """
        expect = str(Program([VarDecl(Id(r'Counter'),IntType()),FuncDecl(Id(r'main'),[],[],[For(Id(r'Counter'),IntLiteral(1),IntLiteral(5),True,[CallStmt(Id(r'gotoxy'),[IntLiteral(25),BinaryOp(r'+',IntLiteral(5),Id(r'Counter'))]),CallStmt(Id(r'Writeln'),[StringLiteral(r'I')])]),For(Id(r'Counter'),IntLiteral(5),IntLiteral(1),False,[CallStmt(Id(r'gotoxy'),[IntLiteral(32),BinaryOp(r'-',IntLiteral(11),Id(r'Counter'))]),CallStmt(Id(r'Writeln'),[StringLiteral(r'I')])]),For(Id(r'Counter'),IntLiteral(1),IntLiteral(6),True,[CallStmt(Id(r'gotoxy'),[BinaryOp(r'+',IntLiteral(25),Id(r'Counter')),IntLiteral(11)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'-')])]),For(Id(r'Counter'),IntLiteral(6),IntLiteral(1),False,[CallStmt(Id(r'gotoxy'),[BinaryOp(r'-',IntLiteral(32),Id(r'Counter')),IntLiteral(5)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'-')])]),CallStmt(Id(r'Gotoxy'),[IntLiteral(25),IntLiteral(5)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'+')]),CallStmt(Id(r'GotoXy'),[IntLiteral(25),IntLiteral(11)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'+')]),CallStmt(Id(r'GotoXy'),[IntLiteral(32),IntLiteral(5)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'+')]),CallStmt(Id(r'GotoXy'),[IntLiteral(32),IntLiteral(11)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'+')]),CallStmt(Id(r'GotoXy'),[IntLiteral(45),IntLiteral(7)]),CallStmt(Id(r'Write'),[StringLiteral(r'Made with For Loops :)')]),CallStmt(Id(r'Readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_complex377(self):
        input = """
        var d: integer;
        f: string;
        procedure Hn(n,a,b: integer);
            begin
            if n = 0 then exit();
            Hn(n-1,a,6-a-b);
            inc(d);
            writeln(f,d,". ",a," -> ",b);
            Hn(n-1,6-a-b,b);
            end
        procedure runHn(n: integer);
            begin
            d :=  0;
            assign(f,"hanoi.out");
            rewrite(f);
            writeln("-----------------");
            Hn(n,1,2);
            writeln(f,"Total: ",d," step(s)");
            close(f);
            readln();
            end
        procedure main();
        BEGIN
        runHn(3);
        END
        """
        expect = str(Program([VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'f'),StringType()),FuncDecl(Id(r'Hn'),[VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(0)),[CallStmt(Id(r'exit'),[])],[]),CallStmt(Id(r'Hn'),[BinaryOp(r'-',Id(r'n'),IntLiteral(1)),Id(r'a'),BinaryOp(r'-',BinaryOp(r'-',IntLiteral(6),Id(r'a')),Id(r'b'))]),CallStmt(Id(r'inc'),[Id(r'd')]),CallStmt(Id(r'writeln'),[Id(r'f'),Id(r'd'),StringLiteral(r'. '),Id(r'a'),StringLiteral(r' -> '),Id(r'b')]),CallStmt(Id(r'Hn'),[BinaryOp(r'-',Id(r'n'),IntLiteral(1)),BinaryOp(r'-',BinaryOp(r'-',IntLiteral(6),Id(r'a')),Id(r'b')),Id(r'b')])],VoidType()),FuncDecl(Id(r'runHn'),[VarDecl(Id(r'n'),IntType())],[],[Assign(Id(r'd'),IntLiteral(0)),CallStmt(Id(r'assign'),[Id(r'f'),StringLiteral(r'hanoi.out')]),CallStmt(Id(r'rewrite'),[Id(r'f')]),CallStmt(Id(r'writeln'),[StringLiteral(r'-----------------')]),CallStmt(Id(r'Hn'),[Id(r'n'),IntLiteral(1),IntLiteral(2)]),CallStmt(Id(r'writeln'),[Id(r'f'),StringLiteral(r'Total: '),Id(r'd'),StringLiteral(r' step(s)')]),CallStmt(Id(r'close'),[Id(r'f')]),CallStmt(Id(r'readln'),[])],VoidType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'runHn'),[IntLiteral(3)])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,377))    

    def test_complex378(self):
        input = """
PROCEDURE main(); 
  BEGIN (* To De-Militarize Time *)
  Read(MilTime);
  Hours := MilTime  DIV 100;
  Minutes :=  MilTime MOD 100;
  Write(Hours,  Minutes);
  END (* of  De-Militarizing Time *)
        """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Read'),[Id(r'MilTime')]),Assign(Id(r'Hours'),BinaryOp(r'DIV',Id(r'MilTime'),IntLiteral(100))),Assign(Id(r'Minutes'),BinaryOp(r'MOD',Id(r'MilTime'),IntLiteral(100))),CallStmt(Id(r'Write'),[Id(r'Hours'),Id(r'Minutes')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_complex379(self):
        input = """
Var Ch : String;

Procedure main();
Begin
	Writeln("Press \\"\\"q\\"\\" to exit...");
	Ch := Readkey();
	While Ch <> "q" do 
	Begin
		Writeln("Please press \\"\\"q\\"\\" to exit.");
		Ch := Readkey();
	End
End
        """
        expect = str(Program([VarDecl(Id(r'Ch'),StringType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Writeln'),[StringLiteral(r'Press \"\"q\"\" to exit...')]),Assign(Id(r'Ch'),CallExpr(Id(r'Readkey'),[])),While(BinaryOp(r'<>',Id(r'Ch'),StringLiteral(r'q')),[CallStmt(Id(r'Writeln'),[StringLiteral(r'Please press \"\"q\"\" to exit.')]),Assign(Id(r'Ch'),CallExpr(Id(r'Readkey'),[]))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,379))
        

    def test_complex380(self):
        input = """
Function Factorial(n : Integer) : Integer;
Var
	Result : Integer;
	i : Integer;

Begin
	Result := n;
	If (n <= 1) Then
		Result := 1;
	Else
	For i := n-1 DownTo 1 do
		Result := Result * i; 
	Factorial := Result;
End
        """
        expect = str(Program([FuncDecl(Id(r'Factorial'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'Result'),IntType()),VarDecl(Id(r'i'),IntType())],[Assign(Id(r'Result'),Id(r'n')),If(BinaryOp(r'<=',Id(r'n'),IntLiteral(1)),[Assign(Id(r'Result'),IntLiteral(1))],[For(Id(r'i'),BinaryOp(r'-',Id(r'n'),IntLiteral(1)),IntLiteral(1),False,[Assign(Id(r'Result'),BinaryOp(r'*',Id(r'Result'),Id(r'i')))])]),Assign(Id(r'Factorial'),Id(r'Result'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,380))
        

    def test_complex381(self):
        input = """
Function Factorial(n : Integer) : Integer;
Var
	Result : Integer;

Begin
	If n = 1 Then 
		Factorial := 1;
	Else
		Factorial := n*Factorial(n-1);
End
        """
        expect = str(Program([FuncDecl(Id(r'Factorial'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'Result'),IntType())],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(1)),[Assign(Id(r'Factorial'),IntLiteral(1))],[Assign(Id(r'Factorial'),BinaryOp(r'*',Id(r'n'),CallExpr(Id(r'Factorial'),[BinaryOp(r'-',Id(r'n'),IntLiteral(1))])))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,381))
        

    def test_var382(self):
        input = """
var
age, weekdays : integer;
taxrate, net_income: real;
choice, isready: boolean;
name, surname : string;
        """
        expect = str(Program([VarDecl(Id(r'age'),IntType()),VarDecl(Id(r'weekdays'),IntType()),VarDecl(Id(r'taxrate'),FloatType()),VarDecl(Id(r'net_income'),FloatType()),VarDecl(Id(r'choice'),BoolType()),VarDecl(Id(r'isready'),BoolType()),VarDecl(Id(r'name'),StringType()),VarDecl(Id(r'surname'),StringType())]))
        self.assertTrue(TestAST.test(input,expect,382))
        

    def test_complex383(self):
        input = """
var
firstname, surname: string;

procedure main();
begin
   writeln("Please enter your first name: ");
   readln(firstname);
   
   writeln("Please enter your surname: ");
   readln(surname);
   
   writeln();
   writeln(message, " ", firstname, " ", surname);
end
        """
        expect = str(Program([VarDecl(Id(r'firstname'),StringType()),VarDecl(Id(r'surname'),StringType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'writeln'),[StringLiteral(r'Please enter your first name: ')]),CallStmt(Id(r'readln'),[Id(r'firstname')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Please enter your surname: ')]),CallStmt(Id(r'readln'),[Id(r'surname')]),CallStmt(Id(r'writeln'),[]),CallStmt(Id(r'writeln'),[Id(r'message'),StringLiteral(r' '),Id(r'firstname'),StringLiteral(r' '),Id(r'surname')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,383))
        
    def test_complex384(self):
        input = """
var
   i: integer;
function fibonacci(n: integer): integer;

begin
   if n=1 then
      fibonacci := 0;
   
   else if n=2 then
      fibonacci := 1;
   
   else
      fibonacci := fibonacci(n-1) + fibonacci(n-2);
end

procedure main();
begin
   for i:= 1 to 10 do
   
   write(fibonacci (i), "  ");
end
        """
        expect = str(Program([VarDecl(Id(r'i'),IntType()),FuncDecl(Id(r'fibonacci'),[VarDecl(Id(r'n'),IntType())],[],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(1)),[Assign(Id(r'fibonacci'),IntLiteral(0))],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(2)),[Assign(Id(r'fibonacci'),IntLiteral(1))],[Assign(Id(r'fibonacci'),BinaryOp(r'+',CallExpr(Id(r'fibonacci'),[BinaryOp(r'-',Id(r'n'),IntLiteral(1))]),CallExpr(Id(r'fibonacci'),[BinaryOp(r'-',Id(r'n'),IntLiteral(2))])))])])],IntType()),FuncDecl(Id(r'main'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'write'),[CallExpr(Id(r'fibonacci'),[Id(r'i')]),StringLiteral(r'  ')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,384))
    
    def test_complex385(self):
        input = """procedure nested_ifelseChecking();
var
   { local variable definition }
   a, b : integer;

begin
   a := 100;
   b:= 200;
   
   (* check the boolean condition *)
   if (a = 100) then
      (* if condition is true then check the following *)
      if ( b = 200 ) then
         (* if nested if condition is true  then print the following *)
         writeln("Value of a is 100 and value of b is 200" );
   
end
        """
        expect = str(Program([FuncDecl(Id(r'nested_ifelseChecking'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[Assign(Id(r'a'),IntLiteral(100)),Assign(Id(r'b'),IntLiteral(200)),If(BinaryOp(r'=',Id(r'a'),IntLiteral(100)),[If(BinaryOp(r'=',Id(r'b'),IntLiteral(200)),[CallStmt(Id(r'writeln'),[StringLiteral(r'Value of a is 100 and value of b is 200')])],[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,385))
    
    def test_complex386(self):
        input = """
var
   a, b, c,  min: integer;
procedure findMin(x, y, z: integer; m: integer); 
(* Finds the minimum of the 3 values *)

begin
   if x < y then
      m:= x;
   else
      m:= y;
   
   if z < m then
      m:= z;
end { end of procedure findMin }  

procedure main();
begin
   writeln(" Enter three numbers: ");
   readln( a, b, c);
   findMin(a, b, c, min); (* Procedure call *)
   
   writeln(" Minimum: ", min);
end
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'min'),IntType()),FuncDecl(Id(r'findMin'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType()),VarDecl(Id(r'm'),IntType())],[],[If(BinaryOp(r'<',Id(r'x'),Id(r'y')),[Assign(Id(r'm'),Id(r'x'))],[Assign(Id(r'm'),Id(r'y'))]),If(BinaryOp(r'<',Id(r'z'),Id(r'm')),[Assign(Id(r'm'),Id(r'z'))],[])],VoidType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'writeln'),[StringLiteral(r' Enter three numbers: ')]),CallStmt(Id(r'readln'),[Id(r'a'),Id(r'b'),Id(r'c')]),CallStmt(Id(r'findMin'),[Id(r'a'),Id(r'b'),Id(r'c'),Id(r'min')]),CallStmt(Id(r'writeln'),[StringLiteral(r' Minimum: '),Id(r'min')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,386)) 

    def test_if387(self):
        input = """
var
   { local variable definition }
   a : integer;

procedure main();
begin
   a := 100;
   (* check the boolean condition *)
   if( a < 20 ) then
      (* if condition is true then print the following *)
      writeln("a is less than 20" );
   
   else
      (* if condition is false then print the following *) 
      writeln("a is not less than 20" );
      writeln("value of a is : ", a);
end
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),IntLiteral(100)),If(BinaryOp(r'<',Id(r'a'),IntLiteral(20)),[CallStmt(Id(r'writeln'),[StringLiteral(r'a is less than 20')])],[CallStmt(Id(r'writeln'),[StringLiteral(r'a is not less than 20')])]),CallStmt(Id(r'writeln'),[StringLiteral(r'value of a is : '),Id(r'a')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,387))
        

    def test_if388(self):
        input = """
var
   { local variable definition }
   a : integer;

procedure main();
begin
   a := 100;
   (* check the boolean condition *)
   if (a = 10)  then
      (* if condition is true then print the following *)
      writeln("Value of a is 10" );
   
   else if ( a = 20 ) then
      (* if else if condition is true *)
      writeln("Value of a is 20" );
   
   else if( a = 30 ) then 
      (* if else if condition is true  *)
      writeln("Value of a is 30" );
   
   else
      (* if none of the conditions is true *)
      writeln("None of the values is matching" );
      writeln("Exact value of a is: ", a );
end
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),IntLiteral(100)),If(BinaryOp(r'=',Id(r'a'),IntLiteral(10)),[CallStmt(Id(r'writeln'),[StringLiteral(r'Value of a is 10')])],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(20)),[CallStmt(Id(r'writeln'),[StringLiteral(r'Value of a is 20')])],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(30)),[CallStmt(Id(r'writeln'),[StringLiteral(r'Value of a is 30')])],[CallStmt(Id(r'writeln'),[StringLiteral(r'None of the values is matching')])])])]),CallStmt(Id(r'writeln'),[StringLiteral(r'Exact value of a is: '),Id(r'a')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,388))
        

    def test_if389(self):
        input = """
var
   { local variable definition }
   a, b : integer;

procedure main();
begin
   a := 100;
   b:= 200;
   
   (* check the boolean condition *)
   if (a = 100) then
      (* if condition is true then check the following *)
      if ( b = 200 ) then
         (* if nested if condition is true  then print the following *)
         writeln("Value of a is 100 and value of b is 200" );
   
   writeln("Exact value of a is: ", a );
   writeln("Exact value of b is: ", b );
end
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),IntLiteral(100)),Assign(Id(r'b'),IntLiteral(200)),If(BinaryOp(r'=',Id(r'a'),IntLiteral(100)),[If(BinaryOp(r'=',Id(r'b'),IntLiteral(200)),[CallStmt(Id(r'writeln'),[StringLiteral(r'Value of a is 100 and value of b is 200')])],[])],[]),CallStmt(Id(r'writeln'),[StringLiteral(r'Exact value of a is: '),Id(r'a')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Exact value of b is: '),Id(r'b')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,389))
        
    def test_while390(self):
        input = """
var
   a: integer;

procedure main();
begin
   a := 10;
   while  a < 20  do
   
   begin
      writeln("value of a: ", a);
      a := a + 1;
   end
end
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),IntLiteral(10)),While(BinaryOp(r'<',Id(r'a'),IntLiteral(20)),[CallStmt(Id(r'writeln'),[StringLiteral(r'value of a: '),Id(r'a')]),Assign(Id(r'a'),BinaryOp(r'+',Id(r'a'),IntLiteral(1)))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,390))
        
    def test_break391(self):
        input = """
var
   a: integer;

procedure main();
begin
   a := 10;
   (* while loop execution *)
   while  a < 20 do
   
   begin
      writeln("value of a: ", a);
      a:=a +1;
      
      if( a > 15) then
         (* terminate the loop using break statement *)
      break;
   end
end
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),IntLiteral(10)),While(BinaryOp(r'<',Id(r'a'),IntLiteral(20)),[CallStmt(Id(r'writeln'),[StringLiteral(r'value of a: '),Id(r'a')]),Assign(Id(r'a'),BinaryOp(r'+',Id(r'a'),IntLiteral(1))),If(BinaryOp(r'>',Id(r'a'),IntLiteral(15)),[Break()],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,391))
        
    def test_continue392(self):
        input = """
var
   a: integer;

procedure main();
begin
   a := 10;
   
   while not ( a = 20 ) do
   begin
      if( a = 15) then
      
      begin
         (* skip the iteration *)
         a := a + 1;
         continue;
      end
      
      writeln("value of a: ", a);
      a := a+1;
   end
end
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),IntLiteral(10)),While(UnaryOp(r'not',BinaryOp(r'=',Id(r'a'),IntLiteral(20))),[If(BinaryOp(r'=',Id(r'a'),IntLiteral(15)),[Assign(Id(r'a'),BinaryOp(r'+',Id(r'a'),IntLiteral(1))),Continue()],[]),CallStmt(Id(r'writeln'),[StringLiteral(r'value of a: '),Id(r'a')]),Assign(Id(r'a'),BinaryOp(r'+',Id(r'a'),IntLiteral(1)))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,392))
        
    def test_function393(self):
        input = """
function max(num1, num2: integer): integer;

var
   (* local variable declaration *)
   result: integer;

begin
   if (num1 > num2) then
      result := num1;
   
   else
      result := num2;
   max := result;
end
        """
        expect = str(Program([FuncDecl(Id(r'max'),[VarDecl(Id(r'num1'),IntType()),VarDecl(Id(r'num2'),IntType())],[VarDecl(Id(r'result'),IntType())],[If(BinaryOp(r'>',Id(r'num1'),Id(r'num2')),[Assign(Id(r'result'),Id(r'num1'))],[Assign(Id(r'result'),Id(r'num2'))]),Assign(Id(r'max'),Id(r'result'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,393))
        
    def test_proc394(self):
        input = """proCeduRe foo(c: real) ;
                  var x,y: real ;
                  BEGIN
                  END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,394))
    
    def test_func395(self):
        input = """
                FUNcTION foo(a, b: integer ; c: real): real;
                  BEGIN
                    return a[1];
                  END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[],[Return(ArrayCell(Id(r'a'),IntLiteral(1)))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,395))
    
    def test_random396(self):
        input = """
        PROCEDURE test();
        var a: real;
        begin
            putln();
            writeln(abced+aced);
        end
        """
        expect = str(Program([FuncDecl(Id(r'test'),[],[VarDecl(Id(r'a'),FloatType())],[CallStmt(Id(r'putln'),[]),CallStmt(Id(r'writeln'),[BinaryOp(r'+',Id(r'abced'),Id(r'aced'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test_function397(self):
        input = """
var
   a, b, ret : integer;

(*function definition *)
function max(num1, num2: integer): integer;
var
   (* local variable declaration *)
   result: integer;

begin
   if (num1 > num2) then
      result := num1;
   
   else
      result := num2;
   max := result;
end

procedure main();
begin
   a := 100;
   b := 200;
   (* calling a function to get max value *)
   ret := max(a, b);
   
   writeln( "Max value is : ", ret );
end
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'ret'),IntType()),FuncDecl(Id(r'max'),[VarDecl(Id(r'num1'),IntType()),VarDecl(Id(r'num2'),IntType())],[VarDecl(Id(r'result'),IntType())],[If(BinaryOp(r'>',Id(r'num1'),Id(r'num2')),[Assign(Id(r'result'),Id(r'num1'))],[Assign(Id(r'result'),Id(r'num2'))]),Assign(Id(r'max'),Id(r'result'))],IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),IntLiteral(100)),Assign(Id(r'b'),IntLiteral(200)),Assign(Id(r'ret'),CallExpr(Id(r'max'),[Id(r'a'),Id(r'b')])),CallStmt(Id(r'writeln'),[StringLiteral(r'Max value is : '),Id(r'ret')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,397))
        

    def test_procedure398(self):
        input = """
procedure findMin(x, y, z: integer; m: integer); 
(* Finds the minimum of the 3 values *)

begin
   if x < y then
      m := x;
   else
      m := y;
   
   if z <m then
      m := z;
end { end of procedure findMin }  
        """
        expect = str(Program([FuncDecl(Id(r'findMin'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType()),VarDecl(Id(r'm'),IntType())],[],[If(BinaryOp(r'<',Id(r'x'),Id(r'y')),[Assign(Id(r'm'),Id(r'x'))],[Assign(Id(r'm'),Id(r'y'))]),If(BinaryOp(r'<',Id(r'z'),Id(r'm')),[Assign(Id(r'm'),Id(r'z'))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,398))
        

    def test_procedure399(self):
        input = """
var
   a, b, c,  min: integer;
procedure findMin(x, y, z: integer; m: integer); 
(* Finds the minimum of the 3 values *)

begin
   if x < y then
      m:= x;
   else
      m:= y;
   
   if z < m then
      m:= z;
end { end of procedure findMin }  

procedure main();
begin
   writeln(" Enter three numbers: ");
   readln( a, b, c);
   findMin(a, b, c, min); (* Procedure call *)
   
   writeln(" Minimum: ", min);
end
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'min'),IntType()),FuncDecl(Id(r'findMin'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType()),VarDecl(Id(r'm'),IntType())],[],[If(BinaryOp(r'<',Id(r'x'),Id(r'y')),[Assign(Id(r'm'),Id(r'x'))],[Assign(Id(r'm'),Id(r'y'))]),If(BinaryOp(r'<',Id(r'z'),Id(r'm')),[Assign(Id(r'm'),Id(r'z'))],[])],VoidType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'writeln'),[StringLiteral(r' Enter three numbers: ')]),CallStmt(Id(r'readln'),[Id(r'a'),Id(r'b'),Id(r'c')]),CallStmt(Id(r'findMin'),[Id(r'a'),Id(r'b'),Id(r'c'),Id(r'min')]),CallStmt(Id(r'writeln'),[StringLiteral(r' Minimum: '),Id(r'min')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,399))
        

   