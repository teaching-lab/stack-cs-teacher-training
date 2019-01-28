def game(board_size, print_state=True):
    position = 0
    round_ = 0
    while position <= board_size - 1:    
        number = randint(1, 6)
        number_2 = 0
        number_3 = 0
        if number == 6:
            if board_size - position < number:
                number_2 = randint(1, 6)
                if number_2 == 6:
                    if board_size - position - number < number_2:
                        number_3 = randint(1, 6)
                        if number_3 == 6:
                            position = 0
        round_ += 1
        if position + number + number_2 + number_3 <= board_size and number_3 != 6:
            position += number + number_2 + number_3
        if print_state == True:
            print("Round", round_, "--", "Roll: ", number, str(number_2).replace("0", ""), str(number_3).replace("0", ""))
            print("I am on position", position)
    if print_state == False:
        return round_
    else:
        print("Game finished in Round ", round_)