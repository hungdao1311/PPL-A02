import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_proc300(self):
        input = """ procedure main();
        begin
        end"""
        expect ="successful"
        self.assertTrue(TestAST.test(input,expect,300))
        

    def test_var301(self):
        input = """var a,b : integer;"""
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,301))
        
    def test_built_in302(self):
        input = """procedure foo(a : integer);
            begin
            putIntLn(4);
            end
        """
        expect = "successful"
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
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,303))

    def test_assign304(self):
        input = """procedure foo(a : integer;b : real);
    begin
        d := a[b] := b + 5;
    return;
    end
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,304))

    def test_if305(self):
        input = """procedure main();
            begin
                 if a>b then a := b; else b:=a ;
            end
        """
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(name),StringType),VarDecl(Id(surname),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(write),[StringLiteral(Enter your name:)]),CallStmt(Id(readln),[Id(name)]),CallStmt(Id(write),[StringLiteral(Enter your surname:)]),CallStmt(Id(readln),[Id(surname)]),CallStmt(Id(writeln),[]),CallStmt(Id(writeln),[]),CallStmt(Id(writeln),[StringLiteral(Your full name is: ),Id(name),StringLiteral( ),Id(surname)]),CallStmt(Id(readln),[])])])"
        self.assertTrue(TestAST.test(input,expect,306))

    def test_index307(self):
        input = """function foo(a : integer;b : real): array [1 .. 5] of real;
             begin
                 foo(2)[3+x] := a[b[2]] + 3;
                 return a;
            end
        """
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(Sel),StringType),VarDecl(Id(N1),FloatType),VarDecl(Id(N2),FloatType),VarDecl(Id(Total),FloatType),VarDecl(Id(YN),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(Total),IntLiteral(0)),CallStmt(Id(GotoXy),[IntLiteral(4),IntLiteral(3)]),CallStmt(Id(Writeln),[StringLiteral(1.Addition)]),CallStmt(Id(GotoXy),[IntLiteral(4),IntLiteral(4)]),CallStmt(Id(Writeln),[StringLiteral(2.Subtraction)]),CallStmt(Id(GotoXy),[IntLiteral(4),IntLiteral(5)]),CallStmt(Id(Writeln),[StringLiteral(3.Exit)]),CallStmt(Id(GotoXy),[IntLiteral(6),IntLiteral(8)]),CallStmt(Id(Write),[StringLiteral(Select: )]),AssignStmt(Id(Sel),CallExpr(Id(Readkey),[])),If(BinaryOp(=,Id(Sel),StringLiteral(1)),[CallStmt(Id(ClrScr),[]),CallStmt(Id(Write),[StringLiteral(Input No.1:)]),CallStmt(Id(Readln),[Id(N1)]),CallStmt(Id(Write),[StringLiteral(Input No.2:)]),CallStmt(Id(Readln),[Id(N2)]),AssignStmt(Id(Total),BinaryOp(+,Id(N1),Id(N2))),CallStmt(Id(Writeln),[StringLiteral(Addition: ),Id(N1),StringLiteral( + ),Id(N2),StringLiteral( = ),Id(Total)]),CallStmt(Id(Write),[StringLiteral(Press any key to continue...)]),CallStmt(Id(Readkey),[])],[]),If(BinaryOp(=,Id(Sel),StringLiteral(2)),[CallStmt(Id(ClrScr),[]),CallStmt(Id(Write),[StringLiteral(Input No.1:)]),CallStmt(Id(Readln),[Id(N1)]),CallStmt(Id(Write),[StringLiteral(Input No.2:)]),CallStmt(Id(Readln),[Id(N2)]),AssignStmt(Id(Total),BinaryOp(-,Id(N1),Id(N2))),CallStmt(Id(Write),[StringLiteral(Subtraction: )]),CallStmt(Id(Write),[Id(N1),StringLiteral( - ),Id(N2),StringLiteral( = ),Id(Total)]),CallStmt(Id(Write),[StringLiteral(Press any key to continue...)]),CallStmt(Id(Readkey),[])],[]),If(BinaryOp(=,Id(Sel),StringLiteral(3)),[CallStmt(Id(ClrScr),[]),CallStmt(Id(Write),[StringLiteral(Are you sure?(Y/N))]),AssignStmt(Id(YN),CallExpr(Id(Readkey),[])),If(BinaryOp(=,Id(YN),StringLiteral(y)),[CallStmt(Id(Halt),[])],[]),If(BinaryOp(=,Id(YN),StringLiteral(n)),[CallStmt(Id(Goto1),[])],[])],[])])])"
        self.assertTrue(TestAST.test(input,expect,308))
        
    def test_if309(self):
        input = """procedure main();
            begin
                 if a>b then a := b; else b:=a ;
            end
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,309))

    def test_expr310(self):
        input = """procedure foo(a:integer);
                begin
                    while true do putstring(a);
                end
        """
        expect = "successful"
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
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(SEL),IntType),VarDecl(Id(YN),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral([1]. PLAY GAME)]),CallStmt(Id(WRITELN),[StringLiteral([2]. LOAD GAME)]),CallStmt(Id(WRITELN),[StringLiteral([3]. MULTIPLAYER)]),CallStmt(Id(WRITELN),[StringLiteral([4]. EXIT GAME)]),CallStmt(Id(Writeln),[StringLiteral(note: Do not press anything except)]),CallStmt(Id(Writeln),[StringLiteral(numbers; otherwise an error occurs!)]),CallStmt(Id(Readln),[Id(SEL)]),If(BinaryOp(=,Id(SEL),IntLiteral(1)),[CallStmt(Id(Writeln),[StringLiteral(You will soon be able to create)]),CallStmt(Id(Writeln),[StringLiteral(games using Pascal Programming :-))]),CallStmt(Id(Delay),[IntLiteral(3000)]),CallStmt(Id(Goto),[Id(Ret)])],[]),If(BinaryOp(=,Id(SEL),IntLiteral(2)),[CallStmt(Id(Writeln),[StringLiteral(Ahhh... no saved games)]),CallStmt(Id(Delay),[IntLiteral(3000)]),CallStmt(Id(Goto),[Id(Ret)])],[]),If(BinaryOp(=,Id(SEL),IntLiteral(3)),[CallStmt(Id(Writeln),[StringLiteral(networking or 2 players?)]),CallStmt(Id(Delay),[IntLiteral(3000)]),CallStmt(Id(Goto),[Id(Ret)])],[]),If(BinaryOp(=,Id(SEL),IntLiteral(4)),[CallStmt(Id(Writeln),[StringLiteral(Are you sure you want to Exit?)]),AssignStmt(Id(YN),Id(Readkey)),If(BinaryOp(=,Id(YN),StringLiteral(y)),[CallStmt(Id(Writeln),[StringLiteral(Good Bye...)]),CallStmt(Id(Delay),[IntLiteral(1000)]),CallStmt(Id(Halt),[])],[]),If(BinaryOp(=,Id(YN),StringLiteral(n)),[CallStmt(Id(Goto),[Id(Ret)])],[])],[])])])"
        self.assertTrue(TestAST.test(input,expect,312))
        

    def test_func313(self):
        input = """
        fUnCTiOn foo(): integer;
        var a,b: integer;
        begin
            a := a+b;
            bar(a);
        end"""
        expect = "successful"
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
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,314))
    
    def test_index_exp315(self):
        input = """
procedure main();
begin
    a := a[2] := 1[2] := a[b[2]];
end
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,315))

    def test_array_dec316(self):
        input = """
        var  a: array [4 .. 9] of real ;          
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,316))

    def test_array_dec317(self):
        input = """
        var  a: array [-4 .. 2] of integer ;          
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,317))

    def test_assign318(self):
        input = """procedurE inndeeexxx();
        begin
            (e>d)[5] := abc+a[1][2]; 
            foo(2)[a+3] := 5;
            ca[1][10] := 123;
        end"""
        expect = "successful"
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
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,319))

    def test_for320(self):
        input = """
