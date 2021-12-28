print("Isaac Muchiri Muthui")
print("0----")
print(" ||||")
print("*" * 10)

price= 10
price= 20
rating= 4.9
name= "Muchiri"
is_published= True

full_name= "John Smith"
age= 20
is_new= True
print(price)
print("The ratings are;",rating,)
[print("Name of patient:", full_name)]
print("Age of patient:", age)
print("Is the patint new:", is_new)

name= "Andrew Venis"
branch= "Computer Science"
age= 25
print("My name is:",name,)
print("My age is:",age,)

name= input("What is your name? ")
print("Hi " + name)
persons_name= input("What is your name? ")
favourite_colour= input("What is your favourite colour? ")
print(name + "likes" + favourite_colour)

list1= {1,2,3,4,5}
for i in list1:
    print(i)
    if i==4:
        break
        print("End of for loop")

name=("Thomas") #Assigning string value in the name variable
print(name)
Fees=10000 # defining course fees is 10000
Fees=20000 # dehfining course fees is 20000

course= "python's course for beginners"
print(course)
course='python for "Beginners"'
print(course)
course='''
Hi, John

here is our first email to you.

thank you

The support team.

'''
print(course)

course='python for beginners'
print(course[-1])

course='python for beginners'
print(course[0:3])

course='python for beginners'
print(course[0:])

course='python for beginners'
print(course[1:])

course='python for beginners'
print(course[:5])

course='python for beginners'
print(course[:])

course='python for beginners'
another= course[:]
print(another)

name="Jennifer"
print(name[1:-1])

# Formatted strings
first='John'
last='Smith'
msg=f'{first} [{last}] is a coder'
print(msg)

# counting number of strings in a character
course='python for beginners'
print(len(course))

# the dot. functions
course='python for beginners'
print(course.upper())

# strings in python(.dot functions and methods)
course='python for beginners'
print(course.upper())
print(course.lower())
print(course.find('n'))
print(course.find("beginners"))
print(course.replace('beginners', 'Absolute beginners'))
print(course.replace('p', 'J'))
print('python'in course )
print(course)

# arithmetic operations in python(+,-,*./,//,%,**)
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)

# augmented operations
x= 10
x= x+3
print(x)

# augmented assignment operator
x= 10
x+=3
print(x)

# augmented assignment operator
x= 10
x-=3
print(x)

# operator precedence
x= 10+3*2**2
print(x)

# exercise on the above
x=(2+3)*10-3
print(x)

# math functions(round function)
x= 2.9
print(round(x))

# math functions(absolute abs value)
x= 2.9
print(abs(-2.9))

 # using math module (import math)
import math
print(math.ceil(2.9))

# USING IF STATEMENTS
is_hot =False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("its a cold day")
    print("wear warm clothes")
else:
    print("Its a lovely day")
print("Enjoy your day")

# PROGRAM TO CALCULATE THE PRICE OF A HOUSE WHICH IS $1MILLION
price= 1000000
has_good_credit= True
if has_good_credit:
    down_payment= 0.1*price
else:
    down_payment= 0.2*price
print(f"down payment: ${down_payment}")

# AND OPERATOR
has_high_income= True
has_good_credit= True
if has_high_income and has_good_credit:
    print("Eligible for loan")

# OR OPERATOR
has_high_income= False
has_good_credit= True
if has_high_income or has_good_credit:
    print("Eligible for loan")

# NOT OPERATOR
has_good_credit= True
has_criminal_record= False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

# comparison operator using>,<,
    temparature = 38
    if temparature > 30:
        print("it's a hot day")
    else:
        print("it's not a hot day")

# names and characters
name="Isaac Muchiri Muthui"
if len(name)<3:
    print("Name must be at least 3 characters")
elif len(name)>50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")

# weight converters from kilograms to pounds and viceversa
weight= int(input("weight: "))
unit= input("(L)bs or (K)g: ")
if unit.upper()=="L":
    converted=weight*0.45
    print(f"You are{converted} kilos")
else:
    converted=weight/0.45
    print(f"You are{converted} pounds")

# while loops
i=1
while i<=5:
    print(i)
    i=i+1
print("Done")

# printing an asterisk
i=1
while i<=5:
    print('*' * i)
    i=i+1
print("Done")

# program to guess a number

secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("Guess: "))
    guess_count+=1
    if guess==secret_number:
        print("You won!")
        break
else:
    print("You failed")

# a car game code
command=""
while command !="quit":
    command =input("> ").lower()
    if command =="Start ":
        print("Car started")
    elif command =="Stop":
        print("Car stopped")
    elif command =="Help":
        print("""
        Start- To start the car
        Stop- To stop the car
        Quit- To quit
        """)
        break
    else:
        print("Sorry i don't understand that")

