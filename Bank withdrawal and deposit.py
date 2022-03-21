# Author == Hammad Ahmed
# Python IDLE

# a program to enter the balance and give withdrawal and deposit options
# using while loop to make the program run for unlimited period of time
i=1
j=2
while(i<j):
  # we will take a floating point number from the user as balance and save it in the variable 'balance'
  balance=float(input(" Enter account balance : "))
  # using if condition to withdraw or deposit the required amount from the current balance
  if balance>0 :
              print(" 1.Withdrawal \n 2.Deposit")
              # ch variable represents the choice to write either 1 or 2 to give withdrawal or deposit command
              ch=eval(input("\n Type 1 or 2 according to your use: "))
              # if the user enters 1 then the withdrawal option will be considered 
              if ch==1:
                    # program will ask the user to enter the withdrawable amount and store  it in 'withdr'
                    withdr=float(input(" How much amount do you want to withdraw : "))
                    # the new balance will be the earlier balance minus the withdrawal and will be stored in the variable 'newbalance'
                    newbalance=balance-withdr
                    # if the newbalance is in negative, then the amount to be withdrawn is more than the actual balance so the else option will be printed
                    if newbalance>=0:
                        print(" The new balance is ", newbalance)
                    else:
                        print(" Insufficiant funds ")
              # if the user enters 2 then the deposit option will be considered          
              elif ch==2:
                    # program will ask the user to enter the deposit amount and store  it in 'depos'
                    depos=float(input(" How much amount do you want to deposit into your account : "))
                    # the new balance is the previous balance plus the deposited amount and will be stored in the variable 'newbalan' 
                    newbalan=balance+depos
                    print(" The new balance is ", newbalan)
              else:
                  print("Please enter 1 or 2")
  # if the user enters 0, then the account balance would be empty and else option would be condidered                      
  else :
     print(" You don't have any balance in your account ...... ")
