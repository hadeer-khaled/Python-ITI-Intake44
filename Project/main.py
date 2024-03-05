from helper_functions import switch
from user_services import create_users_info_csv 
import os

file_path = "users_info.csv"
user_info = []

if not os.path.exists(file_path):
    fields = ['first_name', 'last_name', 'email', 'password' , 'phone']
    create_users_info_csv( fields, file_path)


user_input = input("To register press 1.\nTo login press 2 \n")
if not user_input.isdigit():
    print("Invlaid Input")
else:
    switch(int(user_input))
