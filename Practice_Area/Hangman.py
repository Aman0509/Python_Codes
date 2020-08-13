#!/usr/bin/env  python3

import random
import time

file_object = open("word_list", "r")
file_content_list = file_object.readlines()


def intro_graphics():

    player_name = input("Your Name: ")
    print(f"Welcome {player_name}!!")
    print("Loading......\n")
    time.sleep(1.5)
    print()
    for _ in range(80):
        print("-", end="")
    print()
    print("|", end="")
    for _ in range(78):
        print(" ", end="")
    print("|")
    print("|", end="")
    for _ in range(78):
        if 10 < _ < 38:
            print("-", end="")
        else:
            print(" ", end="")
    print("|")
    temp = 0
    while temp < 3:
        print("|", end="")
        for _ in range(78):
            if _ == 11 or _ == 34:
                print("|", end="")
            else:
                print(" ", end="")
        print("|")
        temp += 1
    print("|", end="")
    for _ in range(78):
        if _ == 11:
            print("|", end="")
        elif _ == 34:
            print("O", end="")
        else:
            print(" ", end="")
    print("|")
    print("|", end="")
    for _ in range(78):
        if _ == 11 or _ == 34:
            print("|", end="")
        elif _ == 33:
            print("\\", end="")
        elif _ == 35:
            print("/", end="")
        else:
            print(" ", end="")
    print("|")
    print("|", end="")
    for _ in range(78):
        if _ == 11 or _ == 34:
            print("|", end="")
        else:
            print(" ", end="")
    print("|")
    print("|", end="")
    for _ in range(78):
        if _ == 11:
            print("|", end="")
        elif _ == 33:
            print("/", end="")
        elif _ == 35:
            print("\\", end="")
        else:
            print(" ", end="")
    print("|")
    temp = 0
    while temp < 3:
        print("|", end="")
        for _ in range(78):
            if _ == 11:
                print("|", end="")
            else:
                print(" ", end="")
        print("|")
        temp += 1
    print("|", end="")
    for _ in range(78):
        if 5 < _ < 17:
            print("-", end="")
        else:
            print(" ", end="")
    print("|")
    print("|", end="")
    game_name = "HANGMAN"
    count = 0
    for _ in range(78):
        if 60 < _ < 68 :
            print(game_name[count], end="")
            count += 1
        else:
            print(" ", end="")
    print("|")
    print("|", end="")
    for _ in range(78):
        print("_", end="")
    print("|")


