##Udemy-100 days of code
## day 11 capstone
## Create Blackjack program.
## Used minimal hints (Difficutly Hard)
## Denise T. 
## 3/2/2021

import random
import art
global computer_sum, player_sum
#global player_lost
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_hand = []
player_hand = []
computer_sum = 0
player_sum = 0

def Draw_Card():
  global drawn_card
  drawn_card = random.choice(cards)

def Initial_Deal():
  #global computer_sum, player_sum
  for players in range(2):
    Draw_Card()
    computer_hand.append(drawn_card)
    Draw_Card()
    player_hand.append(drawn_card)

  print (art.logo)
  print (f"\nThe dealer's starting hand is: [{computer_hand[0]}, X]\n")
  print (f"Your starting hand is: {player_hand}\n")  

def Computer_play():
  global computer_sum
  computer_sum = sum(computer_hand)
  while computer_sum < 17:
    Draw_Card()
    computer_hand.append(drawn_card)
    computer_sum = sum(computer_hand)
    #print (f"ComputerHand: {computer_hand}")
  if computer_sum > 21:
    #print (f"ComputerSum is over!: {computer_sum}")
    for index,item in enumerate(computer_hand):
      if item == 11:  ##Sub 1 for 11 computer
        computer_hand[index] = 1
        Computer_play()

def Player_play():
  global player_sum
  resume = True
  player_sum = sum(player_hand) 
  while resume == True:
    new_card = input ("Do you want to hit? (yes/no)\n >>> ")
    if new_card =="no" or new_card == "n":
      resume = False
      Final_Calculations()
    else:
      Draw_Card()
      player_hand.append(drawn_card)
      player_sum = sum(player_hand)
      print (f"\nYou drew: {drawn_card}")
      if player_sum > 21:
        for index,item in enumerate(player_hand):
          if item == 11:  ##Sub 1 for 11
            player_hand[index] = 1
            print (f"Your current hand: {player_hand}")
            Player_play()
        Final_Calculations()
        return
      print (f"Your current hand is: {player_hand}")
      print (f"Your total is: {player_sum}")

def Final_Calculations():
  global player_lost
  player_lost = False
  if computer_sum >= player_sum and computer_sum <= 21:
    player_lost = True
  elif player_sum > 21:
    player_lost = True
  elif computer_sum > 21 and player_sum <= 21:
    player_lost = False
  Final_Communications()

def Final_Communications():
  if player_lost == True:
    print ("\nThe dealer won")
    print (f"You had: {player_sum} and the dealer had {computer_sum}")

  elif player_lost == False:
    print ("\nYou have won!")
    print (f"The computer total was: {computer_sum} and your total was: {player_sum}")

  print (f"\nFinal Computer hand: {computer_hand}")
  print (f"Your final hand: {player_hand}")

Initial_Deal()
Computer_play()
Player_play()

