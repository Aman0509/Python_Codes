import csv
import logging
import os

os.chdir(r"D:\\Python_Code_Detail\\Class_Exercises\\Assignment\\Banking_Assignment")
# Creating a Logger for tracking password related activities.
logger = logging.getLogger(__name__)

# setting log level
logger.setLevel(logging.INFO)

# defining file handler and setting formatter for password
file_handler = logging.FileHandler(r"DB_and_Logs\\Logs\\main.log")
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)


class Admin:

    def __init__(self, user):
        self.user = user
        logger.info(f"Inside Admin Environment and User {self.user} is in session")

    def emp_id(self):
        logger.info(f"New Emp ID Creation Request is raised by {self.user}")
        with open(r"DB_and_Logs\\DB\\emp_info.csv", "r") as csvfile1:
            csv_read = list(csv.reader(csvfile1))
        if csv_read == list():
            logger.info("Emp ID generated is 100001")
            return 100001
        else:
            present_ID = [int(csv_read[i][0]) for i in range(1,len(csv_read))]
            max_ID = max(present_ID)
            logger.info(f"Emp ID generated is {max_ID+1}")
            return max_ID+1

    def emp_creation(self):
        logger.info(f"New Employee record creation is in progress and it is created by {self.user} ")
        emp_info_ques = ["First Name - ",
                         "Last Name - ",
                         "Department - ",
                         "Manager - ",
                         "Contact Number - ",
                         "Compensation - ",
                         "Privilege - ",
                         "Emp Type(Regular or Contracter) - ",
                         "Is presently Working with us?(Y/N) - "
                         ]

        inp_data = list(map(input, emp_info_ques))
        inp_data.insert(0,self.emp_id())
        logger.info(f"Collected data from admin {self.user} is now saving into database")
        with open(r"DB_and_Logs\\DB\\emp_info.csv", "a+", newline="") as csvfile1:
            # fields= [
            # "Emp_ID","First Name", "Last Name","Department",
            # "Manager", "Contact Number", "Compensation",
            # "Privilege","Emp_Status","Working?"
            # ]
            cr = csv.writer(csvfile1)
            cr.writerow(inp_data)
        with open(r"DB_and_Logs\\Credentials\\pass_emp.csv", "a+", newline="") as f_p:
            cred = [f"{inp_data[0]}", "abcd1234"]
            csv.reader(f_p).writerow(cred)
        logger.info(f"All the data is saved in database successfully")
        logger.info(f"Employee ID created for {inp_data[1]} {inp_data[2]} by {self.user}")
        print(f"Employee ID of {inp_data[1]} {inp_data[2]} is {inp_data[0]}")
        inp = input("Do you want to create another Employee ID?\nPress Y for YES and Press any Key to return to Home ").upper()
        if inp == "Y":
            logger.info("Creating another Employee")
            self.emp_creation()
        else:
            return 1

    def emp_modification(self):
        logger.info("Employee data modification is requested.")
        print("-----------------------------------------------------------------------------------------------------")
        emp_id_to_modify = input("Enter the Emp_ID - ")
        logger.info(f"Employee for which data needs to be modified has ID {emp_id_to_modify}")
        logger.info("Checking in database..")
        with open(r"DB_and_Logs\\DB\\emp_info.csv", "r") as csvfile1:
            cr = list(csv.reader(csvfile1, delimiter=","))
            first_list = cr[0]
            # print(first_list[1:])
            try:
                for i in cr[1:]:
                    if i[0] == emp_id_to_modify:
                        logger.info(f"Employee Found with Emp ID {emp_id_to_modify}")
                        print()
                        print(f"{i[0]} belongs to {i[1]} {i[2]}")
                        print("Below is the full information")
                        for k,l in dict(zip(first_list, i)).items():
                            print(f"{k} - {l}")
                        print()
                        print("------------------------------------"
                              "-----------------------------------------------------------------")
                        try:
                            parameter = int(input(
                                "Press 1 to change First Name\n"
                                "Press 2 to change the Last Name\n"
                                "Press 3 to change the Department\n"
                                "Press 4 to change the Manager\n"
                                "Press 5 to change the contact number\n"
                                "Press 6 to change the Compensation\n"
                                "Press 7 to change the Privilege\n"
                                "Press 8 to change the Emp type\n"
                                "Press 9 to change the Working Status\n"
                                "Press 0 to go back to Main Menu\n"
                                "Enter your choice - "))
                            if parameter == 0:
                                return 1
                        except ValueError:
                            print("You have entered invalid input")
                            return 1
                        new_par = input(f"Enter {first_list[parameter]} - ")
                        del(i[parameter])
                        i.insert(parameter, new_par)
                        logger.info(f"{first_list[parameter]} has been changed for Emp ID {i[0]}")
                        print("Changes has been made!!")
                        with open(r"DB_and_Logs\\DB\\emp_info.csv","w", newline="") as csvfile2:
                            cr2 = csv.writer(csvfile2)
                            for j in cr:
                                cr2.writerow(j)
                        return 1
                else:
                    logger.info(f"{emp_id_to_modify} ID does not exist in database")
                    print(f"{emp_id_to_modify} ID does not exist.")
                    return 1
            except IndexError:
                logger.info("Wrong selection is made")
                print("You have entered the wrong choice")
                return 1

    def full_data(self):
        logger.info(f"{self.user} is requested to see full employee data")
        count = 0
        with open(r"DB_and_Logs\\DB\\emp_info.csv", "r") as csvfile:
            cr = list(csv.reader(csvfile, delimiter = ","))
            print("-------------------------------------------"
                  "--------------------------------------------"
                  "---------------------------------------------"
                  "------------------------------------------------------------------------")
            col_len = [len(x) for x in cr[0]]
            for line in cr[1:]:
                for d in range(len(line)):
                    if len(line[d])> col_len[d]:
                        col_len[d] = len(line[d])

            for line in cr:
                count = 0
                for b in line:
                    print(b.ljust(col_len[count]," "), end="\t")
                    count+=1
                print()
            print("------------------------------------"
                  "-------------------------------------"
                  "-------------------------------------"
                  "------------------------------------------"
                  "----------------------------------------------------")

        return 1

    def change_password(self):
        logger.info(f"User {self.user} is trying to change his/her password")
        with open(r"DB_and_Logs\\Credentials\\pass_admin.csv", "r") as f:
            f_r = list(csv.reader(f))
        with open(r"DB_and_Logs\\Credentials\\pass_admin.csv", "w", newline="") as f1:
            for list_ in f_r:
                if list_[0] == self.user:
                    while True:
                        old_pass = input("Enter your Current Password - ")
                        if old_pass == list_[1]:
                            new_pass = input("Enter your New Password - ")
                            list_[1] = new_pass
                            for p in f_r:
                                csv.writer(f1).writerow(p)
                            print("Your Password has been changed successfully")
                            logger.info(f"{self.user} has successfully changed his/her password")
                            break
                        else:
                            logger.info(f"Old Password entered by {self.user} does not match")
                            print("Password do not match. Please try again")
                    break
            return 1
