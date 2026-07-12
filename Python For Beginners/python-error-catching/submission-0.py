def divide_numbers(a: str, b: str) -> None:
    try:
        ai = int(a)
        bi = int(b)
        result = ai / bi
        print(result)
    except Exception as error:
        print("An error occurred:", error)

    pass



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
