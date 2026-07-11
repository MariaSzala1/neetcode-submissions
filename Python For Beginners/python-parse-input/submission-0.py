from typing import List

def read_integers() -> List[int]:
    my_list = []
    line = input()
    nlist = line.split(",")
    for i in nlist:
        integer = int(i)
        my_list.append(integer)
    return my_list
    pass

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
