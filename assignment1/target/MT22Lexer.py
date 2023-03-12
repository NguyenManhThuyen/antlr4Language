# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01de\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\5\2\u008c\n\2\3\3\3\3\7\3\u0090\n\3\f")
        buf.write("\3\16\3\u0093\13\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7\3\7")
        buf.write("\5\7\u009e\n\7\3\7\6\7\u00a1\n\7\r\7\16\7\u00a2\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\7\n\u00ab\n\n\f\n\16\n\u00ae\13\n\3")
        buf.write("\n\5\n\u00b1\n\n\3\n\7\n\u00b4\n\n\f\n\16\n\u00b7\13\n")
        buf.write("\3\n\5\n\u00ba\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5")
        buf.write("\13\u00c3\n\13\3\13\3\13\3\13\3\13\3\13\5\13\u00ca\n\13")
        buf.write("\3\13\3\13\3\f\3\f\5\f\u00d0\n\f\3\r\3\r\7\r\u00d4\n\r")
        buf.write("\f\r\16\r\u00d7\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3.\3.\7.\u0172\n.\f.\16.\u0175")
        buf.write("\13.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("8\39\39\3:\3:\3:\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\6")
        buf.write("?\u019f\n?\r?\16?\u01a0\3?\3?\3@\3@\3@\3@\7@\u01a9\n@")
        buf.write("\f@\16@\u01ac\13@\3@\3@\3@\3@\3@\3A\3A\7A\u01b5\nA\fA")
        buf.write("\16A\u01b8\13A\3A\3A\3B\3B\7B\u01be\nB\fB\16B\u01c1\13")
        buf.write("B\3B\5B\u01c4\nB\3B\3B\3C\3C\7C\u01ca\nC\fC\16C\u01cd")
        buf.write("\13C\3C\3C\3C\3C\3C\3D\3D\3D\6D\u01d7\nD\rD\16D\u01d8")
        buf.write("\5D\u01db\nD\3D\3D\3\u01aa\2E\3\2\5\2\7\2\t\2\13\2\r\2")
        buf.write("\17\2\21\2\23\3\25\4\27\5\31\6\33\7\35\b\37\t!\n#\13%")
        buf.write("\f\'\r)\16+\17-\20/\21\61\22\63\23\65\24\67\259\26;\27")
        buf.write("=\30?\31A\32C\33E\34G\35I\36K\37M O!Q\"S#U$W%Y&[\'](_")
        buf.write(")a*c+e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67}8\1779\u0081")
        buf.write(":\u0083;\u0085<\u0087=\3\2\16\6\2\n\f\16\17$$^^\3\2\62")
        buf.write(";\t\2$$^^ddhhppttvv\4\2GGgg\4\2--//\5\2C\\aac|\3\2\63")
        buf.write(";\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\4\2\f\f\17\17\7\3")
        buf.write("\n\f\16\17$$))^^\t\2))^^ddhhppttvv\2\u01ea\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u008b\3\2\2")
        buf.write("\2\5\u008d\3\2\2\2\7\u0094\3\2\2\2\t\u0096\3\2\2\2\13")
        buf.write("\u0098\3\2\2\2\r\u009b\3\2\2\2\17\u00a4\3\2\2\2\21\u00a6")
        buf.write("\3\2\2\2\23\u00b9\3\2\2\2\25\u00c9\3\2\2\2\27\u00cf\3")
        buf.write("\2\2\2\31\u00d1\3\2\2\2\33\u00db\3\2\2\2\35\u00e0\3\2")
        buf.write("\2\2\37\u00e2\3\2\2\2!\u00e4\3\2\2\2#\u00e6\3\2\2\2%\u00e8")
        buf.write("\3\2\2\2\'\u00ea\3\2\2\2)\u00ec\3\2\2\2+\u00ee\3\2\2\2")
        buf.write("-\u00f0\3\2\2\2/\u00f2\3\2\2\2\61\u00f4\3\2\2\2\63\u00fa")
        buf.write("\3\2\2\2\65\u00ff\3\2\2\2\67\u0107\3\2\2\29\u010d\3\2")
        buf.write("\2\2;\u0116\3\2\2\2=\u0119\3\2\2\2?\u011e\3\2\2\2A\u0124")
        buf.write("\3\2\2\2C\u012a\3\2\2\2E\u012e\3\2\2\2G\u0137\3\2\2\2")
        buf.write("I\u013a\3\2\2\2K\u0142\3\2\2\2M\u014a\3\2\2\2O\u014d\3")
        buf.write("\2\2\2Q\u0151\3\2\2\2S\u0158\3\2\2\2U\u015f\3\2\2\2W\u0164")
        buf.write("\3\2\2\2Y\u0169\3\2\2\2[\u016f\3\2\2\2]\u0176\3\2\2\2")
        buf.write("_\u0178\3\2\2\2a\u017a\3\2\2\2c\u017c\3\2\2\2e\u017e\3")
        buf.write("\2\2\2g\u0180\3\2\2\2i\u0182\3\2\2\2k\u0185\3\2\2\2m\u0188")
        buf.write("\3\2\2\2o\u018a\3\2\2\2q\u018d\3\2\2\2s\u018f\3\2\2\2")
        buf.write("u\u0192\3\2\2\2w\u0194\3\2\2\2y\u0197\3\2\2\2{\u019a\3")
        buf.write("\2\2\2}\u019e\3\2\2\2\177\u01a4\3\2\2\2\u0081\u01b2\3")
        buf.write("\2\2\2\u0083\u01bb\3\2\2\2\u0085\u01c7\3\2\2\2\u0087\u01da")
        buf.write("\3\2\2\2\u0089\u008c\n\2\2\2\u008a\u008c\5\13\6\2\u008b")
        buf.write("\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\4\3\2\2\2\u008d")
        buf.write("\u0091\7\60\2\2\u008e\u0090\t\3\2\2\u008f\u008e\3\2\2")
        buf.write("\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\6\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095")
        buf.write("\t\3\2\2\u0095\b\3\2\2\2\u0096\u0097\7$\2\2\u0097\n\3")
        buf.write("\2\2\2\u0098\u0099\7^\2\2\u0099\u009a\t\4\2\2\u009a\f")
        buf.write("\3\2\2\2\u009b\u009d\t\5\2\2\u009c\u009e\t\6\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a0\3\2\2\2")
        buf.write("\u009f\u00a1\t\3\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a2\3")
        buf.write("\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\16")
        buf.write("\3\2\2\2\u00a4\u00a5\t\7\2\2\u00a5\20\3\2\2\2\u00a6\u00a7")
        buf.write("\t\b\2\2\u00a7\22\3\2\2\2\u00a8\u00ac\5\21\t\2\u00a9\u00ab")
        buf.write("\5\7\4\2\u00aa\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00b5\3\2\2\2")
        buf.write("\u00ae\u00ac\3\2\2\2\u00af\u00b1\7a\2\2\u00b0\u00af\3")
        buf.write("\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4")
        buf.write("\5\7\4\2\u00b3\u00b0\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00ba\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b8\u00ba\7\62\2\2\u00b9\u00a8")
        buf.write("\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write("\u00bc\b\n\2\2\u00bc\24\3\2\2\2\u00bd\u00be\5\23\n\2\u00be")
        buf.write("\u00bf\5\5\3\2\u00bf\u00ca\3\2\2\2\u00c0\u00c2\5\23\n")
        buf.write("\2\u00c1\u00c3\5\5\3\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\5\r\7\2\u00c5")
        buf.write("\u00ca\3\2\2\2\u00c6\u00c7\5\5\3\2\u00c7\u00c8\5\r\7\2")
        buf.write("\u00c8\u00ca\3\2\2\2\u00c9\u00bd\3\2\2\2\u00c9\u00c0\3")
        buf.write("\2\2\2\u00c9\u00c6\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc")
        buf.write("\b\13\3\2\u00cc\26\3\2\2\2\u00cd\u00d0\5U+\2\u00ce\u00d0")
        buf.write("\5? \2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\30")
        buf.write("\3\2\2\2\u00d1\u00d5\5\t\5\2\u00d2\u00d4\5\3\2\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2")
        buf.write("\u00d5\u00d6\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3")
        buf.write("\2\2\2\u00d8\u00d9\5\t\5\2\u00d9\u00da\b\r\4\2\u00da\32")
        buf.write("\3\2\2\2\u00db\u00dc\7d\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de")
        buf.write("\7q\2\2\u00de\u00df\7n\2\2\u00df\34\3\2\2\2\u00e0\u00e1")
        buf.write("\7*\2\2\u00e1\36\3\2\2\2\u00e2\u00e3\7+\2\2\u00e3 \3\2")
        buf.write("\2\2\u00e4\u00e5\7]\2\2\u00e5\"\3\2\2\2\u00e6\u00e7\7")
        buf.write("_\2\2\u00e7$\3\2\2\2\u00e8\u00e9\7\60\2\2\u00e9&\3\2\2")
        buf.write("\2\u00ea\u00eb\7.\2\2\u00eb(\3\2\2\2\u00ec\u00ed\7=\2")
        buf.write("\2\u00ed*\3\2\2\2\u00ee\u00ef\7<\2\2\u00ef,\3\2\2\2\u00f0")
        buf.write("\u00f1\7}\2\2\u00f1.\3\2\2\2\u00f2\u00f3\7\177\2\2\u00f3")
        buf.write("\60\3\2\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7t\2\2\u00f6")
        buf.write("\u00f7\7t\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7{\2\2\u00f9")
        buf.write("\62\3\2\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7w\2\2\u00fc")
        buf.write("\u00fd\7v\2\2\u00fd\u00fe\7q\2\2\u00fe\64\3\2\2\2\u00ff")
        buf.write("\u0100\7d\2\2\u0100\u0101\7q\2\2\u0101\u0102\7q\2\2\u0102")
        buf.write("\u0103\7n\2\2\u0103\u0104\7g\2\2\u0104\u0105\7c\2\2\u0105")
        buf.write("\u0106\7p\2\2\u0106\66\3\2\2\2\u0107\u0108\7d\2\2\u0108")
        buf.write("\u0109\7t\2\2\u0109\u010a\7g\2\2\u010a\u010b\7c\2\2\u010b")
        buf.write("\u010c\7m\2\2\u010c8\3\2\2\2\u010d\u010e\7e\2\2\u010e")
        buf.write("\u010f\7q\2\2\u010f\u0110\7p\2\2\u0110\u0111\7v\2\2\u0111")
        buf.write("\u0112\7k\2\2\u0112\u0113\7p\2\2\u0113\u0114\7w\2\2\u0114")
        buf.write("\u0115\7g\2\2\u0115:\3\2\2\2\u0116\u0117\7f\2\2\u0117")
        buf.write("\u0118\7q\2\2\u0118<\3\2\2\2\u0119\u011a\7g\2\2\u011a")
        buf.write("\u011b\7n\2\2\u011b\u011c\7u\2\2\u011c\u011d\7g\2\2\u011d")
        buf.write(">\3\2\2\2\u011e\u011f\7h\2\2\u011f\u0120\7c\2\2\u0120")
        buf.write("\u0121\7n\2\2\u0121\u0122\7u\2\2\u0122\u0123\7g\2\2\u0123")
        buf.write("@\3\2\2\2\u0124\u0125\7h\2\2\u0125\u0126\7n\2\2\u0126")
        buf.write("\u0127\7q\2\2\u0127\u0128\7c\2\2\u0128\u0129\7v\2\2\u0129")
        buf.write("B\3\2\2\2\u012a\u012b\7h\2\2\u012b\u012c\7q\2\2\u012c")
        buf.write("\u012d\7t\2\2\u012dD\3\2\2\2\u012e\u012f\7h\2\2\u012f")
        buf.write("\u0130\7w\2\2\u0130\u0131\7p\2\2\u0131\u0132\7e\2\2\u0132")
        buf.write("\u0133\7v\2\2\u0133\u0134\7k\2\2\u0134\u0135\7q\2\2\u0135")
        buf.write("\u0136\7p\2\2\u0136F\3\2\2\2\u0137\u0138\7k\2\2\u0138")
        buf.write("\u0139\7h\2\2\u0139H\3\2\2\2\u013a\u013b\7k\2\2\u013b")
        buf.write("\u013c\7p\2\2\u013c\u013d\7j\2\2\u013d\u013e\7g\2\2\u013e")
        buf.write("\u013f\7t\2\2\u013f\u0140\7k\2\2\u0140\u0141\7v\2\2\u0141")
        buf.write("J\3\2\2\2\u0142\u0143\7k\2\2\u0143\u0144\7p\2\2\u0144")
        buf.write("\u0145\7v\2\2\u0145\u0146\7g\2\2\u0146\u0147\7i\2\2\u0147")
        buf.write("\u0148\7g\2\2\u0148\u0149\7t\2\2\u0149L\3\2\2\2\u014a")
        buf.write("\u014b\7q\2\2\u014b\u014c\7h\2\2\u014cN\3\2\2\2\u014d")
        buf.write("\u014e\7q\2\2\u014e\u014f\7w\2\2\u014f\u0150\7v\2\2\u0150")
        buf.write("P\3\2\2\2\u0151\u0152\7t\2\2\u0152\u0153\7g\2\2\u0153")
        buf.write("\u0154\7v\2\2\u0154\u0155\7w\2\2\u0155\u0156\7t\2\2\u0156")
        buf.write("\u0157\7p\2\2\u0157R\3\2\2\2\u0158\u0159\7u\2\2\u0159")
        buf.write("\u015a\7v\2\2\u015a\u015b\7t\2\2\u015b\u015c\7k\2\2\u015c")
        buf.write("\u015d\7p\2\2\u015d\u015e\7i\2\2\u015eT\3\2\2\2\u015f")
        buf.write("\u0160\7v\2\2\u0160\u0161\7t\2\2\u0161\u0162\7w\2\2\u0162")
        buf.write("\u0163\7g\2\2\u0163V\3\2\2\2\u0164\u0165\7x\2\2\u0165")
        buf.write("\u0166\7q\2\2\u0166\u0167\7k\2\2\u0167\u0168\7f\2\2\u0168")
        buf.write("X\3\2\2\2\u0169\u016a\7y\2\2\u016a\u016b\7j\2\2\u016b")
        buf.write("\u016c\7k\2\2\u016c\u016d\7n\2\2\u016d\u016e\7g\2\2\u016e")
        buf.write("Z\3\2\2\2\u016f\u0173\t\7\2\2\u0170\u0172\t\t\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\\\3\2\2\2\u0175\u0173\3\2\2")
        buf.write("\2\u0176\u0177\7-\2\2\u0177^\3\2\2\2\u0178\u0179\7/\2")
        buf.write("\2\u0179`\3\2\2\2\u017a\u017b\7,\2\2\u017bb\3\2\2\2\u017c")
        buf.write("\u017d\7\61\2\2\u017dd\3\2\2\2\u017e\u017f\7\'\2\2\u017f")
        buf.write("f\3\2\2\2\u0180\u0181\7#\2\2\u0181h\3\2\2\2\u0182\u0183")
        buf.write("\7(\2\2\u0183\u0184\7(\2\2\u0184j\3\2\2\2\u0185\u0186")
        buf.write("\7~\2\2\u0186\u0187\7~\2\2\u0187l\3\2\2\2\u0188\u0189")
        buf.write("\7?\2\2\u0189n\3\2\2\2\u018a\u018b\7#\2\2\u018b\u018c")
        buf.write("\7?\2\2\u018cp\3\2\2\2\u018d\u018e\7>\2\2\u018er\3\2\2")
        buf.write("\2\u018f\u0190\7>\2\2\u0190\u0191\7?\2\2\u0191t\3\2\2")
        buf.write("\2\u0192\u0193\7@\2\2\u0193v\3\2\2\2\u0194\u0195\7@\2")
        buf.write("\2\u0195\u0196\7?\2\2\u0196x\3\2\2\2\u0197\u0198\7<\2")
        buf.write("\2\u0198\u0199\7<\2\2\u0199z\3\2\2\2\u019a\u019b\7?\2")
        buf.write("\2\u019b\u019c\7?\2\2\u019c|\3\2\2\2\u019d\u019f\t\n\2")
        buf.write("\2\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u019e")
        buf.write("\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a3\b?\5\2\u01a3~\3\2\2\2\u01a4\u01a5\7\61\2\2\u01a5")
        buf.write("\u01a6\7,\2\2\u01a6\u01aa\3\2\2\2\u01a7\u01a9\13\2\2\2")
        buf.write("\u01a8\u01a7\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01ab\3")
        buf.write("\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01aa")
        buf.write("\3\2\2\2\u01ad\u01ae\7,\2\2\u01ae\u01af\7\61\2\2\u01af")
        buf.write("\u01b0\3\2\2\2\u01b0\u01b1\b@\5\2\u01b1\u0080\3\2\2\2")
        buf.write("\u01b2\u01b6\7\61\2\2\u01b3\u01b5\n\13\2\2\u01b4\u01b3")
        buf.write("\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6")
        buf.write("\u01b7\3\2\2\2\u01b7\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2")
        buf.write("\u01b9\u01ba\bA\5\2\u01ba\u0082\3\2\2\2\u01bb\u01bf\7")
        buf.write("$\2\2\u01bc\u01be\5\3\2\2\u01bd\u01bc\3\2\2\2\u01be\u01c1")
        buf.write("\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c4\t\f\2\2")
        buf.write("\u01c3\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\b")
        buf.write("B\6\2\u01c6\u0084\3\2\2\2\u01c7\u01cb\7$\2\2\u01c8\u01ca")
        buf.write("\5\3\2\2\u01c9\u01c8\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb")
        buf.write("\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ce\3\2\2\2")
        buf.write("\u01cd\u01cb\3\2\2\2\u01ce\u01cf\7^\2\2\u01cf\u01d0\n")
        buf.write("\r\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2\bC\7\2\u01d2\u0086")
        buf.write("\3\2\2\2\u01d3\u01db\13\2\2\2\u01d4\u01d6\7\62\2\2\u01d5")
        buf.write("\u01d7\5\7\4\2\u01d6\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2")
        buf.write("\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01db\3")
        buf.write("\2\2\2\u01da\u01d3\3\2\2\2\u01da\u01d4\3\2\2\2\u01db\u01dc")
        buf.write("\3\2\2\2\u01dc\u01dd\bD\b\2\u01dd\u0088\3\2\2\2\30\2\u008b")
        buf.write("\u0091\u009d\u00a2\u00ac\u00b0\u00b5\u00b9\u00c2\u00c9")
        buf.write("\u00cf\u00d5\u0173\u01a0\u01aa\u01b6\u01bf\u01c3\u01cb")
        buf.write("\u01d8\u01da\t\3\n\2\3\13\3\3\r\4\b\2\2\3B\5\3C\6\3D\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT_LIT = 1
    FLOAT_LIT = 2
    BOOL_LIT = 3
    STRING_LIT = 4
    BOOL = 5
    LB = 6
    RB = 7
    LSB = 8
    RSB = 9
    DOT = 10
    COMMA = 11
    SEMI = 12
    COLON = 13
    LCB = 14
    RCB = 15
    ARRAY = 16
    AUTO = 17
    BOOLEAN = 18
    BREAK = 19
    CONTINUE = 20
    DO = 21
    ELSE = 22
    FALSE = 23
    FLOAT = 24
    FOR = 25
    FUNC = 26
    IF = 27
    INHERIT = 28
    INT = 29
    OF = 30
    OUT = 31
    RETURN = 32
    STR = 33
    TRUE = 34
    VOID = 35
    WHILE = 36
    ID = 37
    ADD = 38
    SUB = 39
    MUL = 40
    DIV = 41
    MOD = 42
    NOT = 43
    AND = 44
    OR = 45
    EQ = 46
    NOTEQ = 47
    LT = 48
    LTEQ = 49
    GT = 50
    GTEQ = 51
    COLONCOLON = 52
    EQEQ = 53
    WS = 54
    BlockComment = 55
    LINE_CMT = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    ERROR_CHAR = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'bool'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
            "'{'", "'}'", "'array'", "'auto'", "'boolean'", "'break'", "'continue'", 
            "'do'", "'else'", "'false'", "'float'", "'for'", "'function'", 
            "'if'", "'inherit'", "'integer'", "'of'", "'out'", "'return'", 
            "'string'", "'true'", "'void'", "'while'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "BOOL", "LB", 
            "RB", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "LCB", 
            "RCB", "ARRAY", "AUTO", "BOOLEAN", "BREAK", "CONTINUE", "DO", 
            "ELSE", "FALSE", "FLOAT", "FOR", "FUNC", "IF", "INHERIT", "INT", 
            "OF", "OUT", "RETURN", "STR", "TRUE", "VOID", "WHILE", "ID", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", 
            "NOTEQ", "LT", "LTEQ", "GT", "GTEQ", "COLONCOLON", "EQEQ", "WS", 
            "BlockComment", "LINE_CMT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "CHARLIT", "DECPART", "DIGIT", "DoubleQuote", "ESCAPE_SEQUENCE", 
                  "EXPPART", "NonDigit", "NonZDigit", "INT_LIT", "FLOAT_LIT", 
                  "BOOL_LIT", "STRING_LIT", "BOOL", "LB", "RB", "LSB", "RSB", 
                  "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", "ARRAY", 
                  "AUTO", "BOOLEAN", "BREAK", "CONTINUE", "DO", "ELSE", 
                  "FALSE", "FLOAT", "FOR", "FUNC", "IF", "INHERIT", "INT", 
                  "OF", "OUT", "RETURN", "STR", "TRUE", "VOID", "WHILE", 
                  "ID", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
                  "OR", "EQ", "NOTEQ", "LT", "LTEQ", "GT", "GTEQ", "COLONCOLON", 
                  "EQEQ", "WS", "BlockComment", "LINE_CMT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[8] = self.INT_LIT_action 
            actions[9] = self.FLOAT_LIT_action 
            actions[11] = self.STRING_LIT_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		self.text = self.text.replace("_","")
            	
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		self.text = self.text[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace('"','',1)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


