print()
print()
print()

print("Welcome to the Bank of Florida!")
balance = 100000
original_pin = 1430
def pincode():
    global balance
    global original_pin
    try:
        pin = int(input("Enter the pin: "))
        if pin < 1000 or pin > 9999:
            print("Please Enter a 4 Digit pin")
            pincode()
        elif pin != original_pin:
            print("The Entered pin is Incorrect, Please try again!")
            pincode()
        else:
            def option():

                print()
                print()
                print()
                print("Choose any one of the Options available")
                print("1. Withdraw")
                print("2. Deposit")
                print("3. Balance Enquiry")
                print("4. Pin Change Request")
                print("5. Exit")

                global balance
                global original_pin
                enter = int(input("Enter the Option you want to chose: "))

                if enter >= 1 and enter <= 5:

                    if enter == 1:
                        def pin1():
                            pin = int(input("Enter the pin: "))
                            if pin != original_pin:
                                print("Try Again, You have entered Wrong pin")
                                pin1()
                            else:
                                def withdraw():
                                    global balance
                                    amount = int(input("Enter the amount you want to withdraw: "))
                                    if amount % 100 != 0:
                                        print("Enter the amount in multiples of 100")
                                        withdraw()
                                    else:
                                        balance -= amount
                                        if balance < amount:
                                            print("Insufficient Balance")
                                        else:
                                            print("Money has been Withdrawn Succesfully!!")
                                            print("The remaining balance is: ", balance)
                                            option()

                                withdraw()

                        pin1()
                    elif enter == 2:
                        def pin2():
                            pin = int(input("Enter the pin: "))
                            if pin != original_pin:
                                print("Try Again, You have entered Wrong pin")
                                pin2()
                            else:
                                def deposit():
                                    global balance
                                    amount = int(input("Enter the amount to be deposit: "))
                                    if amount % 100 != 0:
                                        print("Enter the amount in multiples of 100")
                                        deposit()
                                    else:
                                        balance += amount
                                        print("Money has been added to the account succesfully")
                                        print("The remaining balance is: ", balance)
                                        option()

                                deposit()

                        pin2()
                    elif enter == 3:
                        def pin3():
                            global balance
                            pin = int(input("Enter the pin: "))
                            if pin != original_pin:
                                print("Try Again, You have entered Wrong pin")
                                pin3()
                            else:
                                print("The remaining balance is: ", balance)
                                option()

                        pin3()
                    elif enter == 4:
                        def pin4():
                            pin = int(input("Enter the pin: "))
                            if pin != original_pin:
                                print("Try Again, You have entered Wrong pin")
                                pin4()
                            else:
                                def change_pin():
                                    global original_pin
                                    new_pin = int(input("Enter new pin: "))
                                    if new_pin < 1000 or new_pin > 9999:
                                        print("Please Enter a 4 Digit pin")
                                        change_pin()
                                    else:
                                        original_pin = new_pin
                                        print("Pin has been changed succesfully")
                                        option()

                                change_pin()

                        pin4()
                    elif enter == 5:
                        print("You have Exited Succesfully")

                else:
                    print("Choose a Valid Option")
                    option()

            option()
    except ValueError:
        print("Please Enter only 4 digit Integer Value as Pincode")
        pincode()
pincode()
