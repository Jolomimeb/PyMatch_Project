import random

# creates the map
def create_map(rows, cols, seed):
    the_map = []

    file_name = input("What is the symbol file name?: ")
    with open(file_name, 'r') as my_file:
        read_text = my_file.read()
        new_read = read_text.split()

    random.seed(seed)

    for i in range(rows):
        line = []
        for j in range(cols):
            line.append(random.choice(new_read))
        the_map.append(line)

    return the_map


# displays the map
def display_map(the_map):
    for row in the_map:
        for x in row:
            print(x.rjust(3), end='')
        print()


# function to count the number of times a symbol appears
def count_occurrence(grid, x, y):
    item_counter = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[x][y] in grid[i][j]:
                item_counter += 1
    return item_counter


def play_game(rows, cols):
    count = 0

    check_list = []
    dotmap = []

    # makes a new list that carries the symbols and dots
    for i in range(rows):
        line = []
        for j in range(cols):
            line.append('.')
        dotmap.append(line)
    while my_map != dotmap:
        count += 1
        if count <= 1:
            display_map(dotmap)

        guess_pos = input('Enter a position to guess: ').split()

        pos_x = int(guess_pos[0]) - 1
        pos_y = int(guess_pos[1]) - 1

        # checks to see if a position has already been picked
        while guess_pos in check_list:
            print('You already picked there pick again')
            guess_pos = input('Enter a position to guess: ').split()
            pos_x = int(guess_pos[0]) - 1
            pos_y = int(guess_pos[1]) - 1

        check_list.append(guess_pos)

        # checks for out of bounds
        while (pos_x + 1) > len(dotmap) or (pos_y + 1) > len(dotmap[0]):
            print('You went out of bounds pick again')
            guess_pos = input('Enter a position to guess: ').split()
            pos_x = int(guess_pos[0]) - 1
            pos_y = int(guess_pos[1]) - 1
            check_list.append(guess_pos)

        # adds the symbol to the new list when selected
        dotmap[pos_x][pos_y] = my_map[pos_x][pos_y]

        # counts the number of the symbol in the element and tells the user how many is left
        old_symbol_amount = count_occurrence(my_map, pos_x, pos_y)
        new_symbol_amount = count_occurrence(dotmap, pos_x, pos_y)

        if new_symbol_amount == old_symbol_amount and (dotmap[pos_x][pos_y] == my_map[pos_x][pos_y]):
            print(f'You have found all the {dotmap[pos_x][pos_y]}')

        else:
            prev_symbol = dotmap[pos_x][pos_y]

            while new_symbol_amount != old_symbol_amount and (dotmap[pos_x][pos_y] == my_map[pos_x][pos_y]):

                old_symbol_amount = count_occurrence(my_map, pos_x, pos_y)
                new_symbol_amount = count_occurrence(dotmap, pos_x, pos_y)

                if new_symbol_amount != old_symbol_amount:
                    display_map(dotmap)
                    guess_pos = input(f'Enter a position to guess that matches {dotmap[pos_x][pos_y]} '
                                      f'There are {old_symbol_amount - new_symbol_amount} positions remaining: ').split()

                    pos_x = int(guess_pos[0]) - 1
                    pos_y = int(guess_pos[1]) - 1

                    # checks for out of bounds
                    while (pos_x + 1) > len(dotmap) or (pos_y + 1) > len(dotmap[0]):
                        print('You went out of bounds pick again')
                        guess_pos = input('Enter a position to guess: ').split()
                        pos_x = int(guess_pos[0]) - 1
                        pos_y = int(guess_pos[1]) - 1

                    curr_symbol = my_map[pos_x][pos_y]

                    # checks to see if the previous symbol is the same as the current symbol
                    if curr_symbol == prev_symbol:

                        # checks to see if a position has already been picked
                        while guess_pos in check_list:
                            print('You already picked there pick again')
                            guess_pos = input(f'Enter a position to guess that matches {dotmap[pos_x][pos_y]} '
                                              f'There are {old_symbol_amount - new_symbol_amount} positions remaining: ').split()
                            pos_x = int(guess_pos[0]) - 1
                            pos_y = int(guess_pos[1]) - 1

                        # checks for out of bounds
                        while (pos_x + 1) > len(dotmap) or (pos_y + 1) > len(dotmap[0]):
                            print('You went out of bounds pick again')
                            guess_pos = input('Enter a position to guess: ').split()
                            pos_x = int(guess_pos[0]) - 1
                            pos_y = int(guess_pos[1]) - 1

                        check_list.append(guess_pos)

                        # adds the symbol to the new list when selected
                        dotmap[pos_x][pos_y] = my_map[pos_x][pos_y]

                    else:
                        # adds the symbol to the new list when selected
                        dotmap[pos_x][pos_y] = my_map[pos_x][pos_y]
                        print('no match this time')
                        display_map(dotmap)
                        print('Try again!')
                        # clears the board
                        for i in range(len(dotmap)):
                            for j in range(len(dotmap)):
                                if dotmap[i][j] == prev_symbol:
                                    dotmap[i][j] = '.'
                                    check_list.pop()
                                elif dotmap[i][j] == curr_symbol:
                                    dotmap[i][j] = '.'
                else:
                    print(f'You have found all the {dotmap[pos_x][pos_y]}')

        display_map(dotmap)

    if dotmap == my_map:
        print('Congratulations you win!')
    return


if __name__ == '__main__':
    print('Welcome to PyMatch')
    my_new_map = input('Enter rows cols and seed separated by comma: ').split(',')
    rows = int(my_new_map[0])
    cols = int(my_new_map[1])
    seed = int(my_new_map[2])

    my_map = create_map(rows, cols, seed)
    play_game(rows, cols)
