import user
import project


while True:
    print('\033[95m'+"\nMenu:"+'\033[0m')
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Select an option: ")

    if choice == '1':
        user.register_user()
    elif choice == '2':
        user_email = user.login_user()
        if user_email:
            while True:
                print('\033[95m'+"\nProject Management Menu:"+'\033[0m')
                print("1. Create Project")
                print("2. View All Projects")
                print("3. Edit Project (Owner only)")
                print("4. Delete Project (Owner only)")
                print("5. Search Projects by Date")
                print("6. Logout")
                project_choice = input("Select a project management option: ")

                if project_choice == '1':
                    project.create_project(user_email)
                elif project_choice == '2':
                    project.view_all_projects()
                elif project_choice == '3':
                    project.edit_project(user_email)
                elif project_choice == '4':
                    project.delete_project(user_email)
                elif project_choice == '5':
                    project.search_projects_by_date()
                elif project_choice == '6':
                    print('\033[93m'+"Logged out."+'\033[0m')
                    break
                else:
                    print(
                        '\033[91m'+"Invalid choice. Please select a valid option."+'\033[0m')
    elif choice == '3':
        print('\033[93m'+"Goodbye!"+'\033[0m')
        break
    else:
        print('\033[91m'+"Invalid choice. Please select a valid option."+'\033[0m')
