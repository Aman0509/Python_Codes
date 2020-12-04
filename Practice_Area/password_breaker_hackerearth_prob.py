S, P = input("Enter Word and Password separated with space").split()
S_len = len(S)
if P.find(S) != -1:
    l = list(P)
    del(l[P.find(S):S_len+P.find(S)])
    P = "".join(l)
    print(P)
if P == S:
    print("Possible")
else:
    print("Impossible")

