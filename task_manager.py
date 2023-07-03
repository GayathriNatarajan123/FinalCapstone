#  =================Task 17================
# Author: Gayathri Natarajan
# Updated Date: 11/06/2023
# Reference: ChatGPT, W3schools
# This is a Python program, the purpose of this program is to manage users and its tasks.
# Updated Loging features.
# Use the following username and password to access the admin rights 
# username: admin
# Registering User, Assigning tasks, Viewing all tasks and Viewing tasked based on logged user.
# Generating reports.
# Added defensive programing.
#  ======================================

#=====importing libraries===========
import os
from datetime import datetime, date
import tabulate as display

username_password = {}
duedate_message = "Due date of task (YYYY-MM-DD): "
admin = 'admin'
line = "-" * 185
width = 175 

user_report_filename = "user_overview.txt"
task_report_filename = "task_overview.txt"

#=====Adding functions for reusability and readability===========

def validate_datetimeformat(display_message):
    ''' Check if user enters valid date format. 

        Returns the valid date.    
    '''
    while True:
            try:
                value_to_evaluate = input(display_message)
                due_date_time = datetime.strptime(value_to_evaluate, DATETIME_STRING_FORMAT)
                return due_date_time

            except ValueError:
                print("Invalid datetime format. Please use the format specified")

def save_task_tofile():
    ''' Save the task to task.txt file.
    '''
    try:
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:                    
                    str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                    ]
                    task_list_to_write.append(";".join(str_attrs))
                        
            task_file.write("\n".join(task_list_to_write))
    except Exception as error_message:
        print(error_message)

def reg_user():       
        ''' Register new user. ie new user details are saved to the user.txt file.
        ''' 
        while(True):
            try:
                # - Request input of a new username
                new_username = input("New Username: ")

                # - Request input of a new password
                new_password = input("New Password: ")

                # - Request input of password confirmation.
                confirm_password = input("Confirm Password: ")

                is_user_exist = False
                for user in username_password.keys():
                    # - Check if the user name already exist.
                    if(user == new_username):
                        print("The user name already exist. Please enter another username")
                        is_user_exist = True
                        break
                if not(is_user_exist):
                    # - Check if the new password and confirmed password are the same.
                    if new_password == confirm_password:
                        # - If they are the same, add them to the user.txt file,                        
                        username_password[new_username] = new_password
                    # - Otherwise you present a relevant message.
                    else:
                        print("New Passwords and Current Password do no match")
                    
                    # - Saving the new user to the user text file
                    with open("user.txt", "w") as out_file:
                            user_data = []
                            for k in username_password:
                                user_data.append(f"{k};{username_password[k]}")
                            out_file.write("\n".join(user_data))
                            print("New user added")
                            break
            except Exception as error_message:
                print(error_message)

            
def add_task(task_username):    
        ''' Add new task for the user. New task will be added to tast.txt file.
        '''    
        try:
            task_title = input("Title of Task: ")
            task_description = input("Description of Task: ")
            due_date_time = validate_datetimeformat(duedate_message)
            
            # Then get the current date.
            curr_date = date.today()
            ''' Add the data to the file task.txt and
                Include 'No' to indicate if the task is complete.'''
            new_task = {
                "username": task_username,
                "title": task_title,
                "description": task_description,
                "due_date": due_date_time,
                "assigned_date": curr_date,
                "completed": False
            }

            task_list.append(new_task)
            
            save_task_tofile()
            print("Task successfully added.")
        except Exception as error_message:
            print(error_message)

def display_task(header, display_task):
        ''' Displaying the user's task in a grid format. 
        '''       
        print()
        print(display.tabulate(display_task, header, tablefmt="grid"))
        print()

