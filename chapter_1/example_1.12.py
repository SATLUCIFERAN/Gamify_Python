
max_rounds = 5     

for current_round in range(1, max_rounds + 1):
    print(f"--- Round {current_round} ---")    

    play_one_round()
    
    if player_wins():
        print("We have a winner! Stopping the game early.")
        break

else:
    # This else runs only if we never hit a `break`
    print("No winner after 5 rounds. Game over.")

   
