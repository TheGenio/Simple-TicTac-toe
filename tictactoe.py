# Set the initial symbol values
symbols = "XOXOXOXOX"

# This function will check the coordinates given and make sure they are valid
def true_cord():
    while True:
        try:
            num_cord = input("Enter the coordinates: ").replace(" ", "")
            if int(num_cord) > 33: # Since the input will be converted from 2 1 to 21, thus if the input is higher its wrong. EX 4(there is no 4th row) 1 -> 41
                print("Coordinates should be from 1 to 3!")
            else:
                break
        except Exception:
            print("You should enter numbers!")
    return num_cord


def gridfun(): # Function to print the grid
    print("---------")
    print("|", grid[0][0], grid[0][1], grid[0][2], "|")
    print("|", grid[1][0], grid[1][1], grid[1][2], "|")
    print("|", grid[2][0], grid[2][1], grid[2][2], "|")
    print("---------")


# Set the initial values for the game grid and moves
grid = [[" ", " " , " " ], [" ", " ", " "], [" ", " ", " "]]
moves = 0

# Starts the game
print("Welcome to this simple game of XO, this game works by asking for coordinates and then placing a symbol on that coordinate ")
print("for example, 3 1, 1 2 etc. Where (ROW)(COLLUMN):")

for player in symbols: # this will choose the turn from symbols each time
    gridfun()
    x = False
    while True: #this will place the X or O in the coordinate
        try:
            cord = true_cord() # Assigns the correct coordinate to cord 
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
    for i in range(3): # Its a 3x3 grid
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
            elif grid[0][i] == grid[1][i] == grid[2][i]: #this will find any winners in the vertial lines
                who_win = grid[1][i]
                if who_win == " ":
                    who_win = ""
        except Exception: #IndexError
            pass


    if moves >= 5 and (who_win == "X" or who_win == "O"): # this will check if there are any winners and ends the game is there is any winners
        gridfun()
        print(f"{who_win} wins")
        break
    elif moves == 9:
        gridfun()
        print("Draw")
