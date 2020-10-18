import re
from optparse import OptionParser
import inspect

T_KEYWORDS_INIT= "<keyword init>"
T_OPLOGICO= "<opLogic %s>"
T_OPMAT= "<opMat %s>"
T_BOOL= "<opBool %s>"
T_INT = "<int %s>"
T_STRING = "<str %s>"
T_IDENTIF = "<id %s>"
T_COMMENT = "<comentario %s>"
T_LPARENT = "<LParent %s>"
T_RPARENT = "<RParent %s>"
T_LCOLCHETE = "<LColchete %s>"
T_RCOLCHETE = "<RColchete %s>"

T_EOF = "eof"

T_ReservWord =[
    "if",
    "elseif",
    "else"
]

T_ReservWordGets = "<method gets %s>"
T_ReservWordPuts = "<method puts %s>"

def afd_string(token):
    if token[0] == '"' and token[-1] == '"':
        if '"' not in token[1:-1]:
            return True
        else:
            raise ValueError('Aspas em um local inesperado.')
    else:
        return False

def afd_int(token):
    return re.match("[0-9][0-9.]*", token)

def afd_identificador(token):
    return re.match("[a-zA-Z][a-zA-Z_0-9]*", token)

def afd_comentario(token):
    return re.match("([\#][.]*)", token)

def afd_operatorMatematico(token):
    return re.match('[-+*/]', token)

def afd_operatorLogico(token):
    return re.match('[==]||[!=]||[<]||[>]||[<=]||[>=]', token)

def afd_operatorBool(token):
    return re.match('([t][r][u][e])|([f][a][l][s][e])', token)

def afd_reservedWord(token):
    return token in T_ReservWord

def afd_lParent(token):
    return re.match('([(])', token)

def afd_rParent(token):
    return re.match('([)])', token)

def afd_lColchete(token):
    return re.match('([\[])', token)

def afd_rColchete(token):
    return re.match('([\]])', token)

def afd_reservWordPuts(token):
    return re.match('([p][u][t][s])', token)

def afd_reservWordGets(token):
    return re.match('([g][e][t][s])', token)

class Token():

    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        return '<%s %s>' % (self.tipo, self.valor)

def afd_principal(token):
    if token == "init":
        return Token(T_KEYWORDS_INIT)

    elif afd_comentario(token):
        return Token(T_COMMENT, token)

    elif afd_reservedWord(token):
        return Token(T_ReservWord, token)

    elif afd_lColchete(token):
        return Token(T_LCOLCHETE, token)

    elif afd_rColchete(token):
        return Token(T_RCOLCHETE, token)

    elif afd_lParent(token):
        return Token(T_LPARENT, token)

    elif afd_rParent(token):
        return Token(T_RPARENT, token)

    elif afd_reservWordPuts(token):
        return Token(T_ReservWordPuts, token)

    elif afd_reservWordGets(token):
        return Token(T_ReservWordGets, token)

    elif afd_operatorMatematico(token):
        return Token(T_OPMAT, token)

    elif afd_string(token):
        return Token(T_STRING, token)

    elif afd_int(token):
        return Token(T_INT, token)

    elif afd_identificador(token):
        return Token(T_IDENTIF, token)

    elif afd_operatorLogico(token):
        return Token(T_OPLOGICO, token)

    elif afd_operatorBool(token):
        return Token(T_BOOL, token)

    else:
        return None

class Parser():

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.token_atual = None

        self.proximo()

    def proximo(self):
        self.pos += 1

        if self.pos >= len(self.tokens):
            self.token_atual = Token(T_EOF)
        else:
            self.token_atual = self.tokens[self.pos]

        print(self.token_atual)
        return self.token_atual

    def erro(self):
        raise Exception('Erro de sintaxe.')

    def use(self, tipo, valor=None):
        if self.token_atual.tipo != tipo:
            self.erro()
        elif valor is not None and self.token_atual.valor != valor:
            self.erro()
        else:
            self.proximo()

    def statement(self):
        """
        statement ::= <id> <op => expr
        """
        if self.token_atual.tipo == T_IDENTIF:
            self.use(T_IDENTIF)
            self.use(T_OPLOGICO, '=')
            self.expr()

        #elif self.token_atual.tipo == T_ReservWord:
        #    if self.token_atual.valor == "if":
        #        self.use(T_IDENTIF)

        elif self.token_atual.tipo == T_ReservWordPuts:
            self.use(T_ReservWordPuts)
            #self.use(T_STRING)
            self.expr()

        elif self.token_atual.tipo == T_ReservWordGets:
            self.use(T_ReservWordGets)
            self.use(T_STRING)
            self.expr()
        else:
            "teste"

    def expr(self):
        """
        expr ::= term ( <op +> | <op -> term )*
        """

        self.term()
        if self.token_atual.tipo == T_OPMAT:
            while self.token_atual.tipo == T_OPMAT and self.token_atual.valor in ['+', '-','*','/']:
                self.use(T_OPMAT)
                self.term()

            """
            expr ::= term ( <op +> | <op -> term )*
            """
        elif self.token_atual.tipo == T_OPLOGICO:
            while self.token_atual.tipo == T_OPMAT and self.token_atual.valor in ['+', '-','*','/']:
                self.use(T_OPMAT)
                self.term()
            print("teste")

        elif self.token_atual.tipo == T_ReservWordPuts:
            print("expr T_ReservWordPuts")

        elif self.token_atual.tipo == T_ReservWordGets:
            print("expr T_ReservWordGets")

        elif self.token_atual.tipo == T_OPMAT:
            print("teste")

    def term(self):
        """
        term ::= <id> | <int>
        """
        if self.token_atual.tipo == T_INT:
            self.use(T_INT)
        elif self.token_atual.tipo == T_STRING:
            self.use(T_STRING)
        elif self.token_atual.tipo == T_BOOL:
            self.use(T_BOOL)
        elif self.token_atual.tipo == T_IDENTIF:
            self.use(T_IDENTIF)
        elif self.token_atual.tipo == T_ReservWordGets:
            self.use(T_ReservWordGets)
        elif self.token_atual.tipo == T_ReservWordPuts:
            self.use(T_ReservWordPuts)
        else:
            self.erro()

arquivo = open('codigo.rb', 'r')

patternStr = r'"(.*)"'
patternComment = r'#(.*)'

tokens = []
for l in arquivo.readlines():
    l = l.replace("\n", "")

    if l!='':
        m = re.search(patternStr, l)
        if m != None:
            m2= m.group()
            l = l.replace(m2,m2.replace(" ","_"))

        m = re.search(patternComment, l)
        if m != None:
            m2= m.group()
            l = l.replace(m2,m2.replace(" ","_"))

    for token in l.split():
        try:
            tokens.append(afd_principal(token))
        except Exception as e:
            print(tokens)
            print(str(e) + " na posição %i da linha %i" % (l.index(token), ln))
            raise StopExecution

for token in tokens:
    if token.tipo == T_COMMENT:
        tokens.remove(token)

parser = Parser(tokens)



while True:
  parser.statement()
  if len(parser.tokens) == parser.pos:
    break
'''
arvores = arvoreSintatica(tokens)
for arvore in arvores:
    print(arvore.PrintTree())
'''