def view_all():
    ''' View all the task generated for all the users.
    '''
    try:
        header = ["Task", "Assigned to", "Date Assigned", "Due Date", "Task Description"]
        lst_alltask = [
                        [t['title'], 
                        t['username'], 
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT), 
                        t['due_date'].strftime(DATETIME_STRING_FORMAT), 
                        t['description'] ]
                        for t in task_list 
                        ]
        display_task(header, lst_alltask)
    except Exception as error_message:
        print(error_message)
    

def view_mine():
    ''' View the tasks generated for the logged in user.
    '''
    try:        
        lst_mytask = []
        s_no = 0
        # - Get the list of all the task associated with the logined user.
        lst_mytask = [
                        [s_no:= s_no + 1, 
                        t['title'], 
                        t['username'], 
                        # - Changing the date to string type for display purpose.
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT), 
                        t['due_date'].strftime(DATETIME_STRING_FORMAT), 
                        t['description'], 
                        'Yes' if t['completed'] else 'No' ]
                        for t in task_list 
                        if t['username'] == curr_user
                    ]  
        
        # - If there is no task available for the logined user then returning the program flow to the main menu.
        if(len(lst_mytask) == 0):
            print("\nNo task assigned!!!\n")
            return
        
        # - Displaying the user's task in a grid format.
        header = ["S.No", "Task", "Assigned to", "Date Assigned", "Due Date", "Task Description", "Completed status"]
        display_task(header, lst_mytask)
        

        # - Provide edit options for the tasks
        is_exit = True
        is_completed = False
        lst_selectedtask = []
        while(is_exit):
            task_number = input('''If you want to edit any task? please enter one of the following options below: 
            Serial number of the task - edit the task
            -1 - Return to main menu: ''').lower()            
            
            # - Validate the value enterd, matches with the provided options.
            for task in lst_mytask:
                if str(task[0]) == task_number:
                    is_exit = False
                    lst_selectedtask = task
                    is_completed = False
                elif(task_number == '-1'):
                    return

            if(is_exit):
                print("\nPlease enter the task number from the above list only!!!\n")
            else:  
                # - Validate whether user is trying to edit completed task.          
                if(lst_selectedtask[6] == 'Yes'):
                    is_completed = True
                if(is_completed):
                    print("\nYou cannot edit completed task!!!\n")
                    is_exit = True

        # - Providing options for the user to edit the task
        print()
        while(True):
            edit_option = input('''Select one of the following Options below:
            c - Mark the task as complete
            e - Edit the task 
            : ''').lower()
            if(edit_option == 'c'):
                # - Marking the task as completed
                while(True):
                    status = input("\nPlease enter Yes/No to mark the completion status: ").lower()
                    if(status == 'yes' or status =='no'):
                        lst_selectedtask[6] = 'Yes' if status == 'yes' else 'No'
                        break
                    else:
                        print("\nPlease enter only yes or no to update the status!!!")
                
                break
            elif(edit_option == 'e'):
                # - Providing options to edit username and due date.
                while(True):
                    task_username = input("Enter Name of person assigned to the task: ")
                    if task_username not in username_password.keys():
                        print("\nThe Person entered does not exist!!!\n")
                        continue
                    
                    due_date_time = validate_datetimeformat(duedate_message)
                    lst_selectedtask[2] = task_username
                    lst_selectedtask[4] = due_date_time
                    break
                break
            else:
                print("\nPlease enter only from the options provided!!!\n")
        
        lst_mytask[int(lst_selectedtask[0])-1] = lst_selectedtask   
       
        # - Removing the task associated with the current user.
        new_task_list = [item for item in task_list if item['username'] != curr_user]
        task_list.clear()  
        task_list.extend(new_task_list)

        # - Updating the changes to the task_list variable.
        for t in lst_mytask: 
            curr_t = {}
             
            curr_t['username'] =  t[2]
            curr_t['title'] = t[1]
            curr_t['description'] = t[5]
            # - Here due date is already in date time format but saved as tuple in the dict so add this condition.
            curr_t['due_date'] = datetime.strptime(t[4], DATETIME_STRING_FORMAT) if not isinstance(t[4], datetime) else t[4]
            # - Assigned date is in string format.So converting to datetime format.
            curr_t['assigned_date'] = datetime.strptime(t[3], DATETIME_STRING_FORMAT)
            curr_t['completed'] = True if t[6] == "Yes" else False                   
                    
            task_list.append(curr_t)  
        
        # - Saving the data to task.txt file
        save_task_tofile()
        
        print("Task successfully edited.")
    
    except Exception as error_message:
        print(error_message)


