import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_proc200(self):
        input = """ procedure main();
        begin
        end"""
        expect ="successful"
        self.assertTrue(TestParser.test(input,expect,200))

    def test_var201(self):
        input = """var a,b : integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_built_in202(self):
        input = """procedure foo(a : integer);
            begin
            putIntLn(4);
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_proc203(self):
        input = """procedure foo(a : integer;b : real);
    begin
        e := (3+4)/3;
        putint(a);
    return;
    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_array204(self):
        input = """procedure foo(a : integer;b : real);
    begin
        e := (3+4)/3;
        putint(a);
        a := b[4];
    return;
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_with205(self):
        input = """procedure foo(a : integer;b : real);
    begin
        with a,b : integer; d: integer; do d := c[b] + a;
    return;
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_assign206(self):
        input = """procedure foo(a : integer;b : real);
    begin
        d := a[b] := b + 5;
    return;
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_index207(self):
        input = """function foo(a : integer;b : real): array [1 .. 5] of real;
             begin
                 foo(2)[3+x] := a[b[2]] + 3;
                 return a;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_if208(self):
        input = """procedure main();
            begin
                 if a>b then a := b; else b:=a ;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_expr209(self):
        input = """procedure main();
            begin
                 a := (3+4*(5/4)-20+100 mod 4) ;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_expr210(self):
        input = """procedure foo(a:integer);
                begin
                    while true do putstring(a);
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_with211(self):
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
        self.assertTrue(TestParser.test(input,expect,211))

    def test_func212(self):
        input = """function max(num1, num2: integer): integer;

var result: integer;

begin
   if (num1 > num2) then
      result := num1;
   
   else
      result := num2;
   max := result;
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_vardec213(self):
        input = """var abc: integer; def: real;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_proc214(self):
        input = """
        procedurE foo();
        begin
            bar();
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_func215(self):
        input = """
        fUnCTiOn foo(): real;
        begin
            bar();
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_func216(self):
        input = """
        fUnCTiOn foo(): integer;
        var a,b: integer;
        begin
            a := a+b;
            bar(a);
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_func217(self):
        input = """
        fUnCTiOn foo(): integer;
        var a,b: integer;
        begin
            a : a+b;
            bar(a);
        end"""
        expect = "Error on line 5 col 14: :"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_func218(self):
        input = """
        fUnCTiOn foo();
        var a,b: integer;
        begin
            
        end"""
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_break219(self):
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
        self.assertTrue(TestParser.test(input,expect,219))

    def test_while220(self):
        input = """
var
   d: real;
procedure foo();
begin
   a := 10;
   while  a < 20 
    
      if( a > 2) then       
        a:=a+2;
end
        """
        expect = "Error on line 9 col 6: if"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_if221(self):
        input = """
var
   d: real;
procedure main();
begin
   a := 10;
   while  a < 20 do
    
      if( a > 15)      
        a:=a+2;
end
        """
        expect = "Error on line 10 col 8: a"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_proc_222(self):
        input = """

procedure main(): integer;
begin
end
        """
        expect = "Error on line 3 col 16: :"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_index_exp223(self):
        input = """
procedure main();
begin
    a := a[2] := 1[2] := a[b[2]];
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_array_dec224(self):
        input = """
        var  a: array [4 .. 9] of real ;          
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_array_dec225(self):
        input = """
        var  a: array [4 .. 9] of array ;          
        """
        expect = "Error on line 2 col 34: array"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_array_dec226(self):
        input = """
        var  a: array [-4 .. 2] of integer ;          
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_array_dec227(self):
        input = """
        var  a: array [5 .. 9] of integer ;          
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_array_dec228(self):
        input = """
        var  a: array [5 .. ] of integer ;          
        """
        expect = "Error on line 2 col 28: ]"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_built_in229(self):
        input = """
            proceDure main(): real ;
            BEGIN
            putLn();
            end
        """
        expect = "Error on line 2 col 28: :"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_built_in230(self):
        input = """
            function foo(): real ;
            BEGIN
            putLn();
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_bool231(self):
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
        self.assertTrue(TestParser.test(input,expect,231))

    def test_assign232(self):
        input = """procedurE inndeeexxx();
        begin
            (e>d)[5] := abc+a[1][2]; 
            foo(2)[a+3] := 5;
            ca[1][10] := 123;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_complex233(self):
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
        self.assertTrue(TestParser.test(input,expect,233));

    def test_for234(self):
        input = """
Procedure DrawLine(X : Integer; Y : Integer);
    
    Begin 
        For count := 1 to 10 do
        Write(chr(196));
    End


        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_proc235(self):
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
        self.assertTrue(TestParser.test(input,expect,235))

    def test_string236(self):
        input = """procedure main();
                beGin
                    a := "abcede";
                end

            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_string237(self):
        input = """
Var
    UFile : String;

