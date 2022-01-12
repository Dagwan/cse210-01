
print("--------------------------------------------------------\n"
"TIC TAC TOE GAME ASSIGNMENT\n"
"--------------------------------------------------------\n"
"DAGWAN PAN'AN DANLADI\n"
"--------------------------------------------------------")

def main():
    #this program will raise an exception if there is 
    #key, out of range or value errors.
    
    try:
        print()
        #Welcoming message...........................
        print("WELCOME TO TIC TAC TOE GAME. \n"
              "-------------------------------\n"
              "Please enjoy playing the game!\n"
              "--------------------------------")
        
        #setting up the game
        game_container = board_creation()
        game_player = player(">>>")
        
        while not a_game_winner(game_container) or a_draw_game(game_container):
            show_game_container(game_container)
            shift_game_over(game_player, game_container)
            game_player = player(game_player)
        
        if show_game_container(game_container):
            print("Good...awesome game!!!")
       
    except (PermissionError) as error:
        print(error)
        
    except (ValueError) as val_err:
        print("Please enter a valid response (number only.:) ")
        print("Error:", val_err)
        

    except (KeyError) as error:
        print(f"Error")
          
    except (IndexError) as error:
        print("Error", IndexError) 
        print("Please enter a valid number that \n"
              "corresponse with the number (1-9)!")

#this function will create the game board
def board_creation():
    game_container = []
    for game in range (9):
        game_container.append(game +1)
    return game_container

#this function show up the game's container
def show_game_container(game_container):
    print()
    #the game's grids that will holds the numbers in between
    print("------------------- ")
    print(f"|  {game_container[0]}  |  {game_container[1]}  |  {game_container[2]}  |") 
    
    print("------------------- ")
    
    print(f"|  {game_container[3]}  |  {game_container[4]}  |  {game_container[5]}  |") 
    
    print("------------------- ")
    
    print(f"|  {game_container[6]}  |  {game_container[7]}  |  {game_container[8]}  |") 
    
    print("------------------- ")
    
    print()

#check for draw game
def a_draw_game(game_container):
    for game in range (9):
        if game_container[game] != "x" and game_container[game] != "o":
            return False
        
        if game_container[game] == "x" and game_container[game] == "o":
            return True

def shift_game_over(game_player, game_container):
    #ask user for input that only accepts an integer (only mumbers)
    game = int(input(f"{game_player}'s turn to choose a player (1-9): "))
    game_container[game - 1] = game_player
            
#check for winner
def a_game_winner(game_container):
    return (game_container[0] == game_container[1] == game_container[2] or 
            game_container[3] == game_container[4] == game_container[5] or 
            game_container[6] == game_container[7] == game_container[8] or 
            game_container[0] == game_container[3] == game_container[5] or 
            game_container[1] == game_container[4] == game_container[6] or 
            game_container[2] == game_container[5] == game_container[7] or 
            game_container[0] == game_container[4] == game_container[8] or 
            game_container[2] == game_container[5] == game_container[6])

def player(current_game):
    if current_game == ">>>" or current_game == "o":
        return "x"
    
    elif current_game == "x":
        return "o"
    
    else:
        print("Play make a response!")
   
   
    
#call the main to start this program.
if __name__ == "__main__":
    main()