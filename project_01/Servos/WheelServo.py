
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
        self.AceCounter = 1
        self.KingCounter = 1
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
                    self.SlotMovement = 52 + self.SlotDifference
                
                self.RotationValues.append(self.SlotMovement)
        
        print(self.RotationValues)
        "CALCULATE ROTATIONAL VALUE TO SEND TO SERVO"
            
        # loop for user-defined shuffle (AA and COOLER)
        if (self.Ace1 != None):
            self.CurrentSlot = 1
            for i in range (1,53):

                "CALL CAMERA CODE TO TAKE PHOTO"
                "CALL OCR CODE TO ANALYZE PHOTO --> Outputted letter/number = OCR_Output"
                
                # Alters card placement order if Ace is found
                if OCR_Output == 'A':
                    self.PreviousSlot = self.CurrentSlot
                    
                    #determining whether detected card should go in Ace1 slot or Ace2 slot
                    if self.AceCounter == 2:
                        self.CurrentSlot = self.Ace2
                        self.AceCounter = self.AceCounter + 1
                        
                    if self.AceCounter == 1:
                        self.CurrentSlot = self.Ace1
                        self.AceCounter = self.AceCounter + 1

                    self.SlotDifference = self.CurrentSlot - self.PreviousSlot
                
                    if self.SlotDifference > 0:
                        self.SlotMovement = self.SlotDifference
                   
                    else:
                        self.SlotMovement = 52 - self.CurrentSlot

                # Alters card placement order if Ace is found
                if OCR_Output == 'K':
                    self.PreviousSlot = self.CurrentSlot
                    
                    #determining whether detected card is Ace1 or Ace2
                    if self.KingCounter == 2:
                        self.CurrentSlot = self.King2
                        self.KingCounter = self.KingCounter + 1
                        
                    if self.Acecounter == 1:
                        self.CurrentSlot = self.King1
                        self.KingCounter = self.KingCounter + 1

                    self.SlotDifference = self.CurrentSlot - self.PreviousSlot
                
                    if self.SlotDifference > 0:
                        self.SlotMovement = self.SlotDifference
                   
                    else:
                        self.SlotMovement = 52 - self.CurrentSlot
                
                # scenario if non-user defined card is detected (no Ace/King)
                else:
                    self.PreviousSlot = self.CurrentSlot
                    self.CurrentSlot = self.Slots[i-1] 
                    self.SlotDifference = self.CurrentSlot - self.PreviousSlot
                
                    if self.SlotDifference > 0:
                        self.SlotMovement = self.SlotDifference
                   
                    else:
                        self.SlotMovement = 52 - self.CurrentSlot

            
            




    
            
            