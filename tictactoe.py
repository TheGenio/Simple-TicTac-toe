symbols = "XOXOXOXOX"

#this function will check the coordinates given and make sure they are valid
def true_cord():
    while True:
        try:
            num_cord = input("").replace(" ", "")
            if int(num_cord) > 33:
                print("Coordinates should be from 1 to 3!")
            else:
                break
        except Exception:
            print("You should enter numbers!")
    return num_cord


def gridfun():
    print("---------")
    print("|", grid[0][0], grid[0][1], grid[0][2], "|")
    print("|", grid[1][0], grid[1][1], grid[1][2], "|")
    print("|", grid[2][0], grid[2][1], grid[2][2], "|")
    print("---------")

grid = [[" ", " " , " " ], [" ", " ", " "], [" ", " ", " "]]
moves = 0

#starts the game
for player in symbols:
    gridfun()
    x = False
    while True: #this will place the X or O in the coordinate
        try:
            cord = true_cord()
            count = 0
            for i in cord:
                count += 1
                i = int(i)
                if count == 1:
                    row = grid[i-1]
                elif count == 2:
                    if row[i-1] == "X" or row[i-1] == "O":
                        print("This cell is occupied! Choose another one!")
                        break
                    else:
                        row[i-1] = player
                        moves += 1
                        x = True
                        break
            if x:
                break
        except Exception:
            print("Enter valid coordinates")


    # code for gathering the winners
    who_win = ""
    win_num = 0
    win_num_case = 0
    for i in range(3):
        try:
            if grid[i][0] == grid[i][1] == grid[i][2]: #this will find any winners in the horizontal lines
                who_win = grid[i][1]
                if who_win == " ":
                    who_win = ""
            elif grid[0][2] == grid[1][1] == grid[2][0]: #finds the winner for digonal line
                who_win = grid[0][2]
                if who_win == " ":
                    who_win = ""
            elif grid[0][0] == grid[1][1] == grid[2][2]: #finds the winner for digonal line
                who_win = grid[1][1]
                if who_win == " ":
                    who_win = ""
        except Exception: #IndexError
            pass


    if who_win == "": # if its neither, then this will find the winners in  verical lines
        for y in range(3):
            if symbols[y] == symbols[y + 3] and symbols[y + 3] == symbols[y + 6]:
                who_win = symbols[y]
                win_num += 1

    if moves >= 5 and (who_win == "X" or who_win == "O"): # this will check if there are any winners and ends the game is there is any winners
        gridfun()
        print(f"{who_win} wins")
        break
    elif moves == 9:
        gridfun()
        print("Draw")
