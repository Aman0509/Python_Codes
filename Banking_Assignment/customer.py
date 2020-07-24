import csv
import os
import logging
import datetime as dt

os.chdir(r"D:\\Python_Code_Detail\\Class_Exercises\\Assignment\\Banking_Assignment")


def see_profile(user):
    with open(r"DB_and_Logs\\DB\\cust_info.csv", "r") as f1:
        f1_read = list(csv.reader(f1))
        index = int(int(user)%1000)

        print("\n-------------------------------------------"
              "--------------------------------------------"
              "---------------------------------------------"
              "------------------------------------------------------------------------------------")
        col_adjustment = [max(len(f1_read[0][i]), len(f1_read[index][i])) for i in range(len(f1_read[0]) -2)]
        for i in range(len(f1_read[0])-2):
            print(f1_read[0][i].ljust(col_adjustment[i]," "), end="\t\t")
        print()
        for j in range(len(f1_read[0])-2):
            print(f1_read[index][j].ljust(col_adjustment[j]), end="\t\t")

        print("\n-------------------------------------------"
              "--------------------------------------------"
              "---------------------------------------------"
              "------------------------------------------------------------------------------------\n")
    return 1


def edit_profile(user):
    index = int(int(user) % 1000)
    print("Below is your Profile")
    see_profile(user)
    with open(r"DB_and_Logs\\DB\\cust_info.csv", "r") as f2_r:
        f2_read = list(csv.reader(f2_r))
    try:
        parameter = int(input(
                            "You can change below things\n\n"
                            "Press 1 to change Relationship status (Single/Married)\n"
                            "Press 2 to change Address\n"
                            "Press 3 to change Contact number\n"
                            "Press 4 to change Email ID\n"
                            "Press 0 to go back to the Main Menu\n"
                            "Enter your Choice - "))

        if parameter == 0:
            return 1
        for i in f2_read[index]:
            if parameter == 1:
                f2_read[index][6] = input("Enter Relationship Status - ")
                print("Changes have been made.")
                break
            elif parameter == 2:
                f2_read[index][8] = input("Enter your New Address - ")
                print("Changes have been made.")
                break
            elif parameter == 3:
                f2_read[index][9] = input("Enter your New Contact number - ")
                print("Changes have been made.")
                break
            elif parameter == 4:
                f2_read[index][10] = input("Enter your New Email ID - ")
                print("Changes have been made.")
                break
            else:
                print("You've entered wrong choice")
                break

        with open(r"DB_and_Logs\\DB\\cust_info.csv", "w", newline="") as f2_w:
            f2_write = csv.writer(f2_w)
            for i in f2_read:
                f2_write.writerow(i)
        return 1

    except ValueError:
        print("Invalid choice")
        return 1


def available_bal(user):
    with open(f"DB_and_Logs\\DB\\Transaction_DB\\{user}.csv", "r") as cr:
        cr_r = list(csv.reader(cr))
        l_cr = len(cr_r)
        return float(cr_r[l_cr-1][4])


def balance(user):
    try:
        inp_ch = int(input("Press 1 to see the available balance\nPress 2 to see the statement\nEnter your choice - "))
        if inp_ch == 1:
            print(f"Available Balance is {available_bal(user)}")
            return 1
        elif inp_ch == 2:
            with open(f"DB_and_Logs\\DB\\Transaction_DB\\{user}.csv", "r") as cr_r:
                cr_rl = list(csv.reader(cr_r))
                l_len = [len(m) for m in cr_rl[4]]
                for j in cr_rl[5:]:
                    for i in range(len(j)):
                        if len(j[i]) > l_len[i]:
                            l_len[i] = len(j[i])
                print("Statement".center(80, " "))
                print("-------------------------------------------------------------------------------------------"
                      "------------")
                for count in cr_rl[4:]:
                    y = 0
                    print("|", end=" ")
                    for g in count:
                        print(g.ljust(l_len[y]+2, " "), end="| ")
                        y += 1
                    print()
                print("-------------------------------------------------------------------------------------------"
                      "------------")
            return 1
        else:
            print("You have entered wrong choice")
            return 1
    except ValueError:
        print("Invalid Choice")


