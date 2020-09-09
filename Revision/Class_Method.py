"""
- class method is an inbuilt function in Python which returns a class method for given function.
- There are 2 ways to create class methods in Python:
    - Using classmethod(function)
    - Using @classmethod annotation

- class methods are bound to class rather than an object. Class methods can be called by both class and object, but
  calling with it's object does not make more sense.

- Since class method only has access to its class argument(cls), it can't modify object instance state as it requires
  access to that particular object(using self)

- You can use class method as an alternative constructor. To keep generic convention, we start these functions by 'from'

Difference between Class, Static and Instance method
- An instance method knows its instance(and from that, its class)
- A class method knows its class
- A static method doesn't know its class or instance

"""


# Example 1 - Using classmethod()

class Class1:
    var = "I am class variable"

    def __init__(self):
        print("Constructor")

    def cls_method(cls, arg1, arg2):
        cls.arg1 = arg1
        cls.arg2 = arg2
        print("Variable defined inside class - ", Class1.var)
        print("Values passed as an argument - ", cls.arg1, cls.arg2)


Class1.cls_method = classmethod(Class1.cls_method)
Class1.cls_method(34, 55)
print()


# Example 2 - Using @classmethod annotation

class Class2:

    def __init__(self):
        print("Inside Constructor")

    @classmethod
    def cls_method1(cls, arg1):
        cls.arg1 = arg1
        print("Argument passed is - ", cls.arg1)


Class2.cls_method1(34)
print()


# Example 3 - Class method can be used as an alternative constructor. Also displaying the static, class,
# instance methods and along with the property decorator.

class Class3:

    # class or static variable
    raise_amt = 2.0

    # Constructor
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    # Instance Method
    def email(self):
        return self.lname.lower()+'.'+self.fname.lower()+self.age+'@xyz.com'

    # property decorator
    @property
    def fullname(self):
        return self.fname+' '+self.lname

    # Static Method
    @staticmethod
    def status(arg):
        print("Clear")

    # Class Method - This will affect the behaviour/state of all its instances.
    @classmethod
    def set_raise_amt(cls, r):
        cls.raise_amt = r

    # Class method as an alternate constructor. To keep generic convention, we start these function by 'from'
    @classmethod
    def from_string(cls, string):
        fn, ln, age = string.split('-')
        return cls(fn, ln, age)


obj1 = Class3('Jonas', 'Khanwald', '26')
print(obj1.fullname)
print(obj1.email())
print(obj1.raise_amt)
Class3.set_raise_amt(4)
obj = Class3.from_string('Martha-Neilson-25')
print(obj.fullname)
print(obj.email())
print(obj.raise_amt)
