# Condionales
x = 15

# Basic IF
# La indexacion es muy importante y determina los bloques de codigo
if x < 6:
    print('this is true')

# If false
if x < 6:
    print('This is true')
else:
    print('This is false')  
    

# Elif
color = 'red'

if color == 'red':
    print('Color is red')
elif color == 'blue':
    print('Color is blue')
else:
    print('Color is both')  
    
    
# Nested if
if color == 'red':
    if x < 10:
        print('Color is red and x is less than 10')
        
# Logical operatora
if color == 'red' and x > 10:
    print('Color is red and x is more than 10')