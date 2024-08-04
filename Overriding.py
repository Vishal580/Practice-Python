class A:
    def method(self):
        print("Method of class A")

class B(A):
    def method(self):
        print("Method of class B")

class C(B):
    def method(self):
        print("Method of class C")

a=A()
b=B()
c=C()
a.method()
b.method()
c.method()
