a_var = 6
b_var = 7


def outer_foo_ex_3():
    global a_var
    a_var = 3
    b_var = 9

    def inner_foo_ex_3():
        global a_var
        a_var = 8
        b_var = 10
        print("a_var inside inner_foo = ", a_var)
        print("b_var inside inner_foo = ", b_var)
    inner_foo_ex_3()
    print("a_var inside outer_foo_ex_3 = ", a_var)
    print("b_var inside outer_foo_ex_3 = ", b_var)


if __name__ == "__main__":
    outer_foo_ex_3()
    print("a_var outside all functions = ", a_var)
    print("b_var outside all functions = ", b_var)