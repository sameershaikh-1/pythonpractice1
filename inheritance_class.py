# multiple inheritance (the aim of multiple inheritance is reusability)

class grand_parents:
    def method1(self):
        print("I am in grand parents class")
class parent:
    def method1(self):
        print("I am in parent class")

class child(grand_parents,parent):    # multiple inheritance - more than one class
    def method2(self):
        print("I am in child class")

# c = parent()
# c.method1()

d = child()
d.method1()