def reverseString(string):
    if type(string) != str or len(string) < 2:
        print("Either your String has only one letter or it is of no string type. Please Check")
    else:
        str_list = string.split()
        rev_str_list = str_list[::-1]
        for i in rev_str_list:
            print(i[::-1])


# reverseString(2322452)
# reverseString("Hello There!! How you doing?")