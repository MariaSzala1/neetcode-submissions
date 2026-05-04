def print_first_char(word: str) -> None:
    return print(word[0])

def print_second_char(word: str) -> None:
    if len(word) >= 2:
        return print(word[1])
    else:
        return "There is no second character"

def print_last_char(word: str) -> None:
    length = len(word)
    n = length - 1
    return print(word[n])


# do not modify below this line
print_first_char("hello")
print_second_char("hello")
print_last_char("hello")

print_first_char("yay")
print_second_char("yay")
print_last_char("yay")
