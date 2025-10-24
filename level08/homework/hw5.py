#5) მომხმარებელს შემოატანინე:
#--> მომხმარებლის სახელი (username)
#--> პაროლი (password)
#შეამოწმე:
#თუ მომხმარებელი არის "admin" და პაროლი არის 'superSecretPassword' → "მოგესალმები, ადმინ!"
#თუ მომხმარებელი "guest" და პაროლი არის "1234" → "მოგესალმები, სტუმარო!"
#სხვა შემთხვევაში → "მომხმარებელი არ მოიძებნა!"

name=(input("enter your username : "))
password=(input("enter your password : "))
if name == "admin" and password == "adminertiorisami" : 
    print("მოგესალმები ადმინ")
elif name == "guest" and password == "1234" : 
    print("მოგესალმები სტუმარო")
else :
    print("მომხარებელი არ მოიძებნა")
