from art import logo3, vs
from data import data
import random
print(logo3)
play_game = True
score = 0
person1 = random.choice(data)
person2 = random.choice(data)
while play_game:

    print(f"A: {person1['name']} in the filed of {person1['description']}")
    print(vs)
    print(f"B: {person2['name']} in the file of {person2['description']}")
    gess = input("which one has more follower: A or B? ")
    if person1['follower_count'] > person2['follower_count'] and gess.lower() == 'a':
        score += 1
        print(f"Okay, your score is {score}")
        person1 = person2
        person2 = random.choice(data)

    elif person1['follower_count'] < person2['follower_count'] and gess.lower() == 'b':
        score += 1
        print(f"OKay, your score is {score}")
        person1 = person2
        person2 = random.choice(data)

    else:
        play_game = False
        print(f"Game Over, your score is {score}")
