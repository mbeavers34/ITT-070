#Name Michael Beavers
#Date 04/15/24
#Program Grid
#Description Move player on a 10 x 10 grid using W,A,D,S

# Variables--------------------------------------------------------------
# Initialize player position (start in the middle)
GRID_SIZE = 10
player_x, player_y = GRID_SIZE // 2 -1, GRID_SIZE // 2
player2_x, player2_y = GRID_SIZE // 2 +1 , GRID_SIZE // 2


# Function --------------------------------------------------------------
# Display the grid
def display_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if row == player_y and col == player_x:
                print("P", end=" ")  # Player position
            elif row == player2_y and col == player2_x:
                print("Q", end =" ")
            else:
                print(".", end=" ")  # Empty square
        print()  # Newline for the next row


# Main --------------------------------------------------------------------
while True:
    
    display_grid()
    
    move = input("P Enter W/A/S/D to move (or Q to quit): ").upper()
    print(player_x,player2_x,player_y,player2_x)
    if move == "W":
        if player_y - 1 != player2_y or player_x != player2_x:
            player_y = max(player_y - 1, 0)
    elif move == "S":
        if player_y + 1 != player2_y or player_x != player2_x:
            player_y = min(player_y + 1, GRID_SIZE - 1)
    elif move == "A":
        
        if player_x - 1 != player2_x or player_y != player2_y:
            player_x = max(player_x - 1, 0)
    elif move == "D":
        if player_x + 1 != player2_x or player_y != player2_y:
             player_x = min(player_x + 1, GRID_SIZE - 1)
    elif move == "Q":
        print("I'm out")
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid input. Use W/A/S/D to move or Q to quit.")


