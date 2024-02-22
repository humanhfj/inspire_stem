#This is a program to show 


f_name =input("Enter your first name : ")
s_name =input("Enter your second name : ")
salary =float(input("Enter your salary : "))
bonus =float(input("Enter your salary : "))
s_1 =(salary + bonus)

print("My name is",f_name + s_name)
print("The original salary and bonus is", s_1)

s = salary
r =float(input("Enter the rate : "))
b =float(input("Enter the bonus change : "))

h =(s+(s*(r/100)))
n_s =(h+(bonus+s))
print("The new salary and bonus is",n_s)