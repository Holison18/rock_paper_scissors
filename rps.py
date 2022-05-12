import random as rand


list = ["rock","paper","scissors"]

counter  = 10
user1_score = 0
user2_score = 0

while counter > 0:
    
    random_choice = rand.randint(0,len(list)-1)
    user1 = list[random_choice]
    user2 = input("Enter an input: ")

    if user1 == user2:
        print("it's a tire, try again")
        continue
    elif (user1 == list[0] and user2 == list[1]) or (user1 == list[1] and user2 == list[2]) or (user1 == list[0] and user2 == list[2]):
        print("User2 won")
        counter -= 1
        user2_score += 1
        continue
    else:
        print("User1 Won")
        counter -= 1
        user1_score += 1
        continue

print(f"User1 won {user1_score} and User2 won {user2_score}")