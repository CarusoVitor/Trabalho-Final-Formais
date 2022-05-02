class GLUD:
    def __init__(self, file_name):
        self.file_name = file_name
        self.name = ""
        self.var = []
        self.term = [""]
        self.prod = {}
        self.ini = ""
        self.parse_glud()

    def parse_glud(self):
        with open(self.file_name, "r") as f:
            glud_str = f.read().split("\n")
        # primeira linha - exemplo: ({A,B,C},{a,b,c},prod,A)
        defs = glud_str[0].split("=")
        self.name = defs[0]
        # ignora os dois primeiros chars: -> A,B,C},{a,b,c},prod,A)
        elements = defs[1][2:]

        # pega os indices das chaves abertas para a direita }, ou seja, onde acaba as variaveis e onde acaba os termos
        curly_brackets_index = [index for index in range(len(elements)) if elements[index] == "}"]

        # pega os elementos ate o primeiro }
        # A,B,C},{a,b,c},prod,A) -> A,B,C -> ABC -> [A,B,C]
        self.var.extend(list(elements[:curly_brackets_index[0]].replace(",", "")))

        # pega os elementos ate o segundo },
        # },{a,b,c},prod,A) -> a,b,c -> abc -> [a,b,c]
        self.term.extend(list(elements[curly_brackets_index[0]+3:curly_brackets_index[1]].replace(",", "")))

        # pega o indice da ultima virgula, para saber onde acaba o nome da produção
        last_comma = elements[curly_brackets_index[1]+2:].index(",")

        # },prod,A) -> prod
        last_char_prod_name = curly_brackets_index[1]+2+last_comma
        prod_name_def = elements[curly_brackets_index[1]+2:last_char_prod_name]

        # ,A) -> A
        self.ini = elements[curly_brackets_index[1]+2+last_comma+1]
        # segunda linha
        prod_name = glud_str[1]
        if prod_name_def != prod_name:
            raise Exception(f"Nome das produções não é igual ao nome definido\n{prod_name_def}!={prod_name}")
        # terceira linha em diante
        prods = glud_str[2:]
        for prod in prods:
            get_prod = prod.split("->")
            left = get_prod[0].strip()
            right = get_prod[1].strip()
            right_list = []
            # verifica se o termo da esquerda é uma variavel
            if left not in self.var:
                raise Exception(f"Variável {left} não está na lista de variáveis")
            # verifica o termo da direita
            # terminal - variavel
            if len(right) == 2:
                if right[0] in self.term and right[1] in self.var:
                    right_list = [right[0], right[1]]
            # variavel
            elif len(right) == 1:
                if right in self.var:
                    right_list = [right, ""]
            # vazio
            elif len(right) == 0:
                right_list = ["", ""]
            else:
                raise Exception(f"Termo da direita não esta na forma de GLUD")
            # verifica se a variavel ja esta no dicionario ou se precisa criar
            if left in self.prod:
                self.prod[left].append(right_list)
            else:
                self.prod[left] = [right_list]


glud = GLUD("test.txt")
print(glud.name)
print(glud.prod)
print(glud.var)
print(glud.term)
print(glud.ini)
