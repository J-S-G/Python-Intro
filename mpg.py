#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))

#Creating an int variable for gas cost
gas_cost = float(input("Enter cost per gallon:\t\t"))
                       
# calculate miles per gallon
mpg = miles_driven / gallons_used
                       
#Decimal place rounded to 1 
mpg = round(mpg, 1)

#I cannot round 2 variables here:
#gas_cost = round(gas_cost, 1)
#miles_driven = round(miles_driven,1)

# format and display the result
print()
print("Miles Per Gallon:\t" + str(mpg))
#Calculate the cost per mile 
print("Total Gas Cost:\t\t" + str(gallons_used*gas_cost))
#Print gas price per mile /n I can round 2 variables here:
print("Cost Per Mile:\t\t" + str(round(gas_cost/miles_driven,2)))
print("Happy Driving")




