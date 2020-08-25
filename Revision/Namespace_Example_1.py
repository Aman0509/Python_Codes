a_var_ex_1 = 10
print("begin() -> ", dir())


def foo1():
    b_var_ex_1 = 12
    print("inside foo1() -> ", dir())


foo1()
print("end()-> ", dir())
print()
