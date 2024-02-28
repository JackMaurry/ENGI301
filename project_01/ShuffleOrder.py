import random

# Will run segmented display and take in menu button presses
class Menu:
    
    #FOLLOWING ITEMS WILL BE OBTAINED FROM USER
    Shuffle_Choice = 1
    Players = 6
    SBP = 2
    HandSelected = 'COOL'
    
    def __init__(self):
        pass
    
    def getall(self):
        return self.Shuffle_Choice, self.Players, self.SBP, self.HandSelected

# Determines the order of the shuffle for the wheel servo to move between slots
class ShuffleOrder:
    Slots = []
    
    def __init__(self, Shuffle_Choice, Players, SBP, HandSelected):
        self.Shuffle_Choice = Shuffle_Choice
        self.Players = Players
        self.SBP = SBP
        self.HandSelected = HandSelected
   
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
        if self.HandSelected == 'COOL':
            Player_W_KK = random.randint(1,self.Players-1) 
            print(Player_W_KK)
      
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
        random.shuffle(self.Slots) 
       
        print(self.Slots)
                 
        
# If modified shuffle desired, takes photos of each card and determines location
#class ImageProcessing():  
    
# Uses servo 1 and shuffle order data to move slotted wheel to correct position
#class WheelAdjustment():
    
# Uses servo 2 to eject card into the slotted wheel
#class CardEjection():
  
# uses servo 1 to funnel cards through slit
#class DeckRecollection():
    
# ------------------------------------------------------------------   
# MAIN SCRIPT

# Creating an instance of the Menu Class
UserInput = Menu()

# Creating an array to store all variables within the Menu class
menuall=UserInput.getall()

# Creating an instance of the ShuffleOrder Class
UserShufflerOrder = ShuffleOrder(menuall[0],menuall[1],menuall[2],menuall[3])

# Running either shuffling method from ShuffleOrder (depending on user input) 
if menuall[0] == 0:
    UserShufflerOrder.Random_Shuffle()

if menuall[0] == 1:
    UserShufflerOrder.Modified_Shuffle()