def hangman(attempt):
    print()
    for _ in range(40):
        if 10 < _ < 30:
            print("_", end="")
        else:
            print(" ", end="")
    print()

    temp = 0
    while temp < 3:
        for _ in range(40):
            if _ == 10 or _ == 26:
                print("|", end="")
            else:
                print(" ", end="")
        print()
        temp += 1

    if attempt == 7:
        temp = 0
        while temp < 7:
            for _ in range(40):
                if _ == 10:
                    print("|", end="")
                else:
                    print(" ", end="")
            print()
            temp += 1

    elif attempt == 6:
        for _ in range(40):
            if _ == 10:
                print("|", end="")
            elif _ == 26:
                print("O", end="")
            else:
                print(" ", end="")
        print()
        print("          |\n"*6, end="")

    elif attempt == 5:
        for _ in range(40):
            if _ == 10:
                print("|", end="")
            elif _ == 26:
                print("O", end="")
            else:
                print(" ", end="")
        print()
        for _ in range(40):
            if _ == 10 or _ == 26:
                print("|", end="")
            else:
                print(" ", end="")
        print()
        print("          |\n" * 5, end="")

    elif attempt == 4:
        for _ in range(40):
            if _ == 10:
                print("|", end="")
            elif _ == 26:
                print("O", end="")
            else:
                print(" ", end="")
        print()
        for _ in range(40):
            if _ == 10 or _ == 26:
                print("|", end="")
            elif _ == 25:
                print("\\", end="")
            else:
                print(" ", end="")
        print()
        print("          |\n" * 5, end="")

    elif attempt == 3:
        for _ in range(40):
            if _ == 10:
                print("|", end="")
            elif _ == 26:
                print("O", end="")
            else:
                print(" ", end="")
        print()
        for k in range(40):
            if k == 10 or k == 26:
                print("|", end="")
            elif k == 25:
                print("\\", end="")
            elif k == 27:
                print("/", end="")
            else:
                print(" ", end="")
        print()
        print("          |\n" * 5, end="")

    elif attempt == 2:
        for _ in range(40):
            if _ == 10:
                print("|", end="")
            elif _ == 26:
                print("O", end="")
            else:
                print(" ", end="")
        print()
        for _ in range(40):
            if _ == 10 or _ == 26:
                print("|", end="")
            elif _ == 25:
                print("\\", end="")
            elif _ == 27:
                print("/", end="")
            else:
                print(" ", end="")
        print()
        for _ in range(40):
            if _ == 10 or _ == 26:
                print("|", end="")
            else:
                print(" ", end="")
        print()
        print("          |\n"*4, end="")

    elif attempt == 1:
        for _ in range(40):
            if _ == 10:
                print("|", end="")
            elif _ == 26:
                print("O", end="")
            else:
                print(" ", end="")
        print()
        for _ in range(40):
            if _ == 10 or _ == 26:
                print("|", end="")
            elif _ == 25:
                print("\\", end="")
            elif _ == 27:
                print("/", end="")
            else:
                print(" ", end="")
        print()
        for _ in range(40):
            if _ == 10 or _ == 26:
                print("|", end="")
            else:
                print(" ", end="")
        print()
        for _ in range(40):
            if _ == 10:
                print("|", end="")
            elif _ == 25:
                print("/", end="")
            else:
                print(" ", end="")
        print()
        print("          |\n" * 3, end="")

    elif attempt == 0:
        for _ in range(40):
            if _ == 10:
                print("|", end="")
            elif _ == 26:
                print("O", end="")
            else:
                print(" ", end="")
        print()
        for _ in range(40):
            if _ == 10 or _ == 26:
                print("|", end="")
            elif _ == 25:
                print("\\", end="")
            elif _ == 27:
                print("/", end="")
            else:
                print(" ", end="")
        print()
        for _ in range(40):
            if _ == 10 or _ == 26:
                print("|", end="")
            else:
                print(" ", end="")
        print()
        for _ in range(40):
            if _ == 10:
                print("|", end="")
            elif _ == 25:
                print("/", end="")
            elif _ == 27:
                print("\\", end="")
            else:
                print(" ", end="")
        print()
        print("          |\n" * 3, end="")
    for _ in range(40):
        if 6 < _ < 15:
            print("-", end="")
        else:
            print(" ", end="")

    return


def controller():

    attempt = 7
    w = []
    used = []
    word = random.sample(file_content_list, 1)[0].upper().strip("\n")
    print(f"\n\nGuess this {len(word)} letter word - ", end="")
    for i in range(len(word)):
        print("_", end="")
        w.append("_")

    while attempt > 0:

        print()
        print()
        user_input = input("Your Input: ").upper()
        used.append(user_input)
        loc = word.find(user_input)
        print()
        if len(user_input) == 0:
            attempt -= 1
            print("".join(w))
            hangman(attempt)

        elif 1 < len(user_input) < len(word) or len(user_input) > len(word):
            print("You can either enter 1 letter or entire word\n")
            print("".join(w))
            hangman(attempt)

        elif loc == -1:
            attempt -= 1
            print("".join(w))
            hangman(attempt)

        elif loc != -1:
            for i in range(len(word)):
                if word[i] == user_input:
                    w[i] = word[i]
            if user_input == word or "".join(w) == word:
                print("Congrats! You've guessed the word correctly.")
                break
            print("".join(w))
            hangman(attempt)
        print(f"Used ones - {used}")

    if attempt == 0:
        print("\nSorry! You are out of attempts. Man has been hanged!")
        print(f"Word given was {word}")

    return 1


def main():

    temp = True
    intro_graphics()
    time.sleep(1)
    controller()
    while temp:
        play_again = input("Do you want to play again?(Y/N) ").upper()
        if play_again == "Y" or play_again == "YES":
            controller()
        elif play_again == "N" or play_again == "NO":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice!!")


main()
file_object.close()

