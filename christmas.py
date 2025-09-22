from utils.utils import *

def print_christmas_tree(height:int) -> None:
    column_width = 2 * height + 1
    for i in range(height):
        print(center_text("*" * (2 * i + 1), column_width))

    #print trunk
    print(center_text("*",column_width))
    print(center_text("*",column_width))
    print(center_text("*",column_width))

#If this check is not there, then this code will execute even when
#this module is only imported in another module or imported in python shell
if (__name__ == "__main__"):
    height = int(input("Enter height: "))
    print_christmas_tree(height)
