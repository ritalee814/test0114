name=input("What is your name?")
birth_year=int(input("What is your year of birth?"))
age= 2024 - birth_year  #也可以在 int(year)

food=input("What is your favorite food?")
food2=input("any else?")
foodlist=[food,food2]

fathername=input("What is father's name?")
mothername=input("What is mother's name?")

myfamilylist={"Father": fathername,
             "Mother":mothername} 

print("My name is", name, ".")
print("I am", age, "years old", ".")
print("Here are my favorite food:", foodlist,".")
print("My family are", myfamilylist)

