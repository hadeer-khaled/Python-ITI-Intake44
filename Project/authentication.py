import pandas as pd
from file_manipulation import create_users_info_csv ,  add_user_info

filename = "users_info.csv"
users_df = pd.read_csv(filename)

def register():
    first_name = input("first_name: ")
    last_name = input("last_name: ")
    email = input("email: ")
    password = input("password: ")
    repassword = input("password: ")
    while password != repassword:
        print("Password dosn't match")
        password = input("password: ")
        repassword = input("password: ")
    phone = input("phone: ")
    user_info = [first_name, last_name, email, password , phone]
    add_user_info( user_info,filename)

    print("Congratulations, You registered Successfully!")
    print("Now You can log in")
    login()

    return  0

def login():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")

    user_data = users_df.loc[users_df['email'] == email]

    if not user_data.empty:
        stored_password = str(user_data['password'].iloc[0]).strip()
        entered_password = password.strip()
        if stored_password == entered_password:
             print("Congratulations, You logged in Successfully!")
        else:
            print("Invalid password.")
    else:
        print("Email not found.")
