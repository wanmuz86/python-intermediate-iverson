print("Hello World")

# Creating variable

name = "Muzaffar"
age = 16
hungry = True # Notice that we are using capital here True False

print(name)
print(age)
print(hungry)

#Indentation in Python

# Example of if , elif and else in Python

if age < 13:
    print("You cannot watch the movie")
    print("This is another line for fun")
elif age < 18:
    print("You can watch the movie with parent")
else:
    print("You can watch the movie")

#Example of for in Python

for i in range (0,3):
    print("The value of i is currently ",i)


for i in range(1,10,2):
    print("The value of i is currently ",i)


# List in Action

my_list = [10,1,8,3,15]

print(my_list[0]) #retrieving the first item
print(my_list[2]) #retrieving the 3rd item

#Add an item at the end of it

my_list.append(30)
my_list.append(5)

# Remove the last item
my_list.pop()

my_list.insert(0,10) #Insert at index 0 item 10

print(len(my_list)) #length of the list (my_list)
print(len(name)) # length of the string name

# Slicing a list
print(my_list[1:3]) # from one until 3 but exclude 3

print(my_list[1:-1]) # from one until the end  (-1)

# Function declaration
# Identation matter in function declaration

def say_hello(name):
    print("Hello "+name + ", welcome to my website")

say_hello("Wan")

def say_goodbye(name):
    # Formatted String literal (f-string)
    print(f"Goodbye {name} see you tomorrow with next lesson")

say_goodbye("Edmund")

#Function with return statement

def calculate_sum(a,b):
    return a+b

print(calculate_sum(10,3))

print(calculate_sum(b=10,a=5))

# In the beginner you will see there is an exercise 
# to calculate the BMI based on height and weight , you can try do it
# weight/ (height ** 2)

# Dictionary
# pair < key , value>

info = {"name":"Muzaffar","age":40,"location":"Kuala Lumpur"}

print(info["name"])
print(info["location"])
print(info["age"])


#Tuple
#Tupple  to store collection of items, but is immutable (cannot be changed)

my_tuple = (1,2,3)
print(my_tuple[0])
print(len(my_tuple))
