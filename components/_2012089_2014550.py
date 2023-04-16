import copy


def is_final(self):
        no_of_whites, no_of_blacks = 0, 0
        for i in range(8):
            for j in range(8):
                if self.board[i, j] == 1:
                    no_of_whites += 1
                elif self.board[i, j] == -1:
                    no_of_blacks += 1
        if self.final_state(self.board):
            if no_of_whites > no_of_blacks:
                print("AI won!")
            elif no_of_whites < no_of_blacks:
                print("You won!")
            elif no_of_whites == no_of_blacks:
                print("Tie!")

            print(f"Final score: \nBlack {no_of_blacks} - {no_of_whites} White")
            return True
        elif no_of_blacks == 0 or no_of_whites == 0:
            if no_of_blacks == 0:
                print("AI won!")
            else:
                print("You won!")
            print(f"Final score: \nBlack {no_of_blacks} - {no_of_whites} White")
            return True
        elif len(self.generate_possible_moves(1, self.board, False)) == 0 and len(self.generate_possible_moves(-1, self.board, False)) == 0:
            if no_of_whites > no_of_blacks:
                print("AI won!")
            elif no_of_whites < no_of_blacks:
                print("You won!")
            elif no_of_whites == no_of_blacks:
                print("Tie!")
            print(f"Final score: \nBlack {no_of_blacks} - {no_of_whites} White")
            return True
        
        return False



# Used to check on horizontal line for possible places
def horizontal_line(pos_x, pos_y, opposite_color, current_state):
    positions = list()

    table = current_state

    # RIGHT SIDE
    elements = list()
    for i in range(pos_y, 8):
        elements.append(table[pos_x][i])

    for i in range(pos_y + 1, 8):
        if table[pos_x][i] == 0:
            flag = True
            if i - 1 > pos_y:
                for j in range(i - 1, pos_y, -1):
                    if table[pos_x][j] != opposite_color:
                        flag = False
            else:
                flag = False
            if flag:
                positions.append((pos_x, i))

    # LEFT SIDE
    elements.clear()
    for i in range(pos_y, -1, -1):
        elements.append(table[pos_x][i])

    for i in range(pos_y - 1, -1, -1):
        if table[pos_x][i] == 0:
            flag = True
            if i + 1 < pos_y:
                for j in range(i + 1, pos_y):
                    if table[pos_x][j] != opposite_color:
                        flag = False
            else:
                flag = False
            if flag:
                positions.append((pos_x, i))

    return positions

# Used to check on vertical line for possible places
def vertical_line(pos_x, pos_y, opposite_color, current_state):
    positions = list()

    table = current_state

    # DOWN SIDE
    elements = list()
    for i in range(pos_x, 8):
        elements.append(table[i][pos_y])

    for i in range(pos_x + 1, 8):
        if table[i][pos_y] == 0:
            flag = True
            if i - 1 > pos_x:
                for j in range(i - 1, pos_x, -1):
                    if table[j][pos_y] != opposite_color:
                        flag = False
            else:
                flag = False
            if flag:
                positions.append((i, pos_y))

    # UPPER SIDE
    elements.clear()
    for i in range(pos_x, -1, -1):
        elements.append(table[i][pos_y])

    for i in range(pos_x - 1, -1, -1):
        if table[i][pos_y] == 0:
            flag = True
            if i + 1 < pos_x:
                for j in range(i + 1, pos_x):
                    if table[j][pos_y] != opposite_color:
                        flag = False
            else:
                flag = False
            if flag:
                positions.append((i, pos_y))

    return positions

