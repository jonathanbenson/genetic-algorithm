
from random import randint, choice

WORD_LENGTH = 10
NUM = 42
HI = 100
LO = 1

letters = 'abcdefghijklmnopqrstuvwxyz'

def random_word(length) :
    word = ''
    for i in range(length) :
        word += choice(letters)
    return word


file_contents = ''

for i in range(NUM) :
    file_contents += f'{random_word(WORD_LENGTH)},{randint(LO, HI)}'

    if i < NUM - 1 :
        file_contents += '\n'

with open('data.csv', 'w') as writer :
    writer.write(file_contents)
