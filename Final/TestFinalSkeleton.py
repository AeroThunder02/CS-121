''''
Created 12/11/2020 by David Treder
CS 115 - Final Pig Project Test Script Skeleton
'''

import unittest
import ComputerPlayer
import DiceQuad
import Die

D = Die.Die()
DQ = DiceQuad.DiceQuad()
C = ComputerPlayer.ComputerPlayer("dummy", "computer")
#NOTE: I initialize the owner as "dummy". This is not valid but we wont be using functions that use owner.

# =============================================
# INSTRUCTIONS:

# Complete the TODOs, and anything else you think is useful.
# Make sure you also test playing the program normally, this won't be able to test everything

class Test(unittest.TestCase):

# TESTING DIE
# Tests creating a die, rolling the die, setting the face of a die, getting the face of a die, string representation of die


    def test_init(self):
        #Check the die starts at 1
        self.assertEqual(D.getFaceValue(), 1)

    def test_roll(self):
        #TODO - Roll the die and assert that it returns the faceValue
        rolledValue = D.roll()
        self.assertEqual(rolledValue, D.getFaceValue())

    def test_set(self):
        #TODO - Set the face of the die and assert the faceValue properly updates
        D.setFaceValue(3)
        faceValue = D.getFaceValue()
        
        self.assertEqual(faceValue, D.getFaceValue())

    def test_str(self):
        #TODO - Set the face value of the die and assert that the string representation is correct
        D.setFaceValue(3)
        faceValue = D.getFaceValue()
        
        self.assertEqual(faceValue, D.getFaceValue()) 
        

#TESTING DICEQUAD
#Tests creating the Quad, rolling the quad, getting the number of 1s, and the sum of the dice

    def test_initQ(self):
        #Check the string representation of the initial state
        self.assertEqual(str(DQ), "(1,1,1,1)")

    def test_rollQ(self):
        #TODO - Roll the quad and assert the string representation is not the default state
        #NOTE:  Dice rolling is random, you may have rolled 4 1s by chance even if the program works.
        #If you fail only this test case, try again. It is very unlikely to happen twice in a row.

        DQ.roll()
        self.assertNotEqual(str(DQ), "(1,1,1,1)")

    def test_ones(self):
        #TODO - Check number of 1s
        #Don't worry about the loop, it just tests this one multiple times
        for i in range(40):
            DQlist = DQ.roll()
            DQoneList = [7,7,7,7]
            
            for x in range(len(DQlist)):
                DQoneList[x] = DQlist[x].getFaceValue()
                               
           
            valList = list(map(lambda x: x.getFaceValue(), DQ.dieList))
            self.assertEqual(DQoneList.count(1), valList.count(1))
            

    def test_total(self):
        #TODO - Check getDiceTotal returns sum of dice
        DQ.roll()
            
        valList = list(map(lambda x: x.getFaceValue(), DQ.dieList))
        

        self.assertEqual(DQ.getDiceTotal(), sum(valList))

# TESTING PLAYER
# Tests hasWon, resetting, getting the current score, and if the computer wants to continue
# Use ComputerPlayer to do all these tests


    def test_hasWon(self):
        C.reset()

        self.assertFalse(C.hasWon())

        C.score = 150

        self.assertTrue(C.hasWon())

    def test_reset(self):
        C.score = 5000
        C.roundScore = 50
        C.isPlayerTurn = True

        C.reset()

        self.assertEqual(0, C.score)
        self.assertEqual(0, C.roundScore)
        self.assertFalse(C.isPlayerTurn)

    def test_curr_score(self):

        s = 400
        rs = 100

        C.score = s

        self.assertEqual(C.score, C.getCurrentScore())

        C.roundScore = rs

        C.isPlayerTurn = True

        self.assertEqual(C.roundScore+C.score, C.getCurrentScore())
       

    def test_wants_cont(self):
        C.reset()

        self.assertFalse(C.wantsHandOver())

        C.roundScore = 25

        self.assertTrue(C.wantsHandOver())
        




if __name__ == "__main__":
    unittest.main()