Procedure main();
Begin
    Assign(UFile, "C:\\\\ADDTEXT.TXT");
    ReWrite(UFile); 
    Writeln(UFile, "How many sentences " + "are present in this file?");
    Close(UFile);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_compound238(self):
        input = """procedure foo();
                   BEGIN
                    while (true) do begin begin end eND
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_invocation239(self):
        input = """function foo(): integer;
                   BEGIN
                    foo();
                    bar(a);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_invocation240(self):
        input = """function foo(): integer;
                   BEGIN
                    foo(;
                   END"""
        expect = "Error on line 3 col 24: ;"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_invocation241(self):
        input = """function foo(): integer;
                   BEGIN
                    foo(a+2);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_invocation242(self):
        input = """function foo(): integer;
                   BEGIN
                    foo(foo(2));
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_fun243(self):
        input = """
        PROCEDURE test_err();
        begin
            foo := a[b[2]];
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_fun244(self):
        input = """function  foo () :  real ;
        begin
        if ( true )  then return 2;     
        else return 2;     
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_string245(self):
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
        self.assertTrue(TestParser.test(input,expect,245))

    def test_string246(self):
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
        self.assertTrue(TestParser.test(input,expect,246))

    def test_nested247(self):
        input = """
                procedure foo();
                    function foo_child():boolean; 
                        begin
                        end
                  begin
                    end
                """
        expect = "Error on line 3 col 20: function"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_proc248(self):
        input = """
                procedure foo(a, b: integer ; c: real) array [1 .. 2] of integer ;
                  var x,y: real ;
                  BEGIN
                    return;
                  END"""
        expect = "Error on line 2 col 55: array"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_proc249(self):
        input = """
                procedure foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                    return;
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_proc250(self):
        input = """proCeduRe foo(c: real) ;
                  var x,y: real ;
                  BEGIN
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_func251(self):
        input = """
                FUNcTION foo(a, b: integer ; c: real): real;
                  BEGIN
                    return a[1];
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_func252(self):
        input = """FUNcTION fooc( b: boolean; c: real):array [1 .. 2] of integer ;
                  var x: real ;
                  BEGIN
                    a:= a+1;
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_string253(self):
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
        self.assertTrue(TestParser.test(input,expect,253))

    def test_array254(self):
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
        self.assertTrue(TestParser.test(input,expect,254))

    def test_assoc255(self):
        input = """
        PROCEDURE test_err();
        begin
            foo(a >= b = 1);
        end
        """
        expect = "Error on line 4 col 23: ="
        self.assertTrue(TestParser.test(input,expect,255))

    def test_err256(self):
        input = """
        PROCEDURE test_err();
        begin
            (-(1[1]))[1] := """"asd"""" := ("aasd"+1;
        end
        """
        expect = "Error on line 4 col 44: ;"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_string257(self):
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
        self.assertTrue(TestParser.test(input,expect,257))

    def test_string258(self):
        input = """
Var 
    S : String;

Procedure main();
Begin
    S := "Hey! How are you?";
    Insert(" Max", S, 4);
    Write(S);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_string259(self):
        input = """
Var 
    S : String;

Procedure main();
Begin
    S := "MMMMMAAAAAIIIINNNN";
    Write(S);
End
        """
        expect = "successful"

    def test_string260(self):
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
        self.assertTrue(TestParser.test(input,expect,260))

    def test_simple_program261(self):
        input = """
        procedurE foo () ;
            begin
            End          
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_procedure262(self):
        input = """proceDure main () ;
        var x,y: integer;
        BEGIN
            putIntLn(4);
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_string263(self):
        input = """
Var 
    S : String;
    i : Real;

Procedure main();
Begin
    i := -0.563; 
    Str(i, S);
    Write(S); 
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))

    def test_string264(self):
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
        self.assertTrue(TestParser.test(input,expect,264))

    def test_for265(self):
        input = """
         function foo(): integer;
        var a,i: integer;
        begin
            a := 0;
            for i :=  1 to n do
                a := a + i;

        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

    def test_for266(self):
        input = """
        function foo(): integer;
        var a,b: integer;
        begin
        d := 0; 
        for x := 10 to 99 do
        d:= d*x;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

    def test_while267(self):
        input = """
        function foo(): real;
        var a,b: integer;
        begin
        while (a>b) do  
        a := a/b;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))

    def test_for268(self):
        input = """
        procedure main();
        var a : integer;
        begin
        for x:= 1 to 10 do 
        a := a*a + x;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_string269(self):
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
        self.assertTrue(TestParser.test(input,expect,269))

    def test_string270(self):
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
        self.assertTrue(TestParser.test(input,expect,270))

    def test_string271(self):
        input = """
Var 
    S     : String;
   
Procedure main();
Begin
    S := "day la mot \\t string escape"; 
    Write(S); 
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))

    def test_bool272(self):
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
        self.assertTrue(TestParser.test(input,expect,272))

    def test_func273(self):
        input = """function IsPrintable(aCharacter: string): Boolean;
        begin
        result := (aCharacter <> "7") and    //bell (beeps)
                    (aCharacter <> "8") and    //Backspace 
                    (aCharacter <> "10") and   //Carrage return
                    (aCharacter <> "13");      //Line feed
        end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_or274(self):
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
        self.assertTrue(TestParser.test(input,expect,274))

    def test_complex275(self):
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
        self.assertTrue(TestParser.test(input,expect,275))

    def test_complex276(self):
        input = """
                function fibo(x: integer): integer;
                begin
                    if x<=2 then return 1;
                    else return fibo(x-2)+ fibo(x-1);
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_complex277(self):
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
        self.assertTrue(TestParser.test(input,expect,277))

    def test_complex278(self):
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
        self.assertTrue(TestParser.test(input,expect,278))

    def test_complex279(self):
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
        self.assertTrue(TestParser.test(input,expect,279))

    def test_complex280(self):
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
        self.assertTrue(TestParser.test(input,expect,280))

    def test_complex281(self):
        input = """
                procedure HelloWorld();
