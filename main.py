import re

T_KEYWORD = "keyword"
T_OP = "op"
T_INT = "int"
T_STRING = "string"
T_BOOL = "bool"
T_ID = "id"
T_EOF = "eof"
T_PAR = "par"
T_Atribuidor = "<atribuicao %s>"
T_OPLOGICO= "<opLogic %s>"
T_COMMENT = "<comentario %s>"


class Token():

    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        return '<%s %s>' % (self.tipo, self.valor)


class StopExecution(Exception):
    def _render_traceback_(self):
        pass


def afd_int(token):
    try:
        token = int(token)
        return True
    except:
        return False


def afd_string(token):
    if token[0] == '"' and token[-1] == '"':
        if '"' not in token[1:-1]:
            return True
        else:
            raise ValueError('Aspas em um local inesperado.')
    else:
        return False

def afd_bool(token):
    if token == 'true' or token == 'false':
        return True
    return False

def afd_identificador(token):
    regex = re.compile('[a-zA-Z][a-zA-Z0-9_.]*')
    r = regex.match(token)
    if r is not None:
        if r.group() == token:
            return True
        else:
            return False
    else:
        return False


def afd_operadorLogico(token):
    return re.match("([==]|[>=]|[<=]|[>]|[<]|[!=])", token)

def afd_comentario(token):
    return re.match("([\#][.]*)", token)

def afd_principal(token):
    if token == "init":
        return Token(T_KEYWORD, 'init')

    elif token in "+-*/":
        return Token(T_OP, token)

    elif token in "=":
        return Token(T_Atribuidor, token)

    elif afd_operadorLogico(token):
        return Token(T_OPLOGICO, token)

    elif token in "()":
        return Token(T_PAR, token)

    elif afd_int(token):
        return Token(T_INT, token)

    elif afd_string(token):
        return Token(T_STRING, token)

    elif afd_bool(token):
        return Token(T_BOOL, token)

    elif afd_identificador(token):
        return Token(T_ID, token)

    elif afd_comentario(token):
        Token(T_COMMENT, token)
        return

    else:
        raise ValueError('Valor inesperado')

    return None


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Parser():

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.token_atual = None

        self.dict={}
        self.pilha = Stack()
        self.proximo()


        self.batScript= ""

    def proximo(self):

        self.pos += 1

        if self.pos >= len(self.tokens):
            self.token_atual = Token(T_EOF)
        else:
            self.token_atual = self.tokens[self.pos]

        return self.token_atual

    def erro(self):
        raise Exception('Erro de sintaxe.')

    def use(self, tipo, valor=None):

        if self.token_atual.tipo != tipo:
            self.erro()
        elif valor is not None and self.token_atual.valor != valor:
            self.erro()
        else:
            print(self.token_atual)
            self.proximo()

    def statement(self):
        """
        statement ::= expr
        """

        print("E =")
        while True:
            x = self.expr()

            if self.token_atual.tipo == T_ID and self.pos == len(self.tokens)-1 or self.token_atual.tipo == T_EOF:
                if self.token_atual.valor != None:
                    x = self.dict[self.token_atual.valor]
                break

        print("= ", x)
        return x

    def expr(self):
        """
        expr ::= term ( <op +> | <op -> term )*
        """

        a = self.term()
        while self.token_atual.tipo == T_OP and self.token_atual.valor in ['+', '-']:
            op = self.token_atual.valor
            self.use(T_OP)

            b = self.term()

            if op == "+":
                if type(a) == str and type(b) != str or type(a) != str and type(b) == str :
                    a = str(a)
                    b = str(b)
                a += b
            elif op == "-":
                a -= b

        while self.token_atual.tipo == T_OPLOGICO and self.token_atual.valor in ["==",">=","<=",">","<","!="]:
            op = self.token_atual.valor
            self.use(T_OPLOGICO)

            b = self.term()

            if op == "==":
                a = a==b
            elif op == ">=":
                a = a>=b
            elif op == "<=":
                a = a<=b
            elif op == ">":
                a = a>b
            elif op == "<":
                a = a<b
            elif op == "!=":
                a = a!=b

        return a

    def term(self):
        """
        term ::= factor ( <op *> | <op /> factor)*
        """

        a = self.factor()
        while self.token_atual.tipo == T_OP and self.token_atual.valor in ['*', '/']:
            op = self.token_atual.valor

            self.use(T_OP)
            b = self.factor()

            if op == "*":
                a *= b
            elif op == "/":
                a /= b

        return a

    def factor(self):
        """
        factor ::= <id> | <int> | <par (> expr <par )>
        """

        if self.token_atual.tipo == T_INT:
            x = int(self.token_atual.valor)
            self.use(T_INT)
            return x

        elif self.token_atual.tipo == T_STRING:
            x = self.token_atual.valor
            if len(x)>1:
                x = x[1:len(x)-1]
            self.use(T_STRING)
            return x

        elif self.token_atual.tipo == T_BOOL:
            x = self.token_atual.valor == 'true'
            self.use(T_BOOL)

            return x

        elif self.token_atual.tipo == T_ID:
            return self.reserved_functions()

        elif self.token_atual.tipo == T_PAR and self.token_atual.valor == "(":
            self.use(T_PAR, "(")
            x = self.expr()
            self.use(T_PAR, ")")
            return x
        else:
            self.erro()

    def reserved_functions(self):
        vetor = self.token_atual.valor.split('.')
        if self.token_atual.valor == 'puts':
            self.use(T_ID)
            texto = self.expr()
            print(texto)
            self.batScript += "echo "+texto+"\n"
            return

        elif vetor[0] == 'gets' and vetor[1] == 'chomp':

            self.batScript += "SET "
            x = input()

            if vetor[2] == 'to_i':
                self.batScript += "/A "
                x = int(x)

            self.use(T_ID)
            self.batScript += " = "+str(x)+"\n"

            return x
        elif vetor[0] == 'if' or vetor[0] == 'elsif' or vetor[0] == 'else':
            self.use(T_ID)
            booleana = self.expr()
            teste = self.expr()
            return booleana, teste

        elif vetor[0] == 'end':
            return self.use(T_ID)

        else:

            self.pilha.push(self.token_atual.valor)

            self.use(T_ID)
            if self.token_atual.tipo == T_Atribuidor:
                self.use(T_Atribuidor)
                self.dict[self.pilha.pop()] = self.expr()
                return
            elif self.token_atual.tipo == T_OPLOGICO:
                if self.token_atual.valor == "==":
                    self.use(T_OPLOGICO)
                    if self.token_atual.tipo == T_INT:
                        self.use(T_INT)
                    elif self.token_atual.tipo == T_ID:
                        self.use(T_ID)
                    elif self.token_atual.tipo == T_STRING:
                        self.use(T_STRING)
                    elif self.token_atual.tipo == T_BOOL:
                        self.use(T_BOOL)
                    return self.token_atual.valor == self.dict[self.pilha.pop()]
                elif self.token_atual.valor == "!=":
                    self.use(T_OPLOGICO)
                    if self.token_atual.tipo == T_INT:
                        self.use(T_INT)
                    elif self.token_atual.tipo == T_ID:
                        self.use(T_ID)
                    elif self.token_atual.tipo == T_STRING:
                        self.use(T_STRING)
                    elif self.token_atual.tipo == T_BOOL:
                        self.use(T_BOOL)
                    return self.token_atual.valor != self.dict[self.pilha.pop()]
                elif self.token_atual.valor == ">=":
                    self.use(T_OPLOGICO)
                    if self.token_atual.tipo == T_INT:
                        self.use(T_INT)
                    elif self.token_atual.tipo == T_ID:
                        self.use(T_ID)
                    elif self.token_atual.tipo == T_STRING:
                        self.use(T_STRING)
                    return self.token_atual.valor >= self.dict[self.pilha.pop()]
                elif self.token_atual.valor == "<=":
                    self.use(T_OPLOGICO)
                    if self.token_atual.tipo == T_INT:
                        self.use(T_INT)
                    elif self.token_atual.tipo == T_ID:
                        self.use(T_ID)
                    elif self.token_atual.tipo == T_STRING:
                        self.use(T_STRING)
                    return self.token_atual.valor <= self.dict[self.pilha.pop()]
                elif self.token_atual.valor == ">":
                    self.use(T_OPLOGICO)
                    if self.token_atual.tipo == T_INT:
                        self.use(T_INT)
                    elif self.token_atual.tipo == T_ID:
                        self.use(T_ID)
                    elif self.token_atual.tipo == T_STRING:
                        self.use(T_STRING)
                    return self.token_atual.valor > self.dict[self.pilha.pop()]
                elif self.token_atual.valor == "<":
                    self.use(T_OPLOGICO)
                    if self.token_atual.tipo == T_INT:
                        self.use(T_INT)
                    elif self.token_atual.tipo == T_ID:
                        self.use(T_ID)
                    elif self.token_atual.tipo == T_STRING:
                        self.use(T_STRING)
                    return self.token_atual.valor < self.dict[self.pilha.pop()]
                return

            return self.dict[self.pilha.pop()]

