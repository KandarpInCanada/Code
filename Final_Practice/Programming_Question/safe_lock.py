import getpass
password = getpass.getpass("enter the password --> ")
if password == str(4198):
    print("Access Granted")
else:
    print("Access Denied")