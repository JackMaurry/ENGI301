import random

import sys
sys.path.append("UI/Menu")
import display

# Determines the order of the shuffle for the wheel servo to move between slots
class ShuffleOrder:
    
    
    def __init__(self, ShuffleChoice, SBP, Players, HandSelected):
        self.ShuffleChoice = ShuffleChoice
        self.Players = Players
        self.SBP = SBP
        self.HandSelected = HandSelected
        self.Slots = []
        self.Ace1 = None
        self.Ace2 = None
        self.King1 = None
        self.King2 = None
   
    def Random_Shuffle(self):
        #Create array with numbers 1-52
        for i in range (1,53):
            self.Slots.append(i)
        #randomize positions of array
        random.shuffle(self.Slots)
        print(self.Slots)
    
    def Modified_Shuffle(self):
        #Create array with numbers 1-52
        for i in range (1,53):
            self.Slots.append(i)
            
        # formula to place Ace Markers within array 
        self.Ace1 = (self.Players - self.SBP) + 1
        self.Ace2 = (2 * self.Players - self.SBP) + 1
        self.Slots[self.Ace1-1] = 'A1'
        self.Slots[self.Ace2-1] = 'A2'  
        
        # determining slots to place King Markers (if requested by user)
        if self.HandSelected == 1:
            Player_W_KK = random.randint(1,self.Players-1) 
            print('Player W/ KK: ' + str(Player_W_KK))
      
            if Player_W_KK >= self.SBP:
                self.King1 = (Player_W_KK - self.SBP) + 1
                self.King2 = ((Player_W_KK - self.SBP) + self.Players) + 1
                self.Slots[self.King1 - 1] = 'K1'
                self.Slots[self.King2 - 1] = 'K2'            
            
            if Player_W_KK < self.SBP:
                self.King1 = (self.Players - (self.SBP - Player_W_KK)) + 1
                self.King2 = (2*self.Players - (self.SBP - Player_W_KK)) + 1
                self.Slots[self.King1 - 1] = 'K1'
                self.Slots[self.King2 - 1] = 'K2'
   
        #randomize positions of array
        #random.shuffle(self.Slots) WILL COMMENT BACK IN
       
        print(self.Slots)
        

