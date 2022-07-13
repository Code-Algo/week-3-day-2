def int_plus_str(num):
    nsl = []
    sl= []
    for i in num:
        if type(i) == str:
            sl.append(int(i))
        else:
            nsl.append(i)
    return sum(nsl) - sum(sl)
print(int_plus_str([1,2,9,'4','5','6']))