##############################################################################


patternStr = r'((?<![\\])[\'"])((?:.(?!(?<![\\])\1))*.?)\1'
patternComment = r'#(.*)'

class interpretador:

    def __init__(self):
        self.tokens = []
        self.arquivo = ''
        self.parser = None

    def loadfile(self,fileName):
        self.arquivo = open(fileName, 'r')

    def tokenizer(self):
        ln = 1


        for l in self.arquivo.readlines():

            # analisador lexico

            l = l.replace('\n', '')  # remove a quebra de linha

            if l != '':

                tes = re.findall(patternStr, l)
                for t in tes:
                    l = l.replace(t[1], t[1].replace(" ", "_"))

                m = re.search(patternComment, l)
                if m != None:
                    m2 = m.group()
                    l = l.replace(m2, m2.replace(" ", "_"))

            for token in l.split():
                try:
                    t = afd_principal(token)
                    if t!=None:
                        self.tokens.append(t)
                except Exception as e:
                    print(str(e) + " na posição %i da linha %i" % (l.index(token), ln))
                    raise StopExecution
            ln += 1

    def execParser(self):
        self.parser = Parser(self.tokens)
        return self.parser.statement()

if __name__ == '__main__':

    interpreter = interpretador()
    interpreter.loadfile("codigo.x")
    interpreter.tokenizer()

    result = interpreter.execParser()
