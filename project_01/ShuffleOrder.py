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
        # NUMBERS FOR ACE1 and ACE2 RESEMBLE THEIR SLOT # (WILL USE FOR SERVO)
        Ace1 = (self.Players - self.SBP) + 1
        Ace2 = (2 * self.Players - self.SBP) + 1
        self.Slots[Ace1-1] = 'A1'
        self.Slots[Ace2-1] = 'A2'  
        
        # determining slots to place King Markers (if requested by user)
        if self.HandSelected == 1:
            Player_W_KK = random.randint(1,self.Players-1) 
            print('Player W/ KK: ' + str(Player_W_KK))
      
            if Player_W_KK >= self.SBP:
                # NUMBERS FOR KING1 and KING2 RESEMBLE THEIR SLOT # (WILL USE FOR SERVO)
                King1 = (Player_W_KK - self.SBP + 1)
                King2 = ((Player_W_KK - self.SBP) + self.Players + 1)
                self.Slots[King1-1] = 'K1'
                self.Slots[King2-1] = 'K2'            
            
            if Player_W_KK < self.SBP:
                # NUMBERS FOR KING1 and KING2 RESEMBLE THEIR SLOT # (WILL USE FOR SERVO)
                King1 = (self.Players - (self.SBP - Player_W_KK) + 1)
                King2 = (2*self.Players - (self.SBP - Player_W_KK) + 1)
                self.Slots[King1-1] = 'K1'
                self.Slots[King2-1] = 'K2'
   
        #randomize positions of array
        #random.shuffle(self.Slots) 
       
        print(self.Slots)
        
# ------------------------------------------------------------------   
# MAIN SCRIPT

# Creating an instance of the Display Class
Player_Menu = display.Display()
# Creating an instance of the ShuffleOrder Class
UserShufflerOrder = ShuffleOrder(Player_Menu.ShuffleChoice,Player_Menu.SBP,Player_Menu.Players,Player_Menu.HandSelected)

# Running either shuffling method from ShuffleOrder (depending on user input) 
if Player_Menu.ShuffleChoice == 0:
    UserShufflerOrder.Random_Shuffle()
else:
    UserShufflerOrder.Modified_Shuffle()
