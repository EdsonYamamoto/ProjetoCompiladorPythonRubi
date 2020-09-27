import re

T_KEYWORDS_INIT= "<keyword init>"
T_OPLOGICO= "<opLogic %s>"
T_OPMAT= "<opMat %s>"
T_INT = "<int %s>"
T_STRING = "<str %s>"
T_IDENTIF = "<id %s>"
T_COMMENT = "<comentario %s>"
T_LPARENT = "<LParent %s>"
T_RPARENT = "<RParent %s>"
T_EOF = "eof"

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
    return re.match('\"([^\\\n]|(\\.))*?\"', token)

def afd_lParent(token):
    return re.match("[(]", token)

def afd_rParent(token):
    return re.match('[)]', token)

def afd_operatorMatematico(token):
    return re.match('[-+*/]', token)

def afd_operatorLogico(token):
    return re.match('[==]||[!=]||[<]||[>]||[<=]||[>=]', token)

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

    elif afd_lParent(token):
        return Token(T_LPARENT, token)

    elif afd_rParent(token):
        return Token(T_RPARENT, token)

    elif afd_operatorMatematico(token):
        return Token(T_OPMAT, token)

    elif afd_operatorLogico(token):
        return Token(T_OPLOGICO, token)

    elif afd_string(token):
        return Token(T_STRING, token)

    elif afd_int(token):
        return Token(T_INT, token)

    elif afd_identificador(token):
        return Token(T_IDENTIF, token)
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

        self.use(T_IDENTIF)
        self.use(T_OPLOGICO, '=')
        self.expr()

    def expr(self):
        """
        expr ::= term ( <op +> | <op -> term )*
        """

        self.term()
        while self.token_atual.tipo == T_OPMAT and self.token_atual.valor in ['+', '-']:
            self.use(T_OPMAT)
            self.term()

    def term(self):
        """
        term ::= <id> | <int>
        """

        if self.token_atual.tipo == T_INT:
            self.use(T_INT)
        elif self.token_atual.tipo == T_IDENTIF:
            self.use(T_IDENTIF)
        else:
            self.erro()

arquivo = open('codigo.rb', 'r')

pattern = r'"([A-Za-z0-9_\- ]*)"'

tokens = []
for l in arquivo.readlines():
    l = l.replace("\n", "")

    #if l!='':
    #    m = re.search(pattern, l)
    #    if m != None:
    #        print(m.group())

    for token in l.split():
        t = afd_principal(token)
        tokens.append(t)
        print(t.valor)

    Parser(tokens)
'''
arvores = arvoreSintatica(tokens)
for arvore in arvores:
    print(arvore.PrintTree())
'''