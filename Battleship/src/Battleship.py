import sys as s

write_txt = open("Battleship.out", "w")
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', '']
number_1, number_2 = 0, 0


def main_function(): #receives inputs and sends them to the required function
    try:
        files = []
        try:
            ship_1 = open(s.argv[1], "r")
        except IOError:
            files.append(s.argv[1])
        try:
            ship_2 = open(s.argv[2], "r")
        except IOError:
            files.append(s.argv[2])
        try:
            move_1 = open(s.argv[3], "r")
        except IOError:
            files.append(s.argv[3])
        try:
            move_2 = open(s.argv[4], "r")
        except IOError:
            files.append(s.argv[4])
        if len(files) > 1:
            write("IOError: input files " + ', '.join(files) + " are not reachable.")
            exit()
        if len(files) == 1:
            write(f"IOError: input file {files[0]} is not reachable.")
            exit()
    except IndexError:
        write("kaBOOM: run for your life!")
    locations_of_ship_1 = {'B1': {}, 'B2': {}, 'P1': {}, 'P2': {}, 'P3': {}, 'P4': {}, 'D': {}, 'S': {}, 'C': {}}
    locations_of_ship_2 = {'B1': {}, 'B2': {}, 'P1': {}, 'P2': {}, 'P3': {}, 'P4': {}, 'D': {}, 'S': {}, 'C': {}}
    game_board_1, game_board_2 = {}, {}
    check_inputs(s.argv[1]), check_inputs(s.argv[2])
    location(ship_1, locations_of_ship_1, game_board_1), location(ship_2, locations_of_ship_2, game_board_2)
    game(move_1, move_2, locations_of_ship_1, locations_of_ship_2, game_board_1, game_board_2)