Procedure DrawLine(X : Integer; Y : Integer);
    
    Begin 
        For count := 1 to 10 do
        Write(chr(196));
    End


        """
        expect = "successful"
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
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,321))

    def test_stringlit322(self):
        input = """procedure main();
                beGin
                    a := "abcede";
                end

            """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,322))

    def test_compound323(self):
        input = """procedure foo();
                   BEGIN
                    while (true) do begin begin end eND
                   END"""
        expect = "successful"
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
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(n1),StringType),VarDecl(Id(n2),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral(Enter two numbers: (\"\"0\"\" & \"\"0\"\" to exit))]),While(UnaryOp(not,BinaryOp(OR,BinaryOp(=,Id(n1),StringLiteral(0)),BinaryOp(=,Id(n2),StringLiteral(0)))),[CallStmt(Id(Write),[StringLiteral(No.1: )]),CallStmt(Id(Readln),[Id(n1)]),CallStmt(Id(Write),[StringLiteral(No.2: )]),CallStmt(Id(Readln),[Id(n2)]),If(BinaryOp(OR,BinaryOp(=,Id(n1),StringLiteral(0)),BinaryOp(=,Id(n2),StringLiteral(0))),[CallStmt(Id(Halt),[IntLiteral(0)])],[])])])])"
        self.assertTrue(TestAST.test(input,expect,325))  

    def test_CallExpr326(self):
        input = """function foo(): integer;
                   BEGIN
                    foo();
                    bar(a);
                   END"""
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,326))

    def test_CallExpr327(self):
        input = """function foo(): integer;
                   BEGIN
                    foo(a+2);
                   END"""
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,327))

    def test_CallExpr328(self):
        input = """function foo(): integer;
                   BEGIN
                    foo(foo(2));
                   END"""
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,328))

    def test_fun329(self):
        input = """
        PROCEDURE test_err();
        begin
            foo := a[b[2]];
        end
        """
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(age),IntType),FuncDecl(Id(main),[],VoidType(),[],[While(BinaryOp(AND,BinaryOp(>,Id(age),IntLiteral(0)),BinaryOp(<=,Id(age),IntLiteral(100))),[CallStmt(Id(Write),[StringLiteral(Enter age (1 - 100): )]),CallStmt(Id(Readln),[Id(age)]),If(BinaryOp(<,Id(age),IntLiteral(1)),[CallStmt(Id(Writeln),[StringLiteral(Age cannot be less than 1...)])],[If(BinaryOp(>,Id(age),IntLiteral(100)),[CallStmt(Id(Writeln),[StringLiteral(Age cannot be greater than 100...)])],[])])])])])"
        self.assertTrue(TestAST.test(input,expect,330))
    
    def test_fun314(self):
        input = """function  foo () :  real ;
        begin
        if ( true )  then return 2;     
        else return 2;     
        end"""
        expect = "successful"
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
        expect = "successful"
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
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,333))

    def test_proc334(self):
        input = """
                procedure foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                    return;
                  END"""
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,334))
    
    def test_proc335(self):
        input = """proCeduRe foo(c: real) ;
                  var x,y: real ;
                  BEGIN
                  END"""
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,335))

    def test_func336(self):
        input = """
                FUNcTION foo(a, b: integer ; c: real): real;
                  BEGIN
                    return a[1];
                  END"""
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(bool),BoolType),VarDecl(Id(A),IntType),VarDecl(Id(B),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(A),IntLiteral(10)),AssignStmt(Id(B),IntLiteral(30)),AssignStmt(Id(bool),BooleanLiteral(False)),AssignStmt(Id(bool),BinaryOp(OR,BinaryOp(=,Id(A),IntLiteral(10)),BinaryOp(=,Id(B),IntLiteral(10)))),CallStmt(Id(Writeln),[Id(bool)]),AssignStmt(Id(bool),BinaryOp(AND,BinaryOp(=,Id(A),IntLiteral(10)),BinaryOp(=,Id(B),IntLiteral(10)))),CallStmt(Id(Writeln),[Id(bool)])])])"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(quit),BoolType),VarDecl(Id(a),StringType),FuncDecl(Id(main),[],VoidType(),[],[While(UnaryOp(NOT,BinaryOp(=,Id(quit),BooleanLiteral(True))),[CallStmt(Id(Writeln),[StringLiteral(Type \"\"exit\"\" to quit:)]),CallStmt(Id(Readln),[Id(a)]),If(BinaryOp(=,Id(a),StringLiteral(exit)),[AssignStmt(Id(quit),BooleanLiteral(True))],[])])])])"
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
        expect = r"Program([FuncDecl(Id(DrawLine),[],VoidType(),[VarDecl(Id(Counter),IntType)],[CallStmt(Id(textcolor),[Id(green)]),For(Id(Counter)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(Write),[CallExpr(Id(chr),[IntLiteral(196)])])])]),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(10)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(Readkey),[])])])"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = r"Program([FuncDecl(Id(DrawLine),[VarDecl(Id(X),IntType),VarDecl(Id(Y),IntType)],VoidType(),[VarDecl(Id(Counter),IntType)],[CallStmt(Id(GotoXy),[Id(X),Id(Y)]),CallStmt(Id(textcolor),[Id(green)]),For(Id(Counter)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(Write),[CallExpr(Id(chr),[IntLiteral(196)])])])]),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(DrawLine),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id(DrawLine),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id(DrawLine),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id(DrawLine),[IntLiteral(10),IntLiteral(10)]),CallStmt(Id(Readkey),[])])])"
        self.assertTrue(TestAST.test(input,expect,344))
    
    def test_simple_program345(self):
        input = """
        procedurE foo () ;
            begin
            End          
        """
        expect = "successful"
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
        expect = r"Program([FuncDecl(Id(Square),[VarDecl(Id(Index),IntType),VarDecl(Id(Result),IntType)],VoidType(),[],[AssignStmt(Id(Result),BinaryOp(*,Id(Index),Id(Index)))]),VarDecl(Id(Res),IntType),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral(The square of 5 is: )]),CallStmt(Id(Square),[IntLiteral(5),Id(Res)]),CallStmt(Id(Writeln),[Id(Res)])])])"
        self.assertTrue(TestAST.test(input,expect,346))
        
    def test_while347(self):
        input = """
        function foo(): real;
        var a,b: integer;
        begin
        while (a>b) do  
        a := a/b;
        end"""
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,347))
    
    def test_for348(self):
        input = """
        procedure main();
        var a : integer;
        begin
        for x:= 1 to 10 do 
        a := a*a + x;
        end"""
        expect = "successful"
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
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(UserFile),StringType),VarDecl(Id(FileName),StringType),VarDecl(Id(TFile),StringType),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral(Enter the file name (including its full path) of the text file (without the extension):)]),CallStmt(Id(Readln),[Id(FileName)]),CallStmt(Id(Assign),[Id(UserFile),BinaryOp(+,Id(FileName),StringLiteral(.txt))]),CallStmt(Id(Reset),[Id(UserFile)]),While(UnaryOp(NOT,CallExpr(Id(Eof),[Id(UserFile)])),[CallStmt(Id(Readln),[Id(UserFile),Id(TFile)]),CallStmt(Id(Writeln),[Id(TFile)])]),CallStmt(Id(Close),[Id(UserFile)]),CallStmt(Id(Readln),[])])])"
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
        expect = r"Program([VarDecl(Id(FName),StringType),VarDecl(Id(Txt),StringType),VarDecl(Id(UserFile),StringType),FuncDecl(Id(Main),[],VoidType(),[],[AssignStmt(Id(FName),StringLiteral(Textfile)),CallStmt(Id(Assign),[Id(UserFile),BinaryOp(+,BinaryOp(+,StringLiteral(C:\\),Id(FName)),StringLiteral(.txt))]),CallStmt(Id(Rewrite),[Id(UserFile)]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral(PASCAL PROGRAMMING)]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral(if you did not understand something,)]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral(please send me an email to:)]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral(victorsaliba@hotmail.com)]),CallStmt(Id(Writeln),[StringLiteral(Write some text to the file:)]),CallStmt(Id(Readln),[Id(Txt)]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral()]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral(The user entered this text:)]),CallStmt(Id(Writeln),[Id(UserFile),Id(Txt)]),CallStmt(Id(Close),[Id(UserFile)])])])"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(UFile),StringType),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Assign),[Id(UFile),StringLiteral(C:\\ADDTEXT.TXT)]),CallStmt(Id(Erase),[Id(UFile)])])])"
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
        expect = r"Program([VarDecl(Id(t),StringType),VarDecl(Id(s),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Assign),[Id(t),StringLiteral(C:\\ABC.DEF)]),CallStmt(Id(Reset),[Id(t)]),If(BinaryOp(<>,Id(IOResult),IntLiteral(0)),[CallStmt(Id(Writeln),[StringLiteral(The file required to be opened is not found!)]),CallStmt(Id(Readln),[])],[CallStmt(Id(Readln),[Id(t),Id(s)]),CallStmt(Id(Writeln),[StringLiteral(The first line of the file reads: ),Id(s)]),CallStmt(Id(Close),[Id(t)])])])])"
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
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(f),StringType),VarDecl(Id(sz),IntType),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Assign),[Id(f),StringLiteral(C:\\anyfile.txt)]),CallStmt(Id(Reset),[Id(f)]),If(BinaryOp(<>,Id(IOResult),IntLiteral(0)),[CallStmt(Id(Writeln),[StringLiteral(File not found.. exiting)]),CallStmt(Id(Readln),[])],[AssignStmt(Id(sz),CallExpr(Id(Round),[BinaryOp(/,CallExpr(Id(FileSize),[Id(f)]),IntLiteral(1024))])),CallStmt(Id(Writeln),[StringLiteral(Size of the file in Kilobytes: ),Id(sz),StringLiteral( Kb)]),CallStmt(Id(Readln),[]),CallStmt(Id(Close),[Id(f)])])])])"
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
        expect = r"Program([VarDecl(Id(myVar),IntType),VarDecl(Id(myArray),ArrayType(1,5,IntType)),FuncDecl(Id(Main),[],VoidType(),[],[AssignStmt(ArrayCell(Id(myArray),IntLiteral(2)),IntLiteral(25)),AssignStmt(Id(myVar),ArrayCell(Id(myArray),IntLiteral(2)))])])"
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
        expect = "successful"
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
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,360))
    
    def test_complex361(self):
        input = """
                function fibo(x: integer): integer;
                begin
                    if x<=2 then return 1;
                    else return fibo(x-2)+ fibo(x-1);
                end
                """
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(i),IntType),VarDecl(Id(myIntArray),ArrayType(1,20,IntType)),VarDecl(Id(myBoolArray),ArrayType(1,20,BoolType)),FuncDecl(Id(Main),[],VoidType(),[],[For(Id(i)IntLiteral(1),CallExpr(Id(Length),[Id(myIntArray)]),True,[AssignStmt(ArrayCell(Id(myIntArray),Id(i)),IntLiteral(1)),AssignStmt(ArrayCell(Id(myBoolArray),Id(i)),BooleanLiteral(True))])])])"
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
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(myString),StringType),FuncDecl(Id(Main),[],VoidType(),[],[AssignStmt(Id(myString),StringLiteral(Hey! How are you?)),CallStmt(Id(Writeln),[StringLiteral(The length of the string is ),CallExpr(Id(byte),[ArrayCell(Id(myString),IntLiteral(0))])]),CallStmt(Id(Write),[ArrayCell(Id(myString),CallExpr(Id(byte),[ArrayCell(Id(myString),IntLiteral(0))]))]),CallStmt(Id(Write),[StringLiteral( is the last character.)])])])"
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
        expect = r"Program([VarDecl(Id(S),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S),StringLiteral(Hey there! How are you?)),CallStmt(Id(Write),[StringLiteral(The word \"How\" is found at char index )]),CallStmt(Id(Writeln),[CallExpr(Id(Pos),[StringLiteral(How),Id(S)])]),If(BinaryOp(<=,CallExpr(Id(Pos),[StringLiteral(Why),Id(S)]),IntLiteral(0)),[CallStmt(Id(Writeln),[StringLiteral(\"Why\" is not found.)])],[])])])"
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
        expect = r"Program([VarDecl(Id(S),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S),StringLiteral(Hey there! How are you?)),AssignStmt(Id(S),CallExpr(Id(Copy),[Id(S),IntLiteral(5),IntLiteral(6)])),CallStmt(Id(Write),[Id(S)])])])"
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
        expect = r"Program([VarDecl(Id(S),StringType),VarDecl(Id(i),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S),StringLiteral(Hey! How are you?)),For(Id(i)IntLiteral(1),CallExpr(Id(length),[Id(S)]),True,[AssignStmt(ArrayCell(Id(S),Id(i)),CallExpr(Id(UpCase),[ArrayCell(Id(S),Id(i))]))]),CallStmt(Id(Write),[Id(S)])])])"
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
        expect = r"Program([FuncDecl(Id(BubbleSort),[VarDecl(Id(numbers),ArrayType(1,100,IntType)),VarDecl(Id(size),IntType)],VoidType(),[VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),VarDecl(Id(temp),IntType)],[For(Id(i)BinaryOp(-,Id(size),IntLiteral(1)),IntLiteral(1),False,[For(Id(j)IntLiteral(2),Id(i),True,[If(BinaryOp(>,ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1))),ArrayCell(Id(numbers),Id(j))),[AssignStmt(Id(temp),ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1)))),AssignStmt(ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1))),ArrayCell(Id(numbers),Id(j))),AssignStmt(ArrayCell(Id(numbers),Id(j)),Id(temp))],[])])])])])"
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
        expect = r"Program([FuncDecl(Id(InsertionSort),[VarDecl(Id(numbers),ArrayType(1,100,IntType)),VarDecl(Id(size),IntType)],VoidType(),[VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),VarDecl(Id(index),IntType)],[For(Id(i)IntLiteral(2),BinaryOp(-,Id(size),IntLiteral(1)),True,[AssignStmt(Id(index),ArrayCell(Id(numbers),Id(i))),AssignStmt(Id(j),Id(i)),While(BinaryOp(AND,BinaryOp(>,Id(j),IntLiteral(1)),BinaryOp(>,ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1))),Id(index))),[AssignStmt(ArrayCell(Id(numbers),Id(j)),ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1)))),AssignStmt(Id(j),BinaryOp(-,Id(j),IntLiteral(1)))]),AssignStmt(ArrayCell(Id(numbers),Id(j)),Id(index))])])])"
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
        expect = r"Program([FuncDecl(Id(QSort),[VarDecl(Id(numbers),ArrayType(1,100,IntType)),VarDecl(Id(left),IntType),VarDecl(Id(right),IntType)],VoidType(),[VarDecl(Id(pivot),IntType),VarDecl(Id(l_ptr),IntType),VarDecl(Id(r_ptr),IntType)],[AssignStmt(Id(l_ptr),Id(left)),AssignStmt(Id(r_ptr),Id(right)),AssignStmt(Id(pivot),ArrayCell(Id(numbers),Id(left))),While(BinaryOp(<,Id(left),Id(right)),[While(BinaryOp(AND,BinaryOp(>=,ArrayCell(Id(numbers),Id(right)),Id(pivot)),BinaryOp(<,Id(left),Id(right))),[AssignStmt(Id(right),BinaryOp(-,Id(right),IntLiteral(1)))]),If(BinaryOp(<>,Id(left),Id(right)),[AssignStmt(ArrayCell(Id(numbers),Id(left)),ArrayCell(Id(numbers),Id(right))),AssignStmt(Id(left),BinaryOp(+,Id(left),IntLiteral(1)))],[]),While(BinaryOp(AND,BinaryOp(<=,ArrayCell(Id(numbers),Id(left)),Id(pivot)),BinaryOp(<,Id(left),Id(right))),[AssignStmt(Id(left),BinaryOp(+,Id(left),IntLiteral(1)))]),If(BinaryOp(<>,Id(left),Id(right)),[AssignStmt(ArrayCell(Id(numbers),Id(right)),ArrayCell(Id(numbers),Id(left))),AssignStmt(Id(right),BinaryOp(-,Id(right),IntLiteral(1)))],[])]),AssignStmt(ArrayCell(Id(numbers),Id(left)),Id(pivot)),AssignStmt(Id(pivot),Id(left)),AssignStmt(Id(left),Id(l_ptr)),AssignStmt(Id(right),Id(r_ptr)),If(BinaryOp(<,Id(left),Id(pivot)),[CallStmt(Id(QSort),[Id(numbers),Id(left),BinaryOp(-,Id(pivot),IntLiteral(1))])],[]),If(BinaryOp(>,Id(right),Id(pivot)),[CallStmt(Id(QSort),[Id(numbers),BinaryOp(+,Id(pivot),IntLiteral(1)),Id(right)])],[])]),FuncDecl(Id(QuickSort),[VarDecl(Id(numbers),ArrayType(1,100,IntType)),VarDecl(Id(size),IntType)],VoidType(),[],[CallStmt(Id(QSort),[Id(numbers),IntLiteral(0),BinaryOp(-,Id(size),IntLiteral(1))])])])"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(myStack),ArrayType(1,100,IntType)),VarDecl(Id(topPointer),IntType),FuncDecl(Id(InitStack),[],VoidType(),[],[AssignStmt(Id(topPointer),IntLiteral(0))]),FuncDecl(Id(IsEmpty),[],BoolType,[],[AssignStmt(Id(IsEmpty),BooleanLiteral(False)),If(BinaryOp(=,Id(topPointer),IntLiteral(0)),[AssignStmt(Id(IsEmpty),BooleanLiteral(True))],[])]),FuncDecl(Id(IsFull),[],BoolType,[],[AssignStmt(Id(IsFull),BooleanLiteral(False)),If(BinaryOp(=,BinaryOp(+,Id(topPointer),IntLiteral(1)),Id(STACK_SIZE)),[AssignStmt(Id(IsFull),BooleanLiteral(True))],[])]),FuncDecl(Id(Pop),[],IntType,[],[AssignStmt(Id(Pop),Id(nil)),If(UnaryOp(not,Id(IsEmpty)),[AssignStmt(Id(Pop),ArrayCell(Id(myStack),Id(topPointer))),AssignStmt(Id(topPointer),BinaryOp(-,Id(topPointer),IntLiteral(1)))],[])]),FuncDecl(Id(Push),[VarDecl(Id(item),IntType)],VoidType(),[],[If(UnaryOp(not,Id(IsFull)),[AssignStmt(ArrayCell(Id(myStack),BinaryOp(+,Id(topPointer),IntLiteral(1))),Id(item)),AssignStmt(Id(topPointer),BinaryOp(+,Id(topPointer),IntLiteral(1)))],[])]),FuncDecl(Id(GetSize),[],IntType,[],[AssignStmt(Id(GetSize),Id(topPointer))])])"
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
        expect = r"Program([VarDecl(Id(Counter),IntType),FuncDecl(Id(main),[],VoidType(),[],[For(Id(Counter)IntLiteral(1),IntLiteral(5),True,[CallStmt(Id(gotoxy),[IntLiteral(25),BinaryOp(+,IntLiteral(5),Id(Counter))]),CallStmt(Id(Writeln),[StringLiteral(I)])]),For(Id(Counter)IntLiteral(5),IntLiteral(1),False,[CallStmt(Id(gotoxy),[IntLiteral(32),BinaryOp(-,IntLiteral(11),Id(Counter))]),CallStmt(Id(Writeln),[StringLiteral(I)])]),For(Id(Counter)IntLiteral(1),IntLiteral(6),True,[CallStmt(Id(gotoxy),[BinaryOp(+,IntLiteral(25),Id(Counter)),IntLiteral(11)]),CallStmt(Id(Writeln),[StringLiteral(-)])]),For(Id(Counter)IntLiteral(6),IntLiteral(1),False,[CallStmt(Id(gotoxy),[BinaryOp(-,IntLiteral(32),Id(Counter)),IntLiteral(5)]),CallStmt(Id(Writeln),[StringLiteral(-)])]),CallStmt(Id(Gotoxy),[IntLiteral(25),IntLiteral(5)]),CallStmt(Id(Writeln),[StringLiteral(+)]),CallStmt(Id(GotoXy),[IntLiteral(25),IntLiteral(11)]),CallStmt(Id(Writeln),[StringLiteral(+)]),CallStmt(Id(GotoXy),[IntLiteral(32),IntLiteral(5)]),CallStmt(Id(Writeln),[StringLiteral(+)]),CallStmt(Id(GotoXy),[IntLiteral(32),IntLiteral(11)]),CallStmt(Id(Writeln),[StringLiteral(+)]),CallStmt(Id(GotoXy),[IntLiteral(45),IntLiteral(7)]),CallStmt(Id(Write),[StringLiteral(Made with For Loops :))]),CallStmt(Id(Readln),[])])])"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(Ch),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral(Press \"\"q\"\" to exit...)]),AssignStmt(Id(Ch),CallExpr(Id(Readkey),[])),While(BinaryOp(<>,Id(Ch),StringLiteral(q)),[CallStmt(Id(Writeln),[StringLiteral(Please press \"\"q\"\" to exit.)]),AssignStmt(Id(Ch),CallExpr(Id(Readkey),[]))])])])"
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
        expect = r"Program([FuncDecl(Id(Factorial),[VarDecl(Id(n),IntType)],IntType,[VarDecl(Id(Result),IntType),VarDecl(Id(i),IntType)],[AssignStmt(Id(Result),Id(n)),If(BinaryOp(<=,Id(n),IntLiteral(1)),[AssignStmt(Id(Result),IntLiteral(1))],[For(Id(i)BinaryOp(-,Id(n),IntLiteral(1)),IntLiteral(1),False,[AssignStmt(Id(Result),BinaryOp(*,Id(Result),Id(i)))])]),AssignStmt(Id(Factorial),Id(Result))])])"
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
        expect = r"Program([FuncDecl(Id(Factorial),[VarDecl(Id(n),IntType)],IntType,[VarDecl(Id(Result),IntType)],[If(BinaryOp(=,Id(n),IntLiteral(1)),[AssignStmt(Id(Factorial),IntLiteral(1))],[AssignStmt(Id(Factorial),BinaryOp(*,Id(n),CallExpr(Id(Factorial),[BinaryOp(-,Id(n),IntLiteral(1))])))])])])"
        self.assertTrue(TestAST.test(input,expect,381))
        

    def test_var382(self):
        input = """
