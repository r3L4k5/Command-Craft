
import os

blank_space = lambda amount: " " * amount #Dynamically creates a specified amount of blank spaces   

cls = lambda: (os.system("cls"), print("\n")) #Named after powershell command; clears the terminal and adds an empty line

bold = lambda bold_txt: f"\033[1m{bold_txt}\033[0m" #Turns input text bold

#Clamps between a minimum and max value
def clamp(value, max = None, min = None):
    
    if max is not None and value > max:
        value = max
    
    elif min is not None and value < min:
        value = min

    return value

def row_break(index, row_length, amount = 1):

    if index % row_length == 0: 
        print(end= "\n" * amount)

