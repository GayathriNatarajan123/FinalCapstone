## User and Task Management
This _Python command-line program_ is designed to facilitate efficient user and task management through a command prompt interface. The program incorporates defensive programming techniques to ensure robustness and reliability.

Key features of the program include:
* __User Login:__ The program includes a login feature where users can authenticate themselves to access the main functionality.
* __Admin Facility:__ An admin facility is implemented to provide additional privileges. To access admin rights, users can use the username "admin" and the password "password".
* __Available Options:__ The program offers the following options for users to choose from:
    1. __User Registration:__ Users can register new accounts by providing the required information.
    2. __Task Assignment:__ Users can assign tasks to themselves or other users.
    3. __Viewing All Tasks:__ Users have the ability to view all tasks stored in the system.
    4. __Viewing Assigned Tasks__ Users can view tasks that are specifically assigned to them.
* __Report Generation:__ The program can generate reports to provide insights into task and user statistics, aiding in decision-making and performance evaluation.

By leveraging the command-line interface, this program aims to provide a streamlined and efficient means of managing users and their associated tasks.

## Installation Setup for Runing the File
To run the Python file, follow these installation steps:

* Install Visual Studio Code, a popular code editor, by visiting the official website: https://code.visualstudio.com/.
* Download the appropriate installer for your operating system (Windows, macOS, or Linux).
* Run the installer and follow the on-screen instructions to complete the installation.
* Launch Visual Studio Code after installation.
* Open the folder containing the Python file you want to run.
* Install the Python extension for Visual Studio Code. You can do this by navigating to the Extensions tab on the left sidebar, searching 
  for "Python," and clicking on the official Python extension by Microsoft.
* Click the "Install" button to install the Python extension.
* Once the extension is installed, you can open your Python file and execute it using Visual Studio Code.
* Make sure you have Python installed on your system before running the file. You can download Python from the official website: https://www.python.org/downloads/. Follow the installation instructions specific to your operating system.

Note: If you already have Python installed, ensure that the Python executable is added to the system's PATH environment variable for Visual Studio Code to recognize it.

## Application workflow 
When running this application, the following steps are encountered.

1. The program starts and displays a command-line interface.
2. Users are prompted to provide their login credentials.
3. If the user enters valid credentials, they gain access to the main functionality of the application.
4. The main menu is displayed, showing available options such as user registration, task assignment, task viewing, and report generation.
5. Users can choose the desired option by entering the corresponding number.
6. If the user selects user registration, they will be prompted to provide the necessary information to register a new user.
7. If the user selects task assignment, they will be guided through the process of assigning a task to a specific user.
8. If the user selects task viewing, they can view all tasks or tasks assigned to them, depending on the available options.
9. If the user chooses report generation, the program generates reports based on the available data, such as user statistics or task summaries.
10. After completing an action, the user is returned to the main menu and can choose another option or exit the program.
11. If the user enters invalid credentials or encounters an error, appropriate error messages are displayed.
12. The program continues running until the user decides to exit.

## Login Authentication process
The login workflow in this application typically follows the following steps:
* The user launches the application.
* The application prompts the user to enter their login credentials. Enter the username and password. Ensure that you type it accurately, then press the "Enter" button to proceed.
* The application will validate your credentials by comparing them to the stored user data.
* If the username and password combination is correct, the application displays login success message and you will be granted access to the application's main menu.
* In case of incorrect credentials, an error message appears, prompting to re-enter the correct username and password.
* Ensure to keep the login credentials secure and do not share them with unauthorized individuals.

