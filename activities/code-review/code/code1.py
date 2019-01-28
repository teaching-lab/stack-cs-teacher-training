def roll_the_dice(six_probability):
    """ Simulates rolling dice with given prob of rolling 6 """
    if random.random() <= six_probability:
        return 6
    return random.randint(1, 5)


def game(board_size, print_state=True):
    """ Simulates the game """
    end_round = game_logic(board_size, print_state)
    if not print_state:
        return end_round


def game_logic(board_size, print_state, six_probability=1/6):
    """ Simulates the actual logic of the game """
    position = 0
    game_round = 0
    while position < board_size:
        game_round += 1
        if print_state:
            print("Round:", game_round, end="")
        position = game_move(board_size, position, print_state, six_probability)
        if print_state:
            print()
            print("I am on position:", position)
    if print_state:
        print("Game finished in Round", game_round)
    return game_round


def game_move(board_size, position, print_state, six_probability):
    """ Simulates a single move """
    new_position = position
    number_of_sixes = 0
    if print_state:
        print(" -- Rolled: ", end="")
    while number_of_sixes < 3:
        dice_roll = roll_the_dice(six_probability)
        if print_state:
            print(dice_roll, end=" ")
        if dice_roll + new_position > board_size:
            return position
        elif dice_roll != 6:
            return new_position + dice_roll
        new_position += dice_roll
        number_of_sixes += 1
    return position