var
age, weekdays : integer;
taxrate, net_income: real;
choice, isready: boolean;
name, surname : string;
        """
        expect = r"Program([VarDecl(Id(age),IntType),VarDecl(Id(weekdays),IntType),VarDecl(Id(taxrate),FloatType),VarDecl(Id(net_income),FloatType),VarDecl(Id(choice),BoolType),VarDecl(Id(isready),BoolType),VarDecl(Id(name),StringType),VarDecl(Id(surname),StringType)])"
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
        expect = r"Program([VarDecl(Id(firstname),StringType),VarDecl(Id(surname),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(Please enter your first name: )]),CallStmt(Id(readln),[Id(firstname)]),CallStmt(Id(writeln),[StringLiteral(Please enter your surname: )]),CallStmt(Id(readln),[Id(surname)]),CallStmt(Id(writeln),[]),CallStmt(Id(writeln),[Id(message),StringLiteral( ),Id(firstname),StringLiteral( ),Id(surname)])])])"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),If(BinaryOp(<,Id(a),IntLiteral(20)),[CallStmt(Id(writeln),[StringLiteral(a is less than 20)])],[CallStmt(Id(writeln),[StringLiteral(a is not less than 20)])]),CallStmt(Id(writeln),[StringLiteral(value of a is : ),Id(a)])])])"
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
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),If(BinaryOp(=,Id(a),IntLiteral(10)),[CallStmt(Id(writeln),[StringLiteral(Value of a is 10)])],[If(BinaryOp(=,Id(a),IntLiteral(20)),[CallStmt(Id(writeln),[StringLiteral(Value of a is 20)])],[If(BinaryOp(=,Id(a),IntLiteral(30)),[CallStmt(Id(writeln),[StringLiteral(Value of a is 30)])],[CallStmt(Id(writeln),[StringLiteral(None of the values is matching)])])])]),CallStmt(Id(writeln),[StringLiteral(Exact value of a is: ),Id(a)])])])"
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
        expect = r"Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),AssignStmt(Id(b),IntLiteral(200)),If(BinaryOp(=,Id(a),IntLiteral(100)),[If(BinaryOp(=,Id(b),IntLiteral(200)),[CallStmt(Id(writeln),[StringLiteral(Value of a is 100 and value of b is 200)])],[])],[]),CallStmt(Id(writeln),[StringLiteral(Exact value of a is: ),Id(a)]),CallStmt(Id(writeln),[StringLiteral(Exact value of b is: ),Id(b)])])])"
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
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(10)),While(BinaryOp(<,Id(a),IntLiteral(20)),[CallStmt(Id(writeln),[StringLiteral(value of a: ),Id(a)]),AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])])])"
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
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(10)),While(BinaryOp(<,Id(a),IntLiteral(20)),[CallStmt(Id(writeln),[StringLiteral(value of a: ),Id(a)]),AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1))),If(BinaryOp(>,Id(a),IntLiteral(15)),[Break],[])])])])"
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
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(10)),While(UnaryOp(not,BinaryOp(=,Id(a),IntLiteral(20))),[If(BinaryOp(=,Id(a),IntLiteral(15)),[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Continue],[]),CallStmt(Id(writeln),[StringLiteral(value of a: ),Id(a)]),AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])])])"
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
        expect = r"Program([FuncDecl(Id(max),[VarDecl(Id(num1),IntType),VarDecl(Id(num2),IntType)],IntType,[VarDecl(Id(result),IntType)],[If(BinaryOp(>,Id(num1),Id(num2)),[AssignStmt(Id(result),Id(num1))],[AssignStmt(Id(result),Id(num2))]),AssignStmt(Id(max),Id(result))])])"
        self.assertTrue(TestAST.test(input,expect,393))
        
    def test_proc394(self):
        input = """proCeduRe foo(c: real) ;
                  var x,y: real ;
                  BEGIN
                  END"""
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,394))
    
    def test_func395(self):
        input = """
                FUNcTION foo(a, b: integer ; c: real): real;
                  BEGIN
                    return a[1];
                  END"""
        expect = "successful"
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
        expect = "successful"
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
        expect = r"Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(ret),IntType),FuncDecl(Id(max),[VarDecl(Id(num1),IntType),VarDecl(Id(num2),IntType)],IntType,[VarDecl(Id(result),IntType)],[If(BinaryOp(>,Id(num1),Id(num2)),[AssignStmt(Id(result),Id(num1))],[AssignStmt(Id(result),Id(num2))]),AssignStmt(Id(max),Id(result))]),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),AssignStmt(Id(b),IntLiteral(200)),AssignStmt(Id(ret),CallExpr(Id(max),[Id(a),Id(b)])),CallStmt(Id(writeln),[StringLiteral(Max value is : ),Id(ret)])])])"
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
        expect = r"Program([FuncDecl(Id(findMin),[VarDecl(Id(x),IntType),VarDecl(Id(y),IntType),VarDecl(Id(z),IntType),VarDecl(Id(m),IntType)],VoidType(),[],[If(BinaryOp(<,Id(x),Id(y)),[AssignStmt(Id(m),Id(x))],[AssignStmt(Id(m),Id(y))]),If(BinaryOp(<,Id(z),Id(m)),[AssignStmt(Id(m),Id(z))],[])])])"
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
        expect = r"Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(min),IntType),FuncDecl(Id(findMin),[VarDecl(Id(x),IntType),VarDecl(Id(y),IntType),VarDecl(Id(z),IntType),VarDecl(Id(m),IntType)],VoidType(),[],[If(BinaryOp(<,Id(x),Id(y)),[AssignStmt(Id(m),Id(x))],[AssignStmt(Id(m),Id(y))]),If(BinaryOp(<,Id(z),Id(m)),[AssignStmt(Id(m),Id(z))],[])]),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral( Enter three numbers: )]),CallStmt(Id(readln),[Id(a),Id(b),Id(c)]),CallStmt(Id(findMin),[Id(a),Id(b),Id(c),Id(min)]),CallStmt(Id(writeln),[StringLiteral( Minimum: ),Id(min)])])])"
        self.assertTrue(TestAST.test(input,expect,399))
        

   