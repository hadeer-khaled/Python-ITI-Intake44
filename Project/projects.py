import json
import os
from project_services import create_projects_json_file , add_user_project , view_projects ,  edit_project , delete_project ,date_validator


projects_file_path = 'projects.json'
if not os.path.exists(projects_file_path):
    create_projects_json_file(projects_file_path)


def project_manipulation(user_email):
  print("Select one option: ")
  print("1 -> Create a project \n2 -> View my projects \n3 -> Edit project \n4 -> Delete a project")
  selected_option = input("Enter your choice: ")

  if (int(selected_option) == 1):
    print("Enter project information: ")

    new_project ={
        "title": input("Project Title: "),
        "details": input("Project Details: "),
        "total_target": input("Project total target: ")
    }
    start_date =  input("Project start date: ")
    while not date_validator(start_date):
          print("Invalid date format. Please try agein")
          start_date =  input("Project start date: ")
          

    end_date =  input("Project end date: ")
    while not date_validator(end_date):
        print("Invalid date format. Please try agein")
        end_date =  input("Project end date: ")
        
    new_project["start_date"] =start_date
    new_project["end_date"] =end_date

    add_user_project(projects_file_path , user_email , new_project)
    
  elif (int(selected_option) == 2):
      view_projects(projects_file_path, user_email)
  elif (int(selected_option) == 3):
      edit_project(projects_file_path, user_email)
  elif (int(selected_option) == 4):
       delete_project(projects_file_path , user_email )
  else:
      print("Invalid Option")
