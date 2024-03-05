import csv
import pandas as pd
def create_users_info_csv(fields , filename ):  
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

def add_user_info(user_info , filename ): 
    with open(filename, mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(user_info)


print("User added successfully.")

