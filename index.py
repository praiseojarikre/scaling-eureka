# print("hello world")
# Variable[when cakking variables,you dontr need to attacg const or var]
'''name = "praise"
num = 2
num_2 = 9.823
print(name,num_2,num)

full_name = name+ "ojarikre"
print(full_name)
a,b,c = 2 , "onipanu","Lagos"
print(a,b,c)'''

# Data types- strings,NUMBERS(integers,float,complex),SEQUENCE eg lists,sets,tuples,Dictionary.
# strings
surname = 'jessica '
name = 'oluremi'
first_name = 'micheal'
full_name1 = surname + first_name
age = '24'
bmi = 6.8
print(full_name1,type(age),bmi)
print(surname,type(surname))
print(first_name, type(first_name))
print(age, type(age))
print(bmi,type(bmi))


# sting menthods - len,upper,lower,slice,endwith,startwith
print(len(full_name1))
print (full_name1[0])
print (full_name1[1])
print (full_name1[2])
print (full_name1[3])
print (full_name1[4])
print (full_name1[5])
print (full_name1[6])
print(full_name1.upper())
print(full_name1.lower())
# slice[start:end]
print(surname[0:3])
print(full_name1.upper()[7:15])
print(name[3:7].capitalize())
print(full_name1[:8])
print(full_name1[8:])
school ='techstudio'
print(school[0:4].upper())
print(school[4:].capitalize())
# title(used to capitalise first letters of each wrods)
mult_str = 'My name is Praise, I love python'
print(mult_str.title())
print(mult_str.endswith('on'))
print(mult_str.startswith('thy'))

# sting formatting
more_strt = print(f'{mult_str} and javascript {school} {age}')

# numbers--------
print('=====Numbers=====')
# number Data type
num1 = 10
gravity = 9.81
complex_num = 2j
num3 = str(num1)

print(num1,type(num1))
print(gravity,type(gravity))
print(complex_num,type(complex_num))
print(num3,type(num3))
 
my_sum = num1 + int(num3) - int(age)
print(my_sum)
a = 4
b = 5

num_sum = print(f'the sum of {a} and {b} is {a+b}') 
print('the sum of {} and {} is {}'.format(a,b,a+b))
print(f'the product of {a} and {b} is {a*b}')

first_names = 'Praise'
last_name = 'Ojarikre'
age = 99
national = 'Nigeria'
city = 'lagos'
occupation = 'full satck developer'
full_name2 = first_names + ' ' + last_name

print(f'My name is {full_name2} I am {age} years old.I am from {national} and i stay in {city} state. I am a {occupation}')
#REPLACe()
repl_word = 'I love python'
print(repl_word.replace('python','javascript'))

s = 'My name is Fred, a full stack developer'
print(s.split(',')[0])
print(s.split(',')[1].capitalize().strip())

x,y='8',5
print(type(x))
print(type(y))

print(int(x)* 3)
print(int(x)* y)
print(x * 3)
print(x * y)

y,x = '8',5
print(x)
print(y)

tech_stack = 'html,css,javascript,phyton,node'
# front_end = print(tech_stack[0:19].upper())
front_end= tech_stack.upper().split(',')
print(front_end[0],front_end[1],front_end[2])

back_end = tech_stack.title().split(',')
print(back_end[3],back_end[4])

# booleans-True/false statements
a=5
b=10
c='5'

print(a==b)
print(a < b)
print(a>b)
print(a==c)
# print(s and v)

# operators-they are used to assign values to a variable-
# Assignment operator =,>,<,+=,-+,*=,<=,>=,/=

x = 8
y = 3 
if x<y: 
    print(x+y)
else:
    print(y-x) 

x=10
y=15
if y>x:
    print(x+y)
else:
    print(x-y)  
    
#arithmethic operators +,-,*/,//,%,,**
   
