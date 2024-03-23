
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
        self.AceCounter = 0
        self.KingCounter = 0
        self.RotationValues = []

    # Turns random slot order into required wheel rotation to reach each slot
    def ReadRandomSlots(self):
        self.CurrentSlot = 1
        for i in range (1,53):
            self.PreviousSlot = self.CurrentSlot
            self.CurrentSlot = self.Slots[i-1] 
            self.SlotDifference = self.CurrentSlot - self.PreviousSlot
            
            # determining slot rotations required 
            if self.SlotDifference >= 0:
                self.SlotMovement = self.SlotDifference
            else:
                self.SlotMovement = 52 + self.SlotDifference
            
            self.RotationValues.append(self.SlotMovement)
    
        print(self.RotationValues)
        "ROTATIONAL SLOT VALUES TO SEND TO SERVO"

    # Turns modified slot order into required wheel rotation to reach each slot
    def ReadModifiedSlots(self):
        self.CurrentSlot = 1
        for i in range (1,53):
            
            "CALL CAMERA CODE TO TAKE PHOTO"
            "CALL OCR CODE TO ANALYZE PHOTO --> Outputted letter/number = OCR_Output"
            OCR_Output = 'A' #placeholder
            
            if self.AceCounter == 2:
                OCR_Output = 'K'
                
            self.PreviousSlot = self.CurrentSlot
            
            # Alters card placement order if Ace is found 
            if OCR_Output == 'A' and self.AceCounter < 2:
                
                #determining whether detected card should go in Ace1 slot or Ace2 slot
                if self.AceCounter == 1:
                    self.CurrentSlot = self.Ace2
                if self.AceCounter == 0:
                    self.CurrentSlot = self.Ace1
                self.AceCounter = self.AceCounter + 1
                
                # determining slot rotations required 
                self.SlotDifference = self.CurrentSlot - self.PreviousSlot
                if self.SlotDifference >= 0:
                    self.SlotMovement = self.SlotDifference
                else:
                    self.SlotMovement = 52 - self.CurrentSlot
               
                #moving i one forward (since we did not append any positions from the actual Slots list)
                i = i + 1
            
                #appending slot rotation value    
                self.RotationValues.append(self.SlotMovement)
                
            # Alters card placement order if King is found 
            elif OCR_Output == 'K' and self.KingCounter < 2:
            
                #determining whether detected card should go in Ace1 slot or Ace2 slot
                if self.KingCounter == 1:
                    self.CurrentSlot = self.King2
                if self.KingCounter == 0:
                    self.CurrentSlot = self.King1
                self.KingCounter = self.KingCounter + 1

                # determining slot rotations required 
                self.SlotDifference = self.CurrentSlot - self.PreviousSlot
                if self.SlotDifference > 0:
                    self.SlotMovement = self.SlotDifference
                else:
                    self.SlotMovement = 52 - self.CurrentSlot
                
                #moving i one forward (since we did not append any positions from the actual Slots list)
                i = i + 1
            
                #appending slot rotation value    
                self.RotationValues.append(self.SlotMovement)               
            
            # scenario if non-user defined card is detected (no Ace/King)
            else:
                self.CurrentSlot = self.Slots[i - 1 - self.AceCounter - self.KingCounter] 
                self.SlotDifference = self.CurrentSlot - self.PreviousSlot
            
                if self.SlotDifference > 0:
                    self.SlotMovement = self.SlotDifference
               
                else:
                    self.SlotMovement = 52 - self.CurrentSlot
            
                #appending slot rotation value    
                self.RotationValues.append(self.SlotMovement)
                
        print(self.RotationValues)        
        




    
            
            