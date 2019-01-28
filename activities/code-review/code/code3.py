def roll(prob):  # 'p' is the probability of rolling a six
    global roll_one
    global roll_two
    global roll_three
    global roll_sum
    pre_roll = random.random()

    def convert_pre_roll(pre_roll):
        if pre_roll < (1 - prob):
            for i in range(5):
                if i*((1-prob)/5) <= pre_roll < (i+1)*((1-prob)/5):
                    return i + 1
        else:
            return 6

    if convert_pre_roll(pre_roll) == 6:
        roll_one = 6
        pre_roll = random.random()
        if convert_pre_roll(pre_roll) == 6:
            roll_two = 6
            pre_roll = random.random()
            if convert_pre_roll(pre_roll) == 6:
                roll_three = 6
                roll_sum = -position
            else:
                roll_three = convert_pre_roll(pre_roll)
                roll_sum = roll_one + roll_two + roll_three
        else:
            roll_two = convert_pre_roll(pre_roll)
            roll_sum = roll_one + roll_two
    else:
        roll_one = convert_pre_roll(pre_roll)
        roll_sum = roll_one


def game(board_size, print_state=True, prob=1/6):
    position = 0
    round_count = 0

    while position != board_size:
        roll(prob)
        if position + roll_sum <= board_size:
            position += roll_sum
        round_count += 1
        if print_state:
            print("Round", round_count, "-- Roll:", end=" ")
            if roll_one != 6:
                print(roll_one)
            elif roll_two != 6:
                print(roll_one, roll_two)
            else:
                print(roll_one, roll_two, roll_three)
            print("I am on position", position)
    if print_state:
        print("Game finished in Round", round_count, end=".")
    else:
        return round_count
