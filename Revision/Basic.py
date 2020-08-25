#!/usr/bin/env python3

import decimal
import fractions
import Namespace_Example_2
import Namespace_Example_3

v = 5


def print_use():
    """print statement"""
    a, b, c = 4, 5, 5
    print("Demonstration of Print with end and sep")
    print(a, b, c, sep="!")
    print(a, end="")
    print(b, end="")
    print()


# 5+'10' --> error


def frac_deci_use():
    """Using Decimal and Fraction"""

    print("decimal.Decimal(0.5) - ", decimal.Decimal(0.5))
    print("fractions.Fraction(0.5) - ", fractions.Fraction(0.5))
    print("fractions.Fraction(1,5) - ", fractions.Fraction(4, 5))


def exp_in_python():
    """Expression in Python"""
    a = 5
    b = 2
    print(f"{a} + {b} = ", a + b)
    print(f"{a} - {b} = ", a - b)
    print(f"{a} * {b} = ", a * b)
    print(f"{a} / {b} = ", a / b)
    print(f"{a} // {b} = ", a // b)
    print(f"{a} % {b} = ", a % b)
    print(f"{a} ** {b} = ", a ** b)


def var_swap():
    """Swapping of Variable"""

    print("if a = 3 and b = 4 then a,b = b,a will swap the value of a and b")


def if_elif_if():
    """Conditional if elif else"""
    a = 6
    b = 4
    if a == b:
        print("I am inside if")
    else:
        print("I am inside else")

    # Conditional Expressions. Syntax --> <exp1 if condition else exp2>
    var = a if a > b else b
    print("var = a if a > b else b - ", var)


def loop():
    """Use case of Definite and Indefinite Loops"""

    temp = 0
    while temp < 4:
        print("Inside Definite Loop", temp)
        temp += 1

    # Indefinite Loops
    temp = False
    while not temp:

        if input("You are inside an Indefinite Loops. Press 1 to exit - ") == "1":
            temp = True
        else:
            print("Invalid choice!!")

    # loop with else
    password = "hello@123"
    for _ in range(3):
        if password == "hello123":
            break
    else:
        print("Password do not match")


def break_continue_pass():
    """break, continue and pass statement"""
    while True:
        temp = int(input("This is a infinite loop which can only be break if you type 1"))
        if temp == 1:
            break

    for i in range(1, 10):
        if i == 3 or i == 7:
            print(f"skipping {i}")
            continue
        else:
            print(i)

    def inner_func():
        pass

    inner_func()


def global_local_nonlocal_var():
    """global, local and nonlocal variable"""

    def func1():
        global v
        v *= 4
        b = "local_var"
        print(f"b - {b}")

        def inner_func1():
            nonlocal b
            b = "nonlocal_var"
            print(f"b - {b}")

        inner_func1()
        print(f"Outside func1 - {b}")

    func1()
    print(f"Outside(globally) - {v}")


def list_use():
    """Examples of list"""

    # Concatenation of 2 list use + sign
    l1 = [1, 2, 3, 4]
    l2 = [5, 6, 7, 8]
    print(f"{l1} + {l2} = ", l1 + l2)
    print(f"2 * [1,2] = ", 2 * [1, 2])
    print()

    # fetching particular element
    print(f"{l1}[2] = ", l1[2])
    print()

    # Using range function to define a list
    l3 = list(range(1, 20, 2))
    print("list(range(1, 20, 2)) = ", l3)
    print()

    # list assignment and equivalence
    """ if you check the memory add of 10, 20, 30 and 40. It will be same for l_a and l_b """
    l_a = [10, 20, 30, 40]
    l_b = [10, 20, 30, 40]
    print("l_a = ", l_a)
    print("l_b = ", l_b)
    for i in range(4):
        print(f"id of l_a[{i}] =", id(l_a[i]))
        print(f"id of l_b[{i}] =", id(l_b[i]))
    print()
    print("Changing l_b[2] = 35")
    l_b[2] = 35  # It will not change the value of l_a[2]
    print("l_a = ", l_a)
    print("l_b = ", l_b)
    """ Let's assign the list l_a to l_c and then change any element of l_c """
    l_c = l_a
    l_c[3] = 78
    print("Changing l_c[3] = 78")
    print("l_a = ", l_a)
    print("l_c = ", l_c)
    print("This is because both l_a and l_c are pointing/referring to same add of list")
    print()
    """ Let's check the equivalence of l4, l5 and l6 """
    l4 = ["a", "b", "c"]
    l5 = ["a", "b", "c"]
    l6 = l4
    print('l4 = ["a", "b", "c"]')
    print('l5 = ["a", "b", "c"]')
    print('l6 = l4')
    print("Is l4 and l5 equal? ", l4 == l5)
    print("Is l4 an alias of l5? ", l4 is l5)
    print("Is l4 and l6 equal? ", l4 == l6)
    print("Is l4 an alias of l6? ", l4 is l6)
    print()

    # List Slicing
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("x = ", x)
    print("x[2:8:2] = ", x[2:8:2])
    print("x[-4:-1] = ", x[-4:-1])
    print("x[::-1] = ", x[::-1])
    print("x[-2::-1] = ", x[-2::-1])
    print("x[0::-1] = ", x[0::-1])
    print()

    # List methods
    l7 = [1, 'a', 2, 'b']
    l8 = ['d', 'z', 'hello']
    l7.append('Havana')
    print("l7.append('Havana') - ", l7)
    l7.extend([5, 9, 93])
    print("l7.extend([5, 9, 93]) - ", l7)
    l7.insert(3, "num_3")
    print("l7.insert(3, 'num_3') - ", l7)
    print("l7.index('a') - ", l7.index('a'))
    print("l7.count(2) - ", l7.count(2))
    l8.sort()
    print("l8.sort()", l8)
    l8.reverse()
    print("l8.reverse() - ", l8)
    l7.remove('Havana')
    print("l7.remove('Havana') - ", l7)
    l7.pop(3)
    print("l7.pop(3) - ", l7)
    l9 = l8.copy()
    print("l9 = l8.copy() - ", l9)
    print()

    # List Comprehension
    """ Syntax --> [ expression for item in iterable ] """
    l_comp_if = [x for x in range(10) if x % 2 == 0]
    print("l_comp_if created using list comprehension - ", l_comp_if)
    l_comp_nested_if = [x for x in range(20) if x % 2 == 0 if x < 11]
    print("l_comp_nested_if created using list comprehension - ", l_comp_nested_if)
    l_comp_if_else = ["even" if x % 2 == 0 else "odd" for x in range(20)]
    print("l_comp_if_else created using list comprehension - ", l_comp_if_else)
    """Transposing a matrix using nested loop in list comprehension"""
    m = [[1, 3], [5, 7], [9, 11], [13, 15]]
    print("m = ", m)
    transposed_matrix = [[row[i] for row in m] for i in range(2)]
    print("Transpose of m = ", transposed_matrix)


def tupple_use():
    """ Example of tupple """

    t1 = (1, 2, 3, 2, 2, 3, 'a', 'b', 'c')
    t2 = "abc", "def", "ghi"  # Tupple can also define like that. This is called Tupple Packing

    print("t1 = ", t1)
    print("t2 = ,", t2)
    print("t1 + t2 = ", t1 + t2)
    print("t1[4] = ", t1[4])
    print()

    # Tupple Unpacking
    t2_a, t2_b, t2_c = t2
    print("t2_a, t2_b, t2_c = t2")
    print("t2_a = ", t2_a)
    print("t2_b = ", t2_b)
    print("t2_c = ", t2_c)
    print()

    # Tupple method
    print("t1.count(2) = ", t1.count(2))
    print("t1.index(3) = ", t1.index(3))


def set_use():
    """ Example of set """

    # Defining set
    ''' Indexing and Slicing is not allowed in set. 
    Also, storing of duplicate value is not allowed in set. '''
    s1 = {1, 1, 2, 2, 3, 3, 'a', 'a', 'b', 'b', 'c', 'c'}
    print("s1 = ", s1)

    # Set methods
    s2 = {3, 'a', 4, 'd', 5, 'e'}
    s3 = {23, 'x', 24, 'y', 25, 'z'}
    print("s2 = ", s2)
    print("s3 = ", s3)
    s2.add(6)
    print("s2.add(6) = ", s2)
    s2.update(['f', 7, 'g'])
    print("s2.update(['f', 7, 'g']) = ", s2)
    print("s1 is subset of s2 - ", s1.issubset(s2))
    print("s1 is superset of s2 - ", s1.issuperset(s2))
    print("s1 is disjoint of s3 - ", s1.isdisjoint(s3))
    print("s1 union s2 = ", s1.union(s2))  # union can also be written as s1|s2
    print("s1 intersection s2 = ", s1.intersection(s2))  # intersection can also be written as s1&s2
    print("s1 difference s2 = ", s1.difference(s2))  # difference can also be written as s1-s2
    print("s1 symmetric difference s2 = ", s1.symmetric_difference(s2))
    s1_i = s1.copy()
    s2_i = s2.copy()
    s1_i.intersection_update(s2_i)
    print("s1 intersection update s2 = ", s1_i)
    s1_d = s1.copy()
    s2_d = s2.copy()
    s1_d.difference_update(s2_d)
    print("s1 difference update s2 = ", s1_d)
    s1_sd = s1.copy()
    s2_sd = s2.copy()
    s1_sd.symmetric_difference_update(s2_sd)
    print("s1 symmetric difference update s2 = ", s1_sd)
    s1.remove(2)
    print("Removing 2 in s1 = ", s1)
    s1.discard(2)
    print("Discarding 2 in s1 = ", s1)
    print("Popping out from s2 = ", s2.pop())
    print("s1 = ", s2)
    print("s2 = ", s2)
    print("Clearing temporary sets s1_i, s2_i, s1_d, s2_d, s1_sd and s2_sd")
    s1_i.clear()
    s2_i.clear()
    s1_d.clear()
    s2_d.clear()
    s1_sd.clear()
    s2_sd.clear()
    print("s1_i = ", s1_i)
    print("s2_i = ", s2_i)
    print("s1_d = ", s1_d)
    print("s2_d = ", s2_d)
    print("s1_sd = ", s1_sd)
    print("s2_sd = ", s2_sd)


def dict_use():
    """ Example of dictionary"""

    d1 = {1: 'a', 2: 'b', 3: 'c'}
    d2 = {4: 'd', 5: 'e', 6: 'f'}
    print("d1 = ", d1)
    print("d2 = ", d2)
    print("dict([[1, 2], [3, 4], [5, 6]]) = ", dict([[1, 2], [3, 4], [5, 6]]))
    print("{1:2, 1:3, 1:4, 1:5, 2:6, 3:7} = ", {1: 2, 1: 3, 1: 4, 1: 5, 2: 6, 3: 7})

    # dictionary comprehension; Syntax --> {key: value for vars in iterable}
    d3 = {1: 'Aman', 2: 'Basant', 3: 'Chetna', 4: 'Deepak', 5: 'Esha', 6: 'Faizal', 7: 'Imran', 8: 'Hitesh'}
    d3_1 = {i: i + 5 for i in range(10)}
    print("{i: i+5 for i in range(10)} = ", d3_1)
    d3_2 = {k: v for k, v in d3.items() if k % 2 == 0}
    print("{k: v for k, v in d3.items() if k % 2 == 0} = ", d3_2)
    d3_3 = {k: v for k, v in d3.items() if k % 2 != 0 if k < 7}
    print("{k: v for k, v in d3.items() if k % 2 != 0 if k < 7} = ", d3_3)
    d3_4 = {k: ("set A" if k % 2 == 0 else "set B") for k in d3.keys()}
    print('{k: ("set A" if k % 2 == 0 else "set B") for k in d3.keys()} = ', d3_4)

    # dictionary methods
    print("d1.keys() = ", d1.keys())
    print("d1.values() = ", d1.values())
    print("d1.items() = ", d1.items())
    print("d2.get(5) = ", d2.get(5))
    print("d2.get(3) = ", d2.get(3))
    d4 = d2.copy()
    d4.clear()
    print("d4.clear() (Note: d4 is a copy of d2) = ", d4)
    print("d1.pop(2) = ", d1.pop(2))
    print("d2.popitem() = ", d2.popitem())
    print("{}.fromkeys([1,2,3,4], 'a') = ", {}.fromkeys([1, 2, 3, 4], 'a'))
    d1.update(d2)
    print("d1.update(d2) = ", d1)
    print("d1.setdefault('z': 26) = ", d1.setdefault('z', 26))
    print("d1 = ", d1)


def arguments():
    """Keyword Argument, Default Argument, Variable length Arguments, Positional only and keyword only arguments """

    def keyword_arg(arg):
        print("In keyword argument while passing arguments, we pass it with a keyword")
        print("This was passed during function calling: arg = test")

    keyword_arg(arg="test")

    def default_arg(name, sal="Mr"):
        print(f"Hello {sal} {name}!!")

    default_arg("Aman")

    def variable_len_args(*args, **kwargs):
        print(args)
        print(kwargs)

    variable_len_args("Hello", "There", "!", "!", fname="John", lname="Wick", weapon="pencil", alias="babayaga")

    def positional_only(fname, lname, /, sal="Miss", dept="IT"):
        """Positional Arguments ends with forward slash(/)"""
        print(f"Hello {sal} {fname}, {lname}! Welcome to {dept} department")

    positional_only("Baba", "Yaga", sal="Mr")

    def keyword_only(sal="Mr", dept="IT", *, fname, lname, ):
        """Keyword only arguments start with asterisk(*)"""
        print(f"Hello {sal} {fname}, {lname}! Welcome to {dept} department")

    keyword_only(fname="John", lname="Wick", dept="Crime")

    def pos_and_keyword_mix(fname, /, *, lname):
        print(f"Hello {fname} {lname}")

    pos_and_keyword_mix("Captain", lname="fury")


def lambda_func():
    """ Example of lambda function; Syntax --> <lambda argument/s: expression> Remember, you can pass multiple
    arguments but there can be only one expression defined in lambda """

    # With one argument
    f1 = lambda x: x ** 2
    print("f1(16) = ", f1(16))

    # With two argument
    f2 = lambda x, y: (x + y) ** 2
    print("f2(6, 5) = ", f2(6, 5))

    # With zero argument
    f3 = lambda: "lambda with 0 arguments"
    print("f3() = ", f3())

    # With map function
    f4 = list(map(lambda x: x * 2, [23, 46, 72, 98]))
    print("f4() = ", f4)

    # With filter function
    f5 = list(filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("f5() = ", f5)


def string_use():
    """Examples of string"""

    s1 = "abcd123"
    s2 = "xyz1234"
    print("s1 = ", s1)
    print("s2 = ", s2)

    # Slicing Operation
    print("s2[4] = ", s2[4])
    print("s1[2:4] = ", s1[2:4])
    print("s1[3:] = ", s1[3:])
    print("s2[:5] = ", s2[:5])
    print("s2[::-1] = ", s2[::-1])
    print("s1[:-2] = ", s1[:-2])
    print("s1[-2:] = ", s1[-2:])
    print("s2[-4:-2] = ", s2[-4:-2])
    print("s1[2:2] = ", s2[2:2])
    print("s1[-2:-2] = ", s2[-2:-2])

    # Concatenation
    print("s1 + s2 = ", s1 + s2)

    # Comparison
    print("hey > hi? = ", "hey" > "hi")

    # Arithmetic
    print('"ba"+"na"*2 = ', "ba" + "na" * 2)

    # Membership
    print('"na" in "banana"', "na" in "banana")

    # Identity
    print("Yo is yo = ", "Yo" is 'yo')

    # Logical
    print("I and '' = ", 'I' and '')
    print("'' or F = ", '' or 'F')
    print("not('I') = ", not 'I')


def string_method():
    """Examples of String inbuilt methods"""
    str1 = "AmXyZy"
    print("str1 = ", str1)

    # capitalize()
    print("str1.capitalize() = ", str1.capitalize())

    # casefold() --> aggressive version of lowercase
    print("str1.casefold() = ", str1.casefold())

    # center(width, fillchar)
    print("str1.center() = ", str1.center(20, "*"))

    # count(substring, start_index, end_index)
    print("str1.count('x') = ", str1.count("x"))

    # encode(encoding_type, error_response)
    print("str1.encode('UTF-8', 'strict') = ", str1.encode('UTF-8', 'strict'))

    # endswith(suffix, start_index, end_index), here suffix can be tupple or string
    print("str1.endswith('y') = ", str1.endswith('y'))

    # expandtabs(tabsize), if passed without parameter, default tabsize would be 8
    print("'abc\\tXYZ12345\\t#$%'.expandtabs() = ", 'abc\\tXYZ12345\\t#$%'.expandtabs())

    # find(substring, start, end) --> return -1 if substring is not found
    print("'I am Vengeance'.find('e') = ", 'I am Vengeance'.find('e'))

    # rfind(substring, start, end) --> return -1 if substring is not found
    print("'I am Vengeance'.rfind('e') = ", 'I am Vengeance'.rfind('e'))

    # format(positional args, keyword args)
    print("This {} is {} using {} method".format("sentence", "written", "format"))
    print("a - {0:05}, b - {1:08.3f}, c - {2:b}".format(3, 4.56782443, 32))

    # format_map(mapping) mapping --> dictionary
    # d1 = {1: "dog", 2: "cat", 3: "dinosaur"} --> passing this dict in format_map will throw error
    d2 = {'a': "dog", 'b': "cat", 'c': "dinosaur"}
    print("{a}{b}{c}".format_map(d2))

    # index(substring, start, stop) --> return ValueError if substring does not found
    print("'Hello There!! How are you and how's your dog?'.index('ow') = ", 'Hello There!! How are you and how\'s '
                                                                            'your dog?'.index('ow'))

    # rindex(substring, start, stop)  --> return ValueError if substring does not found
    print("'Hello There!! How are you and how's your dog?'.rindex('ow') = ", 'Hello There!! How are you and how\'s '
                                                                             'your dog?'.rindex('ow'))

    # isalnum() alphanumeric scope --> A-Z, a-z and 0-9
    print("'abcdef0123456789'.isalnum() = ", 'abcdef1234567890'.isalnum())

    # isalpha()
    print("'8atman'.isalpha() = ", '8atman'.isalpha())

    # isdecimal() 0-9
    print("'0123456789'.isdecimal() = ", '0123456789'.isdecimal())

    # isdigit() 0-9, superscript and subscript
    print("'123\u00b2'.isdigit() = ", '123\u00b2'.isdigit())

    # isnumeric() 0-9, superscript, subscript, fraction, currency numerators, roman numerals etc
    print("u'½¼'.isnumeric() = ", u'½¼'.isnumeric())

    # isidentifier()
    print("Check is '0_a' is a valid identifier = ", '0_a'.isidentifier())

    # islower()
    print("'Islower'.islower() = ", 'Islower'.islower())

    # isprintable() Printable characters - letters, symbols, digits, punctuation, whitespace
    print("'abcd1234 !@#$%'.isprintable() = ", 'abcd1234 !@#$%'.isprintable())

    # isspace()
    print("'\\t  \\n'.isspace() = ", '\t \n'.isspace())

    # istitle()
    print("'The Batman'.istitle() = ", 'The Batman'.istitle())

    # isupper()
    print("'Dhoni'.isupper() = ", 'Dhoni'.isupper())

    # join(iterable)
    print("','.join(['1', '2', '3', '4']) = ", ','.join(['1', '2', '3', '4']))
    print("','.join([1, 2, 3, 4]) = This will throw error because inside list datatype are of value int")
    print("','.join(('1', '2', '3', '4')) = ", ','.join(('1', '2', '3', '4')))
    print("','.join({'1', '2', '3', '4'}) = ", ','.join({'1', '2', '3', '4'}))
    print("','.join({'a': 1, 'b': 2}) = ", ','.join({'a': 1, 'b': 2}))

    # ljust(width, fillchar)
    print("str1.ljust(10, '%') = ", str1.ljust(10, '%'))

    # rjust(width, fillchar)
    print("str1.rjust(10, '%') = ", str1.rjust(10, '%'))

    # lower()
    print("'AZURE'.lower() = ", 'AZURE'.lower())

    # upper()
    print("'aws'.upper() = ", 'aws'.upper())

    # swapcase()
    print("'COLDhot'.swapcase() = ", 'COLDhot'.swapcase())

    # lstrip(chars)
    print("'	https//:www.google.com'.lstrip('\thtps/:w.') = ", '	https//:www.google.com'.lstrip('\thtps/:w.'))

    # rstrip(chars)
    print("'Hello World!!!!!    '.rstrip('! ') = ", 'Hello World!!!!!    '.rstrip('! '))

    # strip(chars)
    print("'----Hello------'.strip('-') = ", '----Hello------'.strip('-'))

    # partition(value or separator)
    temp_s1 = 'Python is fun'
    temp_s2 = 'Python is fun, isn\'t it'
    print(f"'{temp_s1}'.partition('is') = ", temp_s1.partition('is'))
    print(f"'{temp_s1}'.partition('not') = ", temp_s1.partition('not'))
    print(f"'{temp_s2}'.partition('is') = ", temp_s2.partition('is'))

    # rpartition(value or separator)
    print(f"'{temp_s1}'.rpartition('is') = ", temp_s1.rpartition('is'))
    print(f"'{temp_s1}'.rpartition('not') = ", temp_s1.rpartition('not'))
    print(f"'{temp_s2}'.rpartition('is') = ", temp_s2.rpartition('is'))

    # maketrans(x,y,z)  --> return mapping table for translation usable for translate()
    str_1, str2, str3 = 'abc', 'def', 'abc'
    dict_1 = {'a': '123', 'b': '456', 'c': '789'}
    print(f"'{str_1}'.maketrans({dict_1}) = ", str_1.maketrans(dict_1))
    print(f"'{str_1}'.maketrans(str2, str3)", str_1.maketrans(str2, str3))
    print(f"'{str_1}'.maketrans('abc', 'def', 'abd') = ", str_1.maketrans('abc', 'def', 'abd'))

    # translate(table)
    trans = str_1.maketrans('abc', 'def', 'abd')
    print(f"translate({trans}) = ", trans)
    print("'abc'.translate({'a': '102', 'b': '103', 'c': '104'}) = ",
          'abc'.translate({ord('a'): 102, ord('b'): 103, ord('c'): 104}))

    # replace(old_string, new_string, count)
    print("'I am feeling bad now, I don't know what to do keep this badness away from me'.replace('bad', 'good') = ",
          'I am feeling bad now, I didn\'t earlier know what to do keep this badness away from me'.replace('bad',
                                                                                                           'good', 1))
    # split(seprator, maxsplit) --> seprator default value = space & maxsplit default value = -1
    print("'This;is;sparta;ho;ha'.split(';', 3) = ", 'This;is;sparta;ho;ha'.split(';', 3))

    # rsplit(seprator, maxsplit) --> seprator default value = space & maxsplit default value = -1
    print("'This;is;sparta;ho;ha'.rsplit(';', 3) = ", 'This;is;sparta;ho;ha'.rsplit(';', 3))

    # splitlines(keepends)
    print("'Hello\\nWorld\\Good\\Luck'.splitlines() = ", 'Hello\nWorld\nGood\nLuck'.splitlines())

    # startswith(prefix, start, stop) --> here prefix can be tupple or string
    print("'Is this a dream?'.startwith('Is') = ", 'Is this a dream?'.startswith('Is'))

    # title()
    print("'Fault in our starts'.title() = ", 'Fault in our starts'.title())

    # zfill(width)
    print("'Say my name'.zfill(20) = ", 'Say my name'.zfill(20))


def namespace():
    """Namespace explained with examples
    - A namespace is a simple system to control the names in a program. It ensures that names ae unique and won't lead
    to any conflict.
    - Python implements namespaces in the form of dictionaries.
    - Namespaces make our program immune from name conflicts. However, it doesn't give us a free ride to use a variable
    name anywhere we want.
    - Python restricts names to be bound by specific rules known as scope.
    - Scope determines the parts of the program where you could use that name without any prefix.
    - Multiple namespaces are: Local, Enclosed, Global and built-in.
        - Local --> functions or class methods
        - Enclosed --> a function wrapped inside another function
        - GLobal --> a module level or uppermost level of the executing script itself.
        - BUilt-in --> these are special names that python reserves for itself.
    - Python search for a variable in this order: Local->Enclosed->Global->Built-in
    """
    print("Example 1".center(15, "*"))
    import Namespace_Example_1
    print()
    print("Example 2".center(15, "*"))
    Namespace_Example_2.outer_foo()
    print()
    print("Example 3".center(15, "*"))
    Namespace_Example_3.outer_foo_ex_3()


def null_func():
    """It is null function"""
    pass


if __name__ == "__main__":
    null_func()
    # print_use()
    # frac_deci_use()
    # exp_in_python()
    # var_swap()
    # if_elif_if()
    # loop()
    # break_continue_pass()
    # global_local_nonlocal_var()
    # list_use()
    # tupple_use()
    # set_use()
    # dict_use()
    # arguments()
    # lambda_func()
    # string_use()
    # string_method()
    namespace()