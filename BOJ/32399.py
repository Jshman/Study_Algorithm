S = input()
if (S == "(1)"):
    print(0)
elif (S in ["1)(", "()1", "1()", ")(1"]):
    print(1)
elif (S == ")1("):
    print(2)