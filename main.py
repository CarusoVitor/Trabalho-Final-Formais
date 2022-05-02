from afd_functions import AFD
from glud import GLUD

glud = GLUD("test.txt")
afd = AFD()
afd.glud_to_afd(glud)

words_list = ["b", "", "ab", "abc", "abab", "abcb", "abcab", "ababb", "abababb"]

for word in words_list:
    print(f"word: {word} -> {afd.test(word)}")