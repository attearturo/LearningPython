# Loops

# For loops
people = ['Jhon', 'Sara', 'Tim', 'Bob']
for person in people:
    print('Current Person: ', person)
    
# Iterar por orden de secuencia
for i in range(len(people)):
    print('Current list person: ', people[i])
    
for i in range(0, 10):
    print(i)
    
# While loop
count = 0
while count <= 10:
    print('Count: ', count)
    if count == 5:
        break
    count = count + 1