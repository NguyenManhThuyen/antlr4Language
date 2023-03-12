import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_1(self):
        self.assertTrue(TestLexer.test("123.456", "123.456,<EOF>", 1))

    def test_2(self):
        self.assertTrue(TestLexer.test("1e1", "1e1,<EOF>", 2))

    def test_3(self):
        self.assertTrue(TestLexer.test(".1", ".,1,<EOF>", 3))
        
    def test_4(self):
        self.assertTrue(TestLexer.test("1.1e1", "1.1e1,<EOF>", 4))

    def test_5(self):
        self.assertTrue(TestLexer.test("1.23e456", "1.23e456,<EOF>", 5))

    def test_6(self):
        self.assertTrue(TestLexer.test("12300", "12300,<EOF>", 6))

    def test_7(self):
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 7))

    def test_8(self):
        self.assertTrue(TestLexer.test("_123", "_123,<EOF>", 8))

    def test_9(self):
        self.assertTrue(TestLexer.test("123_", "123,_,<EOF>", 9))
        

    def test_10(self):
        self.assertTrue(TestLexer.test("x y z", "x,y,z,<EOF>", 10))

    def test_11(self):
        self.assertTrue(TestLexer.test("0 1 2 3 4", "0,1,2,3,4,<EOF>", 11))

    def test_12(self):
        self.assertTrue(TestLexer.test(
            "10 20 30 40", "10,20,30,40,<EOF>", 12))

    def test_13(self):
        self.assertTrue(TestLexer.test("1.0 2.5 3.1415 100.123",
                        "1.0,2.5,3.1415,100.123,<EOF>", 13))

    def test_14(self):
        self.assertTrue(TestLexer.test("1abc", "1,abc,<EOF>", 14))

    def test_15(self):
        self.assertTrue(TestLexer.test("_abc", "_abc,<EOF>", 15))

    def test_16(self):
        self.assertTrue(TestLexer.test("a%bc", "a,%,bc,<EOF>", 16))

    def test_17(self):
        self.assertTrue(TestLexer.test("a.bc", "a,.,bc,<EOF>", 17))

    def test_18(self):
        self.assertTrue(TestLexer.test("ab+c", "ab,+,c,<EOF>", 18))

    def test_19(self):
        self.assertTrue(TestLexer.test("a^bc", "a,Error Token ^", 19))

    def test_20(self):
        self.assertTrue(TestLexer.test("a_bc", "a_bc,<EOF>", 20))

    def test_21(self):
        self.assertTrue(TestLexer.test("if a == b: pass",
                        "if,a,==,b,:,pass,<EOF>", 21))

    def test_22(self):
        self.assertTrue(TestLexer.test("if a == b: pass\nelse: pass",
                        "if,a,==,b,:,pass,else,:,pass,<EOF>", 22))

    def test_23(self):
        self.assertTrue(TestLexer.test("do while", "do,while,<EOF>", 23))

    def test_24(self):
        self.assertTrue(TestLexer.test("a + b", "a,+,b,<EOF>", 24))

    def test_25(self):
        self.assertTrue(TestLexer.test("a * b", "a,*,b,<EOF>", 25))

    def test_26(self):
        self.assertTrue(TestLexer.test("a = b", "a,=,b,<EOF>", 26))

    def test_27(self):
        self.assertTrue(TestLexer.test("a == b", "a,==,b,<EOF>", 27))

    def test_28(self):
        self.assertTrue(TestLexer.test("a != b", "a,!=,b,<EOF>", 28))

    def test_29(self):
        self.assertTrue(TestLexer.test("a < b", "a,<,b,<EOF>", 29))

    def test_30(self):
        self.assertTrue(TestLexer.test("a <= b", "a,<=,b,<EOF>", 30))

    def test_31(self):
        self.assertTrue(TestLexer.test("a > b", "a,>,b,<EOF>", 31))

    def test_32(self):
        self.assertTrue(TestLexer.test("a >= b", "a,>=,b,<EOF>", 32))

    def test_33(self):
        self.assertTrue(TestLexer.test("a and b", "a,and,b,<EOF>", 33))

    def test_34(self):
        self.assertTrue(TestLexer.test("a or b", "a,or,b,<EOF>", 34))

    def test_35(self):
        self.assertTrue(TestLexer.test("not a", "not,a,<EOF>", 35))

    def test_36(self):
        self.assertTrue(TestLexer.test("( a + b )", "(,a,+,b,),<EOF>", 36))
  
    def test_37(self):
        self.assertTrue(TestLexer.test("a, b, c", "a,,,b,,,c,<EOF>", 37))

    def test_38(self):
        self.assertTrue(TestLexer.test("if a == b: pass",
                        "if,a,==,b,:,pass,<EOF>", 38))

    def test_39(self):
        self.assertTrue(TestLexer.test("a = b; print(a)",
                        "a,=,b,;,print,(,a,),<EOF>", 39))
        
    def test_40(self):
        self.assertTrue(TestLexer.test(",", ",,<EOF>", 40))

    def test_41(self):
        self.assertTrue(TestLexer.test(";", ";,<EOF>", 41))

    def test_42(self):
        self.assertTrue(TestLexer.test(":", ":,<EOF>", 42))

    def test_43(self):
        self.assertTrue(TestLexer.test("(", "(,<EOF>", 43))

    def test_44(self):
        self.assertTrue(TestLexer.test(")", "),<EOF>", 44))

    def test_45(self):
        self.assertTrue(TestLexer.test(
            "{ } [ ] ( )", "{,},[,],(,),<EOF>", 45))

    def test_46(self):
        self.assertTrue(TestLexer.test("({})[]", "(,{,},),[,],<EOF>", 46))

    def test_47(self):
        self.assertTrue(TestLexer.test("{", "{,<EOF>", 47))

    def test_48(self):
        self.assertTrue(TestLexer.test("}", "},<EOF>", 48))

    def test_49(self):
        self.assertTrue(TestLexer.test(",", ",,<EOF>", 49))

    def test_50(self):
        self.assertTrue(TestLexer.test(
            "/* this is a comment */", "<EOF>", 50))

    def test_51(self):
        self.assertTrue(TestLexer.test(
            "/* this is a\nmulti-line\ncomment */", "<EOF>", 51))

    def test_52(self):
        self.assertTrue(TestLexer.test("// this is a comment", "<EOF>", 52))

    def test_53(self):
        self.assertTrue(TestLexer.test(
            "// this is a comment\na=5", "a,=,5,<EOF>", 53))

    def test_54(self):
        self.assertTrue(TestLexer.test(
            "a=5// this is a comment\nb=6", "a,=,5,b,=,6,<EOF>", 54))

    def test_55(self):
        self.assertTrue(TestLexer.test(
            "// this is not a comment", "<EOF>", 55))
 
    def test_56(self):
        self.assertTrue(TestLexer.test(
            "a=5; // this is a comment\nb=6", "a,=,5,;,b,=,6,<EOF>", 56))

    def test_57(self):
        self.assertTrue(TestLexer.test(
            "a=5; /* this is a\nmulti-line\ncomment */ b=6", "a,=,5,;,b,=,6,<EOF>", 57))

    def test_58(self):
        self.assertTrue(TestLexer.test(
            "// this is a comment\n/* this is a comment */\na=5; b=6", "a,=,5,;,b,=,6,<EOF>", 58))


    def test_59(self):
        self.assertTrue(TestLexer.test(
            "a=5;// this is a comment", "a,=,5,;,<EOF>", 59))

    def test_60(self):
        self.assertTrue(TestLexer.test(
            "a=5/* this is a comment */", "a,=,5,<EOF>", 60))

    def test_61(self):
        self.assertTrue(TestLexer.test("1 + 2 - 3", "1,+,2,-,3,<EOF>", 61))

    def test_62(self):
        self.assertTrue(TestLexer.test("x < y", "x,<,y,<EOF>", 62))

    def test_63(self):
        self.assertTrue(TestLexer.test("x > y", "x,>,y,<EOF>", 63))

    def test_64(self):
        self.assertTrue(TestLexer.test("x <= y", "x,<=,y,<EOF>", 64))
        
  
    def test_65(self):
        self.assertTrue(TestLexer.test('firstName', 'firstName,<EOF>', 65))

    def test_66(self):
        self.assertTrue(TestLexer.test('_age', '_age,<EOF>', 66))

    def test_67(self):
        self.assertTrue(TestLexer.test(
            'userDetails23', 'userDetails23,<EOF>', 67))

    def test_68(self):
        self.assertTrue(TestLexer.test('WriteLn', 'WriteLn,<EOF>', 68))

  
    def test_69(self):
        self.assertTrue(TestLexer.test('user_name1', 'user_name1,<EOF>', 69))

    def test_70(self):
        self.assertTrue(TestLexer.test('$user', 'Error Token $', 70))

    def test_71(self):
        self.assertTrue(TestLexer.test('user#123', 'user,Error Token #', 71))

    def test_72(self):
        self.assertTrue(TestLexer.test('1234', '1234,<EOF>', 72))

    def test_73(self):
        self.assertTrue(TestLexer.test('1_72', '172,<EOF>', 73))

    def test_74(self):
        self.assertTrue(TestLexer.test('1_234_567', '1234567,<EOF>', 74))

    def test_75(self):
        self.assertTrue(TestLexer.test('12_34', '1234,<EOF>', 75))

    def test_76(self):
        self.assertTrue(TestLexer.test('12__34', '12,__34,<EOF>', 76))

    def test_77(self):
        self.assertTrue(TestLexer.test('2352_', '2352,_,<EOF>', 77))

    def test_78(self):
        self.assertTrue(TestLexer.test('1_23_', '123,_,<EOF>', 78))

    def test_79(self):
        self.assertTrue(TestLexer.test('_12_3', '_12_3,<EOF>', 79))

    def test_80(self):
        self.assertTrue(TestLexer.test('123_', '123,_,<EOF>', 80))

    def test_81(self):
        self.assertTrue(TestLexer.test('1.2e3', '1.2e3,<EOF>', 81))

    def test_82(self):
        self.assertTrue(TestLexer.test('1.2e-3', '1.2e-3,<EOF>', 82))

    def test_83(self):
        self.assertTrue(TestLexer.test('1.2E3', '1.2E3,<EOF>', 83))

    def test_84(self):
        self.assertTrue(TestLexer.test('7E-10', '7E-10,<EOF>', 84))

    def test_85(self):
        self.assertTrue(TestLexer.test('""', ',<EOF>', 85))

    def test_86(self):
        self.assertTrue(TestLexer.test('" "', ' ,<EOF>', 86))

    def test_87(self):
        self.assertTrue(TestLexer.test(
            '"Hello, World!"', 'Hello, World!,<EOF>', 87))

    def test_88(self):
        self.assertTrue(TestLexer.test(
            '"HELLO, WORLD!"', 'HELLO, WORLD!,<EOF>', 88))

    def test_89(self):
        self.assertTrue(TestLexer.test('"The quick brown fox jumps over the lazy dog"',
                        'The quick brown fox jumps over the lazy dog,<EOF>', 89))

    def test_90(self):
        self.assertTrue(TestLexer.test('"1234"', '1234,<EOF>', 90))

    def test_91(self):
        self.assertTrue(TestLexer.test(
            '"thuyen dep trai"', 'thuyen dep trai,<EOF>', 91))

    def test_92(self):
        self.assertTrue(TestLexer.test(
            '"Hello World"', 'Hello World,<EOF>', 92))

    def test_93(self):
        self.assertTrue(TestLexer.test(
            '"Line 1\\fLine 2"', 'Line 1\\fLine 2,<EOF>', 93))

    def test_94(self):
        self.assertTrue(TestLexer.test(
            '"Line 1\\rLine 2"', 'Line 1\\rLine 2,<EOF>', 94))
   
    def test_95(self):
        self.assertTrue(TestLexer.test('"Line 1\\\\Line 2"',
                        'Line 1\\\\Line 2,<EOF>', 95))

    def test_96(self):
        self.assertTrue(TestLexer.test('"He asked me: \\"Where is \\"John?\\""',
                        'He asked me: \\"Where is \\"John?\\",<EOF>', 96))

    def test_97(self):
        self.assertTrue(TestLexer.test('"Line 1\\tLine 2\\nLine 3\\bLine 4"',
                        'Line 1\\tLine 2\\nLine 3\\bLine 4,<EOF>', 97))

    def test_98(self):
        self.assertTrue(TestLexer.test('a, b, c: integer = 3, 4,6;',
                        'a,,,b,,,c,:,integer,=,3,,,4,,,6,;,<EOF>', 98))

    def test_99(self):
        self.assertTrue(TestLexer.test('main: function void () {}',
                        'main,:,function,void,(,),{,},<EOF>', 99))
        
    def test_100(self):
        self.assertTrue(TestLexer.test(']', '],<EOF>', 100))

