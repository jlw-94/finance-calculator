# user chooses which calculator they want
# investment or home loan repayment (bond)
# user input can be upper or lower case 

# if user selects investment
    # user inputs 
        # amount of money deposited 
        # interest rate (as percentage) input as an integer 
        # number of years investing
# declare variable of interest 
    # user inputs 
        # simple or compound interest 
# if-else statement inclues formula for simple and interest
# print output

# if user selects bond investment
    # user inputs 
        # value of house
        # interest rate 
        # number of months expected to repay
# condition includes formula for bond 
# print output of monthly repayments

import math

print("\n|| Investment / Bond Calculator ||\n")
print("\nInvestment - to calculate the amount of interest you'll earn on your investment")
print("Bond       - to calculate the amount you'll have to pay on a home loan\n\n")


menu = input("Enter either 'Investment' or 'Bond' from the menu to proceed: ")

# interest calculator
# or added for ease of debugging ( type i or b to proceed )
if menu.lower() == "investment" or menu.lower() == "i":
    
    print("\nYou have picked the Investment calculator:\n")
    
    p = int(input("How much are you investing: "))
    r = float(input("What is the interest rate (Enter a number between 0-100): "))
    t = int(input("How many years do you plan on investing for?: "))
    
    r = r/100.

    simple_interest = p*(t*r+1)

    compound_interest = p * math.pow((1+r),t) 

    # round the interest for better output reading
    rounded_ci = round(compound_interest, 2)
    rounded_si = round(simple_interest, 2)

    interest = str(input("\nDo you want to calculate Simple or Compound interest: \n"))

    if interest.lower() == "simple" or interest.lower() == "s":
        print(f"\nThe simple interest on your investment will be: {rounded_si} \n")
   
    elif interest.lower() == "compound" or interest.lower() == "c":
        print(f"\nThe compound interest on your investment will be: {rounded_ci} \n")
   
    else:
        print("You haven't chosen anything!")

# bond calculator 
elif menu.lower() == "bond" or menu.lower() == "b":
    print ("\nYou have picked the Bond calculator\n") 
    
    v = int(input("Enter the value of your house i.e if 500,500 enter 500500: "))
    i = float(input("Enter the interest rate: "))
    n = int(input("Enter the number of repayment months: "))

    i = i/100.

    monthly_i = i / 12

    repayment = (monthly_i * v)/(1 - (1 + monthly_i)**(-n))

    rounded_r = round(repayment, 2)

    print(f"\n The monthly repayment amount will be: {rounded_r}\n")

else:
    print("\nRestart & Try again, You need to enter either Investment or Bond!\n")






