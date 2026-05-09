import random

print("----- HAND CRICKET GAME -----")
print()

#TOSS
print("TOSS TIME")
print("Choose Head or Tail")

player_toss = input("Enter Head or Tail: ").lower()
toss_result = random.choice(["head", "tail"])

print("Toss result is:", toss_result)

# Decision
if player_toss == toss_result:
    print("You won the toss!")

    choice = input("Choose Bat or Bowl: ").lower()

    if choice == "bat":
        player_batting_first = True
    else:
        player_batting_first = False

else:
    print("Computer won the toss!")
    computer_choice = random.choice(["bat", "bowl"])
    print("Computer chooses to", computer_choice)

    if computer_choice == "bat":
        player_batting_first = False
    else:
        player_batting_first = True

# Scores
player_score = 0
computer_score = 0

#PLAYER BATS FIRST
if player_batting_first:
    print()
    print("----- YOU ARE BATTING FIRST -----")

    while True:
        player = int(input("Enter your number (1-10): "))

        if player < 1 or player > 10:
            print("Invalid input!")
            continue

        computer = random.randint(1, 10)

        print("Computer chose:", computer)

        # OUT
        if player == computer:
            print("YOU ARE OUT!")
            break

        player_score += player

        print("Your score:", player_score)
        print()

    target = player_score + 1

    print()
    print("Computer needs", target, "runs to win")
    print()

    # COMPUTER BATTING
    print("----- COMPUTER IS BATTING -----")
    while True:
        player = int(input("Enter your number (1-10): "))

        if player < 1 or player > 10:
            print("Invalid input!")
            continue

        computer = random.randint(1, 10)

        print("Computer chose:", computer)

        # OUT
        if player == computer:
            print("COMPUTER IS OUT!")
            break

        computer_score += computer

        print("Computer score:", computer_score)
        print()

        # Computer wins
        if computer_score >= target:
            break

#COMPUTER BATS FIRST
else:
    print()
    print("----- COMPUTER IS BATTING FIRST -----")

    while True:
        player = int(input("Enter your number (1-10): "))

        if player < 1 or player > 10:
            print("Invalid input!")
            continue

        computer = random.randint(1, 10)

        print("Computer chose:", computer)

        # OUT
        if player == computer:
            print("COMPUTER IS OUT!")
            break

        computer_score += computer

        print("Computer score:", computer_score)
        print()

    target = computer_score + 1

    print()
    print("You need", target, "runs to win")
    print()

    # PLAYER BATTING
    print("----- YOU ARE BATTING -----")
    while True:
        player = int(input("Enter your number (1-10): "))

        if player < 1 or player > 10:
            print("Invalid input!")
            continue

        computer = random.randint(1, 10)

        print("Computer chose:", computer)

        # OUT
        if player == computer:
            print("YOU ARE OUT!")
            break

        player_score += player

        print("Your score:", player_score)
        print()

        # Player wins
        if player_score >= target:
            break

#FINAL RESULT
print()
print("----- FINAL RESULT -----")
print("Your score:", player_score)
print("Computer score:", computer_score)
print()

if player_score > computer_score:
    print("YOU WIN!")
elif computer_score > player_score:
    print("COMPUTER WINS!")
else:
    print("MATCH DRAW!")
