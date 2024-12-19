
import os


blank_space = lambda amount: " " * amount #Creates a specified amount of blank spaces   
 
clear = lambda: (os.system("cls"), print("\n")) #Named after powershell command; clears the terminal and adds an empty line

bold = lambda bold_txt: f"\033[1m{bold_txt}\033[0m" #Turns input text bold


#Clamps between a minimum and max value
def clamp(value, max = None, min = None):
    
    if max is not None and value >= max:
        value = max
    
    elif min is not None and value <= min:
        value = min
        
    return value


#Breaks into new line after a certain length
def row_break(index: int, row_length: int, line_breaks: int = 1):

    if index % row_length == 0: 
        print(end= "\n" * line_breaks)


#Standardizes
def standardize(text: str, lower: bool = True, del_space: bool = True):

    if del_space:
        text = "".join(list(filter(lambda x: x != " ", text)))
    
    if lower:

        text.lower()
    
    return text






