import csv
import pandas as pd
import json

def create_users_info_csv(fields , filename ):  
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

def add_user_info(user_info , filename ): 
    with open(filename, mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(user_info)

def create_projects_json(filename):
    json_data = json.dumps({"users_projecs": {}})
    with open(filename, 'w') as json_file:
        json_file.write(json_data)

def add_user_project(filename , user_email , new_project):
    with open(filename, 'r') as json_file:
        projects_data = json.load(json_file)

    if user_email in projects_data["users_projecs"]:
        projects_data["users_projecs"][user_email].append(new_project)
    else:
        projects_data["users_projecs"][user_email] = [new_project]

    with open(filename, 'w') as json_file:
        json.dump(projects_data, json_file)

    print("Updated JSON file: projects_data.json")


