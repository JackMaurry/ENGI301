
from ShuffleOrder import ShuffleOrder

import sys

sys.path.append("UI/Menu")
import display

#sys.path.append("Computer Vision")

sys.path.append("Servos")
import WheelServo
#import CardEjectionServo


# ------------------------------------------------------------------   
# MAIN SCRIPT

# Creating an instance of the Display Class
Player_Menu = display.Display()
# Creating an instance of the ShuffleOrder Class
User_Shuffler_Order = ShuffleOrder(Player_Menu.ShuffleChoice,Player_Menu.SBP,Player_Menu.Players,Player_Menu.HandSelected)

# Running either shuffling method from ShuffleOrder (depending on user input) 
if Player_Menu.ShuffleChoice == 0:
    User_Shuffler_Order.Random_Shuffle()
else:
    User_Shuffler_Order.Modified_Shuffle()
    
# Creating an instance of the WheelMovement class
Servo_Movements = WheelServo.WheelMovement(
    User_Shuffler_Order.Slots, 
    User_Shuffler_Order.Ace1, 
    User_Shuffler_Order.Ace2, 
    User_Shuffler_Order.King1, 
    User_Shuffler_Order.King2
)
 
Servo_Movements.ReadSlots()   
 



    
