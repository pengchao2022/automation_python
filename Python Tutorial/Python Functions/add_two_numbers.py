

# this function is to add two numbers

def add_numbers_recursive(x,y):
    if y == 0:
        return x
    else:
        return add_numbers_recursive(x+1,y-1)
    
num1 = 200
num2 = 0

result = add_numbers_recursive(num1, num2)

print(result)

    
