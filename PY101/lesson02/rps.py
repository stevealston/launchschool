import random

VALID_CHOICES = ['rock', 'paper', 'scissors']



def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        prompt("You win!")
    elif (player == computer):
        prompt("It's a tie!")
    else:
        prompt("Computer Wins!")

def prompt(msg):
    print(f"==> {msg}")
    
while True:
  prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
  player_choice = input()

  while player_choice not in VALID_CHOICES:
      prompt("That's not a valid choice")
      player_choice = input()

  computer_choice = random.choice(VALID_CHOICES)

  display_winner(player_choice, computer_choice)

  while True:
      prompt("Do you want to play again (y/n)?")
      answer = input().lower()

      if answer.startswith('n') or answer.startswith('y'):
          break
      else:
          prompt("That's not a valid choice")

  if answer[0] == 'n':
      break
