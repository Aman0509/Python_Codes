"""
- @property is built-in decorator in python language which is used to make functions like getter and setters in a class
  behave as properties.

- There are 2 ways to use property decorator:
   - Define @attribute_name(as getter), @attribute_name.setter(as setter) and @attribute_name.deleter(as deleter)
   - Using property inbuilt function, property(fget, fset, fdel, doc) where fget, fset and fdel are methods define in
     the class and doc contains the documentation or docstring for the attribute
"""


# Example to demonstrate that why we need property decorator

class Student:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = self.fname + ' ' + self.lname

    def email(self):
        return self.fname.lower() + '.' + self.lname.lower() + '@xyz.com'


obj = Student('Tom', 'Hanks')
print("Fullname - ", obj.fullname)
print("email - ", obj.email())

# Updating the name
print("Changing first name to John")
obj.fname = 'John'

print("Fullname - ", obj.fullname)  # It will return the initialised fullname not the one we have updated
print("email - ", obj.email())  # However, it will show email as per updated name because it is function which is called
# at the time when we want the email to be returned
print()


# This can be fixed by creating a function of fullname so that whenever we needs fullname, we can call this function
# and it will return the fullname as per the current value of fname and lname. However, this is not a pythonic
# way of doing this. Pythonic way is to decorate the fullname method with property decorator and then instead of
# calling, use it like a variable. You can also define set and delete property decorator.


class Student1:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def fullname(self):
        """ This is a getter method"""
        return self.fname + " " + self.lname

    @fullname.setter
    def fullname(self, name):
        """ This is a setter method"""
        fname, lname = name.split()
        self.fname = fname
        self.lname = lname

    @fullname.deleter
    def fullname(self):
        """ This is a deleter method"""
        self.fname = None
        self.lname = None
        print("Name Deleted")

    def email(self):
        return self.fname.lower() + '.' + self.lname.lower() + '@xyz.com'


obj1 = Student1('Tom', 'Hanks')
print("Fullname - ", obj1.fullname)  # Notice here that as fullname is a method but we are using it as a variable
print("email - ", obj1.email())

# Updating the name
print("Changing first name to David")
obj1.fname = 'David'

print("Fullname - ", obj1.fullname)  # Notice here that as fullname is a method but we are using it as a variable
print("email - ", obj1.email())

obj1.fullname = "Dawid Malan"
print("fullname updated to Dawid Malan")
print("First Name - ", obj1.fname)
print("Last Name - ", obj1.lname)