def location(ship, dictionary, game_board): #finds the locations of users' ships
    dictionary_of_ships = {}
    for i in range(1, 11):
        inputs = ship.readline().rstrip("\n").split(";")
        if len(inputs) != 10:
            write("kaBOOM: run for your life!")
            exit()
        for k in inputs:
            if len(k) != 1 and len(k) != 0:
                write("IndexError: Ship types can only be one character long.")
                exit()
            elif k not in ['B', 'P', 'C', 'D', 'S', '']:
                write("IndexError: Invalid ship type entered.")
                exit()
        for k in range(10):
            dictionary_of_ships[str(i) + letter[k]] = inputs[k]
            game_board[str(i) + letter[k]] = "-"
    liste_b, liste_p = [], []
    number_b, number_p = 0, 0
    for i in list(dictionary_of_ships.keys()):
        if dictionary_of_ships[i] == 'B':
            if i[:-1] == "1":
                dictionary_of_ships['0' + i[-1]] = ''
            if i[:-1] == "10":
                dictionary_of_ships['11' + i[-1]] = ''
            if i[-1] == "A":
                dictionary_of_ships[i[:-1] + letter[letter.index("A") - 1]] = ''
            if i[-1] == "J":
                dictionary_of_ships[i[:-1] + letter[letter.index("J") + 1]] = ''
            if dictionary_of_ships[str(int(i[:-1]) + 1) + i[-1]] == 'B' and dictionary_of_ships[str(int(i[:-1]) - 1) + i[-1]] != 'B' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) + 1]] != 'B' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) - 1]] != 'B' and i not in liste_b:
                number_b += 1
                dictionary["B" + str(number_b)][i] = ''
                dictionary["B" + str(number_b)][str(int(i[:-1]) + 1) + i[-1]] = ''
                dictionary["B" + str(number_b)][str(int(i[:-1]) + 2) + i[-1]] = ''
                dictionary["B" + str(number_b)][str(int(i[:-1]) + 3) + i[-1]] = ''
                liste_b.extend([i, str(int(i[:-1]) + 1) + i[-1], str(int(i[:-1]) + 2) + i[-1], str(int(i[:-1]) + 3) + i[-1]])
            elif dictionary_of_ships[str(int(i[:-1]) + 1) + i[-1]] != 'B' and dictionary_of_ships[str(int(i[:-1]) - 1) + i[-1]] == 'B' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) + 1]] != 'B' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) - 1]] != 'B' and i not in liste_b:
                number_b += 1
                dictionary["B" + str(number_b)][i] = ''
                dictionary["B" + str(number_b)][str(int(i[:-1]) - 1) + i[-1]] = ''
                dictionary["B" + str(number_b)][str(int(i[:-1]) - 2) + i[-1]] = ''
                dictionary["B" + str(number_b)][str(int(i[:-1]) - 3) + i[-1]] = ''
                liste_b.extend([i, str(int(i[:-1]) - 1) + i[-1], str(int(i[:-1]) - 2) + i[-1], str(int(i[:-1]) - 3) + i[-1]])
            elif dictionary_of_ships[str(int(i[:-1]) + 1) + i[-1]] != 'B' and dictionary_of_ships[str(int(i[:-1]) - 1) + i[-1]] != 'B' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) + 1]] == 'B' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) - 1]] != 'B' and i not in liste_b:
                number_b += 1
                dictionary["B" + str(number_b)][i] = ''
                dictionary["B" + str(number_b)][i[:-1] + letter[letter.index(i[-1]) + 1]] = ''
                dictionary["B" + str(number_b)][i[:-1] + letter[letter.index(i[-1]) + 2]] = ''
                dictionary["B" + str(number_b)][i[:-1] + letter[letter.index(i[-1]) + 3]] = ''
                liste_b.extend([i, i[:-1] + letter[letter.index(i[-1]) + 1], i[:-1] + letter[letter.index(i[-1]) + 2], i[:-1] + letter[letter.index(i[-1]) + 3]])
            elif dictionary_of_ships[str(int(i[:-1]) + 1) + i[-1]] != 'B' and dictionary_of_ships[str(int(i[:-1]) - 1) + i[-1]] != 'B' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) + 1]] != 'B' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) - 1]] == 'B' and i not in liste_b:
                number_b += 1
                dictionary["B" + str(number_b)][i] = ''
                dictionary["B" + str(number_b)][i[:-1] + letter[letter.index(i[-1]) - 1]] = ''
                dictionary["B" + str(number_b)][i[:-1] + letter[letter.index(i[-1]) - 2]] = ''
                dictionary["B" + str(number_b)][i[:-1] + letter[letter.index(i[-1]) - 3]] = ''
                liste_b.extend([i, i[:-1] + letter[letter.index(i[-1]) - 1], i[:-1] + letter[letter.index(i[-1]) - 2], i[:-1] + letter[letter.index(i[-1]) - 3]])
        if dictionary_of_ships[i] == 'P':
            if i[:-1] == "1":
                dictionary_of_ships['0' + i[-1]] = ''
            if i[:-1] == "10":
                dictionary_of_ships['11' + i[-1]] = ''
            if i[-1] == "A":
                dictionary_of_ships[i[:-1] + letter[letter.index("A") - 1]] = ''
            if i[-1] == "J":
                dictionary_of_ships[i[:-1] + letter[letter.index("J") + 1]] = ''
            if dictionary_of_ships[str(int(i[:-1]) + 1) + i[-1]] == 'P' and dictionary_of_ships[str(int(i[:-1]) - 1) + i[-1]] != 'P' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) + 1]] != 'P' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) - 1]] != 'P' and i not in liste_p:
                number_p += 1
                dictionary["P" + str(number_p)][i] = ''
                dictionary["P" + str(number_p)][str(int(i[:-1]) + 1) + i[-1]] = ''
                liste_p.extend([i, str(int(i[:-1]) + 1) + i[-1]])
            if dictionary_of_ships[str(int(i[:-1]) + 1) + i[-1]] != 'P' and dictionary_of_ships[str(int(i[:-1]) - 1) + i[-1]] == 'P' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) + 1]] != 'P' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) - 1]] != 'P' and i not in liste_p:
                number_p += 1
                dictionary["P" + str(number_p)][i] = ''
                dictionary["P" + str(number_p)][str(int(i[:-1]) - 1) + i[-1]] = ''
                liste_p.extend([i, str(int(i[:-1]) - 1) + i[-1]])
            if dictionary_of_ships[str(int(i[:-1]) + 1) + i[-1]] != 'P' and dictionary_of_ships[str(int(i[:-1]) - 1) + i[-1]] != 'P' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) + 1]] == 'P' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) - 1]] != 'P' and i not in liste_p:
                number_p += 1
                dictionary["P" + str(number_p)][i] = ''
                dictionary["P" + str(number_p)][i[:-1] + letter[letter.index(i[-1]) + 1]] = ''
                liste_p.extend([i, i[:-1] + letter[letter.index(i[-1]) + 1]])
            if dictionary_of_ships[str(int(i[:-1]) + 1) + i[-1]] != 'P' and dictionary_of_ships[str(int(i[:-1]) - 1) + i[-1]] != 'P' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) + 1]] != 'P' and dictionary_of_ships[i[:-1] + letter[letter.index(i[-1]) - 1]] == 'P' and i not in liste_p:
                number_p += 1
                dictionary["P" + str(number_p)][i] = ''
                dictionary["P" + str(number_p)][i[:-1] + letter[letter.index(i[-1]) - 1]] = ''
                liste_p.extend([i, i[:-1] + letter[letter.index(i[-1]) - 1]])
        if dictionary_of_ships[i] == 'S':
            dictionary['S'][i] = ''
        if dictionary_of_ships[i] == 'D':
            dictionary['D'][i] = ''
        if dictionary_of_ships[i] == 'C':
            dictionary['C'][i] = ''


