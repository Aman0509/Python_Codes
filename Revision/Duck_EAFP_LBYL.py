"""
Duck Typing - Duck typing is a concept related to dynamic typing, where the type or the class of an object is less
important than the methods it defines. When you use duck typing, you do not check types at all. Instead, you check for
the presence of a given method or attribute.

Duck-typing emphasis what the object can really do, rather than what the object is. If you want to call a method on
object, there is no need to check the type of object and there is no need to check whether that method really belongs to
that object.

"""


# Example 1 - Demonstrating Duck Typing

class Specialstring:
    def __len__(self):
        return 34


string = Specialstring()
print(len(string))
print()


# Example 2

class Duck:
    def sound(self):
        print("Quack Quack")


class Cat:
    def sound(self):
        print("Meow")


class Human:
    def sound(self):
        print("Talks")


class Test:
    def invoke(self, obj):
        obj.sound()


t = Test()
h = Human()
c = Cat()
d = Duck()

for i in (h, c, d):
    t.invoke(i)

print()

# ======================================================================================================================

# EAFP --> Easier to Ask Forgiveness than Permission

person = {"Name": 'John', 'Age': None}
try:
    if person.get('Age') > 18:
        print("Congrats! You can drive now")

except Exception as e:
    print(e)
    print("Please update your age")


# LBYL --> Look Before You Leap

if person.get('Age') is None:
    print("Please update your age")
elif person.get('Age') > 18:
    print("Congrats! You can drive now")

