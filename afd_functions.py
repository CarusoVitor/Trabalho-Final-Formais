from itertools import product


class AFD:
    def __init__(self):
        self.alphabet = []
        self.states = []
        self.program_function = {}
        self.initial_state = ""
        self.final_states = []

    def glud_to_afd(self, glud):
        """
        :param glud: estrutura que representa uma GLUD
        :return:
        - Estrutura que representa um AFD
        """
        # Repassa todas as produções para o dicionário da função programa do AFD
        self.program_function = glud.productions.copy()
        self.final_states.append("Qf")

        # Troca as produções que não possuem variáveis no lado direito por transições para um estado final
        for transitions in self.program_function:
            for transition in self.program_function[transitions]:
                if transition[1] == "":
                    transition[1] = self.final_states[0]

        self.alphabet = glud.terminals.copy()
        self.states = glud.variables.copy()
        self.states.append("Qf")
        self.initial_state = glud.initial_variable

    def test_rec(self, word, current_state, word_index):
        """
        :param word: palavra a ser testada se é aceita pelo AFD
        :param current_state: estado atual em que estamos no AFD
        :param word_index: letra atual da palavra que estamos testando no AFD
        :return:
        - True: se a palavra pertencer à ACEITA(AFD)
        - False: se a palavra não pertencer à ACEITA(AFD)
        """
        valid_state = False
        word_len = len(word)

        # se checou toda a palavra e estamos num estado final
        if word_index == word_len and current_state in self.final_states:
            return True

        for state in self.program_function.keys():      # Verifica se existe transição começando no estado atual
            if state == current_state:
                valid_state = True
                break

        if not valid_state:
            return False

        for transition in self.program_function[current_state]:        # Verifica todas as transições do estado atual
            if word_index != word_len and transition[0] == word[word_index] :  # se achou uma transição possível
                if self.test_rec(word, transition[1], word_index + 1): # avança no AFD e atualiza a letra
                    return True
            elif transition[0] == "":                                  # se achou uma transição vazia
                if self.test_rec(word, transition[1], word_index):     # avança no AFD e continua com a mesma letra
                    return True

        return False                                    # se não achou nenhuma transição, rejeita por indefinição

    def test(self, word):
        """
        :param word: palavra a ser testada se é aceita pelo AFD
        :return:
        - True: se a palavra pertencer à ACEITA(AFD)
        - False: se a palavra não pertencer à ACEITA(AFD)
        """
        return self.test_rec(word, self.initial_state, 0)  # começa o teste no estado inicial e com a primeira letra

    def is_finite(self):
        """
        :return:
        - True: se a linguagem ACEITA(AFD) for finita
        - False: se a linguagem ACEITA(AFD) for infinita
        """
        is_finite = True
        words = self.generate_all_words()
        if "" in words:
            words.remove("")

        for word in words:
            if self.test(word):
                is_finite = False
                break

        return is_finite

    def generate_all_words(self):
        """
        Gera todas as palavras de tamanho w com os caractares do alfabeto, em que n <= w < 2n,
        sendo n o numero de estados do autômato
        """
        words = []
        for i in range(len(self.states), len(self.states)*2):
            words.extend(product(self.alphabet, repeat=i))
        words_list = ["".join(word_tuple) for word_tuple in words]
        return words_list

    def test_words(self, file_name):
        """
        Testa todas as palavras de uma lista de palavras
        :param file_name: nome do arquivo txt contendo a lista de palavras
        """
        with open(file_name,"r") as f:
            for line in f:
                # não pega o \n
                word = line[:-1]
                accept = self.test(word)
                print(f"palavra: {word} -> {'Aceita' if accept else 'Recusa'}")

    def __str__(self):
        alphabet = f"Alfabeto: {self.alphabet}\n"
        states = f"Estados: {self.states}\n"
        initial_states = f"Estado inicial: {self.initial_state}\n"
        final_states = f"Estado final: {self.final_states[0]}\n"
        pf = f"Função programa: {self.program_function}\n"

        return alphabet + states + initial_states + final_states + pf