begin
   writeln("Hello, World!");
   readkey();
end 
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_complex282(self):
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
        self.assertTrue(TestParser.test(input,expect,282))

    def test_complex283(self):
        input = """function GetRadius() : real;
                var
                radius : real;
                begin
                Write("Enter the radius: ");
                ReadLn(radius);
                GetRadius := radius;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_compled284(self):
        input = """
        procedure LoadMaze(filename: String);
        var
        input: string;
        line: String;
        l, c: Integer;
        begin
        Assign(input, filename);
        Reset(input);
        
        for l := 1 to LINE_COUNT do
        begin
            ReadLn(input, line);
            for c := 1 to COLUMN_COUNT do
            begin
            //case line[c] of
                " ":= maze[l, c] := EMPTY;
                "W":= maze[l, c] := WALL;
                "P":= 1 
                begin
                maze[l, c] := PLAYER;
                PlayerX := c; //the column is x
                PlayerY := l; //the line is y
                end
                "G":= maze[l, c] := GOAL;
            end
            end
        end
        end
        """
        expect = "Error on line 17 col 19: :="
        self.assertTrue(TestParser.test(input,expect,284))

    def test_complex285(self):
        input = """
        procedure MovePlayer(dx, dy: Integer);
        var
        newX, newY: Integer;
        begin
        newX := PlayerX + dx;
        newY := PlayerY + dy;
        
        //if we are not out of bounds
        if not ((newX <= 0) or (newX > COLUMN_COUNT) or (newY <= 0) or (newY > LINE_COUNT)) then
        begin
            if maze[newY, newX] = EMPTY then
            begin
            //clear the only location
            maze[PlayerY, PlayerX] := EMPTY;
            
            //update player location
            PlayerY := newY;
            PlayerX := newX;      
            maze[PlayerY, PlayerX] := PLAYER;
            end
        end
        end
        """
        expect = "Error on line 12 col 24: ,"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_complex286(self):
        input = """
        procedure test();
        Var
            myString : String;

        Begin
            myString := "Hey! How are you?";
            Writeln("The length of the string is " , to_integer(myString[0]));
            Write(myString[to_integer(myString[0])]);
            Write(" is the last character.");
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_complex287(self):
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
        self.assertTrue(TestParser.test(input,expect,287))

    def test_complex288(self):
        input = """
Var       
    Num1, Num2, Sum : Integer;
Procedure main();
Begin {no semicolon}
    Write("Input number 1:"); 
    Readln(Num1);
    Writeln("Input number 2:");
    Readln(Num2);
    Sum := Num1 + Num2; 
    Writeln(Sum);
    Readln();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_complex289(self):
        input = """
var a, b, c: integer;
procedure main();
begin
a := a1 := a2 := a3 := 4+2;
end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))

    def test_complex290(self):
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
        self.assertTrue(TestParser.test(input,expect,290))

    def test_buit_in291(self):
        input = """
procedure main();
begin
    writeln("abacad");
    putstring("wegwbwe");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_complex_292(self):
        input = """
function foo (i :integer) : real; begin a:= 5; end
                   var a, b, c: integer;
                   //do something
                   procedure xinchao();
                   bEgin
                     writeln("xin chao");
                   End
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_complex293(self):
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
        self.assertTrue(TestParser.test(input,expect,293))

    def test_err294(self):
        input = """
var
   num, f: integer;
function fact(x: integer): integer; (* calculates factorial of x - x! *)

begin
   if x=0 then
      fact := 1;
   else
      fact := x * fact(x-1); (* recursive call *)
end; { end of function fact}

procedure main();
begin
   writeln(" Enter a number: ");
   readln(num);
   f := fact(num);
   
   writeln(" Factorial ", num, " is: " , f);
end
        """
        expect = "Error on line 11 col 3: ;"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_complex295(self):
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
        self.assertTrue(TestParser.test(input,expect,295))

    def test_complex296(self):
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
        self.assertTrue(TestParser.test(input,expect,296))

    def test_err297(self):
        input = """
        PROCEDURE test(): real;
        begin
            foo();
        end
        """
        expect = "Error on line 2 col 24: :"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_err298(self):
        input = """
        PROCEDURE test();
        var a: long;
        begin
            foo();
        end
        """
        expect = "Error on line 3 col 15: long"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_random299(self):
        input = """
        PROCEDURE test();
        var a: real;
        begin
            putln();
            writeln(abced+aced);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))