# Used to check on principal diagonal for possible places
def principal_diagonal_line(pos_x, pos_y, opposite_color, current_state):
    positions = list()

    table = current_state

    # Ascending
    i, j = pos_x, pos_y

    elements = list()
    while i < 8 and j < 8:
        elements.append(table[i][j])
        i += 1
        j += 1

    i, j = pos_x, pos_y
    while i < 8 and j < 8:
        if table[i][j] == 0:
            flag = True
            if i - 1 > pos_x:
                row = i - 1
                col = j - 1
                while row > pos_x:
                    if table[row][col] != opposite_color:
                        flag = False
                    row -= 1
                    col -= 1
            else:
                flag = False
            if flag:
                positions.append((i, j))
        i += 1
        j += 1

    # Descending
    i, j = pos_x, pos_y
    elements.clear()
    while i > -1 and j > -1:
        elements.append(table[i][j])
        i -= 1
        j -= 1

    i, j = pos_x, pos_y
    while i > -1 and j > -1:
        if table[i][j] == 0:
            flag = True
            if i + 1 < pos_x:
                row = i + 1
                col = j + 1
                while row < pos_x:
                    if table[row][col] != opposite_color:
                        flag = False
                    row += 1
                    col += 1
            else:
                flag = False
            if flag:
                positions.append((i, j))
        i -= 1
        j -= 1

    return positions

# Used to check on secondary diagonal for possible places
def secondary_diagonal_line(pos_x, pos_y, opposite_color, current_state):
    positions = list()

    table = current_state

    # Ascending
    i, j = pos_x, pos_y

    elements = list()
    while i < 8 and j > -1:
        elements.append(table[i][j])
        i += 1
        j -= 1

    i, j = pos_x, pos_y
    while i < 8 and j > -1:
        if table[i][j] == 0:
            flag = True
            if i - 1 > pos_x:
                row = i - 1
                col = j + 1
                while row > pos_x:
                    if table[row][col] != opposite_color:
                        flag = False
                    row -= 1
                    col += 1
            else:
                flag = False
            if flag:
                positions.append((i, j))
        i += 1
        j -= 1

    # Descending
    i, j = pos_x, pos_y
    elements.clear()
    while i > -1 and j < 8:
        elements.append(table[i][j])
        i -= 1
        j += 1

    i, j = pos_x, pos_y
    while i > -1 and j < 8:
        if table[i][j] == 0:
            flag = True
            if i + 1 < pos_x:
                row = i + 1
                col = j - 1
                while row < pos_x:
                    if table[row][col] != opposite_color:
                        flag = False
                    row += 1
                    col -= 1
            else:
                flag = False
            if flag:
                positions.append((i, j))
        i -= 1
        j += 1

    return positions


def generate_possible_moves(color, current_state):
    all_moves = list()
    if color == -1:
        opposite_color = 1
    else:
        opposite_color = -1

    value = current_state
    for i in range(8):
        for j in range(8):
            if current_state[i][j] == color:
                h_l = horizontal_line(i, j, opposite_color, value)
                v_l = vertical_line(i, j, opposite_color, value)
                p_l = principal_diagonal_line(i, j, opposite_color, value)
                s_l = secondary_diagonal_line(i, j, opposite_color, value)

                if len(h_l) > 0:
                    for item in h_l:
                        all_moves.append(item)

                if len(v_l) > 0:
                    for item in v_l:
                        all_moves.append(item)

                if len(p_l) > 0:
                    for item in p_l:
                        all_moves.append(item)

                if len(s_l) > 0:
                    for item in s_l:
                        all_moves.append(item)

    return set(all_moves)


def heuristic_function(current_state, player_to_move):
        whites, blacks = 0, 0
        for i in range(8):
            for j in range(8):
                if current_state[i][j] == 1:
                    whites += 1
                elif current_state[i][j] == -1:
                    blacks += 1
        if player_to_move == 1:
            return whites - blacks
        else:
            return blacks - whites


def compare_states(state, board):
        last_position = None
        for i in range(8):
            for j in range(8):
                if board[i][j] == 0:
                    if state[i][j] == 1 or state[i][j] == -1:
                        last_position = (i, j)
        return last_position

def final_state(current_state):
        if current_state is None:
            return False

        empty_slot = False
        for i in range(8):
            for j in range(8):
                if current_state[i][j] == 0:
                    empty_slot = True
        if empty_slot:
            return False
        return True


