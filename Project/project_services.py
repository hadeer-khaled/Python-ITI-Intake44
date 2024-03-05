import csv
import pandas as pd
import json
from datetime import datetime


        
def create_projects_json_file(filename):
    json_data = json.dumps({"users_projecs": {}})
    with open(filename, 'w') as json_file:
        json_file.write(json_data)

def add_user_project(filename , user_email , new_project):
    projects_data = get_projects(filename)
    if user_email in projects_data["users_projecs"]:
        projects_data["users_projecs"][user_email].append(new_project)
    else:
        projects_data["users_projecs"][user_email] = [new_project]

    with open(filename, 'w') as json_file:
        json.dump(projects_data, json_file)

    print("Updated JSON file: projects_data.json")


def view_projects(filename,user_email):
    all_projects_data = get_projects(filename)
    user_projects =all_projects_data["users_projecs"][user_email]
    for project in user_projects:
        print(project,"\n")

def edit_project(filename,user_email):
    project_title = input("Enter project name you want to edit")
    requested_project , all_projects_data =get_project_by_email_and_title(filename,user_email, project_title)

    print("1 -> title \n2 -> details \n3 -> total_target \n4 -> start_date \n5 -> end_date")
    selected_choise = int(input("what you want to edit ?"))
    if (selected_choise == 1):
        new_title = input("Enter new title: ")
        requested_project["title"] = new_title
    elif (selected_choise == 2):
        new_details = input("Enter new details: ")
        requested_project["details"] = new_details
    elif (selected_choise == 3):
        new_total_target = input("Enter new total_target: ")
        requested_project["total_target"] = new_total_target
    elif (selected_choise == 4):
        new_start_date = input("Enter new start_date: ")
        requested_project["start_date"] = new_start_date
    elif (selected_choise == 5):
        new_end_date = input("Enter new end_date: ")
        requested_project["end_date"] = new_end_date
    else:
        print("Invalid Option")
    with open(filename, "w") as file:
        json.dump(all_projects_data, file, )

    

def delete_project(filename , user_email ):
    project_title = input("Enter project name you want to delete")
    all_projects_data  = get_projects(filename)
    user_projects =all_projects_data["users_projecs"][user_email]
    for project in user_projects:
        if project["title"] == project_title:
            user_projects.remove(project)
            
    with open(filename, "w") as file:
        json.dump(all_projects_data, file, )

def get_projects(filename):
        with open(filename, 'r') as json_file:
            return json.load(json_file)
        
def get_project_by_email_and_title(filename , email, title):
    all_projects_data = get_projects(filename)
    user_projects =all_projects_data["users_projecs"][email]
    for project in user_projects:
        if project["title"] == title:
             matching_project = project

    return matching_project , all_projects_data
    

def date_validator(date_str, format_str="%d-%m-%Y"):
    try:
        datetime.strptime(date_str, format_str)
        return True
    except ValueError:
        return False
