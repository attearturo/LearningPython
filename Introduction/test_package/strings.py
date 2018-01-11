# Strings funtions
miString = 'hello world'

# Capitalize
print(miString.capitalize())

# Swap case
print(miString.swapcase())

# Get lenght
print(len(miString))

# Replace
print(miString.replace('world', 'todos'))

letra = 'l'
print(miString.count(letra))

# Startwith
print(miString.startswith('hello'))
print(miString.endswith('hello'))

# Split to list
print(miString.split())

# find inside the code
print(miString.find('h')) # retorna -1 porque no esta
print(miString.index('h')) # retorn un error

# si todo es alfanumerico
print(miString.isalnum())

# si todo es alfabetico
print(miString.isalpha())

# si todo es numerico
print(miString.isnumeric())