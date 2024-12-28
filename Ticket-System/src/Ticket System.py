import sys

txt_read = open(sys.argv[1], "r")
txt_write = open("output.txt", "w")
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
category = {}

def main(): #This function takes all the input and sends it to the required function.
    for j in range(len(open(sys.argv[1], "r").readlines())):
        inputs = txt_read.readline().rstrip("\n").split(" ")
        if inputs[0] == "CREATECATEGORY": create_category(inputs)
        if inputs[0] == "SELLTICKET": sell_ticket(inputs)
        if inputs[0] == "CANCELTICKET": cancel_ticket(inputs)
        if inputs[0] == "BALANCE": balance(inputs)
        if inputs[0] == "SHOWCATEGORY": show_category(inputs)

def create_category(x): #This function creates the desired category if the input is in the correct format.
    if int(x[2].split("x")[0]) > 26: return
    if x[1][-2] not in ["1", "2"]: return
    if x[1] in category:
        write(f"Warning: Cannot create the category for the second time. The stadium has already {x[1]}")
        return
    category[x[1]] = {}
    for i in range(int(x[2].split("x")[0])):
        for k in range(int(x[2].split("x")[1])):
            category[x[1]][letter[i] + str(k)] = "X"
    write(f"The category '{x[1]}' having {len(category[x[1]])} seats has been created")

def sell_ticket(x): #This function sells the ticket of that seat according to the occupancy of the desired seat.
    if x[2] == "student": x[2] = "S"
    if x[2] == "full": x[2] = "F"
    if x[2] == "season": x[2] = "T"
    if x[3] not in category: return
    for i in range(4, len(x)):
        if len(x[i]) <= 3:
            if (x[i][0] + "0") not in category[x[3]] and int(x[i][1:]) > int(list(category[x[3]])[-1][1:]):
                write(f"Warning: The category '{x[3]}' has less row and column than the specified index {x[i]}!")
            elif (x[i][0] + "0") not in category[x[3]]:
                write(f"Warning: The category '{x[3]}' has less row than the specified index {x[i]}!")
            elif int(x[i][1:]) > int(list(category[x[3]])[-1][1:]):
                write(f"Warning: The category '{x[3]}' has less column than the specified index {x[i]}!")
            else:
                if category[x[3]][x[i]] != "X":
                    write(f"Warning: The seat {x[i]} cannot be sold to {x[1]} since it was already sold!")
                else:
                    category[x[3]][x[i]] = x[2]
                    write(f"Success: {x[1]} has bought {x[i]} at {x[3]}")
        if len(x[i]) > 3:
            if (x[i][0] + "0") not in category[x[3]] and int(x[i].split("-")[1]) > int(list(category[x[3]])[-1][1:]):
                write(f"Warning: The category '{x[3]}' has less row and column than the specified index {x[i]}!")
            elif (x[i][0] + "0") not in category[x[3]]:
                write(f"Warning: The category '{x[3]}' has less row than the specified index {x[i]}!")
            elif int(x[i].split("-")[1]) > int(list(category[x[3]])[-1][1:]):
                write(f"Warning: The category '{x[3]}' has less column than the specified index {x[i]}!")
            else:
                seats_are_sold = False
                list_of_seats = []
                for k in range(int(x[i].lstrip(x[i][0]).split("-")[0]), int(x[i].lstrip(x[i][0]).split("-")[1]) + 1):
                    list_of_seats.append(x[i][0] + str(k))
                    if category[x[3]][x[i][0] + str(k)] != "X":
                        seats_are_sold = True
                        break
                if seats_are_sold:
                    write(f"Warning: The seats {x[i]} cannot be sold to {x[1]} due some of them have already been sold!")
                else:
                    for k in list_of_seats:
                        category[x[3]][k] = x[2]
                    write(f"Success: {x[1]} has bought {x[i]} at {x[3]}")

def cancel_ticket(x): #This function cancels seat tickets sold, if the seat has already been sold.
    if x[1] not in category: return
    for i in range(2, len(x)):
        if (x[i][0] + "0") not in category[x[1]] and int(x[i][1:]) > int(list(category[x[1]])[-1][1:]):
            write(f"Warning: The category '{x[1]}' has less row and column than the specified index {x[i]}!")
        elif (x[i][0] + "0") not in category[x[1]]:
            write(f"Warning: The category '{x[1]}' has less row than the specified index {x[i]}!")
        elif int(x[i][1:]) > int(list(category[x[1]])[-1][1:]):
            write(f"Warning: The category '{x[1]}' has less column than the specified index {x[i]}!")
        else:
            if category[x[1]][x[i]] == "X":
                write(f"Warning: The seat {x[i]} at {x[1]} has already been free! Nothing to cancel")
            else:
                category[x[1]][x[i]] = "X"
                write(f"Success: The seat {x[i]} at {x[1]} has been canceled and now ready to sell again")

def balance(x): #This function calculates profit from a certain category.
    if x[1] not in category: return
    student = int(list(category[x[1]].values()).count("S"))
    full = int(list(category[x[1]].values()).count("F"))
    season = int(list(category[x[1]].values()).count("T"))
    write(f"Category report of '{x[1]}'")
    write((len(x[1]) + 21) * "-")
    write(f"Sum of students = {student}, Sum of full pay = {full}, Sum of season ticket = {season}, and Revenues = {student * 10 + full * 20 + season * 250} Dollars")

def show_category(x): #This function illustrates a specific category.
    if x[1] not in category: return
    write(f"Printing category layout of '{x[1]}'")
    for i in range(int(letter.index(list(category[x[1]])[-1][0])), -1, -1):
        print(letter[i], end=" "), txt_write.write(letter[i] + " ")
        for k in range(int(list(category[x[1]])[-1][1:]) + 1):
            if k == int(list(category[x[1]])[-1][1:]):
                print(category[x[1]][letter[i] + str(k)]), txt_write.write(category[x[1]][letter[i] + str(k)] + "\n")
            else:
                print(category[x[1]][letter[i] + str(k)], end="  "), txt_write.write(category[x[1]][letter[i] + str(k)] + "  ")
    for i in range(int(list(category[x[1]])[-1][1:]) + 1):
        if i < 10:
            print(f"  {i}", end=""), txt_write.write(f"  {i}")
        else:
            print(f" {i}", end=""), txt_write.write(f" {i}")
    print("\n", end=""), txt_write.write("\n")

def write(x): #This function prints output to both terminal and txt file.
    print(x), txt_write.write(x + "\n")

main()