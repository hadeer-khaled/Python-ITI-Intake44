import authentication 
import pandas as pd

def print_users_info():
    users_info = pd.read_csv('./users_info.csv')
    print(users_info)
    
def switch(value):
    match value:
        case 1:
            return authentication.register()
        case 2:
            return authentication.login()
        case _:
            print("Invalid option")
