# In this challenge, I used os module to clear the screen instead of replit

import random
import os
from art import logo

# function to clear the terminal screen
def clear():
  os.system('cls' if os.name=='nt' else 'clear')

# function to deal a card from the deck
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# function to calculate the score of a hand of cards
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

# function to compare the scores of the player and computer
def compare(user_score, computer_score):
  
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

# function to play a game of Blackjack
def play_game():

  # print the Blackjack logo
  print(logo)

  # initialize the player and computer's hands and game status
  user_cards = []
  computer_cards = []
  is_game_over = False

  # deal two cards to each player
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  # continue playing until the game is over
  while not is_game_over:
    
    # calculate the scores and show the player's cards and the computer's first card
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    # end the game if the player or computer has Blackjack or has gone over 21
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      # ask the player if they want to hit or pass
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  # finish the computer's turn
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  # show the final hands and scores and compare them to determine the winner
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
