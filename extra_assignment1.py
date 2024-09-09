
def print_instructor() -> None:
    print("HOPE AI")

def print_instructor_got_from_input() -> None:
    instructor = input("Enter your institute name? : ")
    print(instructor)

def prompt_for_details() -> None:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    schoolname = input("enter your school name: ")
    degree = input("Enter your degree: ")
    print(f"name={name},age={age},school={schoolname},degree={degree}")

def add() -> None:
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    total = a + b
    print(f"a={a}\nb={b}\nadd={total}")

def subtract() -> None:
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    diff = a - b
    print(f"a={a}\nb={b}\nsub={diff}")

def multiply() -> None:
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    product = a * b
    print(f"a={a}\nb={b}\nmul={product}")

def divide() -> None:
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    result = a / b
    print(f"a={a}\nb={b}\nFloat Div ={result}")

def floor_division() -> None:
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    result = a // b
    print(f"a={a}\nb={b}\nFloor Div ={result}")

def modulo() -> None:
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    result = a % b
    print(f"a={a}\nb={b}\nModulo ={result}")

def power() -> None:
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    result = a ** b
    print(f"a={a}\nb={b}\nPower ={result}")





if __name__ == "__main__":
    print_instructor()
    print_instructor_got_from_input()
    prompt_for_details()
    add()
    subtract()
    multiply()
    divide()
    floor_division()
    modulo()
    power()
