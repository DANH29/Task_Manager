# admin program that allows users to:
# login
# register new users (only for "Admin")
# assign tasks to users
# view all tasks
# view current users tasks
# generate 2 statistics file based on task_manager data
# view statistics in terminal (only for "Admin")

from datetime import date

# function for admin to register new users
# cannot register a username that is already in use
# username cannot be the same as password
# asks user to confirm password before registering
# new user log in details are written to "user.txt"

def reg_user():

    while True:
        new_username = input("\nEnter a new username: ")
        for user_index in range(len(list_of_users)):

            # if input username is in user.txt and its index is divisible by 2 tell user username is already in use
            if new_username in list_of_users and list_of_users[user_index] == new_username and user_index % 2 == 0:
                print("\nUsername already in use")
                break

        # else prompt for password
        # if input password is the same as input username tell user they can't be the same, prompt again
        else:
            new_password = input("Enter a password: ")
            if new_username == new_password:
                print("\nPassword cannot be the same as Username")

            # ask user to confirm password
            else:
                confirm_new_password = input("Confirm password: ")
                if new_password == confirm_new_password:
                    print("\nSuccessfully registered user" + "\n")

                    # write new registered user to user.txt
                    with open("user.txt", "r+") as updated_user_file:
                        updated_user_file.read()
                        updated_user_file.write("\n" + new_username + ", " + confirm_new_password)
                        break

                else:
                    print("\nPasswords don't match")

# function for users to add tasks
# user has option to enter "-1" at start to return to menu
# cannot assign a task number that has already been used
# checks if user is trying to assign task to a valid user
# writes new task to "tasks,txt"

def add_task():

    new_task = True

    # prompt user for whom new task should be assigned to or to go back to menu
    while new_task:
        assigned_user = input("\nEnter username for whom the task is assigned to or \"-1\" to return to menu: ")
        if assigned_user == "-1":
            print("")
            new_task = False
            break

        # if input username is not in user.txt print "invalid username"
        if assigned_user not in list_of_users:
            print("\nInvalid username entered")

        else:
            while new_task:

                # loop through each even index in user.txt
                for user_index in range(len(list_of_users[::2])):
                    # if user_index == input user prompt for new task number
                    if list_of_users[user_index] == assigned_user:
                        task_number = input("Enter number for task: ")
                        # if input task number already in tasks.txt
                        # with an index divisible by 7 prompt for another task number
                        if task_number in list_of_tasks and list_of_tasks.index(task_number) % 7 == 0:
                            print("\nTask number already exists\n")

                        # else enter rest of task info
                        else:
                            task_description = input("Enter a description of the task: ")
                            task_title = input("Enter title of task: ")
                            date_task_assigned = input("Enter task assignment date in format yyyy-mm-dd: ")
                            task_due_date = input("Enter task due date yyyy-mm-dd: ")

                            # write new task to tasks.txt
                            with open("tasks.txt", "r+") as updated_tasks_file:
                                updated_tasks_file.read()
                                updated_tasks_file.write(
                                    "\n" + assigned_user + ", " + task_title + ", " + task_description + ", "
                                    + task_due_date + ", " + date_task_assigned + ", No")

                                print("\nTask Successfully Assigned\n")
                                new_task = False

                # if input username in user.txt but index is not divisible by 2
                if list_of_users[user_index] == assigned_user and user_index % 2 != 0:
                    print("\nInvalid username entered")
                    break

# function for users to view all tasks in terminal
# skips blank lines in tasks.txt

def view_all():

    for task in tasks_txt_lines:
        if task.split(", ") == [""]:
            continue

        else:
            task = task.split(", ")
            print(f"""\nAssigned user: {task[0]}
Task Name: {task[1]}
Task Description: {task[2]}
Assignment Date: {task[3]}
Due Date: {task[4]}
Completed? {task[5]}\n""")

# function for users to view their own tasks
# will notify user if they have no tasks currently assigned
# once tasks have been displayed will ask if user wants to return to menu or edit a specific task
# user then has option of setting an incomplete task to complete
# or edit the assigned user or date of the task
# all changes are then written to tasks.txt
# checks throughout if inputs are valid or not

