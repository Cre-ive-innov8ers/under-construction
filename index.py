from datetime import datetime
import os #interacts with the operating sytem.
import re

# Get the current date and time
the_datetime = datetime.now()
current_datetime = the_datetime.strftime("%Y %H:%M:%S")

def is_alpha_input(user_input):
    # Check if all characters in the input are alphabets
    return all(char.isalpha() for char in user_input)

'''This regex pattern ensures that the password contains    
    exactly 4 characters, which can be numbers (0-9) or 
    letters (both lowercase and uppercase).'''
def is_valid_password(password):
    # Define the regex pattern
    pattern = r'^[0-9a-zA-Z]{4}$'
    
    # Use re.match to check if the password matches the pattern
    if re.match(pattern, password):
        return True
    else:
        return False

def create_txt(name,opening_balance):
    with open(f"{name}.txt", "w") as f:
        f.write(f"{current_datetime} balance : +R{opening_balance:.2f}\n")#To be edited
        
    # print(f"{name}.txt created with an opening balance of R{opening_balance:.2f}")
    print("----------------------------------------------------------------------")



def bankdata_txt_deposit(name,time,amount):
    with open("Bank_data.txt", "a") as file:
        # file.write(f"{time} Balance: +R{amount}\n")
        file.write(f"{time} {name}: +R{amount}\n")
    file_name = name+".txt"
    with open(file_name, "a") as file:
        file.write(f"{current_datetime} {name}: +R{amount}\n")
    

def bankdata_txt_withdrawal(name,time,amount):
    with open("Bank_data.txt", "a") as file:
        file.write(f"{time} {name} : -R{amount}\n")
    
    file_name = name+".txt"
    with open(file_name,"a")as f:
        f.write(f"{time} {name}: -R{amount}")

def withdraw(amount, balance):
    if balance >= amount:
        new_balance = balance - amount
    else:
        print("Insufficient funds!")
        print("----------------------------------------------------------------------")
    return new_balance

def balance_update_deposit(balance, amount):
    new_balance = balance + amount
    return new_balance

def balance_update_deposit(balance, amount):
    new_balance = balance - amount
    return new_balance

