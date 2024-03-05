import csv
import pandas as pd
import json
import re


def create_users_info_csv(fields , filename ):  
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

def add_user_info(user_info , filename ): 
    with open(filename, mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(user_info)

def phone_number_validator(phone_number):
    egyption_phone_pattern = re.compile(r'^\+20(10|11|12|15)[0-9]{8}$')
    return bool(egyption_phone_pattern.match(phone_number))
