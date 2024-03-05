import json
import os
from file_manipulation import create_projects_json , add_user_project


projects_file_path = 'projects.json'
if not os.path.exists(projects_file_path):
    create_projects_json(projects_file_path)

user_email = "rahma@gmail.com"
new_project = {
        "title": "Project 2",
        "details": "Nikhil",
        "total_target": "nikhil@geeksforgeeks.org",
        "start_date": "Full Time",
        "end_date": "Full Time"
      }

add_user_project(projects_file_path , user_email , new_project)
