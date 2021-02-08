#************************************************************
# *  Name  : Maciej Kowalczyk
# * Pledge : I pledge my honor that I have abided by the Stevens Honor System.
#************************************************************
#IMPORTANT PLEASE READ:
#Zero clue what is happening with self.displayWinner, but i breaks the automatic detection for a
#winner. Theres nothing in that function that messes with auto win recog. but it breaks it for some
#strange reason that I cannot wrap my head around.
'''
4-Dice Pig, this time with classes!

Adapted from Java to Python by David Treder, 12/2020

---

For your final project, we are going to revisit the Pig game we programmed
for a previous lab. If you need a refresher for the rules for pig, just check
back on the previous lab. All the rules are the same for this assignment.

Just like in the previous assignment, we have provided the structure the code
should follow. All you have to do is fill in the blanks! Unlike previous
assignments, this game is broken up into multiple files. Make sure you
implement all the missing functions in all the files.

Also, this time the AI is not optional. Don’t worry though, we have provided
enough of a skeleton to lead you to the right solutions.

You may need to add additional functions to help get your code working. Feel
free to do that, just try to avoid renaming existing functions. That can
mess up our testing.

On a similar note, do not change the names of the files provided to you.
We may be testing individual classes which requires the name to be predictable.

Good luck!
'''

import HumanPlayer as hp
import ComputerPlayer as cp


class Pig:
    def __init__(self, isPlayer1Human = True, name1 = "Human 1", isPlayer2Human = False, name2 = "Computer 2"):
        if (isPlayer1Human):
            self.player1 = hp.HumanPlayer(self, name1)
        else:
            self.player1 = cp.ComputerPlayer(self, name1)

        if (isPlayer2Human):
            self.player2 = hp.HumanPlayer(self, name2)
        else:
            self.player2 = cp.ComputerPlayer(self, name2)

        self.currentPlayer = self.player1
        self.run()

    
    
    def wantsPlayAgain(self):
        '''Once the game is over, asks the user if they want to play again'''
        #TODO (F)
        
        ans = input("Do you want to play again? Please input yes or  no.")
        
        if ans == 'yes':
            return True
        
        else:
            return False

    def displayHeader(self, player):
        print("----------")
        print(player.getName() + "\'s turn.")
        print("----------")
            
    def gameOver(self):
        '''return a boolean if the game is over'''
        
        if self.player1.hasWon():
            return True
        
        elif self.player2.hasWon():
            return True
        
        else:
            return False
            

    def swapTurn(self):
        '''Once a player's turn is over, switches to the other players turn'''
        #TODO (F)
        
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
           
        else:
            self.currentPlayer = self.player1

        

    def playOnce(self):
        '''Plays one full game of Pig. Should also reset any required variables'''
        
        
        
        while self.gameOver() == False:
            
            self.displayHeader(self.currentPlayer)
            self.currentPlayer.doTurn()
            self.swapTurn()

        self.displayWinner()   
        self.player1.reset()
        self.player2.reset()
        

    def run(self):
        self.playOnce()
        while(self.wantsPlayAgain()):
            self.playOnce()


    def __str__(self):
        '''The current score, or the name of the winner if game is over.'''

        if (self.gameOver()):
            winner = self.player1.getName() if self.player1.hasWon() else self.player2.getName()
            return winner + " won!"
        else:
            return "Game status: " + "\n\t" + str(self.player1) + "\n\t" + str(self.player2)


    

    def displayScores(self):
        print(self)

    def displayWinner(self):
        print("====================")
        self.displayScores()
        print("====================")

    

if __name__ == "__main__":
    '''Welcomes the user to the game, get the user's names and
        if each user is a human or not.
        Then creates a Pig object.'''

    #TODO (F)
    p1Name = input("Welcome player 1, please enter a name.")
    p2Name = input("Welcome player 2, please enter a name.")

    p1check = input(p1Name + ": If you are human, please enter Y. Otherwise, enter N") 
    p2check = input(p2Name + ": If you are human, please enter Y. Otherwise, enter N")
    
    if p1check == "N":
        p1Human = False 
    else:
        p1Human = True

    if p2check == "N":
        p2Human = False 
    else:
        p2Human = True
        

    Pig(p1Human, p1Name, p2Human, p2Name)















        
