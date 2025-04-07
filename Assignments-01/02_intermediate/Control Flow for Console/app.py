import random
NUM_ROUNDS = 5
def get_user_guess():
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess not in ["higher", "lower"]:
        guess = input("Please enter either higher or lower: ").lower()
    return guess

def play_round(round_num, score):
    print(f"Round {round_num}")
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"Your number is {user_number}")
    guess = get_user_guess()

    correct = False
    if guess == "higher" and user_number > computer_number:
        correct = True
    elif guess == "lower" and user_number < computer_number:
        correct = True

    if correct:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")

    print(f"Your score is now {score}\n")
    return score

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        score = play_round(round_num, score)

    print("Thanks for playing!")
    print(f"Your final score: {score}")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()