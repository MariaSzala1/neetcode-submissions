def print_string_characters(my_string: str) -> None:
    length = len(my_string)
    i = 0
    while i < length:
        print(my_string[i])
        i += 1
        if i == length:
            break



# do not modify below this line
print_string_characters("Hello, World!")
print_string_characters("Good Job!")
