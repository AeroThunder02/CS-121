from Die import Die

class DiceQuad():

    def __init__(self):
        '''Initilizes dieList as a list of 4 Die objects
            To create a die object, call Die()'''

        self.dieList = [Die(), Die(), Die(), Die()]
        
    def roll(self):
        '''Rolls all four dice in dieList'''
        
        self.dieList[0].roll()
        self.dieList[1].roll()
        self.dieList[2].roll()
        self.dieList[3].roll()


        return self.dieList
        
    
    def num1s(self):
        '''return the number of ones rolled'''
        onesTotal = 0
        
        for x in self.dieList:
            
            if x.getFaceValue() == 1:
                onesTotal += 1
            else:
                continue
        
        return onesTotal        
        
    
    
    def getDiceTotal(self):
        '''return the sum of the dice'''
        diceTotal = 0

        for x in range(len(self.dieList)):
            diceTotal += self.dieList[x].getFaceValue()

        return diceTotal
    
        

    def __str__(self):
        '''String representation of the dice roll'''
        s = "("+str(self.dieList[0])
        for x in range(1, len(self.dieList)):
            s = s+","+str(self.dieList[x])
        s = s+")"
        return s
