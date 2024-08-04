"""
If we are not passing 'name' argument, it gets the default,
but if we overload it with a 'name' argument,it does that operation.
This is called Overloading.
"""

class Human:
    def greetHello(self,name=None):
        if name is not None:
            print("Hi "+name)
        else:
            print("Hello")

h=Human()
h.greetHello('Sam')
