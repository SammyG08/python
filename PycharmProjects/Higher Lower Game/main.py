import random
import game_database

first_player = random.choice(game_database.people_to_compare)
second_player = random.choice(game_database.people_to_compare)

number_of_correct_guesses = 0

def printing_info_needed(first_player, second_player):
    print(f"\nCandidate's name is {first_player["Name"]}.\nHe comes from {first_player["Country"]} and plays professional {first_player["Profession"]} for {first_player["Team"]}.")
    print(f"He has an instagram followers count of {first_player["Instagram Followers"]} million.")

    print("\n                   VS\n")

    print(f"Candidate's name is {second_player["Name"]}.\nHe comes from {second_player["Country"]} and plays professional {second_player["Profession"]} for {second_player["Team"]}.")

def game_process(first_player, second_player, number_of_correct_guesses):
    while first_player == second_player:
        second_player = random.choice(game_database.people_to_compare)
    printing_info_needed(first_player, second_player)
    userGuess = input("\n\nDoes the second candidate have higher or lower instagram followers as compared to the first?\n").lower()
    if userGuess == "higher":
        if second_player["Instagram Followers"] > first_player["Instagram Followers"]:
            number_of_correct_guesses = number_of_correct_guesses + 1
            first_player = second_player
            second_player = random.choice(game_database.people_to_compare)
            game_process(first_player, second_player, number_of_correct_guesses)
        elif second_player["Instagram Followers"] < first_player["Instagram Followers"]:
            guess_status = False
            print(f"\nYou had a score of {number_of_correct_guesses}.")
            return guess_status
    elif userGuess == "lower":
        if second_player["Instagram Followers"] < first_player["Instagram Followers"] :
            number_of_correct_guesses = number_of_correct_guesses + 1
            first_player = second_player
            second_player = random.choice(game_database.people_to_compare)
            game_process(first_player, second_player, number_of_correct_guesses)
        elif second_player["Instagram Followers"] > first_player["Instagram Followers"]:
            guess_status = False
            print(f"\nYou had a score of {number_of_correct_guesses}.")
            return guess_status
    elif userGuess == "higher" or userGuess == "lower":
        if first_player["Instagram Followers"] == second_player["Instagram Followers"]:
            guess_status = False
            print(f"\nYou had a score of {number_of_correct_guesses}.")
            return guess_status

guess_status = True

while guess_status:
    guess_status = game_process(first_player, second_player, number_of_correct_guesses)



