# Fields

fo = open('objectW.py', 'w') # w SIGNIFICA ESCRIBIR EN EL ARCHIVO
fo = open('objectW.py', 'a') # a SIGNIFICA SOBREESCRIBIR EN EL ARCHIVO

# Get some info
print('Name of the field: ', fo.name)
print('Is closed: ',fo.closed)
print('Opening mode: ',fo.mode)

fo.write('I love python')
fo.write(' and Javascript')
fo.close()

# Re open
fo = open('objectW.py','r+')
text = fo.read()
print(text)
fo.close

#Create a file
creado = open('creado.txt','w+')
creado.write('Este es mi archivo creado')
creado.closed()
