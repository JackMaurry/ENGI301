
class WheelMovement:
    
    
    def __init__(self, Slots, Ace1, Ace2, King1, King2):
        self.Slots = Slots
        self.Ace1 = Ace1
        self.Ace2 = Ace2
        self.King1 = King1
        self.King2 = King2
        self.CurrentSlot = None
        self.PreviousSlot = None
        self.SlotDifference = None
        self.SlotMovement = None
        
        self.Acecounter = 0
        self.RotationValues = []

   
    def ReadSlots(self):
        
        # loop for random slot config (no need to call OCR or Camera code)
        if (self.Ace1 == None):
            self.CurrentSlot = 1
            for i in range (1,53):
                self.PreviousSlot = self.CurrentSlot
                self.CurrentSlot = self.Slots[i-1] 
                self.SlotDifference = self.CurrentSlot - self.PreviousSlot
                
                if self.SlotDifference >= 0:
                    self.SlotMovement = self.SlotDifference
                   
                else:
                    self.SlotMovement = 52 - self.CurrentSlot
                
                self.RotationValues.append(self.SlotMovement)
        
        print(self.RotationValues)
        "CALCULATE ROTATIONAL VALUE TO SEND TO SERVO"
            
        # loop for AA user-defined shuffle
        if (self.King1 == None and self.Ace1 != None):
            for i in range (1,52):

                "CALL CAMERA CODE TO TAKE PHOTO"
                "CALL OCR CODE TO ANALYZE PHOTO --> Outputted letter/number = OCR_Output"
                
                
                # scenario if non-user defined card is detected (no Ace or King)
                if OCR_Output != A and OCR_Output != K:
                    self.PreviousSlot = self.CurrentSlot
                    self.CurrentSlot = self.Slots[i] 
                    self.SlotDifference = self.CurrentSlot - self.PreviousSlot
                
                    if self.SlotDifference > 0:
                        self.SlotMovement = self.SlotDifference
                   
                    else:
                        self.SlotMovement = 52 - self.CurrentSlot
                
                else:
                    self.PreviousSlot = self.CurrentSlot
                    
                    #determining whether detected card is Ace1 or Ace2
                    if self.Acecounter == 0:
                        self.CurrentSlot = self.Ace1
                        self.Acecounter = self.Acecounter + 1
                    else:
                        self.CurrentSlot = self.Ace2

                    self.SlotDifference = self.CurrentSlot - self.PreviousSlot
                
                    if self.SlotDifference > 0:
                        self.SlotMovement = self.SlotDifference
                   
                    else:
                        self.SlotMovement = 52 - self.CurrentSlot

                    


            
            




    
            
            