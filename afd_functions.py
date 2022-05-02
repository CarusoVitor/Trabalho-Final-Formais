class AFD:
    def __init__(self, alphabet, states, program_function, initial_state, final_states):
        self.alphabet = alphabet
        self.states = states
        self.program_function = program_function
        self.initial_state = initial_state
        self.final_states = final_states


def glud_to_afd(glud):
    """
    :param glud: estrutura que representa uma GLUD
    :return:
    - Estrutura que representa um AFD
    """
    program_function = {
        #FAZER AQUI A TRANSCRIÇÃO DOS DICIONÁRIOS
    }

    afd = AFD(glud.terminals, glud.variables, program_function, glud.inititalVariable, "qf")
    return afd


def afd_test(afd, word):
    """
    :param afd: estrutura que representa um AFD
    :param word: palavra a ser testada se é aceita pelo AFD
    :return:
    - True: se a palavra pertencer à ACEITA(AFD)
    - False: se a palavra não pertencer à ACEITA(AFD)
    """
    return afd_test_rec(afd, word, afd.initial_state, 0)  # começa o teste no estado inicial e com a primeira letra


def afd_test_rec(afd, word, current_state, word_index):
    """
    :param afd: estrutura que representa um AFD
    :param word: palavra a ser testada se é aceita pelo AFD
    :param current_state: estado atual em que estamos no AFD
    :param word_index: letra atual da palavra que estamos testando no AFD
    :return:
    - True: se a palavra pertencer à ACEITA(AFD)
    - False: se a palavra não pertencer à ACEITA(AFD)
    """
    if word_index == len(word):                     # se checou toda a palavra já
        return current_state in afd.final_states    # testa se estamos num estado final

    for transition in afd.program_function[current_state]:
        if transition[0] == word[word_index]:                               # se achou uma transição possível
            return afd_test_rec(afd, word, transition[1], word_index + 1)   # avança no AFD e atualiza a letra
        elif transition[0] == "":                                           # se achou uma transição vazia
            return afd_test_rec(afd, word, transition[1], word_index)       # avança no AFD e continua com a mesma letra

    return False                                    # se não achou nenhuma transição, rejeita por indefinição