£££££
for item in 'Python':
    print(item)

£££££3
for item in ['Melon', 'Mango', 'Oranges', 'Pineapple']:
    print(item)

£££££
for item in [1,2,3,4,5]:
    print(item)

$$$ range ffunction
for item in range(5, 10):
    print(item)

£££££ steps in ffor loops
for item in range(5, 10,2):
    print(item)

£££££ program to calculate total cost of items in an imaginary cart
prices =[10,20,30]
total= 0
for price in prices:
    total +=price
    print(f'Total :{total}')

£££££ nested loops
for x in range(4):
    for y in range(3):#
        print(f'({x}, {y})')

£££££ lists in python
names =['isaac', 'muchiri', 'muthui', 'kiuna', 'martin', 'muraya']
print(names[-1])
print(names)

£££ code to define largest number in a list
numbers= [2,3,5,7,8,10,2]
max= numbers[0]
for number in numbers:
    if number> max:
        max= number
print(max)

# printing a matrix
matrix= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(matrix)

# list methods
numbers=[5,2,1,7,4]
numbers.append(20)
numbers.insert(0, 10)
numbers.remove(2)
numbers.pop(4)
print(numbers.index(5))
print(50 in numbers)

#arranging in both ascending and descending order
numbers=[5,2,1,7,4]
numbers.sort()
numbers.reverse()
print(numbers)

# program to remove the duplicates in a list
numbers=[2,2,4,6,3,4,6,1]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#tuples in python
numbers=(1,2,3)
print(numbers.index(3)

# using dictionaries in python
customer= {
    "name":"John Smith",
"age" : 30,
"is_verified":True,
}
print(customer.get("name"))
print(customer["age"])
print(customer["is_verified"])
print(customer["birthdate"]= "jan 1 2020")

# projct to input phone number as 123 and print the output as words using a dictionary
phone= input("phone: ")
digits_mapping={
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output= ""
for ch in phone:
    output +=digits_mapping.get(ch, "!") + ""
    print(output)

Dict={
    "Name": "Tom",
    "Age": "22"
      }
print(Dict["Age"])

Employee= {
    "Name": "Isaac Muchiri",
    "Age": 22,
    "Salary": 25000,
    "Company": "GOOGLE"
}
print("printing Employee data......")
print(Employee)

333
functions in python
def greet_user():
    print('Hi there')
    print('welcome aboard')


print('Start')
greet_user()
print('Finish')

22222 function to call hello world

def hello_world():
    print('hello_world')


hello_world()

3333 creating a function with a return statement


def sum():
    a = 10
    b = 20
    c = a + b
    return c


print('The sum is:', sum())

3333 creating a function without a return statement it results to none

def sum():
    a= 10
    b= 20
    c= a+b
print(sum())

## calculating the square of a number
def square(number):
    return number*number


result= square(3)
print(result)

##calculating the sum of two variables
def sum(a,b):
    return a+b
a= int(input('Enter a: '))
b=int(input("Enter b: "))
print('sum =',sum(a,b))

#passing immutable Object(List)
def change_list(list1):
    list1.append(20)
    list1.append(30)
    print('list inside function= ',list1)
#defining the list
list1 =[10,30,40,50]
#calling the function
change_list(list1)
print('list outside function= ',list1)

# passing mutable object (String)
#defining the function
def change_string(str):
    str=  str + "Hows you"
    print('printing the string inside function: ',  str)

string1 ='Hi i am there'

#calling the function
change_string(string1)

print('printing the string outside function:', string1)

#required arguments to ask one for his name and put a hi,, infront of the name
def func(name):
    message= 'Hi'+ name
    return message
name=input('Enter the name:')
print(func(name))

#the function simple_interest accepts three arguments and returns the simple interest accordingly
def simple_intrest(p,t,r):
    return(p*t*r)/100
p= float(input('Enter the principal amount? '))
r= float(input('Enter the rate of intrest? '))
t= float(input('Enter the time in years?'))
print('Simple Intrest:',simple_intrest(p,t,r))

#prompting the user to enter the 2 numbers and also display the sum ov=f the two numbers
def calculate_sum(a,b):
    return a + b
a= int(input('Enter value of a: '))
b= int(input('Enter value of b: '))

print('sum:', calculate_sum(a,b))

#program to print the age
age= int(input('Age: '))
print(age)

#exception errors in python
try:
    age= int(input('Age: '))
    print(age)
except ValueError:
     print('Invalid value')



