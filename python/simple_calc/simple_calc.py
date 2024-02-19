# simple calculator code

import operator 
import sys

operators = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv,
    "%" : operator.mod,
    ">>": operator.lshift,
    "<<": operator.rshift,
    "**": operator.pow
    
}

def get_user_input():
    try:
        number1 = float(input("Enter first number : "))
        number2 = float(input("Enter second number : "))
        op      = input("Enter function (valid values are +,-,*,/): ")
        
        func    = operators.get(op)
    except:
        return(None, None, None)
        
    return (number1, number2, func)
        
if __name__ == "__main__":
   
    Python_Version = sys.version_info[0]
    
    if Python_Version == 2:
        def input(prompt):
            return raw_input(prompt)
    
    while True:
        (num1, num2, func) = get_user_input()
        
        if (num1 == None) or (num2 == None) or (func == None):
            print ("Invalid input")
            break
        
        print (func(num1, num2))