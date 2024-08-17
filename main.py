#JHammit

#import libraries
import random
import time

# Random AI choice of light color (red, green, or yellow)
def get_ai_choice():
    """Random AI light color choice."""
    return random.choice(["Red Light", "Green Light", "Yellow Light"])

# Main game loop
def check_player_move(light, move, warning_issued):
    """Checks if the player's move is valid based on the AI's light."""
    #if elif loop depending on user input of light color
    if light == "Red Light" and move != "Stop":
        return False, warning_issued
    #if user runs on yellow, they are issued a warning, and they are not allowed to do it twice in a row
    elif light == "Yellow Light" and move == "Run":
        if warning_issued:
            return False, warning_issued  
        else:
            print("Warning: Running on a Yellow Light is risky!")
            return True, True  
    return True, warning_issued

# Gameplay
def play_game():
    print("Welcome to Red Light, Green Light!")
    print("You need to reach the destination without breaking any rules.")
    # set short distance for total game (50)
    #starting distance 
    distance = 50  
    warning_issued = False  

    # Until distance is 0, the AI will provide a light color to impact user input 
    while distance > 0:
        light = get_ai_choice()
        print(f"AI says: {light}")

        #print instructions on choosing a move, which will also print distance to end
        move = input("Choose your move (Stop, Walk, Run): ").capitalize()

        # Must input either stop, walk, or run (can't input anything else)
        if move not in ["Stop", "Walk", "Run"]:
            print("Invalid move! Please choose Stop, Walk, or Run.")
            continue
        # Check if inputted move is valid based on the AI's light
        valid_move, warning_issued = check_player_move(light, move, warning_issued)

        # If move is bad choice, the user will lose the game
        if not valid_move:
            print("You lost! You made an invalid move.")
            return

        # Walk distance is set at 5 versus run distance of 10 (double)
        if move == "Walk":
            distance -= 5
        elif move == "Run":
            distance -= 10

        # Print distance remaining
        print(f"Distance left: {distance} meters")

        # Print winning message once distance has been reached
        if distance <= 0:
            print("Congratulations! You've won the game.")
            return

        time.sleep(1)

# Main function running
if __name__ == "__main__":
    play_game()
    
# JHammit
