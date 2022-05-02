from afd_functions import AFD
from glud import GLUD
from time import sleep

glud_file = input("Digite o nome do arquivo da GLUD: ")
if ".txt" not in glud_file:
    glud_file += ".txt"

glud = GLUD(glud_file)
print("GLUD:")
sleep(1)
print(glud)

print("AFD:")
afd = AFD()
afd.glud_to_afd(glud)
sleep(1)
print(afd)

words_file = input("Digite o nome do arquivo da lista de palavras: ")
if ".txt" not in words_file:
    words_file += ".txt"

print("Teste lista de palavras:")
sleep(1)
afd.test_words(words_file)

is_finite = afd.is_finite()
print("\nA linguagem é finita?")
sleep(1)
print(f"{'Sim' if is_finite else 'Não'}")
