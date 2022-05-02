class AFD:
    def __init__(self):
        self.alphabet = [""]
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
        for production in glud.prod:
            self.program_function[production] = glud.prod[production]
        self.final_states.append("Qf")

        # Troca as produções que não possuem variáveis no lado direito por transições para um estado final
        for transitions in self.program_function:
            for transition in self.program_function[transitions]:
                if transition[1] == "":
                    transition[1] = self.final_states[0]

        self.alphabet = glud.term
        self.states = glud.var
        self.initial_state = glud.ini

    def afd_test(self, word):
        """
        :param word: palavra a ser testada se é aceita pelo AFD
        :return:
        - True: se a palavra pertencer à ACEITA(AFD)
        - False: se a palavra não pertencer à ACEITA(AFD)
        """
        return afd_test_rec(self, word, afd.initial_state, 0)  # começa o teste no estado inicial e com a primeira letra


    def afd_test_rec(self, word, current_state, word_index):
        """
        :param word: palavra a ser testada se é aceita pelo AFD
        :param current_state: estado atual em que estamos no AFD
        :param word_index: letra atual da palavra que estamos testando no AFD
        :return:
        - True: se a palavra pertencer à ACEITA(AFD)
        - False: se a palavra não pertencer à ACEITA(AFD)
        """
        if word_index == len(word):                     # se checou toda a palavra já
            return current_state in self.final_states    # testa se estamos num estado final

        for transition in self.program_function[current_state]:
            if transition[0] == word[word_index]:                               # se achou uma transição possível
                return afd_test_rec(self, word, transition[1], word_index + 1)  # avança no AFD e atualiza a letra
            elif transition[0] == "":                                           # se achou uma transição vazia
                return afd_test_rec(self, word, transition[1], word_index)      # avança no AFD e continua com a mesma letra

        return False                                    # se não achou nenhuma transição, rejeita por indefinição
