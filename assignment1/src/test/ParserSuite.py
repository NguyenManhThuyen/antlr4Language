import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    
    def test_simple_program(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 101))

    def test_nested_functions(self):
        input = """outer: function void () {
            x: integer = 10;
            inner: function void() {
                y: integer = 20;
                print(x + y);
            }
            inner();
        }"""
        expect = "Error on line 3 col 19: function"
        self.assertTrue(TestParser.test(input, expect, 102))

    def test_function_declaration(self):
        input = """func: function void (a: integer, b: float, c: boolean) {
            x: integer;
            y: float = 3.14;
            z: boolean = true;
            if (c && b > 0) {
                x = a + y;
            }
            else {
                x = a - y;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 103))

   
    def test_simple_short_variable_declaration(self):
        input = """x: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 104))

    def test_simple_full_variable_declaration(self):
        input = """x: integer = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 105))

    def test_multi_full_variable_declaration(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 106))

    def test_error_multi_full_variable_declaration(self):
        input = """x, y, z: integer = 1, 2, 3, 6, 3;"""
        expect = "Error on line 1 col 26: ,"
        self.assertTrue(TestParser.test(input, expect, 107))

    def test_simple_function_declaration(self):
        input = """foo: function integer (){ }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 108))

    def test_function_declaration_with_return(self):
        input = """foo: function void (x: integer, y: float) { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 109))

    def test_function_declaration_with_return(self):
        input = """foo:function integer(x: integer, y: float) {
                z: integer;
                z = x + y;
                return z;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 110))

    def test_multi_function_declaration(self):
        input = """ foo: function integer(x: integer){ }
                    bar: function float(y: float){ }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 111))

    def test_multi_function_declaration_and_bodies(self):
        input = """foo: function integer(x: integer) {
                z: integer;
                z = x + 1;
                return z;
            }
            bar: function float(y: float) {
                z: float;
                z = y * 2.0;
                return z;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 112))

    def test_missing_semicolon_after_function_declaration(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3)
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "Error on line 11 col 12: inc"
        self.assertTrue(TestParser.test(input, expect, 113))

    def test_missing_semicolon_after_function_parameter_list(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta)
            delta = delta / 4;
        }"""
        expect = "Error on line 12 col 12: delta"
        self.assertTrue(TestParser.test(input, expect, 114))

    def test_missing_semi_function_body(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "Error on line 4 col 12: else"
        self.assertTrue(TestParser.test(input, expect, 115))

    def test_program_multi_function(self):
        input = """x: integer = 10;
        y: integer = 20;
        z: integer = 30;
        main: function void() {
            foo();
            bar();
            baz();
        }
        foo: function void() {
            x = y + z;
        }
        bar: function void() {
            y = x + z;
        }
        baz: function void() {
            z = x + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 116))

    def test_program_single_line(self):
        input = """x: integer = 10; // This is x
        y: integer = 20; // This is y
        z: integer = 30; // This is z
        main: function void() {
            // This is a comment
            foo(); // Call foo
            bar(); // Call bar
            baz(); // Call baz
        }
        foo: function void() {
            x = y + z;
        }
        bar: function void() {
            y = x + z;
        }
        baz: function void() {
            z = x + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 117))

    def test_program_single_line(self):
        input = """/* This is a block comment
        This is a multiline comment */
        x: integer = 10;
        y: integer = 20;
        z: integer = 30;
        /* This is another comment */
        main: function void() {
            foo();
            bar();
            baz();
        }
        foo: function void() {
            x = y + z;
        }
        bar: function void() {
            y = x + z;
        }
        baz: function void() {
            z = x + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 118))

    def test_error_program_single_line(self):
        input = """/* This is a block comment
        This is a multiline comment */
        x: integer = 10;
        y: integer = 20;
        z: integer = 30;
        /* This is another comment */ */
        main: function void() {
            foo();
            bar();
            baz();
        }
        foo: function void() {
            x = y + z;
        }
        bar: function void() {
            y = x + z;
        }
        baz: function void() {
            z = x + y;
        }"""
        expect = "Error on line 6 col 38: *"
        self.assertTrue(TestParser.test(input, expect, 119))

    def test_error_program_string(self):
        input = """x: boolean = true;
        y: boolean = false;
        z: boolean = (x == y);
        main: function void() {
            if (x) {
                print("x is true");
            } else {
                print("x is false");
            }
            if (y) {
                print("y is true");
            } else {
                print("y is false");
            }
            if (z) {
                print("z is true");
            } else {
                print("z is false");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 120))

    def test_error_program_single_line(self):
        input = """x: string = "Hello";
        y: string = "World";
        z: string = x + y;
        main: function void() {
            print(z);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 121))

    def test_error_program_if_statement(self):
        input = """x: integer = 10;
        y: integer = 20;
        main: function void() {
            if (x > y) {
                print("x is greater than y");
            } else {
                print("x is less than or equal to y");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 122))

    def test_invalid_main_function_declaration(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "Error on line 9 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 123))

    def test_invalid_variable_declaration(self):
        input = """x integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "Error on line 1 col 2: integer"
        self.assertTrue(TestParser.test(input, expect, 124))

    def test_invalid_function_declaration(self):
        input = """x: integer = 65;
        fact: function integer (n integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "Error on line 2 col 34: integer"
        self.assertTrue(TestParser.test(input, expect, 125))

  

    def test_invalid_expression(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1)
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "Error on line 5 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 126))


    def test_multiple_func_definitions_and_operations(self):
        input = """x: integer = 10;
        y: integer = 20;
        z: integer = 30;
        foo: function integer (a: integer, b: integer, c: integer) {
            return a + b * c;
        }
        bar: function integer (n: integer) {
            return foo(x, y, z) + n;
        }
        main: function void() {
            printIntLn(bar(5));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 127))

    def test_mul_func_and_boolean_exprs(self):
        input = """foo: function boolean (a: boolean, b: boolean) {
            return (a || b) && (! a || b);
        }
        bar: function boolean (n: integer) {
            return (n > 0) && (n < 10);
        }
        main: function void() {
            printBoolLn(foo(true, false) || bar(5));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 128))

    def test_nested_func_calls_and_complex_exprs(self):
        input = """x: integer = 5;
        y: integer = 10;
        foo: function integer (a: integer, b: integer) {
            return a + b * (a - b);
        }
        bar: function boolean (n: integer) {
            return (n > 0) && (n < 10);
        }
        main: function void() {
            z: integer = foo(x + y, y - x) * 2 - 5;
            printIntLn(z);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 129))


    def test_error_exist_func_in_program(self):
        input = """x: integer = 4;
        while (x <= 10) {
            sum = sum + x * 2;
            x = x + 1;
        }
        printIntLn(sum);
        """
        expect = "Error on line 2 col 8: while"
        self.assertTrue(TestParser.test(input, expect, 130))

    def test_multi_variable_assignment(self):
        input = """a: integer = 5;
            b, c: float = 2.5, 3.2;
            d, e, f: boolean = true, false, true;
            g: string = "hello";
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 131))

    
    def test300(self):
        input = """endtest: function void(){
            printString("Let's end test parsersuite. I'm tired");
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 132))
    
  
        self.assertTrue(TestParser.test(input, expect, 133))
    def test283(self):
        input = """main: function void() {sum = a[1] + a[2] +a[3] ;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 134))
    def test284(self):
        input = """main: function void() {sum =;}"""
        expect = """Error on line 1 col 28: ;"""
        self.assertTrue(TestParser.test(input, expect, 135))
    def test285(self):
        input = """test: function array[2] of string(){
            return {"hello", "hi"};
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 136))
    def test286(self):
        input = """float = 10.2;"""
        expect = """Error on line 1 col 0: float"""
        self.assertTrue(TestParser.test(input, expect, 137))
    def test287(self):
        input = """auto : integer = 1;"""
        expect = """Error on line 1 col 0: auto"""
        self.assertTrue(TestParser.test(input, expect, 138))
    def test288(self):
        input = """ a + b = c"""
        expect = """Error on line 1 col 3: +"""
        self.assertTrue(TestParser.test(input, expect, 139))
    def test289(self):
        input = """main: function void() {if (n == 0) printString("Hello");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 140))

    def test293(self):
        input = """test :function integer(inherit n:integer, out m: integer) inherit test1 {
            m = 0;
            return 0;
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 141))
    def test294(self):
        input = """main: function void() inherit test {
            a = super(b,c);
            printInteger(a);
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 142))
    def test295(self):
        input = """main: function void() {
            printBoolean(a && b);
            printBoolean(a || b); 
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 143))
    def test296(self):
        input = """main: function void() {}
        //Test linecomment !@#$%^&*()"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 144))
    def test297(self):
        input = """main: function void() {
            //Test line comment !@#$%^&*()
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 145))


    def test_parser_234(self):
        input = """foo: function void (in: integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 146))

    def test_parser_235(self):
        input = """foo: function void (x: integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 147))

    def test_parser_236(self):
        input = """foo: function boolean (x) {}"""
        expect = "Error on line 1 col 24: )"
        self.assertTrue(TestParser.test(input, expect, 148))

    def test_parser_262(self):
        input = """foo: function integer(x: integer) {
                z: integer;
                z = x + 1;
                return z;
            }
            bar: function float(y: float) {
                z: float;
                z = y * 2.0;
                return z;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 149))

    def test_parser_263(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3)
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "Error on line 11 col 12: inc"
        self.assertTrue(TestParser.test(input, expect, 150))

    def test_parser_264(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta)
            delta = delta / 4;
        }"""
        expect = "Error on line 12 col 12: delta"
        self.assertTrue(TestParser.test(input, expect, 151))

    def test_parser_265(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "Error on line 4 col 12: else"
        self.assertTrue(TestParser.test(input, expect, 152))

    def test_parser_266(self):
        input = """x: integer = 10;
        y: integer = 20;
        z: integer = 30;
        main: function void() {
            foo();
            bar();
            baz();
        }
        foo: function void() {
            x = y + z;
        }
        bar: function void() {
            y = x + z;
        }
        baz: function void() {
            z = x + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 153))

    def test_parser_267(self):
        input = """x: integer = 10; // This is x
        y: integer = 20; // This is y
        z: integer = 30; // This is z
        main: function void() {
            // This is a comment
            foo(); // Call foo
            bar(); // Call bar
            baz(); // Call baz
        }
        foo: function void() {
            x = y + z;
        }
        bar: function void() {
            y = x + z;
        }
        baz: function void() {
            z = x + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 154))

    

    def test_parser_282(self):
        input = """isEven:function boolean(n: integer) {
            return (n % 2 == 0) && (n > 0);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 155))

    def test_parser_283(self):
        input = """swap: function void(a: integer,  b:integer) {
            temp = a;
            a = b;
            b = temp;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 156))

    def test_parser_284(self):
        input = """x: integer = 10;
        y: integer = 20;
        z: integer = 30;
        foo: function integer (a: integer, b: integer, c: integer) {
            return a + b * c;
        }
        bar: function integer (n: integer) {
            return foo(x, y, z) + n;
        }
        main: function void() {
            printIntLn(bar(5));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 157))

    def test_parser_285(self):
        input = """foo: function boolean (a: boolean, b: boolean) {
            return (a || b) && (! a || b);
        }
        bar: function boolean (n: integer) {
            return (n > 0) && (n < 10);
        }
        main: function void() {
            printBoolLn(foo(true, false) || bar(5));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 158))

    def test_parser_286(self):
        input = """x: integer = 5;
        y: integer = 10;
        foo: function integer (a: integer, b: integer) {
            return a + b * (a - b);
        }
        bar: function boolean (n: integer) {
            return (n > 0) && (n < 10);
        }
        main: function void() {
            z: integer = foo(x + y, y - x) * 2 - 5;
            printIntLn(z);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 159))

    def test_parser_287(self):
        input = """x: integer = 10;
        y: integer = 20;
        z: integer = 30;
        foo: function integer (a: integer, b: integer) {
            if (a > b) return a;
            else return b;
        }
        bar: function boolean (n: integer) {
            return (n >= x) && (n <= z);
        }
        main: function void() {
            if (bar(y)) print("y is in range");
            else print("y is out of range");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 160))

    def test_parser_288(self):
        input = """x: integer = 4;
        while (x <= 10) {
            sum = sum + x * 2;
            x = x + 1;
        }
        printIntLn(sum);
        """
        expect = "Error on line 2 col 8: while"
        self.assertTrue(TestParser.test(input, expect, 161))

    def test_parser_289(self):
        input = """
            foo: function float (a: integer, b: float) inherit bar {
                a = 5;
                b = 3 * 5;
                if (3 > 5) c = 123.123;
                if( true && false) {d = a + b;} else {d = a;}
                for(i = 1, i < 10, i + 1) {writeInt(i);}
                while(a>= b) a = a - b;
                do {a = a + 1;} while (a < 100);
                return a + b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 162))
     
    def test238(self):
        input = """main: function void(){
            a,b,c: integer = 10, 20 ,30;
            d: integer = a*b+c;
            printInteger(d);
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 163))
   
    def test_202(self):
        input = """
        x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 164))

    def test_203(self):
        input = """
            a: integer = 65;
            main: function void() {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 165))

    def test_204(self):
        input = """
            a: integer = 65, 66;
            main: function void() {}
        """
        expect = "Error on line 2 col 27: ,"
        self.assertTrue(TestParser.test(input, expect, 166))

    def test_205(self):
        input = """
            a,b: integer = 65;
            main: function void() {}
        """
        expect = "Error on line 2 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 167))

    def test_206(self):
        input = """
            inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 168))

    def test_207(self):
        input = """
            main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 169))

    def test_208(self):
        input = """
            fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 170))

    def test_209(self):
        input = """
            x,y,z: integer = 3+2, 4+double(2,3), 6*square(1,2);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 171))

    def test_210(self):
        input = """
            a:array [2] of integer;
            b:function array [2] of integer(){return a;}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 172))


    

    def test_214(self):
        input = """
            test: function integer()
            {
                i:integer=1;
                do
                {
                    r, s: integer;
                    i=i+1;
                }
                while(i<10);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 173))
        
    
    def test_279(self):
        input = """
            main:function void(){
                while(true)
                {
                    printString("May cua ban da bi hack");
                }
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 174))

    def test_280(self):
        input = """
            main:function void(){
                do
                {
                    printString("May cua ban da bi hack");
                }
                while(true);
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 175))

    def test_281(self):
        input = """
            main:function void(){
                for(i=1,i>0,i+1)
                    printString("May cua ban da bi hack");
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 176))

    def test_282(self):
        input = """
            main:function integer(){
                x,y,z:float=1.5,2e4,.e3;
                a:integer=5;
                return a-x;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 177))

    def test_284(self):
        input = """
            main:function integer() inherit b{
                x,y,z:float=1.5,2e4,.e3;
                a:integer=5;
                return super(1,2);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 178))

    def test_285(self):
        input = """
            main:function integer(inherit a:integer) inherit b{
                x,y,z:float=1.5,2e4,.e3;
                return super(1,2);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 179))

    def test_286(self):
        input = """
            main:function integer(inherit a:integer) inherit super_B{
                x,y,z:float=1.5,2e4,.e3;
                return super(x,y*z);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 180))

   

    def test_288(self):
        input = """
            Add:function integer(a:float, b:float)
            {
                return a+b;
            }
            main: function integer()inherit Add{
                return super(3.5,2e3);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 181))

    def test_289(self):
        input = """
            Sub:function integer(a:float, b:float)
            {
                return a-b;
            }
            main: function float(a:float,b:float)inherit Sub{
                return super(a,b);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 182))

 
    def test_293(self):
        input = """
            square:function integer(a:integer)
            {
                return a*a;
            }
            main:function void()
            {
                a:integer=square(5);//Binh phuong cua 5
                printInteger(a);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 183))

    def test_294(self):
        input = """
            x,y,z: integer = 3, 4, 6;
            /*
                Comment Multi;
            */
            // Comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 184))

    def test_295(self):
        input = """
           a,b,c:float=2.5,2e3,.e10;
            /*
                Comment Multi;
            */
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 185))

    def test_296(self):
        input = """
            x,y,z: integer = 3, 4, 6;
            /*
            Div:function integer(a:float, b:float)
            {
                return a/b;
            }
            Sub:function integer(a:float, b:float)
            {
                return a-b;
            }*/
            main:function integer(inherit a:integer) inherit b{
                a:integer=4;//Comment comment
                x,y,z:float=1.5,2e4,.e3;
                return super(1,2);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 186))

    
    def test_298(self):
        input = """
        a : boolean = true;
        inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) {
            n = n + delta;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 187))

    def test_299(self):
        input = """
                x: integer = 323;
                n: integer = 123;
                s1 : string = "dinh";
                s2 : string = "qua";
                s3 : string = "mon";
                inc: function void(out n: integer, delta: integer) {
                    n = n + delta;
                }
                main: function void() {
                    uranus : string = s1 :: s2;
                    if (n != 65) return;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 188))

    
    def test223(self):
        input = """int: integer = 100;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            return 5;
            inc(x);
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 189))

    def test224(self):
        input = """
        x: integer = 65;
        y: float = 1e10;
        fact: function integer (n: integer) {
            if (n == 0) return 1; 
            else return n * fact(n - 1);
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 190))
    
    

    def test_complex_34(self):
        input = """func: function integer(a: integer, b: integer) {
                    result = 1;
                    for (i = a, i <= b, i + 1) {
                        result = result * i;
                    }
                    return result;
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 191))

    def test_complex_26(self):
        input = """func: function void() {
            a = 2;
            b = 3;
            if (a > b) {
                writeString("a is greater than b");
            } else if (a < b) {
                writeString("a is less than b");
            } else {
                writeString("a is equal to b");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 192))

    def test_complex_27(self):
        input = """func: function void() {
            i = 0;
            while (i < 10) {
                if (i == 5) {
                    break;
                }
                writeInt(i);
                i = i + 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 193))

    
    def test249(self):
        input = """main: function void() {
        n1, n2, max: integer;
        readInteger(n1,n2);
        if (n1>n2) max = n1;
        else max = n2;
        return 0;
        } """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 194))
    def test250(self):
        input = """main: function void() {
        do {
        if ( (max % n1 == 0) && (max % n2 == 0) )
            {
                print("LCM = ");
                printInteger(max);
                break;
            }
        else max = max +1;
        } while (true);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 195))
    def test251(self):
        input = """main: function void() {
            max: integer;
            for (i=0, i<10, i + 1) {
                max = max + i;
            }
            printInteger(max);
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 196))
    def test252(self):
        input = """main: function void(){
            while (a>b) {
                while (b<c) 
                    b = b + 1;         
                break;
            }
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 197))
    def test253(self):
        input = """main: function void(){
            while (a!=b){
                writeInteger(a);
                a = a + 1;
                }
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 198))
    def test254(self):
        input = """main: function void()[]"""
        expect = """Error on line 1 col 21: ["""
        self.assertTrue(TestParser.test(input, expect, 199))
    def test255(self):
        input = """main: function string(){
            for (i = 2, i!=100, i+1)  
                if ((a+b)>(c+d))  
                    return "Something\\"Just Like This\\n"; 
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 200))
    def test256(self):
        input = """main: function integer(){a = "abc"::"bcd";}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 201))
    def test257(self):
        input = """main: function integer(){printString("Hello World")}"""
        expect = """Error on line 1 col 51: }"""
        self.assertTrue(TestParser.test(input, expect, 202))
    def test258(self):
        input = """main: function void(){
            while (x != 10){
                x = x + 1;
                if (x > 10) break;
            }
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 203))
    def test259(self):
        input = """main: function void() {
            a: integer;
            readInteger(a);
            if (a%2 ==0) printString("Even");
            else printString("Odd");
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 204))
 
    