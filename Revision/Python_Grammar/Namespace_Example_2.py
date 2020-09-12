def outer_foo():
    outer_var = 3

    def inner_foo():
        inner_var = 5
        print(dir(), '--> names in inner_foo')

    outer_var = 5
    inner_foo()
    print(dir(), '--> names in outer_foo')


if __name__ == "__main__":
    outer_foo()
    print("Namespace_Example_2.py is called by itself")
    print("Value of name variable is - ", __name__)
else:
    print("Namespace_Example_2.py is called by Another Script")
    print("Value of name variable is - ", __name__)
