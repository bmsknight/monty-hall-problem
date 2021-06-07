from src.contestant import Contestant
from src.host import Host

N_GAMES = 1000000       # 1 million iterations is a good number
WILL_YOU_SWITCH = True
VERBOSE = False
N_DOORS = 3

if __name__ == '__main__':
    print("--------------Welcome to the imaginary Monte Hall show-----------------------")
    print("--------------You will play this for {0:2d} times-----------------------".format(N_GAMES))
    print("--------------There are {0:2d} doors -----------------------".format(N_DOORS))
    if WILL_YOU_SWITCH:
        print("--------------You will change your choice after the host eliminate other doors-----------------------")
    else:
        print("--------------You will always stay with your original decision-----------------------")
    
    host = Host(door_count=N_DOORS)
    you = Contestant(switch=WILL_YOU_SWITCH)
    
    no_of_times_won = 0
    for k in range(N_GAMES):
        total_doors = host.present_doors()
        first_choice = you.select_door(total_doors)
        remaining_door = host.eliminate_others_and_present_one_door(first_choice)
        final_choice = you.wanna_switch(remaining_door)
        won = host.reveal_if_winner(final_choice)
        if won:
            no_of_times_won += 1
            
        if VERBOSE:
            print("Game Number : ", k)
            print("Your first choice : Door no.",first_choice)
            print("Your final choice : Door no.",final_choice)
            if won:
                print("You won this time")
            else:
                print("You didn't win this time")
    
    winning_probability = no_of_times_won/N_GAMES
    print("You played {0:2d} times.".format(N_GAMES))
    print("You won {0:2d} times.".format(no_of_times_won))
    print("You won {0:2.2f} % of times".format(winning_probability*100))
