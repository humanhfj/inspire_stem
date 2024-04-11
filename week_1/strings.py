#string in python
#Date
#Name : Vini
city = "nairobi"

#Convert to upper case
print(city)
print("\n\n") #prints a new line
print(city.upper())

name = "VINCENT MORARA"
print(name)
print(name.lower())#converts string to lower case

town ="    Naiva sha   "
print(town)
print("\t")#new tab
print(town.strip()) 
f_name ="John"
s_name ="Wamai"
full_name = f_name + s_name
print(full_name)

 #replacing a character 
fruit ="Orange00000"
print(fruit.replace("0","Y"))   

subject ="Phydics:Sciences"
print(subject.split(":"))

age = 50
height = 1.5
print("I am {}years old and {} meters tall".format(age,height))

name="vincent morara"
print(len(name))

name="vincent morara"
print(len(name))
print(f"My full name is {name}")

school = "engineering"
course = "electical"
print("I am studying{course}in the school of {school}".format(course,school))
