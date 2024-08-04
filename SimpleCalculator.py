class SimpleCalculator:
    def addition(self,a,b):
        print(f'The sum is {a+b}')

class AdvancedCalculator(SimpleCalculator):
   def subtraction(self,a,b):
       print(f'Difference is {a-b}')

class SuperAdvancedCalculator(AdvancedCalculator):
    def division(Self,a,b):
        print(f'Division is {a/b}')

    def product(self,a,b):
        print(f'product is {a*b}')

print("__________")
s1=SimpleCalculator()
s1.addition(1,2)

print("----------")
s2=AdvancedCalculator()
s2.addition(1,2)

print("---------")
s3=SuperAdvancedCalculator()
s3.addition(1,2)
s3.subtraction(1,2)
s3.product(1,2)
s3.division(1,2)
