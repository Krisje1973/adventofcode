import os, sys
from re import Pattern
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
sys.path.append("C:\DevOps\github\AdventOfCode")

from AOCHelper import * 
input = []

def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
   
    input = readinput_lines(filename)
    
def main():
   readinput("input_ex.txt")
   first_star()       
   second_star()

def first_star():
    result = 0
    
    for line in input:
        test, operators = line.split(":")
        test = int(test)   
        values = list([*map(int,operators.split())])    
     
        if can_add_or_multiply(test, values):
            result += test
        
    print("Result First Star")
    print(result)

def can_add_or_multiply(test,values):
    last = values[-1]
    if len(values) == 1: return test == last                                           

    # Divide 
    if test % last == 0 and can_add_or_multiply(test // last, values[:-1]): return True

    # Add
    if test > last and can_add_or_multiply(test - last,values[:-1]): return True

    return False

def second_star():
    result = 0
   
    print("Result Second Star")
    print(result)

if __name__ == '__main__':
    main()






