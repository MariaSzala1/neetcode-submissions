from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    my_dict = {}
    added = my_dict
    my_dict[f"{name}"] = age
    return added
    pass


def list_to_dict(words: List[str]) -> Dict[str, int]:
    my_dict = {}
    added = my_dict
    n = 0
    for i in words:
        my_dict[f"{i}"] = n
        n+=1
    return added
    pass



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
