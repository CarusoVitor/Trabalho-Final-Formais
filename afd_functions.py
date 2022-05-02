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
        for production in glud.productions:
            self.program_function[production] = glud.productions[production]
        self.final_states.append("Qf")

        # Troca as produções que não possuem variáveis no lado direito por transições para um estado final
        for transitions in self.program_function:
            for transition in self.program_function[transitions]:
                if transition[1] == "":
                    transition[1] = self.final_states[0]

        self.alphabet = glud.terminals
        self.states = glud.variables
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
