import random

def rock_paper_scissors(player1, player2):
    if player1 == player2:
        print("tie")
    elif (player1 == "r" and player2 == "s") or (player1 == "s" and player2 == "p") or (player1 == "p" and player2 == "r"):
        print("player1 won")
    else:
        print("player2 won ..")

def get_valid_input(prompt): # it checks valid input
    while True:
        choice = input(prompt).lower()
        if choice in ["r", "p", "s"]:
            return choice
        else:
            print("Invalid choice. Please choose rock (r), paper (p), or scissor (s).")

def game_computer(player_list):# code for computer game
    player1 = get_valid_input("choose rock, paper, scissor (r/p/s): ")
    if player1 == player_list:
        print("tie")
    elif (player1 == "r" and player_list == "s") or (player1 == "s" and player_list == "p") or (player1 == "p" and player_list == "r"):
        print("user__won 🏆🏆🏆🏆🏆🏆🏆")
    else:
        print("computer__won 🏆🏆🏆😎😎😎🏆🏆..")

def game_player():
    player1 = get_valid_input("choose rock, paper, scissor (r/p/s): ")
    player2 = get_valid_input("choose rock, paper, scissor (r/p/s): ")
    rock_paper_scissors(player1, player2)

def player_input():
    user = input("YOU PLAY WITH COMPUTER OR OTHER PLAYER: (P/C): ").lower()
    game_list = random.choice(["r", "p", "s"])
    if user == "c":
        game_computer(game_list)
    else:
        game_player()

def continue_game():
    play = input("want to continue or not (y/n): ").lower()
    return play == "y"

def main():
    print("welcome to rock, paper, scissor game ✂️✂️🗞️🗞️🤘🏿")
    while True:
        player_input()
        if not continue_game():
            break

if __name__ == "__main__":
    main()
