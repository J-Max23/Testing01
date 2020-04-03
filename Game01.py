import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_______         ",
              "|               ",
              "|      |        ",
              "|      0        ",
              "|     /|\       ",
              "|     / \       ",
              "|               "
              ]
    rletters = list(word)
    print rletters
    board = ["_"] * len(word)
    win = False
    print ("Welcome to Hangman")

    while wrong < len(stages) -1:
        print ("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            print cind
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print (" ".join(board))
        e = wrong +1
        print ("\n".join(stages[0:e]))
        if "_" not in board:
            print ("You Win!!!")
            print (" ".join(board))
            win = True
            break
    if not win:
        print ("\n".join(stages[0:wrong]))
        print ("You lose! It was {}.".format(word))

Word_list = ["cat","Dog","Mouse","Cup","Tom","Tim","Annie","Bear"]
Excep_list = "".join(random.sample(Word_list,3))
print (Excep_list)
hangman(Excep_list)


