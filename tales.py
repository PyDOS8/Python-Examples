def game():
  score = 0
  if score == 10:
    print("You win!")
  import random
  choices = ["heads", "tales"]
  computer_choice = random.choice(choices) 
  user_choice = input("Heads or tales > ")
  if user_choice == computer_choice:
    print("Correct!")
    score = score+1#increase the score by 1
    game()
  else:
    print("Try again!")
  game()
game()
