
import os

blank_space = lambda amount: " " * amount #Dynamically creates a specified amount of blank spaces   

split_seg = lambda lines: print("-" * 136, "\n" * lines)  #Seperates segments in terminal, dynamic length and line breaks

cls = lambda: (os.system("cls"), print("\n")) #Named after powershell command; clears the terminal and adds an empty line

bold = lambda bold_txt: f"\033[1m{bold_txt}\033[0m" #Turns input text bold


def clamp(value, max = 0, min = None):
    
    if max is not None and value > max:
        value = max
    
    elif min is not None and value < min:
        value = min

    return value

