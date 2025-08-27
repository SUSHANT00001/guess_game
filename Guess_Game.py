import random
word_list = ["python", "computer", "programming", "gemini", "miniproject",
            "development", "challenge", "algorithm"]
secret_word = random.choice(word_list)
secret_number = random.randint(1, 100)


print("<<--  Welcome to Gaming Which game you want to play?  -->")
print("  ")
print("<<--  Try to guess the secret word or random number ! -->")
# print("Select the words from the list: [", word_list, "]")
print("  ")
for word in word_list:
    print(f" - {word}")


print("  ")
print("----  OR  ----")
print("  ")
print("Numbers between 1 and 100")
print("  ")
attempts = 5
print("You have 5 attempts to guess the secret word or number.")
print("-------   Starting...   -------")
print("1. Guess the secret word")
print("2. Guess the secret number")
choice = input("Enter your choice (1 or 2): ")
if choice == "1":
    while attempts > 0:
        guess = input("Enter your guess: ")
        print("  ")
        if guess == secret_word:
            print("Congratulations! You've guessed the word!")
            print("  ")
            break
        else:
            attempts -= 1
            print(f"Sorry, that's not it. You have {attempts} attempts left.")
            print("  ")
            print("<<--  Try again! -->")
            print("  ")
            if attempts == 3:
                print(f"Hint: The secret word starts with '{secret_word[0]}'",
                      f"and ends with '{secret_word[-1]}'")
if choice == "2":
    while attempts > 0:
        guess = int(input("Enter your guess (1-100): "))
        print("  ")
        if guess == secret_number:
            print("Congratulations! You've guessed the number!")
            print("  ")
            break
        else:
            attempts -= 1
            print(f"Sorry, that's not it. You have {attempts} attempts left.")
            if guess < secret_number:
                print("Hint: The secret number is higher.")
            else:
                print("Hint: The secret number is lower.")
            print("  ")
            print("<<--  Try again! -->")
            print("  ")
            # if attempts == 1:
            #     if secret_number % 2 == 0:
            #         print("Hint: The secret number is even.")
            #     else:
            #         print("Hint: The secret number is odd.")
            #     print(f"Hint: The secret number is between {max(1, secret_number-10)} ",
            #           f"and {min(100, secret_number+10)}.")
if choice == "1":
    print("The secret word is: --> ", secret_word)
if choice == "2":
    print("The secret number is: --> ", secret_number)
print("  ")
print("<<--  Thank you for playing the Word Guessing Game! -->")
