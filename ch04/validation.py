#!/usr/bin/env python3

#pass in the input, high validity, low validity 
def get_float(prompt, low, high):
    while True:
        number = float(input(prompt)) 
        if low > number and high <= number:
            print("Your monthly interest rate is:" + number)    
        else:
            print("Entry must be greater than", low, "and less than or equal to", high)
    

def get_int(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low, "and less than or equal to", high)


def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        valid_integer = get_float("Enter number: ", 0, 1000)
    print("Valid number = ", valid_integer)
    print()
    valid_integer = get_int("Enter integer: ", 0, 50)
    print("Valid integer = ", valid_integer)
    print()

        # see if the user wants to continue
    choice = input("Continue? (y/n): ")
    print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
