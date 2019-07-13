from random import randint


def dice_roller(dice_ct=None, dice_size=None, to_beat=None):
    if not dice_ct and not dice_size and not to_beat:
        print("Enter number and size of dice to roll (count, size, AC to beat)")
        raw_specs = input().split(",")
        raw_specs = [entry.strip(" d") for entry in raw_specs]
        dice_ct = int(raw_specs[0])
        dice_size = int(raw_specs[1])
        try:
            to_beat = int(raw_specs[2])
        except IndexError:
            to_beat = 0

    total = 0
    dice_roll_list = []
    total_succeed = 0
    for i in range(0, dice_ct):
        roll = randint(1, dice_size + 1)
        total += roll
        dice_roll_list.append(roll)
        if roll >= to_beat:
            total_succeed += 1

    print("The rolls were:", *dice_roll_list)
    print("The total was:", total)
    if to_beat:
        print("Total succeeding rolls:", total_succeed)


if __name__ == '__main__':
    dice_roller()