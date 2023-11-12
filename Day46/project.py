import datetime
import json


def load_project_data():
    try:
        with open('projects.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_project_data(data):
    with open('projects.json', 'w') as file:
        json.dump(data, file, indent=4)


def is_valid_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def create_project(user_email):
    print('\033[93m'+"Create Project Fundraising Campaign"+'\033[0m')
    title = input("Enter the project title: ")
    details = input("Enter project details: ")

    while True:
        total_target = input("Enter the total target amount (EGP): ")
        if total_target.isdigit():
            total_target = float(total_target)
            break
        else:
            print(
                '\033[91m'+"Invalid total_target. enter a number."+'\033[0m')

    while True:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        if is_valid_date(start_date):
            break
        else:
            print(
                '\033[91m'+"Invalid date format. Please use YYYY-MM-DD."+'\033[0m')

    while True:
        end_date = input("Enter end date (YYYY-MM-DD): ")
        if is_valid_date(end_date):
            break
        else:
            print(
                '\033[91m'+"Invalid date format. Please use YYYY-MM-DD."+'\033[0m')

    project = {
        'title': title,
        'details': details,
        'total_target': total_target,
        'start_date': start_date,
        'end_date': end_date,
        'owner_email': user_email
    }

    project_db = load_project_data()

    project_id = len(project_db) + 1
    project_db[project_id] = project

    save_project_data(project_db)

    print('\033[92m'+"Project created successfully."+'\033[0m')


def view_all_projects():
    print('\033[93m'+"All Projects: "+'\033[0m')
    project_db = load_project_data()
    for project_id, project in project_db.items():
        print(f"Project ID: {project_id}")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Total Target: {project['total_target']} EGP")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")
        print(f"Owner Email: {project['owner_email']}")
        print("==============================================")


def edit_project(user_email):
    project_db = load_project_data()
    print('\033[93m'+"available projects: "+'\033[0m')

    for project in project_db:
        print(
            '\033[94m'+f"Project ID: {project}, Title: {project_db[project]['title']}"+'\033[0m')

    project_id = input("Enter the project ID you want to edit: ")
    if project_id in project_db:
        project = project_db[project_id]
        if user_email == project['owner_email']:
            print("Current Project Details:")
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Total Target: {project['total_target']} EGP")
            print(f"Start Date: {project['start_date']}")
            print(f"End Date: {project['end_date']}")
            print("====================================")

            new_title = input(
                "Enter new project title (or leave empty to keep the same): ")
            new_details = input(
                "Enter new project details (or leave empty to keep the same): ")
            new_total_target = input(
                "Enter new total target amount (EGP) (or leave empty to keep the same): ")
            new_start_date = input(
                "Enter new start date (YYYY-MM-DD) (or leave empty to keep the same): ")
            new_end_date = input(
                "Enter new end date (YYYY-MM-DD) (or leave empty to keep the same): ")

            if new_title:
                project['title'] = new_title
            if new_details:
                project['details'] = new_details
            if new_total_target and new_total_target.isdigit():
                project['total_target'] = float(new_total_target)
            if new_start_date and is_valid_date(new_start_date):
                project['start_date'] = new_start_date
            if new_end_date and is_valid_date(new_end_date):
                project['end_date'] = new_end_date

            save_project_data(project_db)

            print('\033[92m'+"Project edited successfully."+'\033[0m')
        else:
            print('\033[91m'+"You can only edit your own projects."+'\033[0m')
    else:
        print('\033[91m'+"Project not found."+'\033[0m')


def delete_project(user_email):
    project_db = load_project_data()

    print('\033[93m'+"available projects: "+'\033[0m')

    for project in project_db:
        print(
            '\033[94m'+f"Project ID: {project}, Title: {project_db[project]['title']}"+'\033[0m')

    project_id = input("Enter the project ID you want to delete: ")
    if project_id in project_db:
        project = project_db[project_id]
        if user_email == project['owner_email']:
            del project_db[project_id]
            save_project_data(project_db)
            print('\033[92m'+"Project deleted successfully."+'\033[0m')
        else:
            print('\033[91m'+"You can only delete your own projects."+'\033[0m')
    else:
        print('\033[91m'+"Project not found."+'\033[0m')


def search_projects_by_date():
    project_db = load_project_data()
    search_date = input("Enter a date (YYYY-MM-DD) to search for projects: ")
    if is_valid_date(search_date):
        found_projects = []
        for project_id, project in project_db.items():
            if project['start_date'] == search_date:
                found_projects.append(project)
        if found_projects:
            print('\033[93m' +
                  "Projects found on {}:".format(search_date)+'\033[0m')
            for project in found_projects:
                print(f"Project ID: {project_id}")
                print(f"Title: {project['title']}")
                print(f"Details: {project['details']}")
                print(f"Total Target: {project['total_target']} EGP")
                print(f"Start Date: {project['start_date']}")
                print(f"End Date: {project['end_date']}")
                print(f"Owner Email: {project['owner_email']}")
                print("===========================================")
        else:
            print(
                '\033[91m'+"No projects found on {}.".format(search_date)+'\033[0m')
    else:
        print('\033[91m'+"Invalid date format. Please use YYYY-MM-DD."+'\033[0m')
