
def print_institute() -> None:
    print("HOPE AI")

def print_instructor_got_from_input() -> None:
    instructor = input("Enter your instructor name? : ")
    print(instructor)

def prompt_for_details() -> None:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    schoolname = input("enter your school name: ")
    degree = input("Enter your degree: ")
    print(f"name={name},age={age},school={schoolname},degree={degree}")

def add() -> None:
    print("Adding two numbers")
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    total = a + b
    print(f"a={a}\nb={b}\nadd={total}")

def subtract() -> None:
    print("Subtracting two numbers")
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    diff = a - b
    print(f"a={a}\nb={b}\nsub={diff}")

def multiply() -> None:
    print("Multiplying two numbers")
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    product = a * b
    print(f"a={a}\nb={b}\nmul={product}")

def divide() -> None:
    print("Performing float Division on two numbers")
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    result = a / b
    print(f"a={a}\nb={b}\nFloat Div ={result}")

def floor_division() -> None:
    print("Performing floor division on two numbers")
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    result = a // b
    print(f"a={a}\nb={b}\nFloor Div ={result}")

def modulo() -> None:
    print("Performing modulo on two numbers")
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    result = a % b
    print(f"a={a}\nb={b}\nModulo ={result}")

def power() -> None:
    print("Performing x to the power of y")
    a = int(input("enter number x:"))
    b = int(input("enter number y:"))
    result = a ** b
    print(f"a={a}\nb={b}\nPower ={result}")





if __name__ == "__main__":
    print_institute()
    print_instructor_got_from_input()
    prompt_for_details()
    add()
    subtract()
    multiply()
    divide()
    floor_division()
    modulo()
    power()
