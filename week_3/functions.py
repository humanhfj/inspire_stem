def print_name():
    print("My name is domani munga")

#calling the function
print_name()

def print_details(name,age,id,gender):
    print("I am {0},{1}years old.My id no is {2}and gender is {3}".format(name,age,id,gender))

print_details("Domani","20","13504060","male")
print_details("Don","26","43608867","female")


def sum_nums(x,y):
    return x + y

z = sum_nums(10,20)
print(z) 

def product_nums(x,y):
    return x * y

x = product_nums(10,20)
print(x)



def print_odds(first_number, last_number):
    for i in range(first_number,last_number):
        print(i %2)

print_odds(0,15)