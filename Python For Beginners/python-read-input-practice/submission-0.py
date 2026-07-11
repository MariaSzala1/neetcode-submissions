def add_two_numbers() -> int:
    mlist = []
    n = 0
    number = input()
    nlist = number.split(",")
    for i in nlist:
        integer = int(i)
        mlist.append(integer)
    for l in mlist:
        n += l
    return n
    pass



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
