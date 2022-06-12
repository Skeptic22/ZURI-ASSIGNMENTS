import random


def play():
    user = input("what is your choice? 'r' for Rock, 'p' for Paper. 's' for Scissors\n")
    user = user.lower()
    computer = random.choice(['r', 'p', 's'])

    if user != "r" and user != "p" and user != "s":
        print("INVALID INPUT")
        play()

    if user == computer:
        return "You and the computer both chose {}. It's A Tie".format(computer)

    elif is_win(user, computer):
        return "You chose {} and the computer chose {}. You WIN".format(user, computer)

    else:
        return "You chose {} and the computer chose {}. You LOST".format(user, computer)


def is_win(player, opponent):
    # return True if player wins opponent
    # winning conditions: R > S, S > P, P > R
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'P' and opponent == 'r'):
        return True
    return False


def pymain():
    # What does everything
    print(play())

    play_again = input("play again? (yes/no): ").lower()

    if play_again == "yes" or str(play_again).startswith('y'):  # If you choose to play again/...
        # Repeat the process
        pymain()


pymain()
print("Game Over")