![login](https://github.com/GayathriNatarajan123/FinalCapstone/assets/125039533/cc516f44-fc40-4ee4-86fc-318dafe3bea5)

Error message for the Wrong Login details:

![wrong_password](https://github.com/GayathriNatarajan123/FinalCapstone/assets/125039533/adb31348-8a83-4787-95ba-54b9232e38c4)

## User Registration
To add a new user to the application, follow these steps:
* Look for an option "r - Registering a user". Enter "r" in the command prompt.
* Enter the new user's username and password.
* Submit the form by pressing enter.
* The application verifies if a user with the same username already exists.
* If the username already exists, an error message is displayed, indicating that the username is already taken. Prompt the user to enter a different username.
* If the username is unique and does not exist already, the application successfully saves the new user details.
* Upon successful creation, the application notifies that the user has been added.
* The newly created user can now utilize the application by logging in with their username and password.

![registering_user](https://github.com/GayathriNatarajan123/FinalCapstone/assets/125039533/ff761132-4fef-4ad1-86b9-38abe46268e0)

## Task Assignment
To add a task for a user, please adhere the following steps:
* Check for the option "a - Adding a task" in the command prompt.
* Enter "a" to select the option for adding a task.
* Provide the task title, description, and the due date for the task.
* Once you have entered all the necessary details, the task will be saved, and you will receive a confirmation message stating "Task Saved successfully."

![add_task](https://github.com/GayathriNatarajan123/FinalCapstone/assets/125039533/2bb23c00-6b76-4187-aba4-32662a8ec812)

## Viewing all tasks
To view all the user's task, please follow for the following steps:
* Look for the option "va - View all task" in the command prompt.
* Enter "va" to select the option for viewing all tasks.
* Once selected, the system will display a list of all the tasks assigned to the user.

![viewing_task](https://github.com/GayathriNatarajan123/FinalCapstone/assets/125039533/8c7b8f82-d6aa-416d-82fb-37a70eb8953b)

## Viewing tasks assigned to the logged-in user
To view all the task of the logged-in user, please follow for the following steps:
* Look for the option "vm - View my task" in the command prompt.
* Enter "vm" to select the option for viewing tasks assigned to the logged-in user.
* Once selected, the system will display a list of all the tasks assigned specifically to the logged-in user.

![view_user_task](https://github.com/GayathriNatarajan123/FinalCapstone/assets/125039533/b518336b-819a-4e9c-a08b-8d930a0b6469)

## Generating Task and User Statistics Reports
To view the statistics reports of all the users and tasks, please follow these steps:
* Look for the option "gr - Generate report" in the command prompt.
* Enter "gr" to initiate the process of generating the reports.
* Once selected, the system will generate two reports: "task_overview.txt" and "user_overview.txt".
* These reports will provide detailed statistics and information about the tasks and users respectively.

![generate_report](https://github.com/GayathriNatarajan123/FinalCapstone/assets/125039533/c8263b0c-36be-46dc-ab75-479d2f1d3253)
* Report generated for task statistics:
![task_report](https://github.com/GayathriNatarajan123/FinalCapstone/assets/125039533/a4f580ab-6230-4a0f-af45-2962cb9c7136)
* Report generated for user statistics:
  ![user_report](https://github.com/GayathriNatarajan123/FinalCapstone/assets/125039533/07da4b48-c5a1-42ea-a286-b0713facfd65)

## View User and Task Statistics Reports in the Command prompt
To view the statistics reports of all the users and tasks directly in the command prompt, please follow these steps:
* Look for the option "ds - Display Statistics" in the command prompt.
* Enter "ds" to initiate the process of displaying the reports in the command prompt.
* Once selected, the system will generate and display the statistics reports of users and tasks directly in the command prompt.
  
![display_statistics](https://github.com/GayathriNatarajan123/FinalCapstone/assets/125039533/20ef445a-57f4-4918-9436-d05de17e08a1)

## Exit application
* While in the main menu or at any point within the application, if the user decides to log out, then there is an option "e - Exit"
* They can typically do so by entering "e" to exit the application. The application will start the process of terminating.
![exit](https://github.com/GayathriNatarajan123/FinalCapstone/assets/125039533/dd0e78ab-7097-444f-b433-8e47c092d099)

