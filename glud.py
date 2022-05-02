class GLUD:
    def __init__(self, file_name):
        self.file_name = file_name
        self.name = ""
        self.variables = []
        self.terminals = [""]
        self.productions = {}
        self.initial_variable = ""
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
        self.variables.extend(list(elements[:curly_brackets_index[0]].replace(",", "")))

        # pega os elementos ate o segundo },
        # },{a,b,c},prod,A) -> a,b,c -> abc -> [a,b,c]
        self.terminals.extend(list(elements[curly_brackets_index[0]+3:curly_brackets_index[1]].replace(",", "")))

        # pega o indice da ultima virgula, para saber onde acaba o nome da produção
        last_comma = elements[curly_brackets_index[1]+2:].index(",")

        # },prod,A) -> prod
        last_char_prod_name = curly_brackets_index[1]+2+last_comma
        prod_name_def = elements[curly_brackets_index[1]+2:last_char_prod_name]

        # ,A) -> A
        self.initial_variable = elements[last_char_prod_name+1]
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
            if left not in self.variables:
                raise Exception(f"Variável {left} não está na lista de variáveis")
            # verifica o termo da direita
            # terminal - variavel
            if len(right) == 2:
                if right[0] in self.terminals and right[1] in self.variables:
                    right_list = [right[0], right[1]]
                else:
                    raise Exception(f"Termo da direita não esta na forma de GLUD")
            # variavel
            elif len(right) == 1:
                if right in self.terminals:
                    right_list = [right, ""]
                else:
                    raise Exception(f"Termo da direita não esta na forma de GLUD")
            # vazio
            elif len(right) == 0:
                right_list = ["", ""]
            else:
                raise Exception(f"Termo da direita não esta na forma de GLUD")
            # verifica se a variavel ja esta no dicionario ou se precisa criar
            if left in self.productions:
                self.productions[left].append(right_list)
            else:
                self.productions[left] = [right_list]


if __name__ == "__main__":
    glud = GLUD("test.txt")
    print(glud.name)
    print(glud.productions)
    print(glud.variables)
    print(glud.terminals)
    print(glud.initial_variable)
