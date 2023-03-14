def generate_tax(income,percentage):
    tax=income*percentage*0.01
    return tax
'''my_tax = generate_tax(2500,15)
print(my_tax)'''

def my_name(**b):
    full_name = f"My name is {b['firstname']} {b['secondname']} i am {b['age']} years old"
    return full_name