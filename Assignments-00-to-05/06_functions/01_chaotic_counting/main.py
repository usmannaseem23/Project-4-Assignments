import random

DONE_LIKELIHOOD = 8

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return
        print(curr_num)

def done():
    if random.randint(1, 10) > DONE_LIKELIHOOD:
        return True
    return False


def main():
    print(
        "I'm going to count until 10 or until I feel like stopping, whichever comes first."
    )
    chaotic_counting()
    print("I'm done")


if __name__ == "__main__":
    main()