def view_mine():

    view = True

    # if current user username is not in list of tasks
    while view:
        if username not in list_of_tasks:
            print("\nNo tasks assigned\n")
            break

        else:
            # loop through each even index in user.txt
            for user_index in range(len(list_of_users[::2])):
                # if a string with an even index in user.txt == username
                if list_of_users[user_index] == username:
                    # loop through tasks.txt, skip blank lines
                    for task in tasks_txt_lines:
                        task = task.split(", ")
                        if task == [""]:
                            continue

                        # if username equals second element in task, print task
                        elif username == task[1]:
                            print(f"""\nTask number: {task[0]}
Assigned user: {task[1]}
Task Name: {task[2]}
Task Description: {task[3]}
Assignment Date: {task[4]}
Due Date: {task[5]}
Completed? {task[6]}\n""")

                    # prompt if user would like to edit one of their tasks or return to menu
                    while view:
                        task_number = input("If you would like to edit a task enter the task number."
                                            "\nOr enter -1 to return to menu.\nEnter here: ")

                        for task in tasks_txt_lines:
                            # return to menu
                            if task_number == "-1":
                                print("")
                                view = False
                                break

                            # task does not exist
                            if task_number not in list_of_tasks:
                                print("\nTask number does not exist\n")
                                break

                            # task not assigned to user
                            if task[0] == task_number and task.split(", ")[1] != username:
                                print("\nTask is not assigned to you\n")
                                break

                            # task already complete
                            if task[0] == task_number and task.split(", ")[6] == "Yes":
                                print("\nTask already complete\n")
                                break
                            # if index[0] of task == input task number continue
                            if task[0] == task_number:

                                view = True

                                while view:
                                    # split task into list
                                    current_task = task.split(", ")

                                    # prompt user if they would like to set task to complete or edit task
                                    complete_or_edit = input(
                                        "\nIf you would like to mark the task as complete enter \"complete\"."
                                        "\nIf you would like to edit the task enter \"edit\".\nEnter here: ")

                                    # user chooses to complete task
                                    if complete_or_edit.lower() == "complete":

                                        # empty string to store updated task information
                                        new_tasks_txt = ""

                                        # for each task if the first index does not equal task number
                                        # add task to new_tasks_txt
                                        # else replace current_task[6] with "Yes" then add to new_task_txt
                                        for task in tasks_txt_lines:
                                            if task[0] != task_number:
                                                new_tasks_txt = new_tasks_txt + task + "\n"

                                            else:
                                                task = task.replace(current_task[6], "Yes")
                                                new_tasks_txt = new_tasks_txt + task + "\n"

                                        # write updated tasks information to task.txt
                                        with open("tasks.txt", "w+") as updated_tasks_file:
                                            updated_tasks_file.write(new_tasks_txt.strip())

                                        print("\nTask set as complete\n")
                                        view = False
                                        break

                                    # if user chooses to edit task
                                    if complete_or_edit.lower() == "edit":

                                        while view:

                                            # prompt user if they would like to edit assigned user
                                            # or task due date
                                            user_or_date = input(
                                                "\nIf you would like to edit assigned user enter \"user\"."
                                                "\nIf you would like to edit due date enter \"date\".\nEnter here: ")

                                            # if user chooses to edit user
                                            if user_or_date.lower() == "user":

                                                # empty string to store updated task information
                                                new_tasks_txt = ""

                                                # for each task if the first index does not equal task number
                                                # add task to new_user_txt
                                                for task in tasks_txt_lines:
                                                    if task[0] != task_number:
                                                        new_tasks_txt = new_tasks_txt + task + "\n"

                                                    # else prompt user for new assigned user
                                                    # loop through user.txt to check if new assigned user is a valid username
                                                    # then change current_task[1] to new_assigned_user and add to new_

                                                    else:
                                                        new_user = True
                                                        while new_user:
                                                            new_assigned_user = input("\nEnter the new assigned user: ")
                                                            for user_index in range(len(list_of_users)):
                                                                if list_of_users[user_index] == new_assigned_user and user_index % 2 == 0:
                                                                    task = task.replace(current_task[1], new_assigned_user)
                                                                    new_tasks_txt = new_tasks_txt + task + "\n"

                                                                    new_user = False

                                                            # if loop hasn't been broken
                                                            if new_user:
                                                                print("\nUsername invalid")

                                                # write updated_tasks to tasks.txt
                                                with open("tasks.txt", "w+") as updated_tasks_file:
                                                    updated_tasks_file.write(new_tasks_txt.strip())

                                                print("\nTask assigned user updated\n")
                                                view = False
                                                break

                                            # if user selects to change task date
                                            if user_or_date.lower() == "date":

                                                # empty string to store new task information
                                                new_tasks_txt = ""

                                                # loop through tasks.txt
                                                # if task[0] does not equal user input task number
                                                # add task to new_tasks_txt
                                                for task in tasks_txt_lines:
                                                    if task[0] != task_number:
                                                        new_tasks_txt = new_tasks_txt + task + "\n"

                                                    # else prompt for new due date
                                                    # replace current_task[5] with new due date
                                                    # add to new_tasks_txt
                                                    else:
                                                        new_due_date = input("\nEnter the new due date: ")
                                                        task = task.replace(current_task[5], new_due_date)
                                                        new_tasks_txt = new_tasks_txt + task + "\n"

                                                # write new task information to tasks.txt
                                                with open("tasks.txt", "w+") as updated_tasks_file:
                                                    updated_tasks_file.write(new_tasks_txt.strip())

                                                print("\nTask due date updated\n")
                                                view = False
                                                break

                                            else:
                                                print("\nInvalid response entered")
                                    else:
                                        print("\nInvalid response entered")