#  Main function
#####################
while True:
    print("----------------------------------------------------------------------")
    choice = int(input("Welcome to CI Bank solutions\n1) Register\n2) login\n3) Exit\n----------------------------------------------------------------------\nOption: "))
    if choice == 1:#register an accouhnt
        while True:
            name = input("Enter your name: ")
            if is_alpha_input(name):
                while True:
                    password = input("Enter your password: ")
                    
                    if is_valid_password(password):
                        secure = name + password
                        print("----------------------------------------------------------------------")
                        #check if the account is already registered
                        if os.path.isfile(f"{name}.txt"):
                            print("Account already exists")
                            break
                        else:
                            with open("user_infor.txt",'a') as file:
                                file.write(name +" " + password +"\n")
                            with open("user_infor.txt", "r") as file:
                                dat = file.readlines()
                            user_secure = [element.strip().replace(" ", "") for element in dat]
                            
                            # Print the new list
                            
                            
                            strt_amount = float(input("To activate your account you need to deposit a start up amount.\nAmount: "))
                            if strt_amount <= 0:
                                print("your account can't be activated")
                                break
                            elif strt_amount > 0:
                                print(f"Hi {name},your account has been successfully activated.\nCurrent Balance = R{strt_amount}")
                                create_txt(name,strt_amount)
                                bankdata_txt_deposit(name,current_datetime,strt_amount)
                                ##################################
                                            #crate a list from the data in the txt file
                                with open("bank_data.txt", "r") as f:
                                    bank = f.readlines()
                                #check if the account is already registered
                            
                                b_data = bank[0] #first element in the bank data.(balance)
                                strdat = str(b_data) #
                                position_of_r = strdat.find("R")
                                bn_balance = strdat[position_of_r + 1:]
                                #Bank balance.
                                
                                bank_bala =float(bn_balance)# current bank balance
            
                                ################################
                                with open("bank_data.txt", "r") as file:
                                    lines = file.readlines()

                                # Remove the first element (line) from the list
                                lines.pop(0)

                                # Write the modified content back to the text file
                                with open("bank_data.txt", "w") as file:
                                    file.writelines(lines)
                                #############################
                                #Append the new balance to the top of the transaction log
                                new_b_balance =f"{current_datetime} balance : R{bank_bala+strt_amount}\n"
                                # Read the content of the text file
                                with open("bank_data.txt","r")as file:
                                    bank_lines = file.readlines()

                                # Add the new element at the beginning
                                bank_lines.insert(0,new_b_balance)
                                # Write the modified content back to the text file
                                with open("bank_data.txt","w")as file:
                                    file.writelines(bank_lines)
                                    #update bank data
                                ###############################
                                
                                break
                            else:
                                print("Invalid input!")
                                print("----------------------------------------------------------------------")
                                break
                    else:
                        print("----------------------------------------------------------------------")
                        print("Invalid Password,try again")  
                break
            else:
                print("A name can not be anything rather than alphabets only")              
    elif choice == 2:#login
        print("----------------------------------------------------------------------")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        
        #Code that checks if the password and username is in the database 
        with open("user_infor.txt", "r")as file:
            lists = file.readlines()
        # print(lists)
        my_new_list = [element.replace(" ", "").strip() for element in lists]
        
        search_user = name+password

        count = 0
        for item in my_new_list:
            if item == search_user:
                count += 1

        
        ########################
            
        while True:
            #crate a list from the data in the txt file
            with open("bank_data.txt", "r") as f:
                data = f.readlines()
            #check if the account is already registered
           
            bank_data = data[0] #first element in the bank data.(balance)
            str_dat = str(bank_data) #
            position_of_r = str_dat.find("R")
            bn_balance = str_dat[position_of_r + 1:]
            #Bank balance.
            bank_bal =float(bn_balance)# current bank balance
            
            if os.path.isfile(f"{name}.txt") and count > 0:
                print("----------------------------------------------------------------------")
                print(f"Hi {name}, Welcome to CI Bank Solutions!\nPlease navigate your way on this app")
                print("----------------------------------------------------------------------")
                choice = input("1). Deposit\n2). Withdraw \n3). Exit\nOption: ")
                print("----------------------------------------------------------------------")

                if choice == '1':#Deposit
                    deposit_amount = input(f"Hi {name}, how much would you like to deposit?\nAmount: ")
                    print("----------------------------------------------------------------------")
                    ################################
                    #############################
                    file_name = name + ".txt"
                    comb = name+password
                    my_amount = deposit_amount.replace(" ", "").strip()
                    if my_amount.replace('.', '',1).isdigit():
                        my_amount = float(my_amount)
                       
                        #create a list from the users data in the txt
                        with open(file_name, "r") as f:
                            userdata = f.readlines()
                        user_data = userdata[0] #first element in the bank data.(balance)
                        str_userdata = str(user_data) #
                        position_of_r = str_userdata.find("R")
                        us_balance = str_userdata[position_of_r + 1:]
                        #Bank balance.
                        user_bal =float(us_balance)# current bank balance

                        user_bal = user_bal + my_amount #cureent user balance
                        print(f'Deposit of R{my_amount} was successfully made.\n')
                        print(f'Current balance = R{user_bal}.')
                       
                        #Log the deposit in the transaction log file
                        with open("Transaction Log.txt", "a") as log_file:
                            log_file.write(f"{comb}: +R{my_amount}\n")
                        
                       
                        #User update
                        #######################################
                        with open(file_name, "r") as file:
                            lines = file.readlines()
   
                        # Remove the first element (line) from the list
                        lines.pop(0)
 
                        # Write the modified content back to the text file
                        with open(file_name, "w") as file:
                            file.writelines(lines)

                        ######################################
                        #Bank Data update
                        with open('bank_data.txt', "r") as file:
                            bank_lines = file.readlines()
 
                         # Check if there are lines in the file
   
                        # Remove the first element (line) from the list
                        bank_lines.pop(0)
                        # print(f"another:{bank_lines}")
 
                        # Write the modified content back to the text file
                        with open("bank_data.txt", "w") as file:
                            file.writelines(bank_lines)
    
                        #######################################
                       
                        #Append the new balance to the top of the transaction log
                        new_user_balance = f"{current_datetime} balance : R{user_bal}\n"
                        new_bank_balance =f"{current_datetime} balance : R{bank_bal+ my_amount}\n"
                        # Read the content of the text file
                        with open(file_name, "r") as file:
                            lines = file.readlines()
                        with open("bank_data.txt","r")as file:
                            bank_lines = file.readlines()
 
                        # Add the new element at the beginning
                        lines.insert(0, new_user_balance)
                        bank_lines.insert(0,new_bank_balance)
                        # Write the modified content back to the text file
                        with open(file_name, "w") as file:
                            file.writelines(lines)
                        with open("bank_data.txt","w")as file:
                            file.writelines(bank_lines)
                        #update bank data
                        bankdata_txt_deposit(name,current_datetime,my_amount)
                
                    else:
                        print("Invalid input")
                elif choice == '2':#Withdraw
                    withdraw_amount = input(f"Hi {name}, how much would you like to deposit?\nAmount: ")
                    print("----------------------------------------------------------------------")
                    ################################
                    #############################
                    file_name = name + ".txt"
                    comb = name+password
                    my_amount = withdraw_amount.replace(" ", "").strip()
                    if my_amount.replace('.', '',1).isdigit():
                        my_amount = float(my_amount)
                        
                        #create a list from the users data in the txt
                        with open(file_name, "r") as f:
                            userdata = f.readlines()
                        user_data = userdata[0] #first element in the bank data.(balance)
                        str_userdata = str(user_data) #
                        position_of_r = str_userdata.find("R")
                        us_balance = str_userdata[position_of_r + 1:]
                        #Bank balance.
                        user_bal =float(us_balance)# current bank balance
                        #####################
                        #create a list from the users data in the txt
                        with open("bank_data.txt", "r") as f:
                            bdata = f.readlines()
                        ba_data = bdata[0] #first element in the bank data.(balance)
                        str_bankdata = str(ba_data) #
                        position_of_r = str_bankdata.find("R")
                        b_balance = str_bankdata[position_of_r + 1:]
                        #Bank balance.
                        the_bank_balance =float(b_balance)# current bank balance
                        #########################
                        if user_bal > my_amount:
                            
                            user_bal = user_bal - my_amount #cureent user balance
                            print(f'Deposit of R{my_amount} was successfully made.\n')
                            print(f'Current balance = R{user_bal}.')
                            
                            #Log the deposit in the transaction log file
                            with open("Transaction Log.txt", "a") as log_file:
                                log_file.write(f"{comb}: -R{my_amount}\n")
                            
                            #User update
                            #######################################
                            with open(file_name, "r") as file:
                                lines = file.readlines()

                            # Remove the first element (line) from the list
                            lines.pop(0)

                            # Write the modified content back to the text file
                            with open(file_name, "w") as file:
                                file.writelines(lines)
                            ######################################
                            #Bank Data update
                            with open('bank_data.txt', "r") as file:
                                bank_lines = file.readlines()

                                # Check if there are lines in the file

                            # Remove the first element (line) from the list
                            bank_lines.pop(0)

                            # Write the modified content back to the text file
                            with open("bank_data", "w") as file:
                                file.writelines(bank_lines)
                             #######################################
                            
                            #Append the new balanc tot the top of the transaction log
                            new_element = f"{current_datetime} balance : R{user_bal}\n"
                            new_bank_bal = f"{current_datetime} balance : R{the_bank_balance-my_amount}\n"
                             
                            # Read the content of the text file
                            with open(file_name, "r") as file:
                                lines = file.readlines()
                            with open("bank_data.txt","r")as file:
                                banking = file.readlines()

                            # Add the new element at the beginning
                            lines.insert(0, new_element)
                            banking.insert(0,new_bank_bal)
                            # Write the modified content back to the text file
                            with open(file_name, "w") as file:
                                file.writelines(lines)
                            with open("bank_data.txt", "w") as file:
                                file.writelines(banking)
                                
                            
                            #####################33
                             ######################################
                           
                            #######################3
                             #update bank data
                            bankdata_txt_withdrawal(name,current_datetime,my_amount)
                        
                        else:
                            print("Insuficient funds")
                            print("----------------------------------------------------------------------")
                   
                    else:
                        print("Invalid Selection")
                        print("----------------------------------------------------------------------")

                elif choice == '3':#Exit
                    print("Thank you for using our services!")
                    print("----------------------------------------------------------------------")
                    break
                    break
                else:
                    print("Invalid input!")
                    print("----------------------------------------------------------------------")
                    break
 
            else:
                print("Account does not exist, please register your account")
                print("----------------------------------------------------------------------")
                break