def check_inputs(argv): #checks if the inputs are in the correct form
    list_of_inputs = []
    txt_open = open(argv, "r")
    for i in range(10):
        list_of_inputs.extend(txt_open.readline().rstrip("\n").split(";"))
    if list_of_inputs.count("D") != 3 or list_of_inputs.count("C") != 5 or list_of_inputs.count("S") != 3 or list_of_inputs.count("P") != 8 or list_of_inputs.count("B") != 8:
        write("IndexError: The ships in the file are not the required number.")
        exit()


def game(move_1, move_2, location_1, location_2, game_board_1, game_board_2): #the function where the playing of the game and the ending of the game take place
    global number_1, number_2
    P1, B1, C1, D1, S1 = ["-", "-", "-", "-"], ["-", "-"], ["-"], ["-"], ["-"]
    P2, B2, C2, D2, S2 = ["-", "-", "-", "-"], ["-", "-"], ["-"], ["-"], ["-"]
    player1_turn = move_1.readline().rstrip("\n").split(";")
    player2_turn = move_2.readline().rstrip("\n").split(";")
    number_of_round = 0
    for i in range(2, len(player1_turn) + len(player2_turn)):
        if i % 2 == 0:
            x = "1"
            number_of_round += 1
            write("Player1's Move\n")
            write(f"Round : {number_of_round}\t\t\t\t\tGrid Size: 10x10\n")
            write("Player1's Hidden Board\t\tPlayer2's Hidden Board")
            create_board(game_board_1, game_board_2, C1, D1, S1, P1, B1, C2, D2, S2, P2, B2)
            change_board(player1_turn, game_board_2, location_2, C2, D2, S2, P2, B2, x)
            number_1 += 1
        if i % 2 == 1:
            x = "2"
            write("Player2's Move\n")
            write(f"Round : {number_of_round}\t\t\t\t\tGrid Size: 10x10\n")
            write("Player1's Hidden Board\t\tPlayer2's Hidden Board")
            create_board(game_board_1, game_board_2, C1, D1, S1, P1, B1, C2, D2, S2, P2, B2)
            change_board(player2_turn, game_board_1, location_1, C1, D1, S1, P1, B1, x)
            number_2 += 1
            if "-" not in C1 and "-" not in P1 and "-" not in S1 and "-" not in B1 and "-" not in D1 and "-" not in C2 and "-" not in P2 and "-" not in S2 and "-" not in B2 and "-" not in D2:
                pass
            elif "-" not in C2 and "-" not in P2 and "-" not in S2 and "-" not in B2 and "-" not in D2:
                write("Player1 Wins!\n")
                for k in list(location_1.keys()):
                    for j in list(location_1[k].keys()):
                        if location_1[k][j] == '':
                            game_board_1[j] = k[0]
                write("Final Information\n")
                write("Player1's Board\t\t\t\tPlayer2's Board")
                create_board(game_board_1, game_board_2, C1, D1, S1, P1, B1, C2, D2, S2, P2, B2)
                exit()
        if "-" not in C1 and "-" not in P1 and "-" not in S1 and "-" not in B1 and "-" not in D1 and "-" not in C2 and "-" not in P2 and "-" not in S2 and "-" not in B2 and "-" not in D2:
            write("It is a Draw!\n")
            write("Final Information\n")
            write("Player1's Board\t\t\t\tPlayer2's Board")
            create_board(game_board_1, game_board_2, C1, D1, S1, P1, B1, C2, D2, S2, P2, B2)
            exit()
        elif "-" not in C1 and "-" not in P1 and "-" not in S1 and "-" not in B1 and "-" not in D1:
            write("Player2 Wins!\n")
            for k in list(location_2.keys()):
                for j in list(location_2[k].keys()):
                    if location_2[k][j] == '':
                        game_board_2[j] = k[0]
            write("Final Information\n")
            write("Player1's Board\t\t\t\tPlayer2's Board")
            create_board(game_board_1, game_board_2, C1, D1, S1, P1, B1, C2, D2, S2, P2, B2)
            exit()