# function to generate 2 reports based on task_manager stats
# creates 2 files called task_overview and user_overview

def gen_rep():

    with open("user_overview.txt", "w+") as user_overview:
        with open("task_overview.txt", "w+") as task_overview:

            # variable to store task totals
            total_tasks = 0
            complete_tasks = 0
            incomplete_tasks = 0
            overdue_tasks = 0

            for task in tasks_txt_lines:

                # for each task in tasks_txt + 1
                total_tasks += 1

                # if task set to complete + 1
                if task.split(", ")[6] == "Yes":
                    complete_tasks += 1

                # if task set to incomplete + 1
                if task.split(", ")[6] == "No":
                    incomplete_tasks += 1

                # if task set to incomplete and due date has passed + 1
                if task.split(", ")[6] == "No" and task.split(", ")[5] < str(date.today()):
                    overdue_tasks += 1

                # percentage variables of incomplete tasks and overdue tasks
                percent_incomplete_tasks = round((incomplete_tasks / total_tasks) * 100)
                percent_overdue_tasks = round((overdue_tasks / total_tasks) * 100)

            # if total tasks = 0 both percentage variables equal 0
            if total_tasks == 0:
                percent_incomplete_tasks = 0
                percent_overdue_tasks = 0

            # write task information to task_overview.txt
            task_overview.write(f"""Task overview report:
------------------------------------------------------------------------------------------------------------------------
Total number of tasks:                                                                              {total_tasks}
Total number of completed tasks:                                                                    {complete_tasks}
Total number of incomplete tasks:                                                                   {incomplete_tasks}
Total number of tasks that are overdue:                                                             {overdue_tasks}
Percentage of tasks incomplete:                                                                     {percent_incomplete_tasks}%
Percentage of tasks overdue:                                                                        {percent_overdue_tasks}%
------------------------------------------------------------------------------------------------------------------------""")

            # header for user_overview.txt
            total_user = len(user_txt_lines)

            user_overview.write(f"""User overview report:
            
Total number of registered user: {total_user}
Total number of tasks :          {total_tasks}
------------------------------------------------------------------------------------------------------------------------""")

            for user in user_txt_lines:

                # variables to store user totals
                user_tasks = 0
                user_complete_tasks = 0
                user_incomplete_tasks = 0
                user_overdue_tasks = 0

                # split user into list then take index[0] as a variable
                current_user = user.split(", ")[0]

                # if user in tasks.txt
                if current_user in list_of_tasks:
                    for task in tasks_txt_lines:
                        # split task into list
                        task = task.split(", ")

                        # if user in task and index is [1] + 1
                        if current_user in task and task.index(current_user) == 1:
                            user_tasks = user_tasks + 1

                        # if user in task and index is [1] and task set to complete + 1
                        if current_user in task and task.index(current_user) == 1 and task[6] == "Yes":
                            user_complete_tasks = user_complete_tasks + 1

                        # if user in task and index is [1] and task set to incomplete + 1
                        if current_user in task and task.index(current_user) == 1 and task[6] == "No":
                            user_incomplete_tasks = user_incomplete_tasks + 1

                        # if user in task and index is [1] and task set to incomplete and due date has passed + 1
                        if current_user in task and task.index(current_user) == 1 and task[6] == "No" and \
                                task[5] < str(date.today()):
                            user_overdue_tasks = user_overdue_tasks + 1

                    # percentage variables for each user
                    percent_user_tasks = (user_tasks / total_tasks) * 100
                    percent_user_complete_tasks = round((user_complete_tasks / user_tasks) * 100)
                    percent_user_incomplete_tasks = round((user_incomplete_tasks / user_tasks) * 100)
                    percent_user_overdue_tasks = round((user_overdue_tasks / user_tasks) * 100)

                # if user has no tasks assigned percentage variables are 0
                else:
                    percent_user_tasks = 0
                    percent_user_complete_tasks = 0
                    percent_user_incomplete_tasks = 0
                    percent_user_overdue_tasks = 0

                # write user information to user_overview.txt
                user_overview.write(f"""
{current_user}'s metrics:
    Total tasks assigned:                                                                           {user_tasks}
    Percentage of assigned tasks:                                                                   {percent_user_tasks}%
    Percentage of complete assigned tasks:                                                          {percent_user_complete_tasks}%
    Percentage of incomplete assigned tasks:                                                        {percent_user_incomplete_tasks}%
    Percentage of incomplete and overdue assigned tasks:                                            {percent_user_overdue_tasks}%
------------------------------------------------------------------------------------------------------------------------""")

    print("\nReports successfully generated\n")


