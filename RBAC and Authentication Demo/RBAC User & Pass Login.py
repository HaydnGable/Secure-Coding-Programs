roles = {
"Dave":"Admin",
"Sarah":"User"
}
credentials = {
"Dave":"1234",
"Sarah":"4321"
}

name = input("Enter your name: ")

def check_login():
    if credentials.get(name) == password:
        check_role()
    else:
        print("Password is incorrect.")
        
def check_role():
    if roles.get(name) == "Admin":
        print("Welcome Admin!")
    else:
        print("Welcome User!")
    
if name in roles:
    password = input("Enter your password: ")
    check_login()
else:
    print("User not found.")
