#************************************************************
# *  Name  : Maciej Kowalczyk
# * Pledge :  I pledge my Honor that I have abided by the Stevens Honor System.
#************************************************************

'''
4-Dice Pig

Adapted from Java to Python by Justin Barish,  11/2018
Modified Nov '19 by Toby Dalton, Nov '20 by Dominick DiMaggio

~ ~ ~

To exercise your looping ability, we're going to be filling in a bunch
of blanks. Joy!

Pig is a game where players take turns rolling dice.
Traditionally, it's only 2, but this is a variant.

The goal is to have their total score reach a certain # of points.
Players take turns earning points by rolling dice.
Each roll adds that sum onto a round score, which my or may not be added
to their total score, dictated as below:

A person's turn lasts until they want to stop rolling or roll some 1s.

If at any point during the player's turn they roll one 1:
their round ends and their round score is added to their total score.

If they roll two 1s:
they lose all points for the round, and their turn is over.

Three 1s:
they lose all of their points in the game, and their turn is over.

If they're unlucky and recieve the 'luck' of four 1s (four-eyed snake ::S):
they immediately lose the game.

Whenever the player decide to stop their turn, their round points are 
added to their total points.

When a player's total points reach 100 (controllable below), they win.
'''
import random

POINTS_TO_WIN = 100
AI_ROUND_TARGET = 20

'''
This lab has 2 parts:

Part 1 (10 pts): Complete the game for two human players.
That is, fill in all of the methods below

Part 2 (2 pts Extra Credit):
Add in an "AI" as the second player, so you will play against the computer.
The AI takes the place of player 2, and will continue rolling until
it reaches its AI_ROUND_TARGET. NOTE: You *will* need to change some of the
function paramaters (I.E. pass in additional values) and other parts of
functions.
'''

#************************************************************
#**   General Game Stuff
#************************************************************

def main():
  '''This is the main function for the pig game'''
  welcome()
  while True:
    playGame()
    if not wantsPlayAgain():
      print('Bye!')
      return

def playGame():
  '''Play one game of pig
  Alternates between players, and at the end of a player's turn, 
  prints the overall game score for both players'''

 
  scores = initScores()
  
  while (not gameOver(scores)):
    player = 1
    print()                                                 
    print('Current Scores:')
    printScore(scores)
    getMove(scores, player)
    if gameOver(scores):
      if scores[0] >= POINTS_TO_WIN:
        printWinMessage(1, scores)
        break

    player = 2
    print()                                                 
    print('Current Scores:')
    printScore(scores)
    getMove(scores, player)
    if gameOver(scores):
      if scores[0] >= POINTS_TO_WIN:
        printWinMessage(2, scores)
        


def initScores():
  player1_score = 0
  player2_score = 0
  return [player1_score, player2_score]   #puts score values into an easy to work with list


def gameOver(scores):
  '''Checks if the game is over
  Game is over when either player's score reaches >= POINTS_TO_WIN.
  [ or 4 ones are rolled :3]
  Prints the win message for the player who won
  If no one won, just returns false'''
  if scores[0] >= POINTS_TO_WIN:              
    return True
  
  elif scores[1] >= POINTS_TO_WIN:
    return True
  
  else:
    return False

 
def getMove(scores, player):
  '''Gets a player's move.
  Before every move, prints the current round score and the game score for the player
  Checks if the player wants to continue, and if they do, rolls dice and appropriately changes scores
  '''
  printPlayerMessage(player)
  roundScore = 0
  while True:
    printCurrentPlayerScore(scores, player, roundScore)

    if (not wantsRollAgain(player)):
      printScore(scores)
      break

    roll = rollDice()
    showRoll(roll)
    check = list(filter(lambda x: x==1, roll)) #checks for 1's
    roll_result = sum(check)
    
    if roll_result == 4:
      print("Rolled four 1s... Game Over")
      if player == 1:
        printWinMessage(2, scores)
        break
      else:
        printWinMessage(1, scores)
        break
              
    elif roll_result == 3:
      print("Rolled three 1s. Score reset!")
      if player == 1:
        scores[0] = 0
        break
      else:
        scores[1] = 0
        break
      
    elif roll_result == 2: 
      print("Rolled two 1s! Round ended, no score added")
      roll_result -= roll_result
      break
    
    elif roll_result == 1:
      print("Rolled one 1! Round ended, score added")
      roundScore = sum(roll)
      if player == 1:
        scores[0] += roundScore
        break
      if player == 2:
        scores[1] += roundScore
        break
    else:
      roundScore = sum(roll)
      if player == 1:
        scores[0] += roundScore
                
      if player == 2:
        scores[1] += roundScore
                

def rollDie():
  '''rolls a single die (wow)'''
  return random.randint(1,6)


def rollDice():
  '''grabs the roll for four dice'''
  roll = []
  roll.append(rollDie())
  roll.append(rollDie())
  roll.append(rollDie())
  roll.append(rollDie())
  return roll
    

#************************************************************  
#**   Useful functions to check if we want to [X] again
#************************************************************

# TODO
def wantsContinue(response):
  '''Checks if the response a user gives indicates they want to continue.
  assume the user has to give a Y to mean yes and N to mean no'''
  
  ans = response
  while ans == 'Y':
    return True
  else:
    return False

# TODO  
def wantsPlayAgain():
  '''Asks a player if they want to play the game again (use wantsContinue()!)'''
  
  ans = input("Do you want to play again? Please input Y (yes) or N (no).")
  if ans == 'Y':
    return True
  else:
    return False

# TODO
def wantsRollAgain(player):
  '''Asks a player if they want to roll again
  For Part 2, also handle the Computer's decision'''
  response = input("Would you like to roll? Y for yes, N for no:")
  if wantsContinue(response):
    return True
  else:
    return False

#************************************************************
#**   Functions to Print Things
#************************************************************

def welcome():
  '''Prints the welcome message for the game.
  We might also print the rules for the game and any other
  information that the user might need to know.'''
  print('Welcome to Pig!')

# TODO
def printScore(scores):
  '''prints the current game score for each player'''
  print("Player 1: " + str(scores[0]) + " & Player 2: " + str(scores[1]))

def printWinMessage(winningPlayer, scores):
  print()
  print('***********************Player ' + str(winningPlayer) + ' Won!************************')
  print('***********************Final Score:*************************')
  printScore(scores)

# TODO
def showRoll(roll):
  ''' Prints out the roll'''
  print("Roll: " + str(roll))

def printPlayerMessage(player):
  print()
  print('--------------------------------------------------------------')
  print('-------------------Player ' + str(player) + '\'s turn----------------------------')
  print('--------------------------------------------------------------')
  print()

# TODO
def printCurrentPlayerScore(scores, player, roundScore):
  '''Print the score for a specific player. Prints their round score 
  and their overall game score not including their current round score'''
  print("Player " + str(player) + " has a round score of " + str(roundScore) + " and a total score of " + str(scores[player-1]))

if __name__ == '__main__':
  main()
