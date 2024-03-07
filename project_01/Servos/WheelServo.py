
class WheelMovement:
    
    
    def __init__(self, Slots, Ace1, Ace2, King1, King2):
        self.Slots = Slots
        self.Ace1 = Ace1
        self.Ace2 = Ace2
        self.King1 = King1
        self.King2 = King2
        self.CurrentSlot = 1
        self.PreviousSlot = None
        self.SlotDifference = None
        self.SlotMovement = None

   
    def ReadSlots(self):
        
        # loop for random slot config (no need to call OCR or Camera code)
        if (self.Ace1 == None):
            for i in range (1,53):
                self.PreviousSlot = self.CurrentSlot
                self.CurrentSlot = Slots[i] 
                self.SlotDifference = self.CurrentSlot - self.PreviousSlot
                
                if self.SlotDifference > 0:
                    self.SlotMovement = self.SlotDifference
                   
                else:
                    self.SlotMovement = 52 - self.CurrentSlot
                
        
        
        print(self.Ace1)  
        print(self.Ace2)

            
            




    
            
            