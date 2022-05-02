class AFD:
    def __init__(self, alphabet, states, program_function, initial_state, final_states):
        self.alphabet = alphabet
        self.states = states
        self.programFunction = program_function
        self.initialState = initial_state
        self.finalStates = final_states


def glud_to_afd(glud):
    program_function = {
        #FAZER AQUI A TRANSCRIÇÃO DOS DICIONÁRIOS
    }

    afd = AFD(glud.terminals, glud.variables, program_function, glud.inititalVariable, "qf")
    return afd


def afd_test(afd, word):
    return afd_test_rec(afd, word, afd.initial_state, 0)


def afd_test_rec(afd, word, current_state, word_index):
    if word_index == len(word):                 # if reached the end of the word
        if current_state in afd.final_states:    # and if it is in a final state of the AFD
            return True
        else:                                   # or if is not in a final state
            return False

    for transition in afd.program_function[current_state]:
        if transition[0] == word[word_index]:                               # if found a transition
            return afd_test_rec(afd, word, transition[1], word_index + 1)   # try the path and update current word index
        elif transition[0] == "":                                           # if found an empty transition
            return afd_test_rec(afd, word, transition[1], word_index)       # try the path with the same word index

    return False                                # if didn't found a possible transition, end test
