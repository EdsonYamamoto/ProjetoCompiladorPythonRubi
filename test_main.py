import unittest
from main import interpretador

class MyTest(unittest.TestCase):

    def testBasico(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test.rb")
        interpreter.tokenizer()
        self.assertEqual(2, interpreter.execParser(), "soma funcionando")

    def testBasico2(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test2.rb")
        interpreter.tokenizer()
        self.assertEqual(4, interpreter.execParser(), "multiplicacao funcionando")

    def testBasico3(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test3.rb")
        interpreter.tokenizer()
        self.assertEqual(67, interpreter.execParser(), "formula complexa")

    def testBasico4(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test4.rb")
        interpreter.tokenizer()
        self.assertEqual("teste", interpreter.execParser(), "string")

    def testBasico5(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test5.rb")
        interpreter.tokenizer()
        self.assertEqual("teste_formando_uma_definicao_2", interpreter.execParser(), "string")

    def testBasico6(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test6.rb")
        interpreter.tokenizer()
        self.assertEqual(None, interpreter.execParser(), "impressor")

    #Problema de input de valor
    '''
    def testBasico7(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test7.rb")
        interpreter.tokenizer()
        self.assertEqual(None, interpreter.execParser(), "recebedor variavel")
    '''
    def testBasico8(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test8.rb")
        interpreter.tokenizer()
        self.assertEqual(None, interpreter.execParser(), "armazenar variavel")

    def testBasico9(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test9.rb")
        interpreter.tokenizer()
        self.assertEqual(56, interpreter.execParser(), "recebedor variavel")

    def testBasico10(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test10.rb")
        interpreter.tokenizer()
        self.assertEqual("teste", interpreter.execParser(), "recebedor variavel")

    def testBasico11(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test11.rb")
        interpreter.tokenizer()
        self.assertEqual(56, interpreter.execParser(), "recebedor variavel")

    def testBasico12(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test12.rb")
        interpreter.tokenizer()
        self.assertEqual("coma", interpreter.execParser(), "recebedor variavel")

    def testBasico13(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test13.rb")
        interpreter.tokenizer()
        self.assertEqual(68, interpreter.execParser(), "recebedor variavel")

    def testBasico14(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test14.rb")
        interpreter.tokenizer()
        self.assertEqual("mundoolho", interpreter.execParser(), "recebedor variavel")

    def testBasico15(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test15.rb")
        interpreter.tokenizer()
        self.assertEqual(6, interpreter.execParser(), "recebedor variavel")

    def testBasico16(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test16.rb")
        interpreter.tokenizer()
        self.assertNotEqual(None, interpreter.execParser(), "recebedor variavel")
        #self.assertEqual(2, interpreter.execParser(), "recebedor variavel")

    def testBasico17(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test17.rb")
        interpreter.tokenizer()
        self.assertEqual(True, interpreter.execParser(), "recebedor variavel")

    def testBasico18(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test18.rb")
        interpreter.tokenizer()
        self.assertEqual(True, interpreter.execParser(), "recebedor variavel")

    def testBasico19(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test19.rb")
        interpreter.tokenizer()
        self.assertEqual(False, interpreter.execParser(), "recebedor variavel")

    def testBasico20(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigo_test20.rb")
        interpreter.tokenizer()
        self.assertEqual(False, interpreter.execParser(), "recebedor variavel")

    '''
    #Problema de input de valor
    def testNormal(self):
        interpreter = interpretador()
        interpreter.loadfile("codigo.x")
        interpreter.tokenizer()
        self.assertNotEqual(None, interpreter.execParser(), "teste")
    '''

    def testRescreverBasico(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico2(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test2.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico3(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test3.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico4(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test4.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico5(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test5.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico6(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test6.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual("echo Valor_de_a\n", t, "soma funcionando")

    #Problema de input de valor
    #def testRescreverBasico7(self):
    #    interpreter = interpretador()
    #    interpreter.loadfile("test_repository/codigoRescrito_test7.rb")
    #    interpreter.tokenizer()
    #    interpreter.execParser()
    #    t = interpreter.parser.batScript
    #    self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico8(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test8.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico9(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test9.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico10(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test10.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico11(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test11.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico12(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test12.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico13(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test13.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico14(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test14.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico15(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test15.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    def testRescreverBasico16(self):
        interpreter = interpretador()
        interpreter.loadfile("test_repository/codigoRescrito_test16.rb")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

    #Problema de input de valor
    def testRescreverNormal(self):
        interpreter = interpretador()
        interpreter.loadfile("codigo.x")
        interpreter.tokenizer()
        interpreter.execParser()
        t = interpreter.parser.batScript
        self.assertEqual(2, t, "soma funcionando")