# open user.txt and tasks.txt
user_file = open("user.txt", "r+")
tasks_file = open("tasks.txt", "r+")

# read user.txt
# split user.txt into each line
# split user.txt into each element
user_txt = user_file.read()
user_txt_lines = user_txt.split("\n")
list_of_users = user_txt.replace(",", "").split()

# read task.txt
# split task.txt into each line
# split task.txt into each element
tasks_txt = tasks_file.read()
tasks_txt_lines = tasks_txt.split("\n")
list_of_tasks = tasks_txt.replace("\n", ", ").split(", ")

# user log in process
# checks if username is in user_txt and if its index is divisible by 2
# once valid username is entered prompted for password
# if password incorrect ask user to re-enter
# once correct password is entered, user is logged in

login = True

# prompt for username
while login:
    username = input("Enter Username: ")

    # if username in user.txt with an even index prompt for password
    while login:
        if username in list_of_users[::2]:
            user_password = input("Enter Password: ")

            # loop through each index in user.txt
            # if user_password in user_txt
            # and its index - 1 == input username
            # and index is not divisible by 2
            # user logged in
            for password_index in range(len(list_of_users)):
                if list_of_users[password_index] == user_password\
                        and password_index - 1 == list_of_users.index(username) and password_index % 2 != 0:
                    print(f"\n{username} logged in!\n")
                    login = False
                    break

            else:
                print("Incorrect Password\n")

        else:
            print("No matching usernames found\n")
            username = input("Enter Username: ")

    # menu
    # if username is "admin" they get access to all sections
    # if not they only get access to certain sections

    while True:
        if username == "Admin":
            menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
s - Statistics
e - Exit
: ''').lower()
        else:
            menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
e - Exit
: ''').lower()

# all functions called for sections of menu
# statistics generates task_overview and user_overview files then prints them in terminal

        if menu == 'r' and username == "Admin":
            reg_user()

        elif menu == 'a':
            add_task()

        elif menu == 'va':
            view_all()

        elif menu == 'vm':
            view_mine()

        elif menu == "gr":
            gen_rep()

        elif menu == "s" and username == "Admin":

            # generates "user_overview.txt" and "task_overview.txt" and prints them in terminal

            gen_rep()

            with open("task_overview.txt", "r") as s_task_overview:
                s_task_overview = s_task_overview.read()
                print(s_task_overview)

                with open("user_overview.txt", "r") as s_user_overview:
                    s_user_overview = s_user_overview.read()
                    print(s_user_overview)
                    print("")

        # option to end program

        elif menu == 'e':
            print('\nGoodbye!!!')
            exit()

        # if invalid letter is entered

        else:
            print("\nYou have made a wrong choice.\nPlease try again.\n")

user_file.close()
tasks_file.close()
