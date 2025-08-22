def print_vertical(upper_bound:int) -> None:
    for i in range(upper_bound):
        print(i)
    print("-" * 20)

def print_horizontal(starting_number:int, upper_bound:int) -> None:
    for i in range(starting_number,upper_bound):
        print(i, end = " ")
    print("")
    print("-" * 20)

def print_no_of_items(lst:list) -> None:
    print("Number of Items in the List:",len(lst))
    print("-" * 20)

def print_text_vertical(text: str) -> None:
    for c in text:
        print(c)
    print("-" * 20)

def print_tuple(tup: tuple) -> None:
    for item in tup:
        if (isinstance(item,tuple)):
            print_tuple(item)  #recursive call
        else:
            print(f"{item}({type(item)})")
    print("-" * 20)

def print_odd_numbers(lst: list) -> None:
    for n in lst:
        if (n % 2 != 0):
            print(f"{n} is Odd")
    print("-" * 20)

def print_even_numbers(lst: list) -> None:
    for n in lst:
        if (n % 2 == 0):
            print(f"{n} is Even")

    print("-" * 20)

if __name__ == "__main__":
    print_vertical(20)
    print_horizontal(10,20)
    print_no_of_items([10,20,14,55,43,87,76])
    print_text_vertical("Artificial Intelligence")

    tup = (1,"Welcome",2,"Hope")
    print_tuple(tup)

    tup1 = (0,1,2,3)
    tup2 = ('python','Hope')
    tup3 = (tup1,tup2)
    print_tuple(tup3)

    numbers = [20,10,16,19,25,1,276,188]
    print_odd_numbers(numbers)
    print_even_numbers(numbers)



