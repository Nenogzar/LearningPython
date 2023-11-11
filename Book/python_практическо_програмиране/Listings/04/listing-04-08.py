level = 0       # Ниво на достъп

login = ""
while not login:
  login = input("Login: ")
  
password = ""
while not password:
  password = input("Password: ")

if login == "root" and password == "123":
    level = 10
elif login == "den" and password == "321":
    level = 5

if level:
    print("Hello, ", login)
    print("Your access level: ", level)
else:
    print("Access denied!")
