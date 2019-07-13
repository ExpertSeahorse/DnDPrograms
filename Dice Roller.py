from random import randint


def dice_roller(dice_ct=None, dice_size=None, to_beat=None):
    # If there was no input passed...
    if not dice_ct and not dice_size and not to_beat:
        print("Enter number and size of dice to roll (count, size, AC to beat)")
        # Enter the input needed and convert to a list on the ','s
        raw_specs = input().split(",")
    else:
        raw_specs = (dice_ct, dice_size, to_beat)
    # For each of the inputs, strip the spaces and the d (ex. for d20)
    raw_specs = [entry.strip(" d") for entry in raw_specs]

    # Assign the list to variables for readability
    dice_ct = int(raw_specs[0])
    dice_size = int(raw_specs[1])
    # If there is not a number to beat, return 0
    try:
        to_beat = int(raw_specs[2])
    except IndexError:
        to_beat = 0

    total = 0
    dice_roll_list = []
    total_succeed = 0
    # for the number of dice to be rolled...
    for i in range(0, dice_ct):
        # Generate a roll based on the size of the die
        roll = randint(1, dice_size + 1)
        # add that number to the total
        total += roll
        # add that roll to the roll list
        dice_roll_list.append(roll)
        # If the roll beats the number to beat, add 1 to the number of successes
        if roll >= to_beat:
            total_succeed += 1

    # creates pack to simplify returning a value
    pack = {'dice_roll_list': dice_roll_list,
            'total': total}
    print("The rolls were:", *dice_roll_list)
    print("The total was:", total)
    # if there was a number to beat...
    if to_beat:
        # Print the result and add the value to the pack for output
        print("Total succeeding rolls:", total_succeed)
        pack['total_succeed'] = total_succeed
    return pack


if __name__ == '__main__':
    # If running this program directly,
    dice_roller()
