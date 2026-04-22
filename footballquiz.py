score = 0

print("Welcome to Football Quiz!\n")

# Questions
q1 = input("1. Who has won the most Ballon d'Or awards?\n")
if q1.lower() == "lionel messi" or q1.lower() == "messi":
    score += 1

q2 = input("2. Which country won the FIFA World Cup 2006?\n")
if q2.lower() == "italy":
    score += 1

q3 = input("3. Which club is known as 'The Red Devils'?\n")
if q3.lower() == "manchester united" or q3.lower() == "man utd":
    score += 1

q4 = input("4. What was Neymar's transfer fee to PSG in 2017 (in million euros)?\n")
if q4 == "222":
    score += 1

q5 = input("5. Who is known as Mr UCL?\n")
if q5.lower() == "cristiano ronaldo" or q5.lower() == "ronaldo":
    score += 1

q6 = input("6. Which country has won the most FIFA World Cups?\n")
if q6.lower() == "brazil":
    score += 1

q7 = input("7. What is the maximum duration of a football match (with extra time)?\n")
if q7 == "120":
    score += 1

q8 = input("8. Which club went unbeaten in an entire Premier League season?\n")
if q8.lower() == "arsenal":
    score += 1

q9 = input("9. Which club won the UEFA Champions League 2023?\n")
if q9.lower() == "manchester city" q9.lower() == "city":
    score += 1

q10 = input("10. Which country hosted FIFA World Cup 1998?\n")
if q10.lower() == "france":
    score += 1

# Result
print("\nYour Score:", score, "/10")

if score < 4:
    print("Very Poor")
elif score <= 6:
    print("Average")
elif score <= 8:
    print("Good")
else:
    print("Marvellous!")
