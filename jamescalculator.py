import math

def main():
    print("\n|| Investment / Bond Calculator ||\n")
    print("\nInvestment - to calculate the amount of interest you'll earn on your investment")
    print("Bond       - to calculate the amount you'll have to pay on a home loan\n\n")
    menu = input("Enter either 'Investment' or 'Bond' from the menu to proceed: ")
    if menu.lower() == "investment" or menu.lower() == "i":
        print("\nYou have picked the Investment calculator:\n")
        p = int(input("How much are you investing: "))
        r = float(input("What is the interest rate (Enter a number between 0-100): "))
        t = int(input("How many years do you plan on investing for?: "))
        simpleOrCompound = str(input("\nDo you want to calculate Simple or Compound interest: \n"))
        investmentResultMessage = getInvestmentResultMessage(simpleOrCompound, p, r, t)
        print(investmentResultMessage)
    elif menu.lower() == "bond" or menu.lower() == "b":
        print ("\nYou have picked the Bond calculator\n") 
        v = int(input("Enter the value of your house i.e if 500,500 enter 500500: "))
        i = float(input("Enter the interest rate: "))
        n = int(input("Enter the number of repayment months: "))
        bondResultMessage = getBondResultMessage(v,i,n)
        print(bondResultMessage)
    else:
        print("\nRestart & Try again, You need to enter either Investment or Bond!\n")

def getInvestmentResultMessage(simpleOrCompound, p, r, t):
    r = r/100.
    simple_interest = p*(t*r+1)
    compound_interest = p * math.pow((1+r),t) 

    # round the interest for better output reading
    rounded_ci = round(compound_interest, 2)
    rounded_si = round(simple_interest, 2)

    if simpleOrCompound.lower() == "simple" or simpleOrCompound.lower() == "s":
        return "\nThe simple interest on your investment will be:" + str(rounded_si) + "\n"
    elif simpleOrCompound.lower() == "compound" or simpleOrCompound.lower() == "c":
        return "\nThe compound interest on your investment will be:" + str(rounded_ci) + "\n"
    else:
        return "You haven't chosen anything!"

def getBondResultMessage(v,i,n):
    i = i/100.
    monthly_i = i / 12
    repayment = (monthly_i * v)/(1 - (1 + monthly_i)**(-n))
    rounded_r = round(repayment, 2)
    return "\n The monthly repayment amount will be:" + str(rounded_r) + "\n"


if __name__ == "__main__":
    main()