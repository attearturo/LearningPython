# classes and objects
# tambien importa la indexacion dentro de la clase

class Person:
    __name = '' # __ representa la privacidad de la propiedad
    __email = ''
    
    def __init__(self, name, email): # init indica un constructor
        self.__email = email
        self.__name = name
        
    def set_name(self, name): # self es lo mismo que this
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_email(self, email): # self es lo mismo que this
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)
    
arturo = Person('R2D2','gomezardi@hotmail.com')
#arturo.set_name('Arturo Gomez')
#arturo.set_email('gomezardi@hotmail.com')

print(arturo.toString())

class Customer(Person):
    __balance = 0
    
    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email) # Reconocer propiedades de las clases un poco mas largo
    
    def set_balance(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def toString(self):
        return '{} has a balance of {} and can be contacted at {}'.format(self.__name, self.__balance, self.__email)
    
    
alberto = Customer('Arturito', 'gomezardi@hotmail.com', 100)

print(alberto.toString())