def available_menu():
    ''' Restrict menu options based on logged in user.
    '''
    if(curr_user == admin):
        options = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate Reports
ds - Display statistics
e - Exit
: ''').lower()
        return options
    else:
        options = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
        return options

def generate_header(options, filename, total_no_of_user = 0, total_no_of_task = 0):
    '''Generate header for reports.
    '''
    with open(filename, "w") as file:
        file.write("\n\n")
        file.write(line)
        file.write("\n")
        if(options == "user"):
            text = "User Statistics Report"
        elif(options == "task"):
            text = "Task Statistics Report"
                
        file.write(text.center(width))
        file.write("\n")
        file.write(line)

        if(options == "user"):
            file.write("\n")
            file.write("\n" + " " * 50)
            file.write(f"Total number of Users Registered with Task_Manager: \t\t{total_no_of_user}\n")
            file.write("\n" + " " * 50)
            file.write(f"Total number of task generated using Task Manager:  \t\t{total_no_of_task}\n")
                

def generate_footer(options):
    ''' Generate footer for reports.
    '''
    if(options == "user"):
        with open(user_report_filename, "a") as file: 
                    text = "**End**"               
                    file.write("\n\n\n")                
                    file.write(text.center(width))
                    file.write("\n")
                    file.write(line)
        print("Report Generated in user_overview text file.")
    elif(options == "task"):
        with open(task_report_filename, "a") as file: 
            text = "**End**"               
            file.write("\n\n\n")                
            file.write(text.center(width))
            file.write("\n")
            file.write(line)
        print("Report Generated in task_overview text file.")
    else:
        text = "**End**"               
        print("\n\n\n")                
        print(text.center(width))
        print("\n")
        print(line)



def calculate_user_overview(option_type):
    ''' Calculate and generate report in the user_overview text file.
    '''
    try:
        total_no_of_user = len(username_password)
        total_no_of_task = len(task_list)
        # - Generate header for the report file.
        if(option_type == "gr"):
            generate_header("user", user_report_filename, total_no_of_user, total_no_of_task)

        # - Calculate user details.  
        for user in username_password.keys():
            num = 0
            for t in task_list:
                if t['username'] == user:
                    num += 1
            user_tasks = num
            user_completed_task = 0
            user_incompleted_task = 0
            user_overdue_task = 0
                    
            if(user_tasks != 0):
                # Write the table to a text file
                if(option_type == "gr"):
                    with open(user_report_filename, "a") as file:
                        file.write(f"\n\nUsername: {user}\n") 
                elif(option_type == "ds"):
                    print(f"\n\nUserName: {user}\n")                           
                    
                user_overview = []
                for task in task_list:
                    if(task['username'] == user):
                        
                        if(task['completed']):
                            user_completed_task += 1
                        if(not(task['completed'])):
                            user_incompleted_task += 1
                        if((not(task['completed'])) and task['due_date'] < datetime.today()):
                            user_overdue_task += 1
                perct_user_tasks = 0 if user_tasks == 0 else (user_tasks / total_no_of_task) * 100
                perct_user_completed_task = 0 if user_completed_task == 0 else (user_completed_task / user_tasks) * 100
                perct_user_incompleted_task = 0 if user_incompleted_task == 0 else (user_incompleted_task / user_tasks) * 100
                perct_user_overdue_task = 0 if user_overdue_task == 0 else (user_overdue_task / user_tasks) * 100
                user_overview = [
                                    ["Total no of Tasks Assigned",
                                    "Percentage of Total no of Tasks Assigned",
                                    "Percentage of Completed Tasks",
                                    "Percentage of Incompleted Tasks",
                                    "Percentage of Overdue Tasks"],
                                    [user_tasks,
                                    round(perct_user_tasks), 
                                    round(perct_user_completed_task), 
                                    round(perct_user_incompleted_task),
                                    round(perct_user_overdue_task)]
                                ]
                                            

                table_user_task = display.tabulate(user_overview, headers="firstrow", tablefmt="grid")                    

                if(option_type == "gr"):
                    # Write the table to a text file
                    with open(user_report_filename, "a") as file:
                        file.write(table_user_task)
                elif(option_type == "ds"):
                    print(display.tabulate(user_overview, headers="firstrow", tablefmt="grid"))
                    
                        
        if(option_type == "gr"):
            generate_footer("user")

    except Exception as error_message:
        print(error_message)
  

def calculate_task_overview(option_type):
    ''' Calcualte and generate report for task in the task_overview text file.
    '''
    try:
        if(option_type == "gr"):
            generate_header("task", task_report_filename)
        completed_task = 0
        incompleted_task = 0
        overdue_task = 0
        
        for task in task_list:
            if(task['completed']):
                completed_task += 1
            if(not(task['completed'])):
                incompleted_task += 1
            if((not(task['completed'])) and task['due_date'] < datetime.today()):
                overdue_task += 1
        total_no_of_task = len(task_list)
        percentage_of_incompleted_task = 0 if incompleted_task == 0 else (incompleted_task / total_no_of_task)*100
        percentage_of_overdue_task = 0 if overdue_task == 0 else (overdue_task / total_no_of_task)*100
    
        overview = [
                    ["Total number of Tasks Generated", 
                    "Total Completed Tasks", 
                    "Total Incompleted Tasks",
                    "Total Overdue Tasks",
                    "Percentage of Incompleted Tasks",
                    "Percentage of Overdue Tasks"],
                    [str(total_no_of_task), 
                    str(completed_task), 
                    str(incompleted_task), 
                    str(overdue_task), 
                    str(round(percentage_of_incompleted_task)), 
                    str(round(percentage_of_overdue_task))]
                    ]

        table = display.tabulate(overview, headers="firstrow", tablefmt="grid")

        if(option_type == "gr"):
            # Write the table to a text file
            with open(task_report_filename, "a") as file:
                file.write("\n\n")
                file.write(table)
            print("Report Generated in task_overview text file.")  
        elif(option_type == "ds"):
            print(display.tabulate(overview, headers="firstrow", tablefmt="grid"))
              

    except Exception as error_message:
        print(error_message)
        

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write(f"{admin};password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary

for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

if(curr_user == admin):
    # Create task_overview.txt if it doesn't exist
        if not os.path.exists(task_report_filename):
            with open(task_report_filename, "w") as default_file:
                pass
        # Create user_overview.txt if it doesn't exist
        if not os.path.exists(user_report_filename):
            with open(user_report_filename, "w") as default_file:
                pass

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = available_menu()

    if menu == 'r':
        '''Add a new user to the user.txt file'''
        reg_user()
    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        add_task(task_username)
    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''
        view_all() 
    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        view_mine()
    elif menu == 'gr' and curr_user == admin:
        calculate_task_overview("gr")
        calculate_user_overview("gr")
    
    elif menu == 'ds' and curr_user == admin: 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list) 

        print("\n",line)
        print("{:80}Statistics Report".format(""))
        print(line)

        #print("-----------------------------------")
        print("\n{:80}".format(""), end="")
        print(f"Number of users: \t\t {num_users}")
        print("{:80}".format(""), end="")
        print(f"Number of tasks: \t\t {num_tasks}\n")
        #print("-----------------------------------")   
        calculate_task_overview("ds")
        calculate_user_overview("ds") 
        
        generate_footer("")
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
