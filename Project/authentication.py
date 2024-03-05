import pandas as pd
from user_services import  add_user_info ,phone_number_validator
from projects import project_manipulation

filename = "users_info.csv"
users_df = pd.read_csv(filename)

def register():
    first_name = input("first_name: ")
    last_name = input("last_name: ")
    email = input("email: ")
    password = input("password: ")
    repassword = input("password: ")
    while password != repassword:
        print("Password doesn't match")
        password = input("password: ")
        repassword = input("Re-type your password: ")
    phone = input("phone: ")
    while not phone_number_validator(phone):
        print("Invalid Phone numer. Please try again")
        phone = input("phone: ")
        
    user_info = [first_name, last_name, email, password , phone]
    add_user_info( user_info,filename)

    print("Congratulations, You registered Successfully!")
    print("Now You can log in")
    login()

def login():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")

    user_data = users_df.loc[users_df['email'] == email]

    if not user_data.empty:
        stored_password = str(user_data['password'].iloc[0]).strip()
        entered_password = password.strip()
        if stored_password == entered_password:
             print("Congratulations, You logged in Successfully!")
             project_manipulation(email)
        else:
            print("Invalid password.")
    else:
        print("Email not found.")