def set_state_move(current_state, pos_x, pos_y, color):
        current_state[pos_x][pos_y] = color
        return create_state(current_state, pos_x, pos_y, color)


def create_state(current_state, pos_x, pos_y, color):
        directions = dict()
        if pos_x + 1 < 8:
            if current_state[pos_x + 1][pos_y] != color and current_state[pos_x + 1][pos_y] != 0:
                flag = True
                for i in range(pos_x + 2, 8):
                    if current_state[i][pos_y] == 0:
                        flag = False
                    if current_state[i][pos_y] == color and flag is True:
                        directions['vertical_jos'] = (i, pos_y)
                        break

        if pos_x - 1 > -1:
            if current_state[pos_x - 1][pos_y] != color and current_state[pos_x - 1][pos_y] != 0:
                flag = True
                for i in range(pos_x - 2, -1, -1):
                    if current_state[i][pos_y] == 0:
                        flag = False
                    if current_state[i][pos_y] == color and flag is True:
                        directions['vertical_sus'] = (i, pos_y)
                        break

        if pos_y + 1 < 8:
            if current_state[pos_x][pos_y + 1] != color and current_state[pos_x][pos_y + 1] != 0:
                flag = True
                for i in range(pos_y + 2, 8):
                    if current_state[pos_x][i] == 0:
                        flag = False
                    if current_state[pos_x][i] == color and flag is True:
                        directions['orizontal_dreapta'] = (pos_x, i)
                        break

        if pos_y - 1 > -1:
            if current_state[pos_x][pos_y - 1] != color and current_state[pos_x][pos_y - 1] != 0:
                flag = True
                for i in range(pos_y - 2, -1, -1):
                    if current_state[pos_x][i] == 0:
                        flag = False
                    if current_state[pos_x][i] == color and flag is True:
                        directions['orizontal_stanga'] = (pos_x, i)
                        break

        if pos_x + 1 < 8 and pos_y + 1 < 8:
            if current_state[pos_x + 1][pos_y + 1] != color and current_state[pos_x + 1][pos_y + 1] != 0:
                flag = True
                i, j = pos_x + 2, pos_y + 2
                while i < 8 and j < 8:
                    if current_state[i][j] == 0:
                        flag = False
                    if current_state[i][j] == color and flag is True:
                        directions['dp_descendent'] = (i, j)
                        break
                    i += 1
                    j += 1

        if pos_x - 1 > -1 and pos_y - 1 > -1:
            if current_state[pos_x - 1][pos_y - 1] != color and current_state[pos_x - 1][pos_y - 1] != 0:
                flag = True
                i, j = pos_x - 2, pos_y - 2
                while i > -1 and j > - 1:
                    if current_state[i][j] == 0:
                        flag = False
                    if current_state[i][j] == color and flag is True:
                        directions['dp_ascendent'] = (i, j)
                        break
                    i -= 1
                    j -= 1

        if pos_x + 1 < 8 and pos_y - 1 > -1:
            if current_state[pos_x + 1][pos_y - 1] != color and current_state[pos_x + 1][pos_y - 1] != 0:
                flag = True
                i, j = pos_x + 2, pos_y - 2
                while i < 8 and j > -1:
                    if current_state[i][j] == 0:
                        flag = False
                    if current_state[i][j] == color and flag is True:
                        directions['ds_descendent'] = (i, j)
                        break
                    i += 1
                    j -= 1

        if pos_x - 1 > -1 and pos_y + 1 < 8:
            if current_state[pos_x - 1][pos_y + 1] != color and current_state[pos_x - 1][pos_y + 1] != 0:
                flag = True
                i, j = pos_x - 2, pos_y + 2
                while i > -1 and j < 8:
                    if current_state[i][j] == 0:
                        flag = False
                    if current_state[i][j] == color and flag is True:
                        directions['ds_ascendent'] = (i, j)
                        break
                    i -= 1
                    j += 1

        if 'vertical_jos' in directions.keys():
            x, y = directions['vertical_jos']
            for i in range(pos_x + 1, x):
                current_state[i][pos_y] = color

        if 'vertical_sus' in directions.keys():
            x, y = directions['vertical_sus']
            for i in range(pos_x - 1, x, -1):
                current_state[i][pos_y] = color

        if 'orizontal_dreapta' in directions.keys():
            x, y = directions['orizontal_dreapta']
            for i in range(pos_y + 1, y):
                current_state[pos_x][i] = color

        if 'orizontal_stanga' in directions.keys():
            x, y = directions['orizontal_stanga']
            for i in range(pos_y - 1, y, -1):
                current_state[pos_x][i] = color

        if 'dp_descendent' in directions.keys():
            x, y = directions['dp_descendent']
            i, j = pos_x + 1, pos_y + 1
            while i < x and j < y:
                current_state[i][j] = color
                i += 1
                j += 1

        if 'dp_ascendent' in directions.keys():
            x, y = directions['dp_ascendent']
            i, j = pos_x - 1, pos_y - 1
            while i > x and j > y:
                current_state[i][j] = color
                i -= 1
                j -= 1

        if 'ds_descendent' in directions.keys():
            x, y = directions['ds_descendent']
            i, j = pos_x + 1, pos_y - 1
            while i < x and j > y:
                current_state[i][j] = color
                i += 1
                j -= 1

        if 'ds_ascendent' in directions.keys():
            x, y = directions['ds_ascendent']
            i, j = pos_x - 1, pos_y + 1
            while i > x and j < y:
                current_state[i][j] = color
                i -= 1
                j += 1

        return current_state


