def printWelcome() -> None:
    print("Welcome to Assignment-1")

def performAddition(num1:int, num2:int) -> None:
    total = num1 + num2
    print("Num1=",num1)
    print("Num2=",num2)
    print('Add=', total)

def checkBMI(bmi:float) -> None:
    if bmi < 16:
        print("Over Thinness")
    elif bmi >= 16 and bmi < 17:
        print("moderate Thinness")
    elif bmi >= 17 and bmi < 18.5:
        print("mild Thinness")
    elif bmi >= 18.5 and bmi < 25:
        print("Normal")
    elif bmi >= 25 and bmi < 30:
        print("OverWeight")
    elif bmi >= 30 and bmi < 35:
        print("Obese class I")
    elif bmi >= 35 and bmi < 40:
        print("Obese class II")
    elif bmi >= 40:
        print("Obese class III")

if __name__ == "__main__":
    printWelcome()
    performAddition(10,30)
    bmi = float(input("Enter the BMI Index:"))
    checkBMI(bmi)
