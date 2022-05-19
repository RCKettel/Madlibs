from Bicycles import Bicycles
from News_Story import News_Story

def main():
#using a where loop to allow the user to choose between the two functions.

        Choose_your_Madlib = int(input("Type your choice: 1 for 'Bicycles' or 2 'News_Story' -- "))
        if Choose_your_Madlib == 1:
            Bicycles()
        elif Choose_your_Madlib == 2:
            News_Story()
        else :
            Choose_your_Madlib = int(input("Please type A or B and press enter/return. "))

if __name__ == "__main__":
    main()