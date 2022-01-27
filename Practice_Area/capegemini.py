'''
Write a simple decorator
'''

def deco(func):
    def wrapper():
        func()
        print("Goodbye")
    return wrapper

@deco
def test():
    print("Hello World!!")

test()

# =======================

'''
Find the second largest number
'''

l = [3,4,1,6,5,8]

def second_large(l):
    n = len(l)
    for i in range(n):
        for j in range(i+1, n):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    print(l)
    return l[-2]

print(second_large(l))


# =========================

'''
1. String replace – time estimate 15mn
Write a function replace_latest_slice() which takes a string query, and changes all
occurrences of latest_slice::<table> to (SELECT * FROM <table> WHERE ds =
'LATEST').
Example:
#>>> replace_latest_slice(query="""SELECT * FROM
latest_slice::sale_order so INNER JOIN latest_slice::res_partner rp ON 
so.id = rp.id""")
SELECT * FROM (SELECT * FROM sale_order WHERE ds = 'LATEST') so INNER
JOIN (SELECT * FROM res_partner WHERE ds = 'LATEST') rp ON so.id =
rp.id
'''
# import re

def replace_latest_slice(query):
    # pattern = r"\s([\w]+::[\w]+)\s"
    
    temp_list = query.split()
    n = len(temp_list)
    for i in range(n):
        if '::' in temp_list[i]:
            temp_str = temp_list[i].split('::')
            new_str = f"(SELECT * FROM {temp_str[1]} WHERE ds='{temp_str[0].split('_')[0].upper()}')"
            temp_list[i] = new_str
    temp_list = " ".join(temp_list)
    print(temp_list)
    
replace_latest_slice("""SELECT * FROM
latest_slice::sale_order so INNER JOIN latest_slice::res_partner rp ON 
so.id = rp.id""")