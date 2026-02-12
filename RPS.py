#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  again = "Y"
  while again == "Y" or "y":
    game = input("Want to play a game? [Y/N] :")
    if game == "Y" or game == "y":
      RPS = input("Ok! Rock, Paper, or Scissors? [R/P/S]")
      answers = random.choice(["Rock", "Paper", "Scissors"])
      print("I chose", answers)
      if answers == "Rock" and RPS == "S":
        print("Oh no! Better luck next time!")
        losses = losses + 1
      if answers == "Rock" and RPS == "P":
        print("Holy smokes you got me. Good Job!")
        wins = wins + 1
      if answers == "Rock" and RPS == "R":
        print("WOW, we managed to pick the same thing...")
        ties = ties + 1
  

 
    print("Bye, Have fun somewhere else!")


  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