def change_board(turn, board, location, C, D, S, P, B, x): #function where changes are made to the game board
    letterss = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    global number_1, number_2
    if x == "1":
        number = number_1
    if x == "2":
        number = number_2
    number -= 1
    while True:
        number += 1
        write(f"Enter your move: {turn[number]}")
        if number == len(turn) - 1:
            write("ValueError: Moves are over")
            exit()
        try:
            int(turn[number].split(",")[0])
        except ValueError:
            write("ValueError: First part of the move must consist of certain numbers")
            continue
        if len(turn[number].split(",")) != 2:
            write("ValueError: There are too many commas in the input")
            continue
        elif turn[number].split(",")[1] not in letterss:
            write("ValueError: Second part of the move must consist of certain letters")
            continue
        elif int(turn[number].split(",")[0]) > 10:
            write("AssertionError: Invalid Operation.")
            continue
        elif letterss.index(turn[number].split(",")[1]) > 9:
            write("AssertionError: Invalid Operation.")
            continue
        elif board[turn[number][:-2] + turn[number][-1]] == "X" or board[turn[number][:-2] + turn[number][-1]] == "O":
            write("AssertionError: Invalid Operation.")
            continue
        write("")
        break
    compare = False
    for i in list(location.keys()):
        for k in list(location[i].keys()):
            if k == turn[number][:-2] + turn[number][-1]:
                compare = True
                location[i][k] = "X"
    if compare:
        board[turn[number][:-2] + turn[number][-1]] = "X"
    else:
        board[turn[number][:-2] + turn[number][-1]] = "O"
    if '' not in list(location['S'].values()):
        S[0] = 'X'
    if '' not in list(location['D'].values()):
        D[0] = 'X'
    if '' not in list(location['C'].values()):
        C[0] = 'X'
    p = 0
    for i in range(1, 5):
        if '' not in list(location['P' + str(i)].values()):
            p += 1
            location['P' + str(i)][''] = ''
            if P[0] == '-':
                P[0] = 'X'
            elif P[1] == '-':
                P[1] = 'X'
            elif P[2] == '-':
                P[2] = 'X'
            elif P[3] == '-':
                P[3] = 'X'
    b = 0
    for i in range(1, 3):
        if '' not in list(location['B' + str(i)].values()):
            b += 1
            location['B' + str(i)][''] = ''
            if B[0] == '-':
                B[0] = 'X'
            elif B[1] == '-':
                B[1] = 'X'
    if x == "1":
        number_1 = number
    if x == "2":
        number_2 = number


def create_board(game_board_1, game_board_2, C1, D1, S1, P1, B1, C2, D2, S2, P2, B2): #function that prints the game board
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    write("  " + ' '.join(letters) + "\t\t  " + ' '.join(letters))
    for i in range(1, 11):
        write_txt.write(f"{i}")
        print(f"{i}", end="")
        for k in range(10):
            if i == 10 and k == 0:
                write_txt.write(game_board_1[str(i) + letter[k]])
                print(game_board_1[str(i) + letter[k]], end="")
            else:
                write_txt.write(" " + game_board_1[str(i) + letter[k]])
                print(" " + game_board_1[str(i) + letter[k]], end="")
        write_txt.write("\t\t")
        print("\t\t", end="")
        write_txt.write(f"{i}")
        print(f"{i}", end="")
        for k in range(10):
            if i == 10 and k == 0:
                write_txt.write(game_board_2[str(i) + letter[k]])
                print(game_board_2[str(i) + letter[k]], end="")
            else:
                write_txt.write(" " + game_board_2[str(i) + letter[k]])
                print(" " + game_board_2[str(i) + letter[k]], end="")
        write("")
    write("")
    write("Carrier\t\t" + ' '.join(C1) + "\t\t\t\tCarrier\t\t" + ' '.join(C2))
    write("Battleship\t" + ' '.join(B1) + "\t\t\t\tBattleship\t" + ' '.join(B2))
    write("Destroyer\t" + ' '.join(D1) + "\t\t\t\tDestroyer\t" + ' '.join(D2))
    write("Submarine\t" + ' '.join(S1) + "\t\t\t\tSubmarine\t" + ' '.join(S2))
    write("Patrol Boat\t" + ' '.join(P1) + "\t\t\tPatrol Boat\t" + ' '.join(P2) + "\n")


def write(message): #function that prints errors and game both to command line and txt file
    print(message)
    write_txt.write(message + "\n")


write("Battle of Ships Game\n")
main_function()

# Erdinç Arıcı
# 2210356035
