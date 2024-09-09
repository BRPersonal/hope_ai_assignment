def check_number(n:int) -> None:
    if (n == 10):
        print("CORRECT")

def check_password(pwd:str) -> None:
    if (pwd == "HOPE@123"):
        print("Your password is correct")
    else:
        print("Your password is wrong")

def print_category(age:int) -> None:
    if (age < 18):
        print("Child")
    elif (age < 35):
        print("Adult")
    elif (age <= 59):
        print("Citizen")
    else:
        print("senior citizen")

def check_sign(n:int) -> None:
    if (n >= 0):
        print("Positive")
    else:
        print("Negative")

def check_divisibility(numerator:int , denoninator:int) -> None:
    if (numerator % denoninator == 0):
        print (f"Number is divisible by {denoninator}")
    else:
        print(f"Number is not divisible by {denoninator}")

if __name__ == "__main__":
    n = int(input("Enter number:"))
    check_number(n)
    pwd = input("enter password:")
    check_password(pwd)
    age = int(input("Enter age:"))
    print_category(age)
    n = int(input("Enter number:"))
    check_sign(n)
    n = int(input("Enter number:"))
    check_divisibility(n,5)



