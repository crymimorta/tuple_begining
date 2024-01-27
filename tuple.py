myfamily = ("mother", "father", "sister", "brother", "sister") 

print(myfamily) 
print(type(myfamily))
print(myfamily[-3],myfamily[-1])
x = list(myfamily)
x.append("me")
print(x)
x.remove("brother")
myfamily=tuple(x)
print(x,'\n')

laptop = { "brand": "dell", "model": "alienware", "year": 2010 , "Home": True}
print(laptop.get("brand"))
laptop["year"]=2019
print(laptop.get("year"),'\n')

user = { "name": "", "age": "", "country": "", "known":"" }
user["name"]=input("What is the user's name? ")
user["age"]=input("What is the user's age? ")
user["country"]=input("What is the user's country of birth? ")
user["known"]=input("What is the user known for? ")
print(user)