def register_beneficiary(user):
    print("Please provide below details\n")
    inp_data_ben = list(map(input, ["Enter Full Name - ", "Account No - ", "Max Limit - ", "Contact - "]))
    with open(r"DB_and_Logs\\DB\\cust_info.csv", "r") as ci:
        ci_r = list(csv.reader(ci))
        acc_details = [l[1] for l in ci_r[1:]]
    try:
        if acc_details.index(inp_data_ben[1]):
            with open(f"DB_and_Logs\\DB\\Beneficiary\\{user}_Beneficiary_List.csv", "a+", newline="") as cr_b:
                cr_b_w = csv.writer(cr_b)
                cr_b_w.writerow(inp_data_ben)
                print("Beneficiary successfully added")
                return 1
        else:
            print(f"{inp_data_ben[1]} does not exist.")
            return 1
    except ValueError:
        print("Invalid Account type")
        return 1


def see_beneficiary(user):
    with open(f"DB_and_Logs\\DB\\Beneficiary\\{user}_Beneficiary_List.csv", "r") as sb:
        sb_r = list(csv.reader(sb))
        print("-------------------------------------------------------------------------")
        col_len = [len(x) for x in sb_r[0]]
        for line in sb_r[1:]:
            for d in range(len(line)):
                if len(line[d]) > col_len[d]:
                    col_len[d] = len(line[d])

        for line in sb_r:
            count = 0
            for b in line:
                print(b.ljust(col_len[count], " "), end="\t")
                count += 1
            print()
        print("-------------------------------------------------------------------------")

    return 1


def transfer_money_online(user):
    print("List of Beneficiary")
    see_beneficiary(user)
    try:
        v = int(input("\nEnter the serial number adjacent to Beneficiary - "))
        with open(f"DB_and_Logs\\DB\\Beneficiary\\{user}_Beneficiary_List.csv", "r") as cr_b:
            cr_br = list(csv.reader(cr_b))
            with open(r"DB_and_Logs\\DB\\cust_info.csv", "r") as cr_ct:
                cr_ct_r = list(csv.reader(cr_ct))
                for u in cr_ct_r[1:]:
                    if u[1] == cr_br[v][1]:
                        receiving_user_id = u[0]
                money_trans = float(input("Enter the Amount to be transferred - "))
                with open(f"DB_and_Logs\\DB\\Transaction_DB\\{user}.csv", "r+") as cr_be1:
                    cr_be1_r = list(csv.reader(cr_be1))
                    check_balance = cr_be1_r[-1][4]
                    if float(check_balance) - money_trans < 0:
                        print("You don't have enough amount to make this transaction")
                        return 1
                    cr_be1_w = csv.writer(cr_be1)
                    txn_id = transaction_id(user, "online_txn")
                    cr_be1_w.writerow([dt.datetime.today().ctime(), txn_id, "-", money_trans, available_bal(user) - money_trans])
                    print(f"Rs {money_trans} has been transferred to {cr_br[v][0]}")
                    print("Your Current Balance is ", available_bal(user) - money_trans)
                    with open(f"DB_and_Logs\\DB\\Transaction_DB\\{receiving_user_id}.csv", "a+", newline="") as cr_ru:
                        cr_ru_w = csv.writer(cr_ru)
                        cr_ru_w.writerow([dt.datetime.today().ctime(), txn_id, money_trans, "-", available_bal(receiving_user_id) + money_trans])
        return 1
    except ValueError:
        print("Invalid Choice")
    except IndexError:
        print("You don't have any registered beneficiary for choice %d"%v)


def change_password(user):
    with open(r"DB_and_Logs\\Credentials\\pass_emp.csv", "r") as f:
        f_r = list(csv.reader(f))
    with open(r"DB_and_Logs\\Credentials\\pass_emp.csv", "w", newline="") as f1:
        for list_ in f_r:
            if list_[0] == user:
                while True:
                    old_pass = input("Enter your Current Password - ")
                    if old_pass == list_[1]:
                        new_pass = input("Enter your New Password - ")
                        list_[1] = new_pass
                        for p in f_r:
                            csv.writer(f1).writerow(p)
                        print("Your Password has been changed successfully")
                        break
                    else:
                        print("Password do not match. Please try again")
                break
        return 1


def transaction_id(user, txn_type):
    with open(f"DB_and_Logs\\DB\\Transaction_DB\\{user}.csv", "r") as cr:
        cr_read = list(csv.reader(cr))
        if len(cr_read) == 6:
            return f"{user}_{txn_type}_10000000001"
        else:
            len_txn = len(cr_read)
            l_t_id = cr_read[len_txn-1][1].split("_")
            return f"{user}_{txn_type}_{str(int(l_t_id[3])+1)}"


