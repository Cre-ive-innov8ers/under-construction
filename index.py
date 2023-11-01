

balance = 20000000000000.0
#############
while True:
    print("_____________________________________________________________________")
    print("Welcome to CI bank.\n1). Register an account. \n2). Login. \n3). Exit")
    choice = input("Option: ")
    print("##################################################################### \n")
    if choice == '1':  #Register an account   
        #Storing of data
        ######################################
        # Data to be stored
        username = input("Userame:")
        password = input("create password:")
        amount_to_add = float(input("Enter: "))
            
        with open("newdata.txt", "r") as file:
            # Read the lines of the file into a list
            lines = file.readlines()
            new_list = [item[:-1] for item in lines]
            comb = username+password
            print(comb)

            for i in range(len(new_list)):#removing space between the name and password
                words = new_list[i].split()
                new_list[i] = ''.join(words)
                if comb == new_list[i]:
                    isExist = True
                else:
                    isExist = False
            # print(new_list)
            
                
        if isExist:
            print('Use a different password')
        else:    
            file_name = username + ".txt"
            with open(file_name, "w") as file:
                file.write('balance = 0.0 \n')
                
            # Open the file in write mode ("w")
            with open("newdata.txt", "a") as file:
                # Write the data to the file
                file.write(username.lower()  + " "+ password.lower()  + "\n")
            ################################################################
            with open(file_name, "r") as file:
                # Read the lines of the file into a list
                lines = file.readlines()
                new_list = [item[:-1] for item in lines]
                print(new_list)
            #----------------------------------------------------------------
                balance_str = new_list[0].split('=')[1].strip()  # Extract the balance string and remove leading/trailing spaces
                current_balance = float(balance_str.lstrip('R'))  # Convert to float

                # Calculate the new balance
                new_balance = current_balance + amount_to_add

                # Update the first element of the list with the new balance
                new_list[0] = f"balance = R{new_balance:.2f}"
                with open(file_name, 'a') as file:
                    file.write(new_list[0])
            #----------------------------------------------------------------
            
                for i in range(len(new_list)):#removing space between the name and password
                    words = new_list[i].split()
                    new_list[i] = ''.join(words)
                print(new_list)
            ################################################################
            
            print(f"Registration was a success")
            print("Do you want ot proceed with transaction? \n1). Yes. \n2). No.")
            user_choice = input('Option: ')
            if user_choice == '1':#Yes
                print('Continue with transaction')
                print("Welcome again to CI Bank.\n1). Deposit.\n2).withdraw.\n3). Exit")
                print('--------------------------------------------------------')
                option =input('option: ')
                print('--------------------------------------------------------')
                if option == '1':#depositing option
                    the_amount = input("How much would you like to deposit? ")
                    amount = the_amount.replace(" ", "").strip()
                    if amount.replace('.', '',1).isdigit():
                        amount = float(amount)
                        balance += amount
                        print(f'Deposit of R{amount} was successfully made.')

                        #Log the deposit in the transaction log file
                        with open("Transaction Log.txt", "a") as log_file:
                            log_file.write(f"{comb}: +R{amount}\n")
                        with open(file_name, "a") as file:
                            file.write(f"{comb}: +R{amount}\n")
                            
                           
                elif option == '2':#withdrawing option
                    print('withdraw')
                    the_amount = input("How much would you like to withdraw? ")
                    amount = the_amount.replace(" ", "").strip()
                    if amount.replace('.', '',1).isdigit():  # Check if input is a valid number
                        amount = float(amount)
                
                        if amount <= balance:
                            balance -= amount
                            print(f'Withdrawal of R{amount} successful.')
        
                            #Log the withdrawal in the transaction log file
                            with open("Transaction Log.txt", "a") as log_file:
                                log_file.write(f"Withdrawal: -R{amount}\n")
                            with open(username, "a") as file:
                                file.write(f"{comb}: -R{amount}\n")
                        else:
                            print("Insufficient funds.")
   
                elif option == '3':
                    print('Exit')
                    break
                else:
                    print('invalid input')
            elif user_choice == '2':#no
                print('##################################### \n\tThank you for choosing CI Bank \n######################################')
            else:
                print('Invalid selection')
            ######Login
            
    
    elif choice == '2':#Login
        print('please enter your credentials')
        username = input("Userame:")
        password = input("create password:")
        ################################
        #Lets do Deposits and Withdrawals
       
        with open("newdata.txt", "r") as file:
            # Read the lines of the file into a list
            lines = file.readlines()
            new_list = [item[:-1] for item in lines]
            comb = username+password
            print(comb)

            for i in range(len(new_list)):#removing space between the name and password
                words = new_list[i].split()
                new_list[i] = ''.join(words)
            if comb == new_list[i]:
                
                print("lets deposit")
                print("##########################################")
                print(f"Hy {username}, welcome back. \n1). Deposit. \n2). Withdraw. \n3). Exit.")
                option = input("option: ")
                #Option statements
                if option == '1':
                    print('deposit')
                    file_name = username + ".txt"
                    the_amount = input("How much would you like to deposit? ")
                    amount = the_amount.replace(" ", "").strip()
                    if amount.replace('.', '',1).isdigit():
                        amount = float(amount)
                        balance += amount
                        print(f'Deposit of R{amount} was successfully made.')
                        #Log the deposit in the transaction log file
                        with open("Transaction Log.txt", "a") as log_file:
                            log_file.write(f"{comb}: +R{amount}\n")
                        with open(file_name, "a") as file:
                            file.write(f"{comb}: +R{amount}\n")
                    else:
                        print("################################################################\nInvalid input\n################################################################")
                elif option == '2':
                    print('withdraw')
                    the_amount = input("How much would you like to withdraw? ")
                    amount = the_amount.replace(" ", "").strip()
                    if amount.replace('.', '',1).isdigit():  # Check if input is a valid number
                        amount = float(amount)
                
                        if amount <= balance:
                            balance -= amount
                            print(f'Withdrawal of R{amount} successful.')
        
                            #Log the withdrawal in the transaction log file
                            with open("Transaction Log.txt", "a") as log_file:
                                log_file.write(f"Withdrawal: -R{amount}\n")
                            with open(username+".txt", "a") as file:
                                file.write(f"{comb}: -R{amount}\n")
                        else:
                            print("Insufficient funds.")
                elif option == '3':
                    print("Thank you for using our CI Bank App")
                    break
                else:
                    print('invalid input')
            else:
                
                print(f"Please check your credentials and try again or \nregister with us if you do not have an account with us.")
                
                    
            # print(new_list)
            print("##########################################")
    elif choice == '3':
        print("Thank yo for choosing CI bank.")
        print("##########################################\n############################################")
        
    else:
        print('invalid input!')