m=7
n=25
p=-4
print(n+m-p**2/6*2)      
print(n+m-p**2//6*2) 

if n%m ==0 :
    print ('m is a factor of n')
else:
    print('wahala! '*4)    
    
# Logic operators and,or,not 
j=3
k=8
l=-2
z=6
_try=(k>j) and (l<k)
print(_try)

do_math = (k+l or k) > (k-j)
print(do_math)

dood= (k+l or k)==(z)
print(dood)

if _try:
    print('correct')
else:
    print('wahala')
if not _try:
    print('correct')
else:
    print('wahala')
# comparison operators-==,!=,>,<,>=,<= 
if (j!=k):
       print('The numbers are not equal')
else:
    print('good work')

#  input()
'''name = input('What is your name:')
print(name) 

def _sum(a,b):
    return(a+b)

print(_sum(2,3))


def sth():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print (num1+ num2)
sth()

def Area_rectangle():
    lenght = int(input('length: '))
    breadth = int(input('breadth:x '))
    area = lenght*breadth
    print(f'The area of the rectagle is {area}cm^2')
Area_rectangle()'''

# Lists Data type-is a collection of items/any data type in a sqaure bracket seperated by a comma
print('===list==')

lst =['strings',25,9.8,True,[2,3],(1,2,5)]
# list methods index, slice,lenght,pop(picks out the last array)
print(len(lst))
a,b,c,*rest,d = lst
print(*rest)
# print(d)
new_lst=lst[4:6]
print(new_lst)
print(new_lst[0][1])  
# print(lst.pop())
reverse_list= lst[::-1]
print(reverse_list)

fruits = ['banana', 'orange','mango','lemon','apple']
print(fruits[::2])
print(fruits[1::2])
print(fruits[0::4])


# Task 1
scores = [22, 19, 24, 25, 26, 24, 25, 24,15]
'''
a) Arrange the scores in ascending order
b) Arrange the scores in descending order
c) Print the even scores Hint: use list comprehension
d) Print only the maximum score
e) Print only the minimum score
'''
# ascending
scores.sort()
print(f'Ascending: {scores}')
# descending
scores.sort(reverse=True)
print(f'Descending: {scores}')
# even-numbers
evn_num =[i for i in scores if (i%2==0)]
print(evn_num)
# oddnumbers
odd_num = [a for a in scores if (a%2!=0)]
print(odd_num)
# min&max
print(max(scores))
print(min(scores))
# median
len(scores)
mid_index = len (scores)//2
median_score = print(scores[mid_index])
print(scores.count(24))
# Task 2
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
'''
a) Join the two lists above and store in a variable my_stacks
b) Copy the joined list and assign it to a variable full_stack.
c) Then insert 'Python' and SQL after 'Redux'.
'''

my_stacks = (front_end + back_end)
# or
front_end.extend(back_end)
print(front_end)

# full_stack = my_stacks 
# print(full_stack)
back_end.extend(front_end)
print(back_end)
# add_stck =['phyton','SQL']
my_stacks.insert(5,'Phyton')
my_stacks.insert(6,'SQL')
print(my_stacks)

# front_end.extend(add_stck)
# print(front_end[:8])

# new_stacks =(front_end + add_stck + back_end)
# print(new_stacks)
# full_stack.index([5])
# full_stack.insert(index+1, 'chicken')
# print(full_stack)

# =====================tuples===================
# tuple is one of the four collection of sequence data type in phyton.it can be created using () or tuple constructorfunction tuple().tuples are ordered 

tpl1= tuple((2,'baby'))
tpl = ('string',-3,True)
print(tpl,type(tpl))
print(tpl[2])
print(len(tpl))

# updating tuples-we have to convert it to list

tpl1_lst = list(tpl)
print(tpl1_lst)

tpl1_lst.extend(new_lst)
print(tpl1_lst)

tpl1_lst.insert(3,'angela')
print(tpl1_lst, type(tpl1_lst))

# now we have to take it back to list
tpl1_lst = tuple(tpl1_lst)
print(tpl1_lst, type(tpl1_lst))
del tpl1_lst
team = ('LVP','PSG','ARS','CHE','MAN-U')
new_team= team[1::2] 
print(f'The best teams are {new_team}')

# set data type-it is a collection data type-it is enclosed inside a{} set is unordered,unindex. set reads true as 1 and false as 0 Once set is created we cannot change any items but we can add additional set.# Since set is not ordered or indexed, we can only access it via looping, however we can add and remove items from the set
# use .add() to add one item only
# use .update() to add multiple item.
# use .remove() to a spe
# cified item


my_set =set({})
print(my_set,type(my_set))
my_set1={7,8,1,'redeem',True,'redeem',False,0}
print(my_set1)
# to remove from the set
my_set1.remove(8)
print(my_set1)
# to update(add)-can add more than one items
new_set={'green','yellow','thursday'}
my_set1.update(new_set)
print(my_set1)

new_data = {1,8,'black', True,False,0}
print(new_data)

# adding one item add()
new_data.add(3)
print(new_data)

# adding multiple items .update()
extra_items = {2,9,'hello'}
new_data.update(extra_items)
print(new_data)

# removing item
new_data.remove('black')
print(new_data)

# pop() will remove random item and return the removed item
# clear() will clear will clear all the items, returns empty set
# del will delete the set whole set








# control flow if,elif,for,range,while
a='yes'
b='no'
if a in b:
    input('Do you care for a drink?')
    print('Thanks!')
else:
    print('Nothing for you')

j=[1,2,3,4,5,6,7,8,9]
# for i in j:
#     i=int(input('Insert a number: '))
#     if (i%2) == 0: 
#         print('The number is even')
#     else:
#         print('The number is odd')  
        
#using for loop   
'''for i in range(3):
    try:
        j = int(input('Enter an integer: '))
        break
    except ValueError:
        print("Invalid input.Please enter an integer.")
else: 
    print("Max attempts reached.Exiting Program....")
    exit()       
if j%2==0:
    print('The number is even!')
else:
    print("The number is odd.")        

a=4
b=4
if a>b:
    print('a is greater than b')
elif a==b:
    print('a is equal to b')
else:
    print('b is greater than a')'''
    
# loops for and while
# for loop-it runs only once
'''
for condition:
    //run code
'''
'''cars =['mercedes','honda','toyota','BMW','corolla']
for x in cars:
    print(f'My favorite car is {x}')
for brand in cars:
    if brand == 'BMW':
        input('favorite car brand?')
        print(f'My best brand of car is {brand}')
    else:
        print(f'Please pick an option from {cars}')


clubs =('ARSENAL','MANU','LIV','CHELSEA')
for club in clubs:
    if "A" in club:
        print(f'the clubs are {club}')'''
for n in range(0,20,2):
    print(n)

# while loop
i= 1
while i<5:
    print('while loop running....')
    i += 1


cars =['mercedes','honda','toyota','BMW','corolla']
i = 1
while i < 4:
    print(f'My favorite car is {cars[i]}')
    i += 1

# dictionary-Dictionaries are used to store data values in key:value pairs.A dictionary is a collection which is ordered*, changeable and do not allow duplicates.Dictionaries are written with curly brackets, and have keys and values:{'name':'praise'}.if the value is a number it doesnt have to be in a number
# create a dictionary of yourself.
person ={'name':'PRAISE OJARIKRE',
 'age':90,
 'gender':'Female',
 'occupation':'Web developer',
 'state':'Delta state',
 'DOB':{'year':2022,'day': 3,'month': 'April'},
 'fav_food':['rice','beans','indomie'],
 'address':{
 'street_no': 1,
 'street_name': 'Ogunlesi street',
 'city':'Lagos state',
'country':'Nigeria'
}}

# accessing the dictionary
food =person['fav_food']
i = 0
while i < 2:
    print(food[i])
    i += 1
# print(food)
print(person['name'])
str1=person['address']['street_no']
str2=person['address']['street_name']
str3=person['address']['city']
str4=person['address']['country']
print(str1,str2,str3,str4)

# adding items to a dct
person['marital status'] ='single'
print(person)
# removing any key value specified from a dict pop(key) specified key-value print(key.pop(value))
print(person.pop('age'))

# popitem() removes last item and produces the value it deleted in a tuple,
print(person.popitem())
# .items changes dictionary to list of tuples
print(person.items())
# to print the list of keys in ur dict
print(person.keys())

'''Exercise: One 
1) Create a tuple containing names of your sisters.
2) Create a tulle containing names of your brothers. (imaginary siblings are fine)
3) Join brothers and sisters tuples and assign it to siblings
4) Print the total number of your siblings (total _siblings)
5) Modify the siblings tuple and add the name of your father and mother and assign it to family_members.
6) Unpack siblings and parents from family_members.'''

sisters = ('Remi','Lape','Foluke','Maryjane')
print(sisters)
brothers =('Tobi','Bankky','Tope','Kenny')
print(brothers)

siblings = list(sisters + brothers)
siblings = tuple(siblings)
print(siblings)

total_siblings = len(siblings)
print(total_siblings)

parents = ['Bose','Gregson']
siblings = list(siblings)
siblings.extend(parents)
print(siblings)
family_members = siblings
print(family_members)
a,b,c,*rest=family_members
print(a,b,c,d,*rest)
'''new_family = family_members[0:8]
new_family = tuple(new_family)
print(new_family)'''

'''Exercise: Two
Write a python code that will count in 3 steps numbers between 1 and 100.
'''
for n in range(1,100,3):
    print(n)
'''write a multiplication table'''   
for number in range(0,10):
    multiply = number*(number+1)
    print(number,'X',number,'=',multiply)
    
num2=3
for i in range(1,12):
    multiply= i*i
    print(num2,'x',i,'=',multiply)    
    
for number in range(0,10):
    x=number+1
    multiply = number*(x)
    print(number,'X',x,'=',multiply)
    
'''or'''
n=0
while n<11:
    print(f'{n} x {n+1} ={n*n}')
    n=n+1
    
    
    
'''Functions-is a block of code performing a specific task
declaring a Funtion
def functio_name():
    codes
    codes'''
    
def example_function():
    print('this is a function')
example_function()

def add_numbers():
    num_one=2
    num_two=6
    total= num_one+num_two
    print(total)
add_numbers()

def area_circle():
    radius=3.5
    pi_e= 3.142
    total_area = pi_e * radius**2
    print(int(total_area))
area_circle()    

'''functions with parameters'''

def area_circle(radius,pi_e):
    total_area = pi_e * radius**2
    print(int(total_area))
area_circle(3.5,3.142)

def full_name(first_name,last_name):
    print(f'My name is {first_name} {last_name}')
full_name('Praise','Ojarikre') 

def sum_numbers(n):
    total=0
    for i in range(n+1):
        total+=i
    print(total)
sum_numbers(10)

'''arbitary arguments-used when more than one value is needed *arg'''
siblings =['perfect','maro','banky','jerry']
def my_siblings():
    for names in siblings:
        print(f'My sibling name is {names}')
my_siblings()

def my_siblings(*b):
    print(f'The youngest child is {b[4]}')
    print(f'The techie child is {b[2]}')
    print(f'the foodie child is {b[3]}')
my_siblings('Taiwo','Idowu','Dami','Kehinde','Abbey')


'''KEYWORD ARGUMENTS-**arg used when we want to reference a parameter even when their values ard interchanged'''
'''key=valu'''
def my_calc(**y):
    vol= y['l']*y['b']*y['h']
    print(vol)
my_calc(l=2,h=3,b=4) 

'''return statements'''
def my_return(first, second):
    return f'my name is {first} {second}'
print(my_return('praise','micheal')) 

def do_sum(a,b) :
    return a+b*a-b
print(do_sum(5,6))


# pass
def do_pass():
    pass
do_pass()

# continue-to remove an element from the array
fruits = ['apples','orange','mango','pineapple','grape']
def fav_fruit():
    for fruit in fruits:
        if fruit == 'mango':
            continue
        print(f'My favorite fruit is {fruit}')
fav_fruit()



# create a findevennumbers such that print(fi)
def find_even_nums(n):
    evens =[]
    for i in range (n+1):
        if i%2==0:
            if i ==0:
                continue
            evens.append(i)
    return evens
print(find_even_nums(20))    


# lambda functions
# lambda argument: expression
mySum = lambda a,b:a**2+b**2
print(mySum(5,6))


vol_cylinder = lambda pi,r,h:pi*r**2*h
print(int(vol_cylinder(3.142,3.5,2)))



'''Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).'''

'''what is a module-a module is a file containing a set of codes or a set of codes or a set of function which can be included to an application. a module could be a file containing  a single variable ,a function or a big code base'''

import modules
print (modules.generate_tax(2500,15))

from modules import generate_tax as my_tax
print(my_tax(2500,15))

from modules import my_name as my_fullname
print(my_fullname(age=90,firstname='praise',secondname='micheal'))