def alpha_beta(current_state, maximized_level, current_depth, alpha, beta, best_one, player_to_move):
        if current_depth == 0 or final_state(current_state) is True:
            return None, heuristic_function(current_state,  player_to_move)

        if maximized_level is True:
            value = float('-inf')
            possible_states = generate_possible_moves(player_to_move, current_state)
            for i in possible_states:
                copy_of_current_state = copy.deepcopy(current_state)
                new_state = set_state_move(copy_of_current_state, i[0], i[1], player_to_move)
                _, new_val = alpha_beta(new_state, False, current_depth - 1, alpha, beta, best_one, player_to_move)
                if new_val > value:
                    value = new_val
                    best_one = new_state
                if value > alpha:
                    alpha = value
                if alpha >= beta:
                    break
            return best_one, value
        else:
            value = float('inf')
            possible_states = generate_possible_moves( -player_to_move, current_state)
            for i in possible_states:
                copy_of_current_state = copy.deepcopy(current_state)
                new_state = set_state_move( copy_of_current_state, i[0], i[1], -player_to_move)
                _, new_val = alpha_beta( new_state, True, current_depth - 1, alpha, beta, best_one, -player_to_move)
                if new_val < value:
                    value = new_val
                    best_one = new_state
                if value < beta:
                    beta = value
                if beta <= alpha:
                    break
            return best_one, value


def alpha_beta_prunning(cur_state, player_to_move, remain_time, depth=4, ):
    legal_move = generate_possible_moves(player_to_move, cur_state)
    if len(legal_move) == 0:
        return None
    best_state, value = alpha_beta(cur_state, True, 4, float('-inf'), float('inf'), None, player_to_move)

    if best_state is not None:
        last_position = compare_states(best_state,cur_state)
        return last_position
    else:
        return legal_move.pop()


def select_move(cur_state, player_to_move, remain_time):
    return alpha_beta_prunning(cur_state, player_to_move, remain_time)




######## DEBUGGING START HERE ##########

board = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, -1, 0, 1, 1, 1, 1, 0],
            [0, 0, -1, 1, 1, 1, 0, 0],
            [0, 0, 0, -1, -1, -1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

print(select_move(board,1,60))
