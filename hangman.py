# hahaha = [
#     '          -----------          ',
#     '          | 明天上线 |              ',
#     '          -----------          ',
#     '                                ',
#     '--------                --------',
#     '|  怎  |                |  这  |',
#     '|  么  |                |  个  |',
#     '|  实  |                |  需  |',
#     '|  现  |                |  求  |',
#     '|  我  |                |  很  |',
#     '|  不  |                |  简  |',
#     '|  管  |                |  单  |',
#     '--------                --------',
# ]

# for row in hahaha:
#     print(row)

#%%
def hangman(word):
    wrong = 0
    stages = ['_______          ',
              '|                ',
              '|         |      ',
              '|         O      ',
              '|        /|\     ',
              '|        / \     ',
              '|                '
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcome to Hangman')
    for row in stages:
        print(row)
    print('Save me young man!')

    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Guess a letter： '
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print('\n')
        print('The word is: \n')
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('You win!')
            print('It was: ' + ''.join(board))
            win = True
            input()
            break

    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose! It was {}.'.format(word))
        input()


hangman('excited')
