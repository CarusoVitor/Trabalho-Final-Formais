from afd_functions import AFD
from glud import GLUD

glud = GLUD("test.txt")
afd = AFD()
afd.glud_to_afd(glud)

words_list = ["b", "", "ab", "abc", "abab", "abcabc"]

print(words_list)
for word in words_list:
    print(f"word: {word} -> {afd.afd_test(word)}")
