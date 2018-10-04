# Generated from /home/hungdao1311/Documents/PPL/assignment2/upload/src/main/mp/parser/MP.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u025b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\5\37\u010a\n\37\3")
        buf.write(" \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\39\39")
        buf.write("\39\39\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3@\3@\3A\3A\3A\3B\3B\3C\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3L\3M\3M\3N\3N\3")
        buf.write("N\3O\3O\3P\3P\7P\u01d7\nP\fP\16P\u01da\13P\3P\3P\3P\3")
        buf.write("Q\3Q\7Q\u01e1\nQ\fQ\16Q\u01e4\13Q\3Q\3Q\3Q\3Q\3R\3R\7")
        buf.write("R\u01ec\nR\fR\16R\u01ef\13R\3R\3R\3S\3S\7S\u01f5\nS\f")
        buf.write("S\16S\u01f8\13S\3T\6T\u01fb\nT\rT\16T\u01fc\3T\3T\3U\3")
        buf.write("U\3U\3U\7U\u0205\nU\fU\16U\u0208\13U\3U\3U\3U\3U\3U\3")
        buf.write("V\3V\7V\u0211\nV\fV\16V\u0214\13V\3V\3V\3V\3V\3W\3W\3")
        buf.write("W\3W\7W\u021e\nW\fW\16W\u0221\13W\3W\3W\3X\3X\3Y\3Y\5")
        buf.write("Y\u0229\nY\3Y\6Y\u022c\nY\rY\16Y\u022d\3Z\3Z\5Z\u0232")
        buf.write("\nZ\3[\3[\3[\3\\\6\\\u0238\n\\\r\\\16\\\u0239\3]\6]\u023d")
        buf.write("\n]\r]\16]\u023e\3]\3]\7]\u0243\n]\f]\16]\u0246\13]\3")
        buf.write("]\5]\u0249\n]\3]\5]\u024c\n]\3]\3]\6]\u0250\n]\r]\16]")
        buf.write("\u0251\3]\5]\u0255\n]\5]\u0257\n]\3^\3^\3^\4\u0206\u0212")
        buf.write("\2_\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2")
        buf.write("\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63")
        buf.write("\2\65\2\67\39\4;\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O\17Q\20")
        buf.write("S\21U\22W\23Y\24[\25]\26_\27a\30c\31e\32g\33i\34k\35m")
        buf.write("\36o\37q s!u\"w#y${%}&\177\'\u0081(\u0083)\u0085*\u0087")
        buf.write("+\u0089,\u008b-\u008d.\u008f/\u0091\60\u0093\61\u0095")
        buf.write("\62\u0097\63\u0099\64\u009b\65\u009d\66\u009f\67\u00a1")
        buf.write("8\u00a39\u00a5:\u00a7;\u00a9<\u00ab=\u00ad>\u00af\2\u00b1")
        buf.write("\2\u00b3\2\u00b5\2\u00b7?\u00b9@\u00bbA\3\2#\4\2CCcc\4")
        buf.write("\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJj")
        buf.write("j\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2")
        buf.write("QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4")
        buf.write("\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\n\2$$))^^ddh")
        buf.write("hppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\4")
        buf.write("\2\f\f\17\17\3\2\62;\6\2\f\f\17\17$$^^\2\u0250\2\67\3")
        buf.write("\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A")
        buf.write("\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2")
        buf.write("K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2")
        buf.write("\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2")
        buf.write("\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2")
        buf.write("\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3")
        buf.write("\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{")
        buf.write("\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2")
        buf.write("\2\3\u00bd\3\2\2\2\5\u00bf\3\2\2\2\7\u00c1\3\2\2\2\t\u00c3")
        buf.write("\3\2\2\2\13\u00c5\3\2\2\2\r\u00c7\3\2\2\2\17\u00c9\3\2")
        buf.write("\2\2\21\u00cb\3\2\2\2\23\u00cd\3\2\2\2\25\u00cf\3\2\2")
        buf.write("\2\27\u00d1\3\2\2\2\31\u00d3\3\2\2\2\33\u00d5\3\2\2\2")
        buf.write("\35\u00d7\3\2\2\2\37\u00d9\3\2\2\2!\u00db\3\2\2\2#\u00dd")
        buf.write("\3\2\2\2%\u00df\3\2\2\2\'\u00e1\3\2\2\2)\u00e3\3\2\2\2")
        buf.write("+\u00e5\3\2\2\2-\u00e7\3\2\2\2/\u00e9\3\2\2\2\61\u00eb")
        buf.write("\3\2\2\2\63\u00ed\3\2\2\2\65\u00ef\3\2\2\2\67\u00f1\3")
        buf.write("\2\2\29\u00fa\3\2\2\2;\u0102\3\2\2\2=\u0109\3\2\2\2?\u010b")
        buf.write("\3\2\2\2A\u0111\3\2\2\2C\u011a\3\2\2\2E\u011e\3\2\2\2")
        buf.write("G\u0121\3\2\2\2I\u0128\3\2\2\2K\u012b\3\2\2\2M\u012e\3")
        buf.write("\2\2\2O\u0133\3\2\2\2Q\u0138\3\2\2\2S\u013f\3\2\2\2U\u0145")
        buf.write("\3\2\2\2W\u014b\3\2\2\2Y\u014f\3\2\2\2[\u0158\3\2\2\2")
        buf.write("]\u0162\3\2\2\2_\u0166\3\2\2\2a\u016b\3\2\2\2c\u0171\3")
        buf.write("\2\2\2e\u0177\3\2\2\2g\u017a\3\2\2\2i\u017f\3\2\2\2k\u0187")
        buf.write("\3\2\2\2m\u018f\3\2\2\2o\u0196\3\2\2\2q\u019a\3\2\2\2")
        buf.write("s\u019e\3\2\2\2u\u01a1\3\2\2\2w\u01a5\3\2\2\2y\u01a9\3")
        buf.write("\2\2\2{\u01ab\3\2\2\2}\u01ad\3\2\2\2\177\u01af\3\2\2\2")
        buf.write("\u0081\u01b1\3\2\2\2\u0083\u01b4\3\2\2\2\u0085\u01b6\3")
        buf.write("\2\2\2\u0087\u01b9\3\2\2\2\u0089\u01bb\3\2\2\2\u008b\u01bd")
        buf.write("\3\2\2\2\u008d\u01c0\3\2\2\2\u008f\u01c2\3\2\2\2\u0091")
        buf.write("\u01c4\3\2\2\2\u0093\u01c6\3\2\2\2\u0095\u01c8\3\2\2\2")
        buf.write("\u0097\u01ca\3\2\2\2\u0099\u01cd\3\2\2\2\u009b\u01cf\3")
        buf.write("\2\2\2\u009d\u01d2\3\2\2\2\u009f\u01d4\3\2\2\2\u00a1\u01de")
        buf.write("\3\2\2\2\u00a3\u01e9\3\2\2\2\u00a5\u01f2\3\2\2\2\u00a7")
        buf.write("\u01fa\3\2\2\2\u00a9\u0200\3\2\2\2\u00ab\u020e\3\2\2\2")
        buf.write("\u00ad\u0219\3\2\2\2\u00af\u0224\3\2\2\2\u00b1\u0226\3")
        buf.write("\2\2\2\u00b3\u0231\3\2\2\2\u00b5\u0233\3\2\2\2\u00b7\u0237")
        buf.write("\3\2\2\2\u00b9\u0256\3\2\2\2\u00bb\u0258\3\2\2\2\u00bd")
        buf.write("\u00be\t\2\2\2\u00be\4\3\2\2\2\u00bf\u00c0\t\3\2\2\u00c0")
        buf.write("\6\3\2\2\2\u00c1\u00c2\t\4\2\2\u00c2\b\3\2\2\2\u00c3\u00c4")
        buf.write("\t\5\2\2\u00c4\n\3\2\2\2\u00c5\u00c6\t\6\2\2\u00c6\f\3")
        buf.write("\2\2\2\u00c7\u00c8\t\7\2\2\u00c8\16\3\2\2\2\u00c9\u00ca")
        buf.write("\t\b\2\2\u00ca\20\3\2\2\2\u00cb\u00cc\t\t\2\2\u00cc\22")
        buf.write("\3\2\2\2\u00cd\u00ce\t\n\2\2\u00ce\24\3\2\2\2\u00cf\u00d0")
        buf.write("\t\13\2\2\u00d0\26\3\2\2\2\u00d1\u00d2\t\f\2\2\u00d2\30")
        buf.write("\3\2\2\2\u00d3\u00d4\t\r\2\2\u00d4\32\3\2\2\2\u00d5\u00d6")
        buf.write("\t\16\2\2\u00d6\34\3\2\2\2\u00d7\u00d8\t\17\2\2\u00d8")
        buf.write("\36\3\2\2\2\u00d9\u00da\t\20\2\2\u00da \3\2\2\2\u00db")
        buf.write("\u00dc\t\21\2\2\u00dc\"\3\2\2\2\u00dd\u00de\t\22\2\2\u00de")
        buf.write("$\3\2\2\2\u00df\u00e0\t\23\2\2\u00e0&\3\2\2\2\u00e1\u00e2")
        buf.write("\t\24\2\2\u00e2(\3\2\2\2\u00e3\u00e4\t\25\2\2\u00e4*\3")
        buf.write("\2\2\2\u00e5\u00e6\t\26\2\2\u00e6,\3\2\2\2\u00e7\u00e8")
        buf.write("\t\27\2\2\u00e8.\3\2\2\2\u00e9\u00ea\t\30\2\2\u00ea\60")
        buf.write("\3\2\2\2\u00eb\u00ec\t\31\2\2\u00ec\62\3\2\2\2\u00ed\u00ee")
        buf.write("\t\32\2\2\u00ee\64\3\2\2\2\u00ef\u00f0\t\33\2\2\u00f0")
        buf.write("\66\3\2\2\2\u00f1\u00f2\5\3\2\2\u00f2\u00f3\5\35\17\2")
        buf.write("\u00f3\u00f4\5\t\5\2\u00f4\u00f5\7\"\2\2\u00f5\u00f6\5")
        buf.write(")\25\2\u00f6\u00f7\5\21\t\2\u00f7\u00f8\5\13\6\2\u00f8")
        buf.write("\u00f9\5\35\17\2\u00f98\3\2\2\2\u00fa\u00fb\5\37\20\2")
        buf.write("\u00fb\u00fc\5%\23\2\u00fc\u00fd\7\"\2\2\u00fd\u00fe\5")
        buf.write("\13\6\2\u00fe\u00ff\5\31\r\2\u00ff\u0100\5\'\24\2\u0100")
        buf.write("\u0101\5\13\6\2\u0101:\3\2\2\2\u0102\u0103\5/\30\2\u0103")
        buf.write("\u0104\5\23\n\2\u0104\u0105\5)\25\2\u0105\u0106\5\21\t")
        buf.write("\2\u0106<\3\2\2\2\u0107\u010a\5_\60\2\u0108\u010a\5a\61")
        buf.write("\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a>\3\2")
        buf.write("\2\2\u010b\u010c\5\5\3\2\u010c\u010d\5%\23\2\u010d\u010e")
        buf.write("\5\13\6\2\u010e\u010f\5\3\2\2\u010f\u0110\5\27\f\2\u0110")
        buf.write("@\3\2\2\2\u0111\u0112\5\7\4\2\u0112\u0113\5\37\20\2\u0113")
        buf.write("\u0114\5\35\17\2\u0114\u0115\5)\25\2\u0115\u0116\5\23")
        buf.write("\n\2\u0116\u0117\5\35\17\2\u0117\u0118\5+\26\2\u0118\u0119")
        buf.write("\5\13\6\2\u0119B\3\2\2\2\u011a\u011b\5\r\7\2\u011b\u011c")
        buf.write("\5\37\20\2\u011c\u011d\5%\23\2\u011dD\3\2\2\2\u011e\u011f")
        buf.write("\5)\25\2\u011f\u0120\5\37\20\2\u0120F\3\2\2\2\u0121\u0122")
        buf.write("\5\t\5\2\u0122\u0123\5\37\20\2\u0123\u0124\5/\30\2\u0124")
        buf.write("\u0125\5\35\17\2\u0125\u0126\5)\25\2\u0126\u0127\5\37")
        buf.write("\20\2\u0127H\3\2\2\2\u0128\u0129\5\t\5\2\u0129\u012a\5")
        buf.write("\37\20\2\u012aJ\3\2\2\2\u012b\u012c\5\23\n\2\u012c\u012d")
        buf.write("\5\r\7\2\u012dL\3\2\2\2\u012e\u012f\5)\25\2\u012f\u0130")
        buf.write("\5\21\t\2\u0130\u0131\5\13\6\2\u0131\u0132\5\35\17\2\u0132")
        buf.write("N\3\2\2\2\u0133\u0134\5\13\6\2\u0134\u0135\5\31\r\2\u0135")
        buf.write("\u0136\5\'\24\2\u0136\u0137\5\13\6\2\u0137P\3\2\2\2\u0138")
        buf.write("\u0139\5%\23\2\u0139\u013a\5\13\6\2\u013a\u013b\5)\25")
        buf.write("\2\u013b\u013c\5+\26\2\u013c\u013d\5%\23\2\u013d\u013e")
        buf.write("\5\35\17\2\u013eR\3\2\2\2\u013f\u0140\5/\30\2\u0140\u0141")
        buf.write("\5\21\t\2\u0141\u0142\5\23\n\2\u0142\u0143\5\31\r\2\u0143")
        buf.write("\u0144\5\13\6\2\u0144T\3\2\2\2\u0145\u0146\5\5\3\2\u0146")
        buf.write("\u0147\5\13\6\2\u0147\u0148\5\17\b\2\u0148\u0149\5\23")
        buf.write("\n\2\u0149\u014a\5\35\17\2\u014aV\3\2\2\2\u014b\u014c")
        buf.write("\5\13\6\2\u014c\u014d\5\35\17\2\u014d\u014e\5\t\5\2\u014e")
        buf.write("X\3\2\2\2\u014f\u0150\5\r\7\2\u0150\u0151\5+\26\2\u0151")
        buf.write("\u0152\5\35\17\2\u0152\u0153\5\7\4\2\u0153\u0154\5)\25")
        buf.write("\2\u0154\u0155\5\23\n\2\u0155\u0156\5\37\20\2\u0156\u0157")
        buf.write("\5\35\17\2\u0157Z\3\2\2\2\u0158\u0159\5!\21\2\u0159\u015a")
        buf.write("\5%\23\2\u015a\u015b\5\37\20\2\u015b\u015c\5\7\4\2\u015c")
        buf.write("\u015d\5\13\6\2\u015d\u015e\5\t\5\2\u015e\u015f\5+\26")
        buf.write("\2\u015f\u0160\5%\23\2\u0160\u0161\5\13\6\2\u0161\\\3")
        buf.write("\2\2\2\u0162\u0163\5-\27\2\u0163\u0164\5\3\2\2\u0164\u0165")
        buf.write("\5%\23\2\u0165^\3\2\2\2\u0166\u0167\5)\25\2\u0167\u0168")
        buf.write("\5%\23\2\u0168\u0169\5+\26\2\u0169\u016a\5\13\6\2\u016a")
        buf.write("`\3\2\2\2\u016b\u016c\5\r\7\2\u016c\u016d\5\3\2\2\u016d")
        buf.write("\u016e\5\31\r\2\u016e\u016f\5\'\24\2\u016f\u0170\5\13")
        buf.write("\6\2\u0170b\3\2\2\2\u0171\u0172\5\3\2\2\u0172\u0173\5")
        buf.write("%\23\2\u0173\u0174\5%\23\2\u0174\u0175\5\3\2\2\u0175\u0176")
        buf.write("\5\63\32\2\u0176d\3\2\2\2\u0177\u0178\5\37\20\2\u0178")
        buf.write("\u0179\5\r\7\2\u0179f\3\2\2\2\u017a\u017b\5%\23\2\u017b")
        buf.write("\u017c\5\13\6\2\u017c\u017d\5\3\2\2\u017d\u017e\5\31\r")
        buf.write("\2\u017eh\3\2\2\2\u017f\u0180\5\5\3\2\u0180\u0181\5\37")
        buf.write("\20\2\u0181\u0182\5\37\20\2\u0182\u0183\5\31\r\2\u0183")
        buf.write("\u0184\5\13\6\2\u0184\u0185\5\3\2\2\u0185\u0186\5\35\17")
        buf.write("\2\u0186j\3\2\2\2\u0187\u0188\5\23\n\2\u0188\u0189\5\35")
        buf.write("\17\2\u0189\u018a\5)\25\2\u018a\u018b\5\13\6\2\u018b\u018c")
        buf.write("\5\17\b\2\u018c\u018d\5\13\6\2\u018d\u018e\5%\23\2\u018e")
        buf.write("l\3\2\2\2\u018f\u0190\5\'\24\2\u0190\u0191\5)\25\2\u0191")
        buf.write("\u0192\5%\23\2\u0192\u0193\5\23\n\2\u0193\u0194\5\35\17")
        buf.write("\2\u0194\u0195\5\17\b\2\u0195n\3\2\2\2\u0196\u0197\5\35")
        buf.write("\17\2\u0197\u0198\5\37\20\2\u0198\u0199\5)\25\2\u0199")
        buf.write("p\3\2\2\2\u019a\u019b\5\3\2\2\u019b\u019c\5\35\17\2\u019c")
        buf.write("\u019d\5\t\5\2\u019dr\3\2\2\2\u019e\u019f\5\37\20\2\u019f")
        buf.write("\u01a0\5%\23\2\u01a0t\3\2\2\2\u01a1\u01a2\5\t\5\2\u01a2")
        buf.write("\u01a3\5\23\n\2\u01a3\u01a4\5-\27\2\u01a4v\3\2\2\2\u01a5")
        buf.write("\u01a6\5\33\16\2\u01a6\u01a7\5\37\20\2\u01a7\u01a8\5\t")
        buf.write("\5\2\u01a8x\3\2\2\2\u01a9\u01aa\7-\2\2\u01aaz\3\2\2\2")
        buf.write("\u01ab\u01ac\7/\2\2\u01ac|\3\2\2\2\u01ad\u01ae\7\61\2")
        buf.write("\2\u01ae~\3\2\2\2\u01af\u01b0\7,\2\2\u01b0\u0080\3\2\2")
        buf.write("\2\u01b1\u01b2\7>\2\2\u01b2\u01b3\7@\2\2\u01b3\u0082\3")
        buf.write("\2\2\2\u01b4\u01b5\7>\2\2\u01b5\u0084\3\2\2\2\u01b6\u01b7")
        buf.write("\7>\2\2\u01b7\u01b8\7?\2\2\u01b8\u0086\3\2\2\2\u01b9\u01ba")
        buf.write("\7?\2\2\u01ba\u0088\3\2\2\2\u01bb\u01bc\7@\2\2\u01bc\u008a")
        buf.write("\3\2\2\2\u01bd\u01be\7@\2\2\u01be\u01bf\7?\2\2\u01bf\u008c")
        buf.write("\3\2\2\2\u01c0\u01c1\7*\2\2\u01c1\u008e\3\2\2\2\u01c2")
        buf.write("\u01c3\7+\2\2\u01c3\u0090\3\2\2\2\u01c4\u01c5\7]\2\2\u01c5")
        buf.write("\u0092\3\2\2\2\u01c6\u01c7\7_\2\2\u01c7\u0094\3\2\2\2")
        buf.write("\u01c8\u01c9\7=\2\2\u01c9\u0096\3\2\2\2\u01ca\u01cb\7")
        buf.write("\60\2\2\u01cb\u01cc\7\60\2\2\u01cc\u0098\3\2\2\2\u01cd")
        buf.write("\u01ce\7<\2\2\u01ce\u009a\3\2\2\2\u01cf\u01d0\5\u0099")
        buf.write("M\2\u01d0\u01d1\5\u0087D\2\u01d1\u009c\3\2\2\2\u01d2\u01d3")
        buf.write("\7.\2\2\u01d3\u009e\3\2\2\2\u01d4\u01d8\7$\2\2\u01d5\u01d7")
        buf.write("\5\u00b3Z\2\u01d6\u01d5\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8")
        buf.write("\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01db\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01db\u01dc\7$\2\2\u01dc\u01dd\b")
        buf.write("P\2\2\u01dd\u00a0\3\2\2\2\u01de\u01e2\7$\2\2\u01df\u01e1")
        buf.write("\5\u00b3Z\2\u01e0\u01df\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e5\3\2\2\2")
        buf.write("\u01e4\u01e2\3\2\2\2\u01e5\u01e6\7^\2\2\u01e6\u01e7\n")
        buf.write("\34\2\2\u01e7\u01e8\bQ\3\2\u01e8\u00a2\3\2\2\2\u01e9\u01ed")
        buf.write("\7$\2\2\u01ea\u01ec\5\u00b3Z\2\u01eb\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ee\u01f0\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f1\b")
        buf.write("R\4\2\u01f1\u00a4\3\2\2\2\u01f2\u01f6\t\35\2\2\u01f3\u01f5")
        buf.write("\t\36\2\2\u01f4\u01f3\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6")
        buf.write("\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u00a6\3\2\2\2")
        buf.write("\u01f8\u01f6\3\2\2\2\u01f9\u01fb\t\37\2\2\u01fa\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01ff\bT\5\2")
        buf.write("\u01ff\u00a8\3\2\2\2\u0200\u0201\7*\2\2\u0201\u0202\7")
        buf.write(",\2\2\u0202\u0206\3\2\2\2\u0203\u0205\13\2\2\2\u0204\u0203")
        buf.write("\3\2\2\2\u0205\u0208\3\2\2\2\u0206\u0207\3\2\2\2\u0206")
        buf.write("\u0204\3\2\2\2\u0207\u0209\3\2\2\2\u0208\u0206\3\2\2\2")
        buf.write("\u0209\u020a\7,\2\2\u020a\u020b\7+\2\2\u020b\u020c\3\2")
        buf.write("\2\2\u020c\u020d\bU\5\2\u020d\u00aa\3\2\2\2\u020e\u0212")
        buf.write("\7}\2\2\u020f\u0211\13\2\2\2\u0210\u020f\3\2\2\2\u0211")
        buf.write("\u0214\3\2\2\2\u0212\u0213\3\2\2\2\u0212\u0210\3\2\2\2")
        buf.write("\u0213\u0215\3\2\2\2\u0214\u0212\3\2\2\2\u0215\u0216\7")
        buf.write("\177\2\2\u0216\u0217\3\2\2\2\u0217\u0218\bV\5\2\u0218")
        buf.write("\u00ac\3\2\2\2\u0219\u021a\7\61\2\2\u021a\u021b\7\61\2")
        buf.write("\2\u021b\u021f\3\2\2\2\u021c\u021e\n \2\2\u021d\u021c")
        buf.write("\3\2\2\2\u021e\u0221\3\2\2\2\u021f\u021d\3\2\2\2\u021f")
        buf.write("\u0220\3\2\2\2\u0220\u0222\3\2\2\2\u0221\u021f\3\2\2\2")
        buf.write("\u0222\u0223\bW\5\2\u0223\u00ae\3\2\2\2\u0224\u0225\t")
        buf.write("!\2\2\u0225\u00b0\3\2\2\2\u0226\u0228\5\13\6\2\u0227\u0229")
        buf.write("\5{>\2\u0228\u0227\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022b")
        buf.write("\3\2\2\2\u022a\u022c\5\u00afX\2\u022b\u022a\3\2\2\2\u022c")
        buf.write("\u022d\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022e\3\2\2\2")
        buf.write("\u022e\u00b2\3\2\2\2\u022f\u0232\n\"\2\2\u0230\u0232\5")
        buf.write("\u00b5[\2\u0231\u022f\3\2\2\2\u0231\u0230\3\2\2\2\u0232")
        buf.write("\u00b4\3\2\2\2\u0233\u0234\7^\2\2\u0234\u0235\t\34\2\2")
        buf.write("\u0235\u00b6\3\2\2\2\u0236\u0238\5\u00afX\2\u0237\u0236")
        buf.write("\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u0237\3\2\2\2\u0239")
        buf.write("\u023a\3\2\2\2\u023a\u00b8\3\2\2\2\u023b\u023d\5\u00af")
        buf.write("X\2\u023c\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023c")
        buf.write("\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u024b\3\2\2\2\u0240")
        buf.write("\u0244\7\60\2\2\u0241\u0243\5\u00afX\2\u0242\u0241\3\2")
        buf.write("\2\2\u0243\u0246\3\2\2\2\u0244\u0242\3\2\2\2\u0244\u0245")
        buf.write("\3\2\2\2\u0245\u0248\3\2\2\2\u0246\u0244\3\2\2\2\u0247")
        buf.write("\u0249\5\u00b1Y\2\u0248\u0247\3\2\2\2\u0248\u0249\3\2")
        buf.write("\2\2\u0249\u024c\3\2\2\2\u024a\u024c\5\u00b1Y\2\u024b")
        buf.write("\u0240\3\2\2\2\u024b\u024a\3\2\2\2\u024c\u0257\3\2\2\2")
        buf.write("\u024d\u024f\7\60\2\2\u024e\u0250\5\u00afX\2\u024f\u024e")
        buf.write("\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u024f\3\2\2\2\u0251")
        buf.write("\u0252\3\2\2\2\u0252\u0254\3\2\2\2\u0253\u0255\5\u00b1")
        buf.write("Y\2\u0254\u0253\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0257")
        buf.write("\3\2\2\2\u0256\u023c\3\2\2\2\u0256\u024d\3\2\2\2\u0257")
        buf.write("\u00ba\3\2\2\2\u0258\u0259\13\2\2\2\u0259\u025a\b^\6\2")
        buf.write("\u025a\u00bc\3\2\2\2\27\2\u0109\u01d8\u01e2\u01ed\u01f6")
        buf.write("\u01fc\u0206\u0212\u021f\u0228\u022d\u0231\u0239\u023e")
        buf.write("\u0244\u0248\u024b\u0251\u0254\u0256\7\3P\2\3Q\3\3R\4")
        buf.write("\b\2\2\3^\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ANDTHEN = 1
    ORELSE = 2
    WITH = 3
    BOOL_LIT = 4
    BREAK = 5
    CONTINUE = 6
    FOR = 7
    TO = 8
    DOWNTO = 9
    DO = 10
    IF = 11
    THEN = 12
    ELSE = 13
    RETURN = 14
    WHILE = 15
    BEGIN = 16
    END = 17
    FUNCTION = 18
    PROCEDURE = 19
    VAR = 20
    TRUE = 21
    FALSE = 22
    ARRAY = 23
    OF = 24
    REAL = 25
    BOOLEAN = 26
    INTEGER = 27
    STRING = 28
    NOT = 29
    AND = 30
    OR = 31
    DIV = 32
    MOD = 33
    PLUS = 34
    MINUS = 35
    DIVIDE = 36
    MULTIPLE = 37
    NOT_EQUAL = 38
    LT = 39
    LE = 40
    EQUAL = 41
    GT = 42
    GE = 43
    LB = 44
    RB = 45
    LSB = 46
    RSB = 47
    SM = 48
    DOTDOT = 49
    COLON = 50
    ASSIGN = 51
    CM = 52
    STRING_LIT = 53
    ILLEGAL_ESCAPE = 54
    UNCLOSED_STRING = 55
    ID = 56
    WS = 57
    COMMENT_1 = 58
    COMMENT_2 = 59
    LINE_COMMENT = 60
    INT_LIT = 61
    FLOAT_LIT = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'/'", "'*'", "'<>'", "'<'", "'<='", "'='", "'>'", 
            "'>='", "'('", "')'", "'['", "']'", "';'", "'..'", "':'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ANDTHEN", "ORELSE", "WITH", "BOOL_LIT", "BREAK", "CONTINUE", 
            "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", 
            "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", 
            "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", 
            "NOT", "AND", "OR", "DIV", "MOD", "PLUS", "MINUS", "DIVIDE", 
            "MULTIPLE", "NOT_EQUAL", "LT", "LE", "EQUAL", "GT", "GE", "LB", 
            "RB", "LSB", "RSB", "SM", "DOTDOT", "COLON", "ASSIGN", "CM", 
            "STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", "ID", "WS", 
            "COMMENT_1", "COMMENT_2", "LINE_COMMENT", "INT_LIT", "FLOAT_LIT", 
            "ERROR_CHAR" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "ANDTHEN", "ORELSE", "WITH", "BOOL_LIT", 
                  "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", 
                  "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", 
                  "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", 
                  "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", 
                  "MOD", "PLUS", "MINUS", "DIVIDE", "MULTIPLE", "NOT_EQUAL", 
                  "LT", "LE", "EQUAL", "GT", "GE", "LB", "RB", "LSB", "RSB", 
                  "SM", "DOTDOT", "COLON", "ASSIGN", "CM", "STRING_LIT", 
                  "ILLEGAL_ESCAPE", "UNCLOSED_STRING", "ID", "WS", "COMMENT_1", 
                  "COMMENT_2", "LINE_COMMENT", "DIGIT", "EXPONENT", "STRING_CHAR", 
                  "ESCAPE_SEQUENCES", "INT_LIT", "FLOAT_LIT", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
    	if self._actions is None:
    		actions = dict()
    		actions[78] = self.STRING_LIT_action 
    		actions[79] = self.ILLEGAL_ESCAPE_action 
    		actions[80] = self.UNCLOSED_STRING_action 
    		actions[92] = self.ERROR_CHAR_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise IllegalEscape(self.text[1:])
     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


