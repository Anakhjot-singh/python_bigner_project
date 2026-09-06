name = input("What is your name? ")
print("Hello,", name)
print("Welcome to your Python learning journey!")

#variable

name = 'anakhjot'    #string
age = 18             #integar
hight = 5.8          #float
is_student = True    #boolean

print(name)
print(age)

age = age+1
print(age)          #19

#loops
#A loops repeats code

for number in range (1,6):
    print(number)     #1,2,3,4,5

    students = ["aman", "riya","ali"]
    for student in students:
        print("hello ",student)    #hello aman, hello riya, hello ali

#while loop
number = 1
while number <= 5:
    print(number)   #1,2,3,4,5
    number = number + 1

while True:
    answer = input("type exit to stop: ")
    if answer == "exit":
        break

#functions
#A function is a block of code that performs a specific task

def say_hello():
    print("hello! welcome to python")

say_hello()


#Function with parameters
def greet (name):
    print("hello", name)

greet("aman")  #hello aman
greet("riya")  #hello riya

#function with return value

def calculate_total(price, quantity):
    total = price * quantity
    return total
bill = calculate_total(50,3)
print(bill)        #150

