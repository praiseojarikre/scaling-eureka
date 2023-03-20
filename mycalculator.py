'''import re
previous=0
run= True

def my_calc():
    global previous
    global run
do_math =""
if previous==0:
    do_math= input('Enter an epression: ')
else:
    do_math = input(str(previous))
if do_math =='end':
    print('Closing tab....')
    run = False
else:
    do_math= re.sub('[a-zA-Z,.:()""]','',do_math)
if previous == 0:
        previous =eval(do_math)
else:
    
my_calc()''' 
# for a calculator we have to have a default value,a boolen to state its running to be true 
import re
default = 0
run =True
def my_calc():
    global default
    global run
    # default= ""
    if default == 0:
        expression = input('Enter an expression: ')
        # print('You typed',expression)
    else:
        expression = input(str(default))
        
    if expression  == "quit":
        print('end calculation')
        run = False
    else:
        if default == 0:
            expression = re.sub('[a-zA-Z,.:;?@]','',expression)
            default = eval(expression)
            # print(default)
        else:
            default = eval(str(default) + expression)                   
            print('Ans: ',default)
while run:    